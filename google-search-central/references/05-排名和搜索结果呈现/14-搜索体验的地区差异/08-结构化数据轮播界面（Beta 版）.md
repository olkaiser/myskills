# 结构化数据轮播界面（Beta 版）

> 来源：https://developers.google.com/search/docs/appearance/structured-data/carousels-beta?hl=zh-cn  
> 最后更新时间 (UTC)：2026-10-09。

Google 会根据[结构化数据](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data?hl=zh-cn)了解网页上的内容，并使这些内容以更丰富的搜索结果形式呈现，称为“富媒体搜索结果”。本指南重点介绍一种[目前处于 Beta 版阶段的全新轮播界面富媒体搜索结果](https://developers.google.com/search/blog/2024/02/search-experiences-in-eea?hl=zh-cn)，这是一种类似于列表的富媒体搜索结果，用户可以水平滚动查看来自指定网站的更多实体（也称为“托管轮播界面”）。轮播界面中的每个图块都可能包含您网站上关于网页实体的价格、评分和图片的信息。

若要获得使用此 Beta 版富媒体搜索结果的资格，请添加 `ItemList` 结构化数据，并与以下至少一个受支持的结构化数据项搭配使用：

- [`LocalBusiness`](#localbusiness) 及其子类型，例如：
  - [`Restaurant`](https://schema.org/Restaurant)
  - [`Hotel`](https://schema.org/Hotel)
  - [`VacationRental`](https://schema.org/VacationRental)
- [`Product`](#product)
- [`Event`](#event)

将 `ItemList` 标记与支持的内容类型搭配使用时，轮播界面在 Google 搜索中会显示如下：

![新的轮播界面富媒体搜索结果](https://developers.google.com/static/search/blog/images/new-carousel-rich-result.png?hl=zh-cn)

## 功能可用性

此功能目前处于 Beta 版阶段，随着我们开发此功能，您可能会看到相应要求或指南发生变更。此功能同样仅面向[欧洲经济区](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:European_Economic_Area_(EEA)) (EEA) 国家/地区、土耳其和南非提供，支持桌面设备和移动设备。在 EEA 国家/地区，此体验适用于与酒店、民宿、地面交通、航班、本地商家、推荐活动（活动、游览）和商品相关的查询。在土耳其，此体验仅适用于与酒店、民宿和本地商家相关的查询。在南非，此体验适用于与酒店、民宿、推荐活动（活动、游览）、航班、商品、外卖、租车和巴士预订相关的查询。

如果您的商家为 EEA 或土耳其的用户提供服务，请填写相应的表单：

- 对于地面交通、酒店、民宿、本地商家和推荐活动（例如活动、游览）查询，请填写此 [Google 搜索聚合信息网站功能意向调查表](https://support.google.com/websearch/contact/search_aggregator_features?hl=zh-cn)。
- 对于航班功能，请填写此[航班查询意向调查表](https://support.google.com/travel/contact/flight_queries_interest?hl=zh-cn)。
- 对于[提供 CSS 计划的国家/地区](https://support.google.com/css-center/answer/7524491?hl=zh-cn#Supported_countries)的商品查询，请开始使用[购物比较服务 (CSS) 计划](https://support.google.com/css-center/answer/7524491?hl=zh-cn)。

如果您的商家位于南非，请填写 [Google 搜索南非标记和优化条状标签意向调查表](https://docs.google.com/forms/d/e/1FAIpQLSeio2rTpaGNFohJQNKRDLQENyfK5avJFGJSx1nguoRwqsocIQ/viewform?hl=zh-cn)。

## 添加结构化数据

结构化数据是一种提供网页相关信息并对网页内容进行分类的标准化格式。如果您不熟悉结构化数据，可以详细了解[结构化数据的运作方式](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data?hl=zh-cn)。

下面概述了如何向网站中添加结构化数据。

1. 选择一个摘要页面，其中包含有关列表中每个实体的一些信息。
   例如，一个列出“巴黎热门酒店”的类别网页，并提供指向您网站上具体详情页面的链接，以便用户详细了解每家酒店。您可以根据场景的需要，混合搭配不同类型的实体（例如酒店、餐馆）。例如，如果您有一篇“瑞士的推荐活动”文章，其中同时列出了本地活动和本地商家。
2. 向该摘要页面添加[必需的属性](#structured-data-type-definitions)。您无需向详情页面添加标记，即可使用此 Beta 版功能。
   根据您使用的格式，了解[在网页上的什么位置插入结构化数据](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data?hl=zh-cn#format-placement)。

   > **注意**：**使用了 CMS？**使用集成到 CMS 中的插件可能更简单。
   >   
   > **使用了 JavaScript？**了解如何[使用 JavaScript 生成结构化数据](https://developers.google.com/search/docs/appearance/structured-data/generate-structured-data-with-javascript?hl=zh-cn)。
3. 根据轮播界面所涉及的具体内容类型，添加必需属性和建议属性：
   - [`LocalBusiness`](#localbusiness) 及其子类型，例如：
     - [`Restaurant`](https://schema.org/Restaurant)
     - [`Hotel`](https://schema.org/Hotel)
     - [`VacationRental`](https://schema.org/VacationRental)
   - [`Product`](#product)
   - [`Event`](#event)

   您可以根据具体情况选择最合适的类型。例如，如果您的网页上有酒店和民宿列表，请同时使用 `Hotel` 和 `VacationRental` 类型。虽然最好使用最接近您的使用场景的类型，但您可以选择使用更通用的类型（例如，`LocalBusiness`）。
4. 遵循[指南](#guidelines)。
5. 使用[富媒体搜索结果测试](https://search.google.com/test/rich-results?hl=zh-cn)验证您的代码。
6. 部署一些包含您的结构化数据的网页，然后使用[网址检查工具](https://support.google.com/webmasters/answer/9012289?hl=zh-cn)测试 Google 看到的网页样貌。请确保您的网页可供 Google 访问，不会因 robots.txt 文件、`noindex` 标记或登录要求而被屏蔽。如果网页看起来没有问题，您可以[请求 Google 重新抓取您的网址](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl?hl=zh-cn)。

   > **注意**：**注意**：重新抓取和重新编入索引需要一段时间，请耐心等待。请注意，网页发布后，Google 可能需要几天时间才会找到和抓取该网页。
7. 为了让 Google 随时了解日后发生的更改，我们建议您[提交站点地图](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap?hl=zh-cn)。[Search Console Sitemap API](https://developers.google.com/webmaster-tools/search-console-api-original/v3/sitemaps?hl=zh-cn) 可以帮助您自动执行此操作。

## 指南

为使您的网页能够显示为轮播界面富媒体搜索结果（Beta 版），您必须遵循[搜索要素指南](https://developers.google.com/search/docs/essentials?hl=zh-cn)和[结构化数据常规指南](https://developers.google.com/search/docs/guides/sd-policies?hl=zh-cn)。此外，轮播界面富媒体搜索结果（Beta 版）还需要遵循以下指南：

- 允许使用通用类型。不过，如需使用建议的属性，您必须使用相应的类型。例如，如需使用 `amenityFeature`，请使用 `LodgingBusiness` 类型。
- 允许使用额外字段，但这些字段可能不会出现在富媒体搜索结果中。
- 您的网站必须有一个摘要页面和多个详情页面。目前，此功能并不支持其他场景，例如“详情”为同一页面中锚点的一体化页面。
- 该标记必须位于摘要或类别页面上，该页面是类似于列表的页面，其中包含至少三个实体的相关信息，然后链接到您网站上的其他网页，以提供有关这些实体的更多信息。虽然您无需向详情页面添加标记，但必须在摘要页面的标记中添加详情页面网址。
- 标记摘要或类别页面上的所有项目。对于分页类别，请向每个后续页面添加 `ItemList`，并添加该页面上列出的实体。对于无限滚动，请重点标记在视口中初始加载的实体。

## 示例

以下是轮播界面的概要结构。轮播式富媒体搜索结果中的图块将按照标记中指定的顺序排序。

<html>
<head>
<title>Top 5 Restaurants in Italy</title>
<script type="application/ld+json">
{
"@context": "https://schema.org",
"@type": "ItemList",
"itemListElement": [
{
"@type": "ListItem",
"position": 1,
"item": {
"@type": "Restaurant",
"name": "Trattoria Luigi",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"priceRange": "$$$",
"servesCuisine": "Italian",
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.5,
"reviewCount": 250
},
"url": "https://www.example.com/trattoria-luigi"
}
},
{
"@type": "ListItem",
"position": 2,
"item": {
"@type": "Restaurant",
"name": "La Pergola",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"priceRange": "$$$",
"servesCuisine": "Italian",
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.9,
"reviewCount": 1150
},
"url": "https://www.example.com/la-pergola"
}
},
{
"@type": "ListItem",
"position": 3,
"item": {
"@type": "Restaurant",
"name": "Pasta e Basta",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"priceRange": "$$$",
"servesCuisine": "Italian",
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.2,
"reviewCount": 690
},
"url": "https://www.example.com/pasta-e-basta"
}
}
]
}
</script>
</head>
<body>
</body>
</html>
  

```
  <html>
    <head>
      <title>Top 5 Restaurants in Italy</title>
      <script type="application/ld+json">
        {
        "@context": "https://schema.org",
        "@type": "ItemList",
          "itemListElement": [
            {
              "@type": "ListItem",
                "position": 1,
                "item": {
                  "@type": "Restaurant",
                  "name": "Trattoria Luigi",
                  "image": [
                    "https://example.com/photos/1x1/photo.jpg",
                    "https://example.com/photos/4x3/photo.jpg",
                    "https://example.com/photos/16x9/photo.jpg"
                  ],
                  "priceRange": "$$$",
                  "servesCuisine": "Italian",
                  "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": 4.5,
                    "reviewCount": 250
                  },
                "url": "https://www.example.com/trattoria-luigi"
              }
            },
            {
              "@type": "ListItem",
                "position": 2,
                "item": {
                  "@type": "Restaurant",
                  "name": "La Pergola",
                  "image": [
                    "https://example.com/photos/1x1/photo.jpg",
                    "https://example.com/photos/4x3/photo.jpg",
                    "https://example.com/photos/16x9/photo.jpg"
                  ],
                  "priceRange": "$$$",
                  "servesCuisine": "Italian",
                  "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": 4.9,
                    "reviewCount": 1150
                  },
                "url": "https://www.example.com/la-pergola"
              }
            },
            {
              "@type": "ListItem",
              "position": 3,
              "item": {
                "@type": "Restaurant",
                "name": "Pasta e Basta",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "priceRange": "$$$",
                "servesCuisine": "Italian",
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.2,
                  "reviewCount": 690
                },
              "url": "https://www.example.com/pasta-e-basta"
              }
            }
          ]
        }
      </script>
    </head>
    <body>
    </body>
  </html>
  
```

## 不同结构化数据类型的定义

要使您的内容能够显示为富媒体搜索结果，您必须为其添加必需属性。您还可添加建议属性，以便添加与内容相关的更多信息，进而提供更优质的用户体验。

### `ItemList`

`ItemList` 是用于存放列表中所有元素的容器项。列表中元素的所有网址都必须指向同一网域中的不同网页。

如需了解 `ItemList` 的完整定义，请访问 [schema.org/ItemList](https://schema.org/ItemList)。

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">必要属性</th></tr>
</thead>
<tbody>
<tr>
<td><code>itemListElement</code></td>
<td>
<p><a href="https://schema.org/ListItem"><code>ListItem</code></a>
</p>
<p>
包含各个项的列表。如需指定列表，请定义一个包含至少三个 <code>itemListElement.item</code> 元素的 <code>ItemList</code>。
</p>
</td>
</tr>
<tr>
<td><code>itemListElement.item</code>
</td>
<td>
<p><code>LocalBusiness</code>、<code>Product</code> 或 <code>Event</code> 的子类型
</p>
<p>
列表中的单个项。请使用以下元素填充此对象：
</p>
<ul>
<li>所有轮播界面都必须具有的<a href="#common">常规属性</a>（<code>image</code>、<code>url</code>、<code>name</code>）</li>
<li>此数据类型所需的所有其他属性，如您的内容类型文档所述：
<ul>
<li><a href="#localbusiness"><code>LocalBusiness</code> 及其子类型</a></li>
<li><a href="#product"><code>Product</code></a></li>
<li><a href="#event"><code>Event</code></a></li>
</ul>
</li>
</ul>
<p>
<b>示例</b>：对于酒店，请提供 <code>priceRange</code> 和 <code>amenityFeature</code> 属性。
</p>
</td>
</tr>
<tr>
<td><code>itemListElement.position</code>
</td>
<td>
<p>
<a href="https://schema.org/Integer"><code>Integer</code></a>
</p>
<p>
该项在轮播界面中的位置。应为一个数字，从 1 开始。
</p>
</td>
</tr>
</tbody>
</table>

### 通用列表项属性（`LocalBusiness`、`Product,` 或 `Event`）

所有轮播项类型都具有以下通用属性。

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">必要属性</th></tr>
</thead>
<tbody>
<tr>
<td><code>image</code></td>
<td>
<p>重复的 <code><a href="https://schema.org/URL">URL</a></code> 或 <code><a href="https://schema.org/ImageObject">ImageObject</a></code>
</p>
<p>
相关实体或项目的一张或多张图片（例如酒店的图片）。请勿在此图片属性中添加徽标。
</p>
<p>其他的图片指南：
</p><ul>
<li>每个网页必须包含至少 1 张图片（无论您是否添加了标记）。Google 将根据宽高比和分辨率挑选最合适的图片显示在搜索结果中。</li>
<li>图片网址必须可抓取且可编入索引。如需检查 Google 能否访问您的网址，请使用<a href="https://support.google.com/webmasters/answer/9012289?hl=zh-cn">网址检查工具</a>。</li>
<li>图片必须代表标记的内容。</li>
<li>图片必须采用<a href="https://developers.google.com/search/docs/appearance/google-images?hl=zh-cn#supported-image-formats">受 Google 图片支持</a>的文件格式。</li>
<li>为取得最佳效果，建议您提供具有以下宽高比的多个高分辨率图片（宽度乘以高度至少为 50K 像素）：16x9、4x3 和 1x1。</li>
</ul>
<p>例如：</p>
<div></div><pre>"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
]</pre>
</td>
</tr>
<tr>
<td><code>name</code></td>
<td>
<p>
<a href="https://schema.org/Text"><code>Text</code></a>
</p>
<p>
实体或项目的字符串名称。例如，酒店或民宿商家信息的名称。<code>item.name</code> 在轮播界面中显示为单个项的标题。HTML 格式会被忽略。</p>
</td>
</tr>
<tr>
<td><code>url</code></td>
<td>
<p>
<a href="https://schema.org/URL"><code>URL</code></a>
</p>
<p>
项目详情页面的规范网址（例如，摘要页面中引用的单个酒店或民宿商家信息的独立页面）。列表中的所有网址都必须是独一无二的，但属于同一网域（与摘要网页相同的网域或子网域/超级网域）。</p>
<aside>不支持摘要页面或类别页面内的锚链接；您的网站必须为列表中的每一项提供独立的详情页面。</aside>
</td>
</tr>
</tbody>
</table>

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">建议属性</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>aggregateRating.bestRating</code>
</td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
相应评分体系中允许的最高值（例如 <code>5 / 10</code>）。如果省略 <code>bestRating</code>，系统会假定为 <code>5</code>。
</p>
</td>
</tr>
<tr>
<td>
<code>aggregateRating.ratingCount</code>
</td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
相应项在您的网站上获得的评分总数。
</p>
</td>
</tr>
<tr>
<td>
<code>aggregateRating.ratingValue</code>
</td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code> 或 <code><a href="https://schema.org/Text">Text</a></code></p>
<p>相应项的质量评分（以数字表示），可以是数字、分数或百分比（例如 <code>4</code>、<code>60%</code> 或 <code>6 / 10</code>）。Google 能够理解分数和百分比的分制，因为分数本身或百分比就暗含了分制。数字的默认分制为 5 分制，1 为最低值，5 为最高值。如需采用其他分制，请使用 <code>bestRating</code> 和 <code>worstRating</code>。</p>
<p>对于十进制数，请使用句点（而非英文逗号）来指定值（例如，使用 <code>4.4</code> 而不是 <code>4,4</code>）。在微数据和 RDFa 中，您可以使用 <code>content</code> 属性替换可见内容。这样，您就可以向用户显示任何样式惯例，同时满足结构化数据的句点要求。 例如：</p>
<div></div><pre>&lt;span itemprop="ratingValue" content="4.4"&gt;4,4&lt;/span&gt; stars</pre>
</td>
</tr>
</tbody>
</table>

### 其他特定于类型的属性定义

#### `LocalBusiness`（和子类型）

对于轮播界面富媒体搜索结果，除了 [`ListItem` 属性](#listitem)之外，Google 还支持以下 `LocalBusiness` 属性（包括其子类型）。请将这些属性嵌套在 `itemListElement.item` 下。

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">建议属性</th></tr>
</thead>
<tbody>
<tr>
<td><code>amenityFeature</code></td>
<td>
<p>
<a href="https://schema.org/LocationFeatureSpecification"><code>LocationFeatureSpecification</code></a>
</p>
<p><b>仅适用于 <code>LodgingBusiness</code></b>：住宿的设施特征（例如特色或服务）。</p>
<div></div><pre><span>"amenityFeature"</span><span>:</span><span> </span><span>{</span>
<span> </span><span>"@type"</span><span>:</span><span> </span><span>"LocationFeatureSpecification"</span><span>,</span>
<span> </span><span>"name"</span><span> </span><span>:</span><span> </span><span>"beachAccess"</span><span>,</span>
<span> </span><span>"value"</span><span>:</span><span> </span><span>true</span>
<span>}</span></pre>
</td>
</tr>
<tr>
<td><code>priceRange</code></td>
<td>
<p>
<a href="https://schema.org/Text"><code>Text</code></a>
</p>
<p>
商家的相对价格范围，通常由货币符号的标准化值指定。请使用以下任一格式提供价格范围：
</p>
<ul>
<li><b>价位：</b>例如“$”，“$$", "$$$”</li>
<li><b>范围：</b>例如“$-$$”</li>
</ul>
<p>
此字段的长度必须少于 12 个字符。如果字符数超过 12 个，Google 就不会显示商家的价格范围。</p>
</td>
</tr>
<tr>
<td><code>servesCuisine</code></td>
<td>
<p>
<a href="https://schema.org/Text"><code>Text</code></a>
</p>
<p><b>仅适用于餐馆</b>：餐馆供应的菜肴种类。</p>
</td>
</tr>
</tbody>
</table>

#### `Product`

对于轮播界面富媒体搜索结果，除了 [`ListItem` 属性](#listitem)之外，Google 还支持以下 `Product` 属性。请将这些属性嵌套在 `itemListElement.item` 下。

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">建议属性</th></tr>
</thead>
<tbody>
<tr>
<td><code>offers</code></td>
<td>
<p><a href="https://schema.org/Offer"><code>Offer</code></a> 或 <a href="https://schema.org/AggregateOffer"><code>AggregateOffer</code></a></p>
<p>用于销售商品的嵌套 <code>Offer</code> 或 <code>AggregateOffer</code>。请根据您的内容，为 <code>Offer</code> 或 <code>AggregateOffer</code> 添加建议属性。</p>
<p>如果您使用的是 <code>Offer</code>，请添加以下属性：</p>
<ul>
<li><code>offers.price</code></li>
<li><code>offers.priceCurrency</code></li>
</ul>
<p>如果您使用的是 <code>AggregateOffer</code>，请添加以下属性：</p>
<ul>
<li><code>offers.highPrice</code></li>
<li><code>offers.lowPrice</code></li>
<li><code>offers.priceCurrency</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>offers.highPrice</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
所有有效出价中的最高价格。如果您使用 <code>price</code> 指定单个价格，则无需添加 <code>highPrice</code> 和 <code>lowPrice</code> 属性。
</p>
</td>
</tr>
<tr>
<td><code>offers.lowPrice</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
所有有效出价中的最低价格。如果您使用 <code>price</code> 指定单个价格，则无需添加 <code>highPrice</code> 和 <code>lowPrice</code> 属性。
</p>
</td>
</tr>
<tr>
<td><code>offers.price</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
商品或价格组成部分（当附加到 <code>PriceSpecification</code> 及其子类型时）的优惠价格。如果您使用 <code>lowPrice</code> 和 <code>highPrice</code> 指定价格范围，请勿添加 <code>price</code> 属性。
</p>
</td>
</tr>
<tr>
<td><code>offers.priceCurrency</code></td>
<td>
<p>
<a href="https://schema.org/Text"><code>Text</code></a>
</p>
<p>
用于描述商品价格的货币，采用由三个字母表示的 <a href="https://en.wikipedia.org/wiki/ISO_4217">ISO 4217</a> 格式。 如果未提供货币，Google 会默认选择 <code>USD</code>。
</p>
</td>
</tr>
</tbody>
</table>

#### `Event`

对于轮播界面富媒体搜索结果，除了 [`ListItem` 属性](#listitem)之外，Google 还支持以下 `Event` 属性。请将这些属性嵌套在 `itemListElement.item` 下。

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">建议属性</th></tr>
</thead>
<tbody>
<tr>
<td><code>offers</code></td>
<td>
<p><code>Offer</code> 或 <code>AggregateOffer</code></p>
<p>用于销售活动门票的嵌套 <code>Offer</code> 或 <code>AggregateOffer</code>。请根据您的内容，为 <code>Offer</code> 或 <code>AggregateOffer</code> 添加建议属性。</p>
<p>如果您使用的是 <code>Offer</code>，请添加以下属性：</p>
<ul>
<li><code>offers.price</code></li>
<li><code>offers.priceCurrency</code></li>
</ul>
<p>如果您使用的是 <code>AggregateOffer</code>，请添加以下属性：</p>
<ul>
<li><code>offers.highPrice</code></li>
<li><code>offers.lowPrice</code></li>
<li><code>offers.priceCurrency</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>offers.highPrice</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
所有有效出价中的最高价格。如果您使用 <code>price</code> 指定单个价格，则无需添加 <code>highPrice</code> 和 <code>lowPrice</code> 属性。
</p>
</td>
</tr>
<tr>
<td><code>offers.lowPrice</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
所有有效出价中的最低价格。如果您使用 <code>price</code> 指定单个价格，则无需添加 <code>highPrice</code> 和 <code>lowPrice</code> 属性。
</p>
</td>
</tr>
<tr>
<td><code>offers.price</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
门票的价格，包括服务费和手续费。当价格发生变动或门票售罄时，请务必更新此值。如果您使用 <code>lowPrice</code> 和 <code>highPrice</code> 指定价格范围，请勿添加 <code>price</code> 属性。
</p>
<p>如果活动免费、无需手续费或服务费，请将 <code>price</code> 设置为 <code>0</code>。
</p>
<div></div><pre><span>"offers"</span><span>:</span><span> </span><span>{</span>
<span> </span><span>"@type"</span><span>:</span><span> </span><span>"Offer"</span><span>,</span>
<span> </span><span>"price"</span><span>:</span><span> </span><span>0</span>
<span>}</span></pre>
</td>
</tr>
<tr>
<td><code>offers.priceCurrency</code></td>
<td>
<p>
<a href="https://schema.org/Text"><code>Text</code></a>
</p>
<p>
用于描述活动门票的货币，采用由三个字母表示的 <a href="https://en.wikipedia.org/wiki/ISO_4217">ISO 4217</a> 格式。
如果未提供货币，Google 会默认选择 <code>USD</code>。
</p>
</td>
</tr>
</tbody>
</table>

## 常见场景示例

### `Restaurant` 示例

下面是一个 JSON-LD 格式的餐厅轮播界面示例。

<html>
<head>
<title>Top 5 Restaurants in Paris</title>
<script type="application/ld+json">
{
"@context": "https://schema.org",
"@type": "ItemList",
"itemListElement": [
{
"@type": "ListItem",
"position": 1,
"item": {
"@type": "Restaurant",
"name": "Trattoria Luigi",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"priceRange": "$$$",
"servesCuisine": "Italian",
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.5,
"reviewCount": 250
},
"url": "https://www.example.com/restaurant-location-1"
}
},
{
"@type": "ListItem",
"position": 2,
"item": {
"@type": "Restaurant",
"name": "La Pergola",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"priceRange": "$$$",
"servesCuisine": "Italian",
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.9,
"reviewCount": 1150
},
"url": "https://www.example.com/restaurant-location-2"
}
},
{
"@type": "ListItem",
"position": 3,
"item": {
"@type": "Restaurant",
"name": "Pasta e Basta",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"priceRange": "$$$",
"servesCuisine": "Italian",
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.2,
"reviewCount": 690
},
"url": "https://www.example.com/restaurant-location-3"
}
}
]
}
</script>
</head>
<body>
</body>
</html>
  

```
<html>
    <head>
      <title>Top 5 Restaurants in Paris</title>
      <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "ItemList",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "item": {
                "@type": "Restaurant",
                "name": "Trattoria Luigi",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "priceRange": "$$$",
                "servesCuisine": "Italian",
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.5,
                  "reviewCount": 250
                },
                "url": "https://www.example.com/restaurant-location-1"
              }
            },
            {
              "@type": "ListItem",
              "position": 2,
              "item": {
                "@type": "Restaurant",
                "name": "La Pergola",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "priceRange": "$$$",
                "servesCuisine": "Italian",
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.9,
                  "reviewCount": 1150
                },
                "url": "https://www.example.com/restaurant-location-2"
              }
            },
            {
              "@type": "ListItem",
              "position": 3,
              "item": {
                "@type": "Restaurant",
                "name": "Pasta e Basta",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "priceRange": "$$$",
                "servesCuisine": "Italian",
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.2,
                  "reviewCount": 690
                },
                "url": "https://www.example.com/restaurant-location-3"
              }
            }
          ]
        }
      </script>
    </head>
    <body>
    </body>
  </html>
```

### 住宿（`Hotels` 和 `VacationRental`）示例

下面是一个 JSON-LD 格式的住宿轮播界面示例。

<html>
<head>
<title>Top 5 Hotels in Paris</title>
<script type="application/ld+json">
{
"@context": "https://schema.org",
"@type": "ItemList",
"itemListElement": [
{
"@type": "ListItem",
"position": 1,
"item": {
"@type": "Hotel",
"name": "Four Seasons Hotel George V, Paris",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"priceRange": "$$$$",
"amenityFeature": {
"@type": "LocationFeatureSpecification",
"name" : "internetType",
"value": "Free"
},
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.9,
"reviewCount": 50
},
"url": "https://www.example.com/four-seasons"
}
},
{
"@type": "ListItem",
"position": 2,
"item": {
"@type": "VacationRental",
"name": "Downtown Condo",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"priceRange": "$$",
"amenityFeature": {
"@type": "LocationFeatureSpecification",
"name" : "instantBookable",
"value": true
},
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.7,
"reviewCount": 827
},
"url": "https://www.example.com/downtown-condo"
}
},
{
"@type": "ListItem",
"position": 3,
"item": {
"@type": "Hotel",
"name": "Ritz Paris",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"priceRange": "$$$$",
"amenityFeature": {
"@type": "LocationFeatureSpecification",
"name" : "freeBreakfast",
"value": true
},
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.9,
"reviewCount": 1290
},
"url": "https://www.example.com/ritz-paris"
}
}
]
}
</script>
</head>
<body>
</body>
</html>
  

```
<html>
    <head>
      <title>Top 5 Hotels in Paris</title>
      <script type="application/ld+json">
        {
        "@context": "https://schema.org",
        "@type": "ItemList",
            "itemListElement": [
              {
                "@type": "ListItem",
                "position": 1,
                "item": {
                  "@type": "Hotel",
                  "name": "Four Seasons Hotel George V, Paris",
                  "image": [
                    "https://example.com/photos/1x1/photo.jpg",
                    "https://example.com/photos/4x3/photo.jpg",
                    "https://example.com/photos/16x9/photo.jpg"
                  ],
                  "priceRange": "$$$$",
                  "amenityFeature": {
                      "@type": "LocationFeatureSpecification",
                      "name" : "internetType",
                      "value": "Free"
                  },
                  "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": 4.9,
                    "reviewCount": 50
                  },
                  "url": "https://www.example.com/four-seasons"
                }
              },
              {
                "@type": "ListItem",
                "position": 2,
                "item": {
                  "@type": "VacationRental",
                  "name": "Downtown Condo",
                  "image": [
                    "https://example.com/photos/1x1/photo.jpg",
                    "https://example.com/photos/4x3/photo.jpg",
                    "https://example.com/photos/16x9/photo.jpg"
                  ],
                  "priceRange": "$$",
                  "amenityFeature": {
                    "@type": "LocationFeatureSpecification",
                    "name" : "instantBookable",
                    "value": true
                  },
                  "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": 4.7,
                    "reviewCount": 827
                  },
                  "url": "https://www.example.com/downtown-condo"
                }
              },
              {
                "@type": "ListItem",
                "position": 3,
                "item": {
                  "@type": "Hotel",
                  "name": "Ritz Paris",
                  "image": [
                    "https://example.com/photos/1x1/photo.jpg",
                    "https://example.com/photos/4x3/photo.jpg",
                    "https://example.com/photos/16x9/photo.jpg"
                  ],
                  "priceRange": "$$$$",
                  "amenityFeature": {
                    "@type": "LocationFeatureSpecification",
                    "name" : "freeBreakfast",
                    "value": true
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.9,
                  "reviewCount": 1290
                },
                "url": "https://www.example.com/ritz-paris"
              }
            }
          ]
        }
      </script>
    </head>
    <body>
    </body>
  </html>
```

### 推荐活动示例

下面是一个 JSON-LD 格式的推荐活动轮播界面示例。

<html>
<head>
<title>Top 5 Things To Do in Paris</title>
<script type="application/ld+json">
{
"@context": "https://schema.org",
"@type": "ItemList",
"itemListElement": [
{
"@type": "ListItem",
"position": 1,
"item": {
"@type": "Event",
"name": "Paris Seine River Dinner Cruise",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"offers": {
"@type": "Offer",
"price": 45.00,
"priceCurrency": "EUR"
},
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.2,
"reviewCount": 690
},
"url": "https://www.example.com/event-location1"
}
},
{
"@type": "ListItem",
"position": 2,
"item": {
"@type": "LocalBusiness",
"name": "Notre-Dame Cathedral",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"priceRange": "$",
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.8,
"reviewCount": 4220
},
"url": "https://www.example.com/localbusiness-location"
}
},
{
"@type": "ListItem",
"position": 3,
"item": {
"@type": "Event",
"name": "Eiffel Tower With Host Summit Tour",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"offers": {
"@type": "Offer",
"price": 59.00,
"priceCurrency": "EUR"
},
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.9,
"reviewCount": 652
},
"url": "https://www.example.com/event-location2"
}
}
]
}
</script>
</head>
<body>
</body>
</html>
  

```
<html>
    <head>
      <title>Top 5 Things To Do in Paris</title>
      <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "ItemList",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "item": {
                "@type": "Event",
                "name": "Paris Seine River Dinner Cruise",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "offers": {
                  "@type": "Offer",
                  "price": 45.00,
                  "priceCurrency": "EUR"
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.2,
                  "reviewCount": 690
                },
                "url": "https://www.example.com/event-location1"
              }
            },
            {
              "@type": "ListItem",
              "position": 2,
              "item": {
                "@type": "LocalBusiness",
                "name": "Notre-Dame Cathedral",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "priceRange": "$",
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.8,
                  "reviewCount": 4220
                },
                "url": "https://www.example.com/localbusiness-location"
              }
            },
            {
              "@type": "ListItem",
              "position": 3,
              "item": {
                "@type": "Event",
                "name": "Eiffel Tower With Host Summit Tour",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "offers": {
                  "@type": "Offer",
                  "price": 59.00,
                  "priceCurrency": "EUR"
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.9,
                  "reviewCount": 652
                },
                "url": "https://www.example.com/event-location2"
              }
            }
          ]
        }
      </script>
    </head>
    <body>
    </body>
  </html>
  
```

### `Product` 示例

下面是一个 JSON-LD 格式的商品轮播界面示例。

<html>
<head>
<title>Top coats of the season</title>
<script type="application/ld+json">
{
"@context": "https://schema.org",
"@type": "ItemList",
"itemListElement": [
{
"@type": "ListItem",
"position": 1,
"item": {
"@type": "Product",
"name": "Puffy Coat Series by Goat Coat",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"offers": {
"@type": "AggregateOffer",
"lowPrice": 45.00,
"highPrice": 60.00,
"priceCurrency": "EUR"
},
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.9,
"reviewCount": 50
},
"url": "https://www.example.com/puffy-coats"
}
},
{
"@type": "ListItem",
"position": 2,
"item": {
"@type": "Product",
"name": "Wool Coat Series by Best Coats Around",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"offers": {
"@type": "AggregateOffer",
"lowPrice": 189.00,
"highPrice": 200.00,
"priceCurrency": "EUR"
},
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.7,
"reviewCount": 827
},
"url": "https://www.example.com/wool-coats"
}
},
{
"@type": "ListItem",
"position": 3,
"item": {
"@type": "Product",
"name": "Antartic Coat by Cold Coats",
"image": [
"https://example.com/photos/1x1/photo.jpg",
"https://example.com/photos/4x3/photo.jpg",
"https://example.com/photos/16x9/photo.jpg"
],
"offers": {
"@type": "Offer",
"price": 45.00,
"priceCurrency": "EUR"
},
"aggregateRating": {
"@type": "AggregateRating",
"ratingValue": 4.9,
"reviewCount": 1290
},
"url": "https://www.example.com/antartic-coat"
}
}
]
}
</script>
</head>
<body>
</body>
</html>
  

```
<html>
    <head>
      <title>Top coats of the season</title>
      <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "ItemList",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "item": {
                "@type": "Product",
                "name": "Puffy Coat Series by Goat Coat",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "offers": {
                  "@type": "AggregateOffer",
                  "lowPrice": 45.00,
                  "highPrice": 60.00,
                  "priceCurrency": "EUR"
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.9,
                  "reviewCount": 50
                },
                "url": "https://www.example.com/puffy-coats"
              }
            },
            {
              "@type": "ListItem",
              "position": 2,
              "item": {
                "@type": "Product",
                "name": "Wool Coat Series by Best Coats Around",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "offers": {
                  "@type": "AggregateOffer",
                  "lowPrice": 189.00,
                  "highPrice": 200.00,
                  "priceCurrency": "EUR"
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.7,
                  "reviewCount": 827
                },
                "url": "https://www.example.com/wool-coats"
              }
            },
            {
              "@type": "ListItem",
              "position": 3,
              "item": {
                "@type": "Product",
                "name": "Antartic Coat by Cold Coats",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "offers": {
                  "@type": "Offer",
                  "price": 45.00,
                  "priceCurrency": "EUR"
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.9,
                  "reviewCount": 1290
                },
                "url": "https://www.example.com/antartic-coat"
              }
            }
          ]
        }
      </script>
    </head>
    <body>
    </body>
  </html>
  
```

## 问题排查

如果您在实施或调试结构化数据时遇到问题，请查看下面列出的一些实用资源。

- 如果您使用了内容管理系统 (CMS) 或其他人负责管理您的网站，请向其寻求帮助。请务必向其转发列明问题细节的任何 Search Console 消息。
- Google 不能保证使用结构化数据的功能一定会显示在搜索结果中。如需查看导致 Google 无法将您的内容显示为富媒体搜索结果的各种常见原因，请参阅[结构化数据常规指南](https://developers.google.com/search/docs/appearance/structured-data/sd-policies?hl=zh-cn)。
- 您的结构化数据可能存在错误。请查看[结构化数据错误列表](https://support.google.com/webmasters/answer/13300873?hl=zh-cn)和[“无法解析的结构化数据”报告](https://support.google.com/webmasters/answer/9166415?hl=zh-cn)。
- 如果您的网页受到结构化数据手动操作的影响，其中的结构化数据将会被忽略（但该网页仍可能会出现在 Google 搜索结果中）。如需修正[结构化数据问题](https://support.google.com/webmasters/answer/9044175?hl=zh-cn#zippy=,structured-data-issue)，请使用[“人工处置措施”报告](https://support.google.com/webmasters/answer/9044175?hl=zh-cn)。
- 再次查看相关[指南](#guidelines)，确认您的内容是否未遵循指南。问题可能是因为出现垃圾内容或使用垃圾标记导致的。不过，问题可能不是语法问题，因此富媒体搜索结果测试无法识别这些问题。
- 结构化数据问题可能会影响网站内容在搜索结果中的显示方式。请参阅[针对富媒体搜索结果缺失/富媒体搜索结果总数下降进行问题排查](https://support.google.com/webmasters/answer/13300208?hl=zh-cn)指南，了解在 Search Console 中发现、修正和验证这些问题的分步方法。
- 请等待一段时间，以便 Google 重新抓取您的网页并重新将其编入索引。请注意，网页发布后，Google 可能需要几天时间才会找到和抓取该网页。有关抓取和索引编制的常见问题，请参阅 [Google 搜索抓取和索引编制常见问题解答](https://developers.google.com/search/help/crawling-index-faq?hl=zh-cn)。
- 在 [Google 搜索中心论坛](https://support.google.com/webmasters/community?hl=zh-cn)中发帖提问。
