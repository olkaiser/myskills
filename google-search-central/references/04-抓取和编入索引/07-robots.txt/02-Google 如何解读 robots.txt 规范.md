# Google 如何解读 robots.txt 规范

> 来源：https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec?hl=zh-cn  
> 最后更新时间 (UTC)：2026-09-11。

Google 的自动[抓取工具](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers?hl=zh-cn)支持 [REP（robots 协议）](https://www.rfc-editor.org/rfc/rfc9309.html)。这意味着，在抓取某一网站之前，Google 抓取工具会下载并解析该网站的 robots.txt 文件，以提取关于网站中哪些部分可以被抓取的信息。REP 不适用于由用户控制的 Google 抓取工具（例如 Feed 订阅），也不适用于用来提高用户安全性的抓取工具（例如恶意软件分析）。

本页介绍了 Google 对 REP 的解读。有关原始标准的信息，请查看 [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html)。

## 什么是 robots.txt 文件

如果您不希望抓取工具访问您网站中的部分内容，可以创建包含相应规则的 robots.txt 文件。robots.txt 文件是一个文本文件，其中包含关于哪些抓取工具可以访问网站的哪些部分的规则。例如，example.com 的 robots.txt 文件可能如下所示：

```
# This robots.txt file controls crawling of URLs under https://example.com.
# All crawlers are disallowed to crawl files in the "includes" directory, such
# as .css, .js, but Google needs them for rendering, so Googlebot is allowed
# to crawl them.
User-agent: *
Disallow: /includes/

User-agent: Googlebot
Allow: /includes/

Sitemap: https://example.com/sitemap.xml
```

如果您是首次接触 robots.txt，请先阅读我们的 [robots.txt 简介](https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=zh-cn)。您还可以找到[关于创建 robots.txt 文件的提示](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt?hl=zh-cn)。

## 文件位置和有效范围

您必须将 robots.txt 文件放在网站的顶级目录中，并为其使用支持的协议。和其他网址一样，robots.txt 文件的网址也区分大小写。就 Google 搜索而言，支持的协议包括 HTTP、HTTPS 和 FTP。使用 HTTP 和 HTTPS 协议时，抓取工具会使用 HTTP 无条件 `GET` 请求来提取 robots.txt 文件；使用 FTP 时，抓取工具会使用标准 `RETR (RETRIEVE)` 命令，并采用匿名登录方式。

robots.txt 文件中列出的规则只适用于该文件所在的主机、协议和端口号。

## 有效 robots.txt 网址的示例

下表列出了 robots.txt 网址及其适用的网址路径的示例。
第一列包含 robots.txt 文件的网址，第二列包含 robots.txt 文件将适用及不适用的网域。

<table>
<thead>
<tr>
<th colspan="2">robots.txt 网址示例</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>https://example.com/robots.txt</code></td>
<td>
<p>
这属于一般情况。该网址对其他子网域、协议或端口号来说无效。对同一个主机、协议和端口号上的所有子目录中的所有文件有效。
</p>
<span>适用于：</span>
<ul>
<li><code>https://example.com/</code></li>
<li><code>https://example.com/folder/file</code></li>
</ul>
<span>不适用于：</span>
<ul>
<li><code>https://other.example.com/</code></li>
<li><code>http://example.com/</code></li>
<li><code>https://example.com:8181/</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>https://www.example.com/robots.txt</code></td>
<td>
<p>
子网域上的 robots.txt 仅对该子网域有效。
</p>
<p>
<span>适用于：</span>
<code>https://www.example.com/</code>
</p>
<p><span>不适用于：</span></p>
<ul>
<li><code>https://example.com/</code></li>
<li><code>https://shop.www.example.com/</code></li>
<li><code>https://www.shop.example.com/</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>https://example.com/folder/robots.txt</code></td>
<td>
不是有效的 robots.txt 文件。抓取工具不会检查子目录中的 robots.txt 文件。
</td>
</tr>
<tr>
<td><code>https://www.exämple.com/robots.txt</code></td>
<td>
<p>
IDN 等同于其对应的 punycode 版本。另请参阅 <a href="https://www.ietf.org/rfc/rfc3492.txt">RFC 3492</a>。
</p>
<span>适用于：</span>
<ul>
<li><code>https://www.exämple.com/</code></li>
<li><code>https://xn--exmple-cua.com/</code></li>
</ul>
<p>
<span>不适用于：</span>
<code>https://www.example.com/</code>
</p>
</td>
</tr>
<tr>
<td><code>ftp://example.com/robots.txt</code></td>
<td>
<p>
<span>适用于：</span>
<code>ftp://example.com/</code>
</p>
<p>
<span>不适用于：</span>
<code>https://example.com/</code>
</p>
</td>
</tr>
<tr>
<td><code>https://212.96.82.21/robots.txt</code></td>
<td>
<p>
以 IP 地址作为主机名的 robots.txt 只在抓取作为主机名的相应 IP 地址时有效。该 robots.txt 文件并不会自动对该 IP 地址上托管的所有网站有效，但该文件可能是共享的，在此情况下，它也可以在共享主机名下使用。
</p>
<p>
<span>适用于：</span>
<code>https://212.96.82.21/</code>
</p>
<p>
<span>不适用于：</span>
<code>https://example.com/</code>（即使托管在 <code>212.96.82.21</code> 上）
</p>
</td>
</tr>
<tr>
<td><code>https://example.com:443/robots.txt</code></td>
<td>
<p>
标准端口号（HTTP 为 <code>80</code>，HTTPS 为 <code>443</code>，FTP 为 <code>21</code>）等同于其默认的主机名。
</p>
<p><span>适用于：</span></p>
<ul>
<li><code>https://example.com:443/</code></li>
<li><code>https://example.com/</code></li>
</ul>
<p>
<span>不适用于：</span>
<code>https://example.com:444/</code>
</p>
</td>
</tr>
<tr>
<td><code>https://example.com:8181/robots.txt</code></td>
<td>
<p>
非标准端口号上的 robots.txt 文件只对通过这些端口号提供的内容有效。
</p>
<p>
<span>适用于：</span>
<code>https://example.com:8181/</code>
</p>
<p>
<span>不适用于：</span>
<code>https://example.com/</code>
</p>
</td>
</tr>
</tbody>
</table>

## 错误处理和 HTTP 状态代码

在请求 robots.txt 文件时，服务器响应的 HTTP 状态代码会影响 Google 抓取工具使用 robots.txt 文件的方式。下表总结了 Googlebot 针对各种 HTTP 状态代码处理 robots.txt 文件的方式。

<table>
<thead>
<tr>
<th colspan="2">错误处理和 HTTP 状态代码</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2xx (success)</code></td>
<td>
表示成功的 HTTP 状态代码会提示 Google 抓取工具处理服务器提供的 robots.txt 文件。
</td>
</tr>
<tr>
<td><code>3xx (redirection)</code></td>
<td>
<p>
Google 会按照 <a href="https://www.ietf.org/rfc/rfc1945.txt">RFC 1945</a> 的规定跟踪至少五次重定向，然后便会停止，并将其作为 robots.txt 文件的 <code>404</code> 错误来处理。这也适用于重定向链中任何被禁止访问的网址，因为抓取工具会由于重定向而无法提取规则。
</p>
<p>
Google 不会跟踪 robots.txt 文件中的逻辑重定向（框架、JavaScript 或元刷新型重定向）。
</p>
</td>
</tr>
<tr>
<td><code>4xx (client errors)</code></td>
<td>
<p>
Google 抓取工具会将所有 <code>4xx</code> 错误（<code>429</code> 除外）解读为网站不存在有效的 robots.txt 文件，这意味着 Google 会假定没有任何抓取限制。
</p>
<aside>
请勿使用 <code>401</code> 和 <code>403</code> 状态代码限制抓取速度。<code>4xx</code> 状态代码（<code>429</code> 除外）对抓取速度没有影响。
<a href="https://developers.google.com/crawling/docs/crawlers-fetchers/reduce-crawl-rate?hl=zh-cn">了解如何限制抓取速度</a>。
</aside>
</td>
</tr>
<tr>
<td><code>5xx (server errors)</code></td>
<td>
<p>
如果 Google 找到了 robots.txt 文件，但无法提取该文件，则会遵循以下行为方式：</p>
<ol>
<li>在前 12 小时内，Google 会停止抓取相应网站，但会继续尝试提取 robots.txt 文件。</li>
<li>如果 Google 无法提取新版本，那么在接下来的 30 天内，Google 将使用上一个正常版本，同时仍会尝试提取新版本。<code>503 (service unavailable)</code> 错误会导致非常频繁的重试操作。如果没有可用的缓存版本，Google 会假定没有任何抓取限制。
</li>
<li>如果在 30 天后错误仍未更正：
<ul>
<li>如果 Google 能够全面抓取相应网站，则会遵循没有 robots.txt 文件时的行为方式，但仍会继续检查是否有新版本。</li>
<li>如果 Google 无法全面抓取相应网站，则会停止抓取该网站，但仍会定期请求 robots.txt 文件。</li>
</ul>
</li>
</ol>
</td>
</tr>
<tr>
<td>其他错误</td>
<td>
对于因 DNS 或网络问题（例如超时、响应无效、重置或断开连接、HTTP 组块错误等）而无法抓取的 robots.txt 文件，系统在处理时会将其视为<a href="#server-error">服务器错误</a>。
</td>
</tr>
</tbody>
</table>

## 缓存

Google 通常会将 robots.txt 文件的内容最多缓存 24 小时，但在无法刷新缓存版本的情况下（例如出现超时或 `5xx` 错误时），缓存时间可能会延长。已缓存的响应可由各种不同的抓取工具共享。
Google 会根据 [max-age Cache-Control](https://www.rfc-editor.org/rfc/rfc9110.html) HTTP 标头来延长或缩短缓存生命周期。

## 文件格式

robots.txt 文件必须是采用 [UTF-8](https://en.wikipedia.org/wiki/UTF-8) 编码的纯文本文件，且各行代码必须以 `CR`、`CR/LF` 或 `LF` 分隔。

Google 会忽略 robots.txt 文件中的无效行，包括 robots.txt 文件开头处的 Unicode [字节顺序标记](https://en.wikipedia.org/wiki/Byte_order_mark) (BOM)，并且只使用有效行。例如，如果下载的内容是 HTML 格式而非 robots.txt 规则，Google 会尝试解析内容并提取规则，而忽略其他所有内容。

同样，如果 robots.txt 文件的字符编码不是 UTF-8，Google 可能会忽略不属于 UTF-8 范围的字符，从而可能会导致 robots.txt 规则无效。

Google 强制执行的 robots.txt 文件大小限制是 500 [KiB](https://en.wikipedia.org/wiki/Kibibyte)，并忽略超过该上限的内容。您可以通过整合会导致 robots.txt 文件过大的规则来减小 robots.txt 文件的大小。例如，将已排除的内容放在一个单独的目录中。

## 语法

有效的 robots.txt 行由一个字段、一个冒号和一个值组成。字段名称不区分大小写（例如，`User-agent` 和 `user-agent` 被视为相同）。可以选择是否使用空格，但建议使用空格，有助于提高可读性。系统会忽略行开头和结尾的空格。若要添加注释，请在注释前面加上 `#` 字符。请注意，`#` 字符后面的所有内容都会被忽略。常见格式为 `<field>:<value><#optional-comment>`。

Google 支持以下字段（不支持 `crawl-delay` 等其他字段）：

- `user-agent`：标识相应规则适用于哪些抓取工具。
- `allow`：可抓取的网址路径。
- `disallow`：不可抓取的网址路径。
- `sitemap`：站点地图的完整网址。

`allow` 和 `disallow` 字段也称为规则（即指令）。这些规则始终以 `rule: [path]` 的形式指定，其中 `[path]` 可以选择性使用。默认情况下，指定的抓取工具没有抓取限制。抓取工具会忽略不带 `[path]` 的规则。

如果指定了 `[path]` 值，该路径值就是 robots.txt 文件所在网站的根目录的相对路径（使用相同的协议、端口号、主机和域名）。路径值必须以 `/` 开头来表示根目录，该值区分大小写。详细了解[基于路径值的网址匹配](#url-matching-based-on-path-values)。

### `user-agent`

`user-agent` 行用来标识相应规则适用于哪些抓取工具。请参阅 [Google 抓取工具和用户代理字符串](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers?hl=zh-cn)，获取可在 robots.txt 文件中使用的用户代理字符串的完整列表。

`user-agent` 字段名称及其值都不区分大小写。

### `disallow`

`disallow` 规则用来指定不能被 `disallow` 规则所属的 `user-agent` 行所标识的抓取工具访问的路径。
抓取工具会忽略不含路径的规则。

Google 无法将禁止抓取的网页的内容编入索引，但可能仍会将其网址编入索引并将其显示在搜索结果中，但不显示摘要。了解如何[阻止编入索引](https://developers.google.com/search/docs/crawling-indexing/block-indexing?hl=zh-cn)。

字段名称 (`disallow`) 不区分大小写，但其值区分大小写。

用法：

```
disallow: [path]
```

### `allow`

`allow` 规则用来指定相应抓取工具可以访问的路径。如果未指定路径，该规则将被忽略。

字段名称 (`allow`) 不区分大小写，但其值区分大小写。

用法：

```
allow: [path]
```

### `sitemap`

根据 [sitemaps.org](https://sitemaps.org) 规定，Google、Bing 和其他主流搜索引擎支持 robots.txt 中的 `sitemap` 字段。

字段名称 (`sitemap`) 不区分大小写，但其值区分大小写。

用法：

```
sitemap: [absoluteURL]
```

`[absoluteURL]` 行指向站点地图或站点地图索引文件的位置。
此网址必须是完全限定网址，包含协议和主机，且无需进行网址编码。此网址不需要与 robots.txt 文件位于同一主机上。您可以指定多个 `sitemap` 字段，并且可以添加的站点地图数量不受限制。站点地图字段不依赖于任何特定的用户代理，只要未被禁止抓取，所有抓取工具都可以追踪它们。

例如：

```
user-agent: otherbot
disallow: /kale

sitemap: https://example.com/sitemap.xml
sitemap: https://cdn.example.org/other-sitemap.xml
sitemap: https://ja.example.org/テスト-サイトマップ.xml
```

## 行和规则分组

通过对每个抓取工具重复 `user-agent` 行，可将适用于多个用户代理的规则组合在一起。

例如：

```
user-agent: a
disallow: /c

user-agent: b
disallow: /d

user-agent: e
user-agent: f
disallow: /g

user-agent: h
```

此示例中有四个不同的规则组：

- 用户代理“a”为一组
- 用户代理“b”为一组
- 用户代理“e”和“f”为一组
- 用户代理“h”为一组

有关组的技术说明，请参阅 [REP 的第 2.1 节](https://www.rfc-editor.org/rfc/rfc9309.html#section-2.1-2.4)。

## 用户代理的优先顺序

对于某个抓取工具而言，只有一个组是有效的。Google 抓取工具会在 robots.txt 文件中查找包含与抓取工具的用户代理相匹配的最具体用户代理的组，从而确定正确的规则组。其他组会被忽略。所有非匹配文本都会被忽略（例如，`googlebot/1.2` 和 `googlebot*` 均等同于 `googlebot`）。这与 robots.txt 文件中的组顺序无关。

如果为用户代理声明多个特定组，则这些组中适用于该特定用户代理的所有规则会在内部合并成一个组。特定于用户代理的组和全局组 (`*`) 不会合并。

### 示例

#### `user-agent` 字段的匹配情况

```
user-agent: googlebot-news
(group 1)

user-agent: *
(group 2)

user-agent: googlebot
(group 3)
```

以下为抓取工具选择相关组的方法：

| 每个抓取工具追踪的组 | |
| --- | --- |
| Googlebot News | `googlebot-news` 遵循组 1，因为组 1 是最具体的组。 |
| Googlebot（网络） | `googlebot` 遵循组 3。 |
| Googlebot Storebot | `Storebot-Google` 遵循组 2，因为没有具体的 `Storebot-Google` 组。 |
| Googlebot News（抓取图片时） | 抓取图片时，`googlebot-news` 遵循组 1。 `googlebot-news` 不会为 Google 图片抓取图片，因此它只遵循组 1。 |
| 其他机器人（网络） | 其他 Google 抓取工具遵循组 2。 |
| Otherbot（新闻） | 抓取新闻内容但未标识为 `googlebot-news` 的其他 Google 抓取工具遵循组 2。即使有相关抓取工具的对应条目，也只有在明确匹配时才会有效。 |

#### 规则分组

如果 robots.txt 文件中有多个组与特定用户代理相关，则 Google 抓取工具会在内部合并这些组。例如：

```
user-agent: googlebot-news
disallow: /fish

user-agent: *
disallow: /carrots

user-agent: googlebot-news
disallow: /shrimp
```

抓取工具会根据用户代理在内部对规则进行分组，例如：

```
user-agent: googlebot-news
disallow: /fish
disallow: /shrimp

user-agent: *
disallow: /carrots
```

`allow`、`disallow` 和 `user-agent` 以外的其他规则会被 robots.txt 解析器忽略。这意味着以下 robots.txt 代码段被视为一个组，因此 `user-agent` `a` 和 `b` 均受 `disallow: /` 规则的影响：

```
user-agent: a
sitemap: https://example.com/sitemap.xml

user-agent: b
disallow: /
```

当抓取工具处理 robots.txt 规则时，会忽略 `sitemap` 行。
例如，下面说明了抓取工具如何理解之前的 robots.txt 代码段：

```
user-agent: a
user-agent: b
disallow: /
```

## 基于路径值的网址匹配

Google 会以 `allow` 和 `disallow` 规则中的路径值为基础，确定某项规则是否适用于网站上的特定网址。为此，系统会将相应规则与抓取工具尝试抓取的网址的路径部分进行比较。规则中的路径可以是原始 UTF-8 字符，也可以是百分号编码的 UTF-8 字符串（按照 [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986.html)）。
如 [RFC 9309 第 2.2.2 节](https://www.rfc-editor.org/rfc/rfc9309.html#section-2.2.2)中所定义，Google 的抓取工具会使用网址的百分号编码形式来比较规则与网址，并自动将原始 UTF-8 规则路径规范化为百分号编码形式。这意味着，例如，解析器会以相同的方式处理 `Disallow: /foo/bar/ツ` 和 `Disallow: /foo/bar/%E3%83%84`。

对于路径值，Google、Bing 和其他主流搜索引擎支持有限形式的通配符。这些通配符包括：

- `*` 表示出现 0 次或多次的任何有效字符。
- `$` 表示网址结束。

下表显示了不同的通配符对解析的影响：

<table>
<thead>
<tr>
<th colspan="2">路径匹配示例</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/</code></td>
<td>匹配根目录以及任何下级网址。</td>
</tr>
<tr>
<td>
<code>/*</code></td>
<td>等同于 <code>/</code>。结尾的通配符会被忽略。</td>
</tr>
<tr>
<td><code>/$</code></td>
<td>仅匹配根目录。任何更低级别的网址均可抓取。</td>
</tr>
<tr>
<td><code>/fish</code></td>
<td>
<p>
匹配以 <code>/fish</code> 开头的任何路径。请注意，匹配时区分大小写。
</p>
<p><span>匹配项：</span></p>
<ul>
<li><code>/fish</code></li>
<li><code>/fish.html</code></li>
<li><code>/fish/salmon.html</code></li>
<li><code>/fishheads</code></li>
<li><code>/fishheads/yummy.html</code></li>
<li><code>/fish.php?id=anything</code></li>
</ul>
<p><span>不匹配项：</span></p>
<ul>
<li><code>/Fish.asp</code></li>
<li><code>/catfish</code></li>
<li><code>/?id=fish</code></li>
<li><code>/desert/fish</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>/fish*</code></td>
<td>
<p>
等同于 <code>/fish</code>。结尾的通配符会被忽略。
</p>
<p><span>匹配项：</span></p>
<ul>
<li><code>/fish</code></li>
<li><code>/fish.html</code></li>
<li><code>/fish/salmon.html</code></li>
<li><code>/fishheads</code></li>
<li><code>/fishheads/yummy.html</code></li>
<li><code>/fish.php?id=anything</code></li>
</ul>
<p><span>不匹配项：</span></p>
<ul>
<li><code>/Fish.asp</code></li>
<li><code>/catfish</code></li>
<li><code>/?id=fish</code></li>
<li><code>/desert/fish</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>/fish/</code></td>
<td>
<p>
匹配 <code>/fish/</code> 文件夹中的任何内容。
</p>
<p><span>匹配项：</span></p>
<ul>
<li><code>/fish/</code></li>
<li><code>/fish/?id=anything</code></li>
<li><code>/fish/salmon.htm</code></li>
</ul>
<p><span>不匹配项：</span></p>
<ul>
<li><code>/fish</code></li>
<li><code>/fish.html</code></li>
<li><code>/animals/fish/</code></li>
<li><code>/Fish/Salmon.asp</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>/*.php</code></td>
<td>
<p>
匹配包含 <code>.php</code> 的任何路径。
</p>
<p><span>匹配项：</span></p>
<ul>
<li><code>/index.php</code></li>
<li><code>/filename.php</code></li>
<li><code>/folder/filename.php</code></li>
<li><code>/folder/filename.php?parameters</code></li>
<li><code>/folder/any.php.file.html</code></li>
<li><code>/filename.php/</code></li>
</ul>
<p><span>不匹配项：</span></p>
<ul>
<li><code>/</code>（即使其映射到 /index.php）</li>
<li><code>/windows.PHP</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>/*.php$</code></td>
<td>
<p>
匹配以 <code>.php</code> 结尾的任何路径。
</p>
<p><span>匹配项：</span></p>
<ul>
<li><code>/filename.php</code></li>
<li><code>/folder/filename.php</code></li>
</ul>
<p><span>不匹配项：</span></p>
<ul>
<li><code>/filename.php?parameters</code></li>
<li><code>/filename.php/</code></li>
<li><code>/filename.php5</code></li>
<li><code>/windows.PHP</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>/fish*.php</code></td>
<td>
<p>
匹配包含 <code>/fish</code> 和 <code>.php</code>（按此顺序）的任何路径。
</p>
<p><span>匹配项：</span></p>
<ul>
<li><code>/fish.php</code></li>
<li><code>/fishheads/catfish.php?parameters</code></li>
</ul>
<p>
<span>不匹配项：</span></p>
<code>/Fish.PHP</code>
</td>
</tr>
</tbody>
</table>

## 规则的优先顺序

匹配 robots.txt 规则与网址时，抓取工具会根据规则路径的长度使用最具体的规则。如果规则（包括使用通配符的规则）存在冲突，Google 将使用限制性最弱的规则。

以下示例演示了 Google 抓取工具会对特定网址应用什么规则。

<table>
<thead>
<tr>
<th colspan="2">示例情况</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>https://example.com/page</code></td>
<td>
<div></div><pre>allow: /p
disallow: /</pre>
<p>
<b>适用规则</b>：<code>allow: /p</code>，因为它更具体。
</p>
</td>
</tr>
<tr>
<td><code>https://example.com/folder/page</code></td>
<td>
<div></div><pre>allow: /folder
disallow: /folder</pre>
<p>
<b>适用规则</b>：<code>allow: /folder</code>，因为规则存在冲突时，Google 会使用限制性最弱的规则。
</p>
</td>
</tr>
<tr>
<td><code>https://example.com/page.htm</code></td>
<td>
<div></div><pre>allow: /page
disallow: /*.htm</pre>
<p>
<b>适用规则</b>：<code>disallow: /*.htm</code>，因为该规则路径更长，并且它与网址中的字符匹配得更多，因此更具体。
</p>
</td>
</tr>
<tr>
<td><code>https://example.com/page.php5</code></td>
<td>
<div></div><pre>allow: /page
disallow: /*.ph</pre>
<p>
<b>适用规则</b>：<code>allow: /page</code>，因为规则存在冲突时，Google 会使用限制性最弱的规则。
</p>
</td>
</tr>
<tr>
<td><code>https://example.com/</code></td>
<td>
<div></div><pre>allow: /$
disallow: /</pre>
<p>
<b>适用规则</b>：<code>allow: /$</code>，因为它更具体。
</p>
</td>
</tr>
<tr>
<td><code>https://example.com/page.htm</code></td>
<td>
<div></div><pre>allow: /$
disallow: /</pre>
<p>
<b>适用规则</b>：<code>disallow: /</code>，因为 <code>allow</code> 规则仅适用于根网址。
</p>
</td>
</tr>
</tbody>
</table>
