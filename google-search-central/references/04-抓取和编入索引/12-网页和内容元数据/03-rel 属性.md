# 向 Google 说明您的出站链接的用意

> 来源：https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links?hl=zh-cn  
> 最后更新时间 (UTC)：2026-03-08。

对于您网站上的某些链接，您可能需要向 Google 说明您的网站与链接页之间的关系。为此，请在 `<a>` 标记中使用下列 `rel` 属性值之一。

对于您希望 Google 无任何限定条件便直接提取和解析的常规链接，您无需添加 `rel` 属性。例如：

```
<p>My favorite horse is the <a href="https://horses.example.com/Palomino">palomino</a>.</p>
```

对于其他链接，请使用以下一个或多个值：

<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th colspan="2"><code>rel</code> 值</th>
</tr>
</thead>
<tbody>
<tr>
<td><h3><code>rel="sponsored"</code></h3></td>
<td>
<p>请使用 <code>sponsored</code> 值标记广告链接或付费展示位置链接（通常称为“付费链接”<i></i>）。详细了解 <a href="https://developers.google.com/search/docs/essentials/spam-policies?hl=zh-cn#link-spam">Google 对付费链接的态度</a>。</p>
<div></div><pre>&lt;a <b>rel="sponsored"</b> href="https://cheese.example.com/Appenzeller_cheese"&gt;Appenzeller&lt;/a&gt;</pre>
<aside><b>注意：</b>对于这类链接，<a href="https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify?hl=zh-cn">以前推荐</a>使用 <code>nofollow</code> 属性，现在，您仍可以使用该属性进行标记，但更建议您使用 <code>sponsored</code> 标记。</aside>
</td>
</tr>
<tr>
<td><h3><code>rel="ugc"</code></h3></td>
<td>
<p>建议您使用 <code>ugc</code> 值标记用户生成的内容（例如评论和论坛帖子）的链接。</p>
<div></div><pre>&lt;a <b>rel="ugc"</b> href="https://cheese.example.com/Appenzeller_cheese"&gt;Appenzeller&lt;/a&gt;</pre>
<p>如果您想对值得信赖的贡献者（始终如一地做出高质量贡献的成员或用户）表示认可和奖励，则可从他们发布的链接中移除此属性。 详细了解如何<a href="https://developers.google.com/search/docs/monitor-debug/prevent-abuse?hl=zh-cn">防止网站和平台存在用户生成的垃圾内容</a>。</p>
</td>
</tr>
<tr>
<td><h3><code>rel="nofollow"</code></h3></td>
<td>
<p>如果其他值不适用，并且您希望 Google 不跟踪您网站上的出站链接，或不从您的网站上抓取链接页，请使用 <code>nofollow</code> 值。对于您网站中的链接，请使用 <a href="https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt?hl=zh-cn#disallow">robots.txt <code>disallow</code> 规则</a>。</p>
<div></div><pre>&lt;a <b>rel="nofollow"</b> href="https://cheese.example.com/Appenzeller_cheese"&gt;Appenzeller&lt;/a&gt;</pre>
</td>
</tr>
<tr>
<td><h3><i></i>多个值</h3></td>
<td>
<p>您可以使用以空格或英文逗号分隔的列表，指定多个 <code>rel</code> 值。<b>示例</b>：</p>
<div></div><pre>&lt;p&gt;I love &lt;a <b>rel="ugc nofollow"</b> href="https://cheese.example.com/Appenzeller_cheese"&gt;Appenzeller&lt;/a&gt; cheese.&lt;/p&gt;</pre>
<div></div><pre>&lt;p&gt;I hate &lt;a <b>rel="ugc,nofollow"</b> href="https://cheese.example.com/blue_cheese"&gt;Blue&lt;/a&gt; cheese.&lt;/p&gt;</pre>
</td>
</tr>
</tbody>
</table>

Google 通常不会跟踪标有这些 `rel` 属性的链接。请注意，链接页也可能经由其他途径找到（例如站点地图或其他网站的出站链接），因此仍有可能被抓取。这些 `rel` 属性仅能在 [Google 可抓取的 `<a>` 元素](https://developers.google.com/search/docs/crawling-indexing/links-crawlable?hl=zh-cn#crawlable-links)中使用，但 `nofollow` 除外，该属性还可用作[漫游器 `meta` 标记](https://developers.google.com/search/docs/crawling-indexing/special-tags?hl=zh-cn)。

如果您不想让 Google 提取指向您的站内网页的链接，请使用 [robots.txt `disallow` 规则](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt?hl=zh-cn#disallow)。

如果您不想让 Google 将某个网页编入索引，请允许抓取并使用 [`noindex` robots 规则](https://developers.google.com/search/docs/crawling-indexing/block-indexing?hl=zh-cn)。
