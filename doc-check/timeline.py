#!/usr/bin/env python3
"""把一个 Claude Code 会话记录压成 /doc-check 能读的时间线。

  timeline.py find <会话标题、会话 id 或第一句话里的词>
  timeline.py dump <会话 id 或 .jsonl 路径> <输出目录>

dump 写出：
  timeline.md        主会话，一行一个事件，带编号 #n
  agent-<id>.md      每个 subagent 的时间线
  summary.json       用到的 skill（含真实目录）、agent（含定义文件）、cwd
"""
import glob
import json
import os
import re
import sys
from datetime import datetime

ROOT = os.path.expanduser('~/.claude/projects')
BASE_DIR = re.compile(r'^Base directory for this skill: (.+)$', re.M)
COMMAND = re.compile(r'<command-name>/?([^<\s]+)</command-name>')


def load(path):
    out = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            try:
                out.append(json.loads(line))
            except ValueError:
                pass
    return out


def one_line(s, n):
    s = re.sub(r'\s*\n\s*', ' ⏎ ', str(s)).strip()
    return s if len(s) <= n else s[:n] + f' …（共 {len(s)} 字）'


def when(e):
    t = e.get('timestamp')
    if not t:
        return ''
    try:
        return datetime.fromisoformat(t.replace('Z', '+00:00')).astimezone().strftime('%m-%d %H:%M:%S')
    except ValueError:
        return t


def texts(content):
    if isinstance(content, str):
        return [content]
    return [c.get('text', '') for c in content or [] if isinstance(c, dict) and c.get('type') == 'text']


# ---------- find ----------

def title_file(path):
    p = os.path.join(path[:-len('.jsonl')], 'custom-title.json')
    try:
        with open(p, encoding='utf-8') as f:
            return json.load(f).get('customTitle')
    except (OSError, ValueError):
        return None


def peek(path):
    """最后一个标题、第一句用户原话、是否跑过 /doc-check。"""
    title, first, checked = None, None, False
    with open(path, encoding='utf-8') as f:
        for line in f:
            if '"custom-title"' in line:
                try:
                    title = json.loads(line).get('customTitle') or title
                except ValueError:
                    pass
            elif first is None and '"type":"user"' in line:
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                if not e.get('isMeta'):
                    t = ' '.join(texts(e.get('message', {}).get('content'))).strip()
                    if t and not t.startswith('<'):
                        first = t
            if '"skill":"doc-check"' in line or 'command-name>/doc-check' in line:
                checked = True
    return title, first, checked


def find(query):
    q = query.strip().lower()
    files = glob.glob(os.path.join(ROOT, '*', '*.jsonl'))
    hits = [p for p in files
            if os.path.basename(p).startswith(q) or q in (title_file(p) or '').lower()]
    if not hits:  # 标题只写在记录里，或者用户给的是第一句话
        for p in files:
            title, first, _ = peek(p)
            if q in (title or '').lower() or q in (first or '').lower():
                hits.append(p)
    hits.sort(key=os.path.getmtime, reverse=True)
    if not hits:
        print(f'没找到和“{query}”匹配的会话。')
        return
    for p in hits:
        title, first, checked = peek(p)
        mtime = datetime.fromtimestamp(os.path.getmtime(p)).strftime('%Y-%m-%d %H:%M')
        print(f'{os.path.basename(p)[:-6]}  {mtime}  {os.path.getsize(p) // 1024}KB  '
              f'标题：{title_file(p) or title or "（无）"}'
              f'{"  [里面跑过 /doc-check]" if checked else ""}')
        print(f'    项目：{os.path.basename(os.path.dirname(p))}')
        print(f'    第一句：{one_line(first or "", 120)}')


# ---------- dump ----------

def tool_input(name, i):
    if name == 'Bash':
        return one_line(i.get('command', ''), 400)
    if name in ('Read', 'Write', 'Edit', 'NotebookEdit'):
        extra = f'（写入 {len(i.get("content", ""))} 字）' if name == 'Write' else ''
        return i.get('file_path', '') + extra
    if name == 'Skill':
        return f'{i.get("skill")} {one_line(i.get("args", ""), 300)}'
    if name in ('Agent', 'Task'):
        return (f'[{i.get("subagent_type", "general-purpose")}] {i.get("description", "")} ｜ '
                f'{one_line(i.get("prompt", ""), 300)}')
    return one_line(json.dumps(i, ensure_ascii=False), 300)


def result_text(c):
    body = c.get('content')
    if isinstance(body, list):
        body = ' '.join(x.get('text', '') for x in body if isinstance(x, dict))
    return body or ''


