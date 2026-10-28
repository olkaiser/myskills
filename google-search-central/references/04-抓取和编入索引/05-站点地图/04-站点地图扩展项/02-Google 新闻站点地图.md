# Google 新闻站点地图

> 来源：https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap?hl=zh-cn  
> 最后更新时间 (UTC)：2026-02-20。

如果您是一家新闻发布商，可使用 Google 新闻站点地图将您的新闻报道和其他相关信息告知 Google。您既可以使用 Google 新闻专用标记扩展现有站点地图，也可以创建单独的 Google 新闻站点地图，专供您的新闻报道使用。这两种方案对 Google 来说都没有问题。不过，如果为您的新闻报道创建单独的站点地图，可通过 Search Console 更好地跟踪您在 Google 搜索中的内容。

## Google 新闻站点地图最佳实践

由于 Google 新闻站点地图基于常规站点地图，因此[常规站点地图最佳实践](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=zh-cn#general-guidelines)也适用于 Google 新闻站点地图。

发布新的报道时，请更新 Google 新闻站点地图。不要每次更新都创建新的 Google 新闻站点地图。Google 新闻抓取 Google 新闻站点地图的频率与抓取网站其他内容的频率相同。

仅添加过去两天内创建的文章的近期网址。报道发布超过两天后，请从 Google 新闻站点地图中移除这些网址，或从旧网址中移除站点地图中的 `<news:news>` 元数据。

如果您选择从 Google 新闻站点地图中移除旧网址，则可能意味着您的站点地图会在一段时间内（例如，您在过去几天内没有发布报道）为空。您可能会在 Search Console 中看到空站点地图警告，但这只是为了确保这是代表您有意为之。如果文件为空，不会导致 Google 搜索出现任何问题。

## Google 新闻站点地图示例

以下示例显示的是具有新闻扩展的常规站点地图。其中包含一个 `<url>` 标记和一个 `<news:news>` 标记及其必需的子标记：

```scdoc
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
  <url>
  <loc>http://www.example.org/business/article55.html</loc>
  <news:news>
    <news:publication>
      <news:name>The Example Times</news:name>
      <news:language>en</news:language>
    </news:publication>
    <news:publication_date>2008-12-23</news:publication_date>
    <news:title>Companies A, B in Merger Talks</news:title>
  </news:news>
  </url>
</urlset>
```

## Google 新闻站点地图引用

`news` 标记在 Google 新闻站点地图命名空间中定义：[`http://www.google.com/schemas/sitemap-news/0.9`](http://www.google.com/schemas/sitemap-news/0.9?hl=zh-cn)

为确保 Google 能够使用您的 Google 新闻站点地图，您必须使用以下必需的标记：

<table>
<tbody><tr>
<th colspan="2">必需的标记</th>
</tr>
<tr>
<td><code>&lt;news:news&gt;</code></td>
<td>
<code>news:</code> 命名空间中其他标记的父标记。每个 <code>url</code> 站点地图标记只能有一个 <code>news:news</code> 标记（以及相应的结束标记），一个站点地图最多可包含 1,000 个 <code>news:news</code> 标记。如果一个 Google 新闻站点地图中的 <code>&lt;news:news&gt;</code> 标记数量超过 1,000 个，请<a href="https://developers.google.com/search/docs/crawling-indexing/sitemaps/large-sitemaps?hl=zh-cn">将站点地图拆分成多个较小的站点地图</a>。
</td>
</tr>
<tr>
<td><code>&lt;news:publication&gt;</code></td>
<td>
<p>
<code>&lt;news:name&gt;</code> 和 <code>&lt;news:language&gt;</code> 标记的父标记。每个 <code>&lt;news:news&gt;</code> 父标记只能有一个 <code>&lt;news:publication&gt;</code> 标记。
</p>
</td>
</tr>
<tr>
<td><code>&lt;news:name&gt;</code></td>
<td>
<p>
<code>&lt;news:name&gt;</code> 标记是新闻发布内容的名称。此名称必须与 <a href="https://news.google.com/?hl=zh-cn">news.google.com</a> 上的报道中显示的名称完全一致（省略圆括号中的部分）。
</p>
</td>
</tr>
<tr>
<td><code>&lt;news:language&gt;</code></td>
<td>
<p>
<code>&lt;news:language&gt;</code> 是发布内容所使用的语言，采用 <a href="http://www.loc.gov/standards/iso639-2/php/code_list.php">ISO 639 语言代码</a>（由两个或三个字母组成）。
</p>
<p>
<b>例外情况</b>：简体中文请使用 <code>zh-cn</code>，繁体中文请使用 <code>zh-tw</code>。
</p>
</td>
</tr>
<tr>
<td><code>&lt;news:publication_date&gt;</code></td>
<td>
<p>
采用 <a href="http://www.w3.org/TR/NOTE-datetime">W3C 格式</a>的报道发布日期。采用“完整日期”格式 (<code>YYYY-MM-DD</code>) 或含时区标识符的“完整日期加时、分和秒”格式 (<code>YYYY-MM-DDThh:mm:ssTZD</code>)。请指明报道在您的网站上首次发布的原始日期和时间，而非报道添加到站点地图的时间。
</p>
<p>Google 接受以下任意格式：</p>
<ul>
<li>完整日期：<code>YYYY-MM-DD (1997-07-16)</code></li>
<li>
完整日期加时、分：<code>YYYY-MM-DDThh:mmTZD (1997-07-16T19:20+01:00)</code>
</li>
<li>
完整日期加时、分、秒：<code>YYYY-MM-DDThh:mm:ssTZD (1997-07-16T19:20:30+01:00)</code>
</li>
<li>
完整日期加时、分、秒和秒的小数部分：<code>YYYY-MM-DDThh:mm:ss.sTZD</code> (<code>1997-07-16T19:20:30.45+01:00</code>)
</li>
</ul>
</td>
</tr>
<tr>
<td><code>&lt;news:title&gt;</code></td>
<td>
<p>新闻报道的标题。</p>
<aside>
<b>提示：</b>在各种设备中显示报道时，Google 可能会出于空间原因而缩短新闻报道的标题。请提供报道显示在您网站上的标题。请勿在 <code>&lt;news:title&gt;</code> 标记中添加作者姓名、发布内容名称或发布日期。详细了解如何<a href="https://developers.google.com/search/docs/appearance/title-link?hl=zh-cn">创建有效标题</a>。
</aside>
</td>
</tr>
</tbody></table>

## 站点地图问题排查

如果您在站点地图方面遇到问题，可以使用 Google Search Console 调查错误。
如需帮助，请参阅 Search Console 的[站点地图问题排查指南](https://support.google.com/webmasters/answer/7451001?hl=zh-cn#errors)。

## 其他资源

希望了解更多信息？请参阅以下资源：

- [将站点地图提交给 Google](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=zh-cn#addsitemap)
- [了解如何结合使用站点地图扩展](https://developers.google.com/search/docs/crawling-indexing/sitemaps/combine-sitemap-extensions?hl=zh-cn)
