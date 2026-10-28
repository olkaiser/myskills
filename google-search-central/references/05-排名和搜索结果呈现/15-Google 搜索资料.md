# 向您的网站添加 Google 搜索资料徽章

> 来源：https://developers.google.com/search/docs/appearance/search-profiles?hl=zh-cn  
> 最后更新时间 (UTC)：2026-09-23。

如果您是拥有 Google 搜索资料的网站所有者、发布商或创作者，可以向网站添加一个徽章，以便于受众群体找到您的 Google 搜索资料。

![网站上的 Google 搜索资料徽章和 Google 上的 Google 搜索资料示例](https://developers.google.com/static/search/docs/images/search-profile-badge.png?hl=zh-cn)

## Google 搜索资料在 Google 上的运作方式

[Google 搜索资料](https://support.google.com/websearch/answer/16904498?hl=zh-cn)可将您在网络和社交平台上的内容整合到 Google 上的一个位置。当读者关注您的 Google 搜索资料后，您在 Google 搜索资料中关联的内容（例如您在 Instagram、TikTok、YouTube、X、Facebook 和您网站上的内容）就更有可能在 [Google 探索](https://developers.google.com/search/docs/appearance/google-discover?hl=zh-cn)中向您的受众群体展示。

## 向您的网站添加 Google 搜索资料徽章

[声明对 Google 搜索资料的所有权](https://support.google.com/websearch/answer/16904498?hl=zh-cn)后，您可以在自己的网站上添加 Google 搜索资料徽章，鼓励受众群体在整个网络中查找您的内容：

1. **查找您的 Google 搜索资料网址**。请使用以下网址格式，将 `handle` 替换为您的个人资料标识名：

   ```transact-sql
   https://profile.google.com/@handle
   ```
2. [**下载 Google 搜索资料徽章素材资源**](https://developers.google.com/static/search/shared/search-profile-website-badges.zip?hl=zh-cn)，并在决定徽章在网站上的放置位置时，遵循[品牌规范](#follow-brand-guidelines-and-best-practices)。
3. **将以下 HTML 代码段添加到您的网站：**

   ```transact-sql
   <a href="https://profile.google.com/@example"
      aria-label="Find us on Google Search">
     <img src="/path/to/google-search-badge.svg" alt="Google Search">
   </a>
   ```

   **备选方案：**如果您希望在文章署名、简报或个人简介链接中使用文字链接，请使用以下代码段：

   ```transact-sql
   <a href="https://profile.google.com/@example">Find us on Google Search</a>
   ```

## 遵循品牌规范和最佳实践

向您的网站添加 Google 搜索资料徽章时，请遵循以下品牌规范和最佳实践：

- **确保触摸目标符合无障碍标准：**在 Android 设备上，可点击目标的大小应至少为 48 × 48 dp；在 iOS 设备和网页上，可点击目标的大小应至少为 44 × 44 像素。
- **保持徽标完整性：**如果您使用的是 Google 提供的官方素材资源，请勿拉伸、扭曲、旋转或更改“字母 G 徽标”图标和 Google 搜索资料按钮的颜色。
- **避免混用单色徽章和彩色徽章：**例如，如果您使用的所有图标都是单色，那么“G”图标也应是单色。
- **保持徽章清晰度：**如果您想同时使用 Google 搜索资料徽章和[“首选来源”徽章](https://developers.google.com/search/docs/appearance/preferred-sources?hl=zh-cn)，请使用强调效果更显著的带标签 Google 搜索资料按钮，以便与“首选来源”徽章区分开来。请勿将用于 Google 搜索资料的“字母 G 徽标”图标与“首选来源”徽章搭配使用。

## 问题排查

如果您在向网站添加徽章时遇到问题，请在 [Google 搜索中心帮助社区](https://support.google.com/webmasters/community?hl=zh-cn)中发帖咨询。