def timeline(entries):
    """返回 (时间线行, 工具调用 id→事件号, 用到的 skill, agent 调用)。"""
    lines, ids, skills, agents = [], {}, {}, []
    n = 0

    def add(e, text):
        nonlocal n
        n += 1
        lines.append(f'#{n} {when(e)} {text}')
        return n

    def skill(name, at, directory=None):
        name = (name or '?').split(':')[-1]  # 插件 skill 调用时带前缀，加载时只有目录名
        s = skills.setdefault(name, {'name': name, 'dir': None, 'calls': []})
        if at not in s['calls']:
            s['calls'].append(at)
        if directory:
            s['dir'] = directory

    for e in entries:
        kind = e.get('type')
        content = e.get('message', {}).get('content')
        if kind == 'user':
            if isinstance(content, list) and any(c.get('type') == 'tool_result' for c in content if isinstance(c, dict)):
                for c in content:
                    if isinstance(c, dict) and c.get('type') == 'tool_result':
                        src = ids.get(c.get('tool_use_id'), '?')
                        flag = ' 出错' if c.get('is_error') else ''
                        add(e, f'结果(#{src}){flag}：{one_line(result_text(c), 300)}')
                continue
            for t in texts(content):
                m = BASE_DIR.search(t)
                if m:
                    d = m.group(1).strip()
                    at = add(e, f'加载 skill：{os.path.basename(d)}（{d}）')
                    skill(os.path.basename(d), at, d)
                elif t.strip():
                    who = '注入' if e.get('isMeta') else '用户'
                    at = add(e, f'{who}：{one_line(t, 1500)}')
                    for name in COMMAND.findall(t):
                        skill(name, at)
        elif kind == 'assistant':
            for c in content or []:
                if not isinstance(c, dict):
                    continue
                if c.get('type') == 'text' and c.get('text', '').strip():
                    add(e, f'Claude：{one_line(c["text"], 800)}')
                elif c.get('type') == 'tool_use':
                    name, i = c.get('name'), c.get('input') or {}
                    at = add(e, f'工具 {name}：{tool_input(name, i)}')
                    ids[c.get('id')] = at
                    if name == 'Skill':
                        skill(i.get('skill'), at)
                    elif name in ('Agent', 'Task'):
                        agents.append({'type': i.get('subagent_type') or 'general-purpose',
                                       'description': i.get('description'), 'call': at,
                                       'toolUseId': c.get('id')})
    return lines, ids, skills, agents


def agent_definition(kind, cwds):
    for d in [os.path.join(c, '.claude', 'agents') for c in cwds] + [os.path.expanduser('~/.claude/agents')]:
        p = os.path.join(d, kind + '.md')
        if os.path.exists(p):
            return os.path.realpath(p)
    return None


def resolve(arg):
    if arg.endswith('.jsonl') and os.path.exists(arg):
        return arg
    hits = glob.glob(os.path.join(ROOT, '*', arg + '*.jsonl'))
    if len(hits) != 1:
        sys.exit(f'会话 id “{arg}” 匹配到 {len(hits)} 个记录，请给完整 id 或 .jsonl 路径。')
    return hits[0]


def dump(arg, out):
    path = resolve(arg)
    os.makedirs(out, exist_ok=True)
    entries = load(path)
    lines, _, skills, agents = timeline(entries)
    with open(os.path.join(out, 'timeline.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

    cwds = sorted({e['cwd'] for e in entries if e.get('cwd')})
    for s in skills.values():
        s['realpath'] = os.path.realpath(s['dir']) if s['dir'] else None

    sub = os.path.join(path[:-len('.jsonl')], 'subagents')
    metas = {}
    for m in glob.glob(os.path.join(sub, 'agent-*.meta.json')):
        try:
            with open(m, encoding='utf-8') as f:
                metas[json.load(f).get('toolUseId')] = m[:-len('.meta.json')] + '.jsonl'
        except (OSError, ValueError):
            pass
    for a in agents:
        a['definition'] = agent_definition(a['type'], cwds)
        src = metas.get(a.pop('toolUseId'))
        if src and os.path.exists(src):
            name = os.path.basename(src)[:-len('.jsonl')] + '.md'
            sub_lines = timeline(load(src))[0]
            with open(os.path.join(out, name), 'w', encoding='utf-8') as f:
                f.write('\n'.join(sub_lines) + '\n')
            a['timeline'] = name
            a['events'] = len(sub_lines)

    summary = {'session': os.path.basename(path)[:-6], 'transcript': path,
               'title': title_file(path) or peek(path)[0], 'cwd': cwds,
               'events': len(lines), 'skills': list(skills.values()), 'agents': agents}
    with open(os.path.join(out, 'summary.json'), 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f'会话 {summary["session"]}（{summary["title"]}），{len(lines)} 个事件 → {out}/timeline.md')
    for s in skills.values():
        print(f'skill {s["name"]}：事件 {", ".join("#%d" % c for c in s["calls"])}；目录 {s["realpath"] or "未知"}')
    for a in agents:
        print(f'agent {a["type"]}（{a["description"]}）：事件 #{a["call"]}；定义 {a["definition"] or "未找到"}；'
              f'时间线 {a.get("timeline", "无")}')


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == 'find':
        find(' '.join(sys.argv[2:]))
    elif len(sys.argv) == 4 and sys.argv[1] == 'dump':
        dump(sys.argv[2], sys.argv[3])
    else:
        sys.exit(__doc__)
