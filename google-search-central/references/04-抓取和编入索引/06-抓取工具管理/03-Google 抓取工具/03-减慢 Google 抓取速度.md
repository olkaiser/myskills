# 减慢 Google 抓取速度

> 来源：https://developers.google.com/crawling/docs/crawlers-fetchers/reduce-crawl-rate?hl=zh-cn  
> 最后更新时间 (UTC)：2026-10-12。

Google 抓取工具基础架构采用先进的算法来确定网站的最佳抓取速度。我们的目标是，每次访问您的网站时都尽可能多地抓取网页，但不会过多地占用服务器的带宽。在某些情况下，Google 抓取您的网站可能会给您的基础架构带来沉重负载，或在服务中断期间产生不必要的费用。为了避免这种情况，您可以决定减少 Google 抓取工具发出的请求数量。

## 了解导致抓取量急剧增加的原因

抓取速度急剧提升可能是由于您网站的结构效率低下或网站存在其他问题。根据我们过去收到的报告，最常见的原因包括：

- 网站上网址的配置效率低下，这通常是由特定网站功能导致的：
  - 分面导航或其他排序和过滤功能
  - 包含特定日期的大量网址的日历
- [动态搜索广告定位条件](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors?hl=zh-cn#adsbot)

我们强烈建议您与托管公司联系，并查看服务器的近期访问日志，以了解流量的来源，看看是否属于上述导致抓取量急剧增加的常见原因。然后，请参阅我们关于[管理对分面导航网址的抓取](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation?hl=zh-cn)和[优化抓取效率](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors?hl=zh-cn#improve_crawl_efficiency)的指南。

## 紧急减少抓取器流量（紧急情况）

> **警告**：**警告**：减慢 Google 的抓取速度将会产生广泛的影响，请谨慎考虑。对于 Google 搜索，Googlebot 发现的新网页数量会减少，现有网页的刷新频率会降低（例如，价格和商品库存状况可能需要更长时间才能体现在 Google 搜索中），被移除的网页保留在索引中的时间可能会更长。对于 Google Ads，您的广告系列可能会被取消或暂停，并且您的广告可能无法投放。

如需在短时间内（例如几个小时或 1-2 天）紧急降低抓取速度，请向抓取请求返回 `500`、`503` 或 `429` HTTP 响应状态代码，而不是 `200`。

当 Google 的抓取基础架构遇到大量包含 `500`、`503` 或 `429` HTTP 响应状态代码的网址时（例如，如果您[停用了您的网站](https://developers.google.com/search/docs/crawling-indexing/pause-online-business?hl=zh-cn)）：

- **Google 会减慢对您网站整个主机名**（例如 `subdomain.example.com`）的抓取速度，包括会返回错误的网址和会返回内容的网址。
- 这些错误的数量减少后，**系统会自动重新提高抓取速度**。

在返回 `503` 或 `429` 状态代码时，您还可以包含 `Retry-After` HTTP 标头（如 [RFC 9110 HTTP 语义](https://www.rfc-editor.org/rfc/rfc9110.html#name-retry-after)中所定义），通过指定延迟秒数或绝对 UTC 日期和时间，来告知 Google 抓取工具何时可以重试请求：

- **延迟秒数**：

  ```http
  HTTP/1.1 503 Service Unavailable
  Retry-After: 120
  ```
- **绝对 UTC 日期和时间**：

  ```http
  HTTP/1.1 503 Service Unavailable
  Retry-After: Wed, 21 Oct 2026 07:28:00 GMT
  ```

> **警告**：**警告**：我们不建议您长时间（即超过 1-2 天）这么做，因为这可能会对您的网站在 Google 产品中的呈现效果产生负面影响。例如，对于 Google 搜索，如果 Googlebot 一连数天在同一网址上发现上述状态代码，可能会将该网址从 Google 索引中移除。

## 降低抓取速度的特殊请求

如果您的基础架构无法向 Google 抓取工具返回错误响应，您可以[提交特殊请求](https://search.google.com/search-console/googlebot-report?hl=zh-cn)来报告抓取速度异常偏高的问题，并在请求中说明适合您网站的最佳抓取速度。您不能请求提高抓取速度，并且评估和处理该请求可能需要几天时间。
