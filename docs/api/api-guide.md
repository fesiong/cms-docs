# API 接口使用指南

## 一、快速入门

### 1.1 什么是 AICMS API

AICMS 是一个基于 Go 语言开发的开源内容管理系统，提供了完整的 API 接口供开发者调用。API 采用 RESTful 设计风格，支持 JSON 格式的数据交互，允许开发者通过 HTTP 请求与系统进行交互，获取、创建、更新或删除内容。

### 1.2 API 基础概念

- **API 基础路径**：`/api` - 所有 API 请求都需要以该路径为前缀
- **认证方式**：部分接口需要认证，使用 JWT Token 进行身份验证
- **请求格式**：除上传文件外，所有接口均使用 JSON 格式传输数据
- **响应格式**：统一使用 JSON 格式返回数据

### 1.3 第一个 API 调用示例

以获取文章列表为例，介绍一次完整的 API 调用流程：

```shell
GET /api/archive/list?limit=10&page=1 HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

**成功响应：**
```json
{
  "code": 0,
  "msg": "",
  "total": 100,
  "data": [...]
}
```

**错误处理：**
```json
{
  "code": -1,
  "msg": "API 接口未开放"
}
```

## 二、API 基础结构

### 2.1 API 基础路径和请求方式

所有 API 接口都通过以下基础路径访问：
```
{域名地址}/api/接口路径
```

例如：`https://www.aicms.com/api/archive/list`

API 支持的 HTTP 请求方式包括：
- **GET** - 获取数据
- **POST** - 创建数据或提交表单，更新数据、删除数据

### 2.2 认证方式

部分接口需要用户认证，系统采用 JWT Token 认证方式：

- 登录后获取 Token
- 在请求头中携带 Token
- 格式：`Token: {token}`

### 2.3 请求和响应格式

**请求格式：**
- 除文件上传外，所有接口使用 JSON 格式传输数据
- Content-Type: application/json
- GET 请求参数通过 URL Query 传递

**响应格式：**
```json
{
  "code": 0,
  "msg": "",
  "data": {}
}
```

### 2.4 通用请求头

所有 API 接口都遵循以下通用请求头规范：

| 字段名 | 类型 | 说明 |
|--------|------|------|
| Content-Type | string | 固定值：application/json |
| Token | string | JWT 认证令牌（需要认证的接口） |

## 三、API 部分接口分类详解

以下是 AICMS 提供的 API 接口分类，以及部分接口参数，更多的文档接口以及参数配置，请参考详细文档。

### 3.1 内容管理接口

内容管理接口用于处理网站的核心内容，包括文档、分类、标签等。

#### 3.1.1 [获取文档详情接口](archiveDetail.md)
- **接口路径**：`/api/archive/detail`
- **请求方式**：GET
- **功能**：获取单个文档详细信息
- **参数**：
  - `id` (int, 必填) - 文档ID
  - `filename` (string, 可选) - 文档URL别名(id/filename 二选一)
  - `render` (boolean, 可选) - 是否渲染内容成HTML(Markdown文档渲染),默认为true

#### 3.1.2 [获取文档列表接口](archiveList.md)
- **接口路径**：`/api/archive/list`
- **请求方式**：GET
- **功能**：获取文档列表
- **参数**：
  - `moduleId` (int, 可选) - 模型ID
  - `categoryId` (string, 可选) - 分类ID，多个可用逗号分隔
  - `limit` (int, 可选) - 显示数量
  - `page` (int, 可选) - 页码
  - `order` (string, 可选) - 排序方式，如 `id desc`

#### 3.1.3 [获取文档参数接口](archiveParams.md)
- **接口路径**：`/api/archive/params`
- **请求方式**：GET
- **功能**：获取文档自定义参数
- **参数**：
  - `id` (int, 必填) - 文档ID
  - `filename` (string, 可选) - 文档URL别名(id/filename 二选一)
  - `sorted` (int, 可选) - 返回格式，true为数组格式，false为对象格式

#### 3.1.4 [获取分类详情接口](categoryDetail.md)
- **接口路径**：`/api/category/detail`
- **请求方式**：GET
- **功能**：获取分类详细信息
- **参数**：
  - `id` (int, 可选) - 分类ID
  - `filename` (string, 可选) - 分类URL别名

#### 3.1.5 [获取分类列表接口](categoryList.md)
- **接口路径**：`/api/category/list`
- **请求方式**：GET
- **功能**：获取分类列表
- **参数**：
  - `moduleId` (int, 可选) - 模型ID
  - `parentId` (int, 可选) - 上级分类ID
  - `limit` (int, 可选) - 显示数量

#### 3.1.6 [获取标签列表接口](tagList.md)
- **接口路径**：`/api/tag/list`
- **请求方式**：GET
- **功能**：获取标签列表
- **参数**：
  - `itemId` (int, 可选) - 文档ID
  - `letter` (string, 可选) - 首字母筛选
  - `type` (string, 可选) - 返回类型

### 3.2 用户管理接口

用户管理接口用于处理用户注册、登录、信息管理等功能。

#### 3.2.1 [用户登录接口](login.md)
- **接口路径**：`/api/login`
- **请求方式**：POST
- **功能**：用户登录认证
- **参数**：
  - `user_name` (string, 可选) - 用户名
  - `password` (string, 可选) - 密码
  - `email` (string, 可选) - 邮箱
  - `phone` (string, 可选) - 手机号

#### 3.2.2 [用户注册接口](register.md)
- **接口路径**：`/api/register`
- **请求方式**：POST
- **功能**：新用户注册
- **参数**：
  - `user_name` (string, 可选) - 用户名
  - `password` (string, 可选) - 密码
  - `email` (string, 可选) - 邮箱
  - `phone` (string, 可选) - 手机号
  - `captcha` (string, 可选) - 验证码

#### 3.2.3 [获取用户详情接口](userDetail.md)
- **接口路径**：`/api/user/detail`
- **请求方式**：GET
- **功能**：获取用户详细信息
- **需要认证**：是

#### 3.2.4 [用户收藏管理](favorites.md)
- **获取收藏列表**：`/api/favorite/list`
- **添加收藏**：`/api/favorite/add`
- **检查收藏状态**：`/api/favorite/check`
- **移除收藏**：`/api/favorite/delete`

### 3.3 评论互动接口

评论互动接口用于处理用户评论和互动功能。

#### 3.3.1 [获取评论列表接口](commentList.md)
- **接口路径**：`/api/comment/list`
- **请求方式**：GET
- **功能**：获取评论列表
- **参数**：
  - `archive_id` (int, 可选) - 文档ID
  - `parent_id` (int, 可选) - 父评论ID
  - `limit` (int, 可选) - 显示数量

#### 3.3.2 [发布评论接口](commentPublish.md)
- **接口路径**：`/api/comment/publish`
- **请求方式**：POST
- **功能**：发布评论
- **需要认证**：是
- **参数**：
  - `archive_id` (int, 必填) - 文档ID
  - `content` (string, 必填) - 评论内容
  - `parent_id` (int, 可选) - 父评论ID

### 3.4 购物车与订单接口

购物车与订单接口用于处理商品购买流程。

#### 3.4.1 [购物车管理](cartList.md)
- **添加购物车**：`/api/cart/add`
- **获取购物车列表**：`/api/cart/list`
- **更新购物车**：`/api/cart/update`
- **移除购物车**：`/api/cart/remove`

#### 3.4.2 [订单管理](orders.md)
- **创建订单**：`/api/order/create`
- **获取订单详情**：`/api/order/detail`
- **获取订单列表**：`/api/orders`
- **取消订单**：`/api/order/cancel`
- **完成订单**：`/api/order/finished`
- **订单支付**：`/api/order/payment`

### 3.5 评价与优惠券接口

#### 3.5.1 [评价管理](orderReviews.md)
- **发布订单评价**：`/api/review/publish`
- **获取订单评价**：`/api/review/list`

#### 3.5.2 [优惠券管理](couponCodeList.md)
- **获取优惠券码**：`/api/coupon/code`
- **获取优惠券列表**：`/api//coupon/codes`
- **获取有效优惠券列表**：`/api/coupon/valid`

### 3.6 分销接口

分销接口用于处理分销员相关功能。

#### 3.6.1 [分销员管理](retailerInfo.md)
- **获取分销员详情**：`/api/retailer/info`
- **更新分销员信息**：`/api/retailer/update`
- **获取分销员统计**：`/api/retailer/statistics`

#### 3.6.2 [分销收益管理](retailerCommissions.md)
- **获取分销员收益列表**：`/api/retailer/commissions`
- **获取分销团队列表**：`/api/retailer/members`
- **获取分销员订单**：`/api/retailer/orders`

#### 3.6.3 [分销提现管理](retailerWithdraws.md)
- **申请分销员提现**：`/api/retailer/withdraw`
- **获取分销员提现记录**：`/api/retailer/withdraw`

### 3.7 系统与配置接口

系统与配置接口用于获取系统设置和配置信息。

#### 3.7.1 [系统设置](settingSystem.md)
- **获取系统设置**：`/api/setting/system`
- **获取联系信息**：`/api/setting/contact`
- **获取首页设置**：`/api/setting/index`
- **获取自定义字段**：`/api/setting/diy`

#### 3.7.2 [其他系统接口](languages.md)
- **获取多语言站点**：`/api/languages`
- **获取Google URL**：`/api/google/url`
- **统计数据**：`/api/log`

### 3.8 留言与验证接口

#### 3.8.1 [留言管理](guestbook.md)
- **提交留言**：`/api/guestbook.html`
- **获取留言字段**：`/api/guestbook/fields`

#### 3.8.2 [验证管理](captcha.md)
- **获取验证码**：`/api/captcha`
- **发送邮箱验证**：`/api/verify/email`
- **验证邮箱**：`/api/verify/email`

### 3.9 [上传接口](attachmentUpload.md)

- **上传附件接口**：`/api/attachment/upload`
- **请求方式**：POST
- **功能**：上传文件附件

### 3.10 [文档导入接口](importArchive.md)

文档导入接口用于从第三方平台导入内容。

- **导入文档**：`/api/import/archive`
- **检查文档是否存在**：`/api/import/archive/check`
- **获取文档分类列表**：`/api/import/categories`
- **添加友情链接**：`/api/friendlink/create`
- **检查链接是否存在**：`/api/friendlink/check`
- **删除链接**：`/api/friendlink/delete`
- **生成站点地图**：`/api/import/sitemap`

### 3.11 [微信相关接口](wechat.md)

- **微信接口**：`/api/wechat`
- **微信授权接口**：`/api/wechat/auth`
- **获取小程序二维码**：`/api/weapp/qrcode`

### 3.12 [其他接口](paymentCheck.md)

- **订阅接口**：`/api/subscription`
- **支付检查接口**：`/api/payment/check`

## 四、请求参数详解

### 4.1 通用参数格式

API 接口支持两种参数传递方式：
- **Query 参数**：通过 URL 查询字符串传递，适用于 GET 请求
- **Body 参数**：通过请求体传递，适用于 POST 请求

### 4.2 分页参数说明

大多数列表接口支持分页功能，通用分页参数包括：

| 参数名 | 类型 | 说明 |
|--------|------|------|
| page | int | 页码，默认为1, 部分接口使用 `current` 作为当前页码，请以实际接口为准 |
| limit | int | 每页数量，默认为10, 部分接口使用 `paegSize` 作为每页数量，请以实际接口为准 |
| offset | int | 偏移量，用于更灵活的分页, 部分接口不支持，请以实际接口为准 |

### 4.3 排序参数说明

排序参数用于控制返回数据的顺序：

| 参数名 | 类型 | 说明 |
|--------|------|------|
| order | string | 排序方式，如 `id desc`、`created_time asc` |

### 4.4 筛选参数说明

筛选参数用于过滤数据：

| 参数名 | 类型 | 说明 |
|--------|------|------|
| q | string | 搜索关键词 |
| type | string | 列表类型筛选，type="list" 不包含分页，type="page" 包含分页 |
| flag | string | 推荐属性筛选，支持的flag值有：头条[h]推荐[c]幻灯[f]特荐[a]滚动[s]加粗[h]图片[p]跳转[j] |

## 五、响应数据结构

### 5.1 通用响应格式

所有 API 接口都遵循统一的响应格式：

```json
{
  "code": 0,
  "msg": "success message",
  "data": {}
}
```

### 5.2 数据字段说明

| 字段名 | 类型 | 说明 |
|--------|------|------|
| code | int | 错误码，0表示成功 |
| msg | string | 错误信息或成功提示 |
| data | object/array | 实际返回的数据 |

### 5.3 错误码说明

| 错误码 | 说明 |
|--------|------|
| 0 | 成功 |
| -1 | 一般错误 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求成功 |

## 六、认证与授权

### 6.1 JWT Token 认证

AICMS 采用 JWT (JSON Web Token) 进行用户认证：

1. 用户登录成功后获取 Token
2. 在后续请求的 Header 中携带 Token
3. 格式：`Token: {token}`

### 6.2 需要认证的接口

以下类型的接口需要用户认证：
- 用户信息管理接口
- 订单管理接口
- 收藏管理接口
- 评论发布接口
- 购物车管理接口

### 6.3 Token 获取与刷新

Token 通过登录接口获取：
```json
{
  "code": 0,
  "msg": "登录成功",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

## 七、调试与测试

### 7.1 调试工具推荐

- **Postman** - 功能强大的 API 测试工具
- **curl** - 命令行工具
- **浏览器开发者工具** - 查看网络请求

### 7.2 常见错误及解决方案

**错误：Token 过期**
- 解决方案：重新登录获取新 Token

**错误：参数格式错误**
- 解决方案：检查参数类型和格式是否正确

**错误：接口无权限**
- 解决方案：确认用户权限或检查认证信息

### 7.3 性能优化建议

- 使用合适的分页参数避免返回过多数据
- 合理使用缓存机制
- 避免频繁调用同一接口

## 八、最佳实践

### 8.1 接口调用最佳实践

- **错误处理**：始终检查返回的 code 值
- **参数验证**：在调用前验证参数的有效性
- **重试机制**：对于临时性错误实现重试逻辑

### 8.2 安全最佳实践

- **Token 保护**：妥善保管认证 Token
- **HTTPS**：始终使用 HTTPS 连接
- **输入验证**：对用户输入进行严格验证

### 8.3 错误处理最佳实践

```javascript
// 示例：错误处理最佳实践
fetch('/api/archive/list', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Token': token
  }
})
.then(response => response.json())
.then(data => {
  if (data.code === 0) {
    // 成功处理
    console.log(data.data);
  } else {
    // 错误处理
    console.error('API Error:', data.msg);
  }
})
.catch(error => {
  console.error('Network Error:', error);
});
```

## 九、博客站点API调用示例

我们先分析一下博客站点有哪些页面，再拆解每一个页面所需要的接口。

### 9.1 博客站点页面结构分析

典型的博客站点通常包含以下页面：

#### 9.1.1 主要页面类型
- **首页** - 展示最新文章、热门文章、推荐文章等
- **分类页** - 按分类展示文章列表
- **标签页** - 按标签展示文章列表
- **文章详情页** - 展示单篇文章的详细内容
- **归档页** - 按时间归档展示文章
- **搜索页** - 搜索结果页面
- **关于页面** - 单页面内容
- **用户相关页面** - 登录、注册、个人中心等

### 9.2 各页面所需API接口详解

#### 9.2.1 首页

首页是博客最重要的页面，通常包含多种内容展示。

**主要接口调用：**

1. **获取文章列表** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "limit": 10,
     "page": 1,
     "order": "created_time desc"
   }
   ```
   - 用途：获取最新文章列表
   - 参数：limit(每页数量)、page(页码)、order(排序方式)

2. **获取推荐文章** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "flag": "c",  // 推荐文章
     "limit": 5
   }
   ```
   - 用途：获取推荐文章列表
   - 参数：flag(推荐标识)、limit(数量)

3. **获取热门文章** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "order": "views desc",
     "limit": 5
   }
   ```
   - 用途：获取点击量最高的文章
   - 参数：order(按浏览量排序)、limit(数量)

4. **获取分类列表** ([`/api/category/list`](categoryList.md))
   ```json
   {
     "limit": 10
   }
   ```
   - 用途：获取所有分类，用于导航菜单

5. **获取标签列表** ([`/api/tag/list`](tagList.md))
   ```json
   {
     "type": "list",
     "limit": 20
   }
   ```
   - 用途：获取热门标签，用于标签云

6. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站标题、描述、关键词等基础信息

7. **获取首页设置** ([`/api/setting/index`](settingIndex.md))
   - 用途：获取首页特定配置信息

8. **获取导航列表** ([`/api/nav/list`](navList.md))
   - 用途：获取网站导航菜单

9. **获取Banner列表** ([`/api/banner/list`](bannerList.md))
   - 用途：获取首页轮播图

#### 9.2.2 分类页面

分类页面展示特定分类下的文章列表。

**主要接口调用：**

1. **获取分类详情** ([`/api/category/detail`](categoryDetail.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取当前分类信息
   - 参数：id(分类ID) 或 filename(分类别名)

2. **获取分类下文章列表** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "categoryId": 1,
     "limit": 10,
     "page": 1
   }
   ```
   - 用途：获取该分类下的文章列表
   - 参数：categoryId(分类ID)、limit(每页数量)、page(页码)

3. **获取子分类列表** ([`/api/category/list`](categoryList.md))
   ```json
   {
     "parentId": 1,
     "limit": 10
   }
   ```
   - 用途：获取当前分类的子分类
   - 参数：parentId(父分类ID)

4. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

5. **获取分类列表** ([`/api/category/list`](categoryList.md))
   - 用途：获取所有分类，用于侧边栏导航

#### 9.2.3 标签页面

标签页面展示特定标签下的文章列表。

**主要接口调用：**

1. **获取标签详情** ([`/api/tag/detail`](tagDetail.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取当前标签信息
   - 参数：id(标签ID) 或 name(标签名称)

2. **获取标签下文章列表** ([`/api/tag/data/list`](tagDataList.md))
   ```json
   {
     "id": 1,
     "limit": 10,
     "page": 1
   }
   ```
   - 用途：获取该标签下的文章列表
   - 参数：tagId(标签ID)、limit(每页数量)、page(页码)

3. **获取标签列表** ([`/api/tag/list`](tagList.md))
   ```json
   {
     "type": "list",
     "limit": 20
   }
   ```
   - 用途：获取热门标签，用于相关标签推荐

4. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

#### 9.2.4 文章详情页面

文章详情页面展示单篇文章的完整内容。

**主要接口调用：**

1. **获取文章详情** ([`/api/archive/detail`](archiveDetail.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取文章详细内容
   - 参数：id(文章ID) 或 filename(文章别名)

2. **获取文章参数** ([`/api/archive/params`](archiveParams.md))
   ```json
   {
     "id": 1,
     "sorted": true
   }
   ```
   - 用途：获取文章自定义参数
   - 参数：id(文章ID)、sorted(返回格式)

3. **获取上一篇文档** ([`/api/archive/prev`](archivePrev.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取上一篇文章信息

4. **获取下一篇文档** ([`/api/archive/next`](archiveNext.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取下一篇文章信息

5. **获取相关文章** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "type": "related",
     "limit": 5,
     "id": 1
   }
   ```
   - 用途：获取同分类的其他文章
   - 参数：type="related"(相关文档类型)、limit(数量)、id(当前文章)

6. **获取评论列表** ([`/api/comment/list`](commentList.md))
   ```json
   {
     "archive_id": 1,
     "limit": 10,
     "page": 1
   }
   ```
   - 用途：获取文章评论列表
   - 参数：archive_id(文章ID)、limit(每页数量)、page(页码)

7. **检查收藏状态** ([`/api/favorite/check`](favoriteCheck.md))
   ```json
   {
     "archive_id": 1
   }
   ```
   - 用途：检查当前用户是否收藏了该文章
   - 需要认证

8. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

#### 9.2.5 搜索页面

搜索页面展示搜索关键词相关的文章。

**主要接口调用：**

1. **搜索文章列表** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "q": "关键词",
     "limit": 10,
     "page": 1
   }
   ```
   - 用途：搜索包含关键词的文章
   - 参数：q(搜索关键词)、limit(每页数量)、page(页码)

2. **获取热门搜索** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "order": "views desc",
     "limit": 10
   }
   ```
   - 用途：获取热门搜索内容

3. **获取搜索建议** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "q": "关键词前缀",
     "limit": 5
   }
   ```
   - 用途：获取搜索建议

4. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

#### 9.2.6 关于页面

单页面内容展示。

**主要接口调用：**

1. **获取页面详情** ([`/api/page/detail`](pageDetail.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取单页面内容
   - 参数：id(页面ID) 或 filename(页面别名)

2. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

#### 9.2.7 用户相关页面

##### 9.2.7.1 登录页面

**主要接口调用：**

1. **用户登录** ([`/api/login`](login.md))
   ```json
   {
     "user_name": "用户名",
     "password": "密码"
   }
   ```
   - 用途：用户登录认证
   - 参数：user_name(用户名)、password(密码)、email(邮箱)、phone(手机号)

##### 9.2.7.2 注册页面

**主要接口调用：**

1. **用户注册** ([`/api/register`](register.md))
   ```json
   {
     "user_name": "用户名",
     "password": "密码",
     "email": "邮箱",
     "captcha": "验证码"
   }
   ```
   - 用途：新用户注册
   - 参数：user_name(用户名)、password(密码)、email(邮箱)、captcha(验证码)

2. **获取验证码** ([`/api/captcha`](captcha.md))
   - 用途：获取图形验证码

3. **发送邮箱验证** ([`/api/verify/email`](emailVerifySend.md))
   ```json
   {
     "email": "邮箱地址"
   }
   ```
   - 用途：发送邮箱验证码

##### 9.2.7.3 个人中心页面

**主要接口调用：**

1. **获取用户详情** ([`/api/user/detail`](userDetail.md))
   - 用途：获取当前用户详细信息
   - 需要认证

2. **获取用户收藏列表** ([`/api/favorite/list`](favorites.md))
   ```json
   {
     "limit": 10,
     "page": 1
   }
   ```
   - 用途：获取用户收藏的文章列表
   - 需要认证

3. **获取用户评论列表** ([`/api/comment/list`](commentList.md))
   ```json
   {
     "user_id": 1,
     "limit": 10,
     "page": 1
   }
   ```
   - 用途：获取用户发表的评论
   - 需要认证

4. **更新用户信息** ([`/api/user/update`](userDetailUpdate.md))
   ```json
   {
     "nickname": "昵称",
     "email": "邮箱"
   }
   ```
   - 用途：更新用户信息
   - 需要认证

5. **更新用户头像** ([`/api/user/avatar`](userAvatarUpdate.md))
   - 用途：更新用户头像
   - 需要认证

### 9.3 页面加载流程示例

以文章详情页为例，说明完整的API调用流程：

#### 9.3.1 页面初始化
1. 获取文章详情
2. 增加文章浏览量（通过后续请求或服务端处理）
3. 获取文章参数

#### 9.3.2 侧边栏内容加载
1. 获取上一篇/下一篇文章
2. 获取相关文章推荐
3. 获取热门文章列表

#### 9.3.3 评论区域加载
1. 获取评论列表
2. 如果用户已登录，获取用户对当前文章的收藏状态

#### 9.3.4 交互功能
1. 发布评论（需要认证）
2. 收藏/取消收藏（需要认证）
3. 评论点赞（需要认证）

### 9.4 常见页面组合调用

#### 9.4.1 首页 + 分类页组合
```javascript
// 并行请求多个接口
Promise.all([
  fetch('/api/archive/list', { params: { limit: 10, page: 1 } }),
  fetch('/api/category/list', { params: { limit: 10 } }),
  fetch('/api/tag/list', { params: { type: 'list', limit: 20 } }),
  fetch('/api/setting/system')
]).then(responses => {
  // 处理所有响应数据
  const [articles, categories, tags, settings] = responses;
  // 渲染页面
});
```

#### 9.4.2 文章详情页完整调用
```javascript
// 串行或并行调用多个接口
const articleId = 1;
Promise.all([
  fetch(`/api/archive/detail`, { params: { id: articleId } }),
  fetch(`/api/archive/params`, { params: { id: articleId } }),
  fetch(`/api/archive/prev`, { params: { id: articleId } }),
  fetch(`/api/archive/next`, { params: { id: articleId } }),
  fetch(`/api/comment/list`, { params: { archive_id: articleId, limit: 10 } }),
  fetch(`/api/setting/system`)
]).then(responses => {
  const [article, params, prev, next, comments, settings] = responses;
  // 组合数据并渲染页面
});
```

可以看出一个完整的博客站点需要调用多个API接口来构建各个页面，开发者可以根据实际需求选择合适的接口组合，实现丰富的博客功能。

## 十、商城站点API调用示例

我们先分析一下商城站点有哪些页面，再拆解每一个页面所需要的接口。

### 10.1 商城站点页面结构分析

典型的商城站点通常包含以下页面：

#### 10.1.1 主要页面类型
- **首页** - 展示最新商品、热门商品、推荐商品、促销活动等
- **商品分类页** - 按分类展示商品列表
- **商品详情页** - 展示单个商品的详细信息
- **购物车页** - 用户选购商品的购物车页面
- **订单确认页** - 确认订单信息的页面
- **订单支付页** - 完成订单支付的页面
- **个人中心页** - 用户个人信息和订单管理
- **订单详情页** - 查看单个订单的详细信息
- **我的订单页** - 用户订单列表
- **收货地址页** - 管理用户收货地址
- **商品搜索页** - 搜索商品结果页面
- **促销活动页** - 优惠券、秒杀等促销活动页面
- **用户相关页面** - 登录、注册、个人中心等

### 10.2 各页面所需API接口详解

#### 10.2.1 首页

商城首页是最重要的页面，通常包含多种内容展示。

**主要接口调用：**

1. **获取商品列表** ([`/api/archive/list`](archiveList.md))
   ```json
   {
    "moduleId": 2, // 商品模块ID
     "limit": 10,
     "page": 1,
     "order": "created_time desc"
   }
   ```
   - 用途：获取最新商品列表
   - 参数：moduleId=2(商品模块ID是2)、limit(每页数量)、page(页码)、order(排序方式)

2. **获取推荐商品** ([`/api/archive/list`](archiveList.md))
   ```json
   {
    "moduleId": 2, // 商品模块ID
     "flag": "c",  // 推荐商品
     "limit": 5
   }
   ```
   - 用途：获取推荐商品列表
   - 参数：flag(推荐标识)、limit(数量)

3. **获取热门商品** ([`/api/archive/list`](archiveList.md))
   ```json
   {
    "moduleId": 2, // 商品模块ID
     "order": "views desc",
     "limit": 5
   }
   ```
   - 用途：获取点击量最高的商品
   - 参数：order(按浏览量排序)、limit(数量)

4. **获取商品分类列表** ([`/api/category/list`](categoryList.md))
   ```json
   {
    "moduleId": 2, // 商品模块ID
     "limit": 10
   }
   ```
   - 用途：获取所有商品分类，用于导航菜单

5. **获取商品标签列表** ([`/api/tag/list`](tagList.md))
   ```json
   {
     "type": "list",
     "limit": 20
   }
   ```
   - 用途：获取热门标签，用于标签云

6. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取商城标题、描述、关键词等基础信息

7. **获取首页设置** ([`/api/setting/index`](settingIndex.md))
   - 用途：获取首页特定配置信息

8. **获取导航列表** ([`/api/nav/list`](navList.md))
   - 用途：获取网站导航菜单

9. **获取Banner列表** ([`/api/banner/list`](bannerList.md))
   - 用途：获取首页轮播图

10. **获取促销活动信息** ([`/api/setting/system`](settingSystem.md))
    - 用途：获取促销活动配置信息

11. **获取优惠券列表** ([`/api/coupon/codes`](couponCodeList.md))
    ```json
    {
      "limit": 5
    }
    ```
    - 用途：获取可用的优惠券列表

#### 10.2.2 商品分类页面

商品分类页面展示特定分类下的商品列表。

**主要接口调用：**

1. **获取分类详情** ([`/api/category/detail`](categoryDetail.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取当前分类信息
   - 参数：id(分类ID) 或 filename(分类别名)

2. **获取分类下商品列表** ([`/api/archive/list`](archiveList.md))
   ```json
   {
    "moduleId": 2, // 商品模块ID
     "categoryId": 1,
     "limit": 10,
     "page": 1
   }
   ```
   - 用途：获取该分类下的商品列表
   - 参数：categoryId(分类ID)、limit(每页数量)、page(页码)

3. **获取子分类列表** ([`/api/category/list`](categoryList.md))
   ```json
   {
     "parentId": 1,
     "limit": 10
   }
   ```
   - 用途：获取当前分类的子分类
   - 参数：parentId(父分类ID)

4. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

5. **获取商品分类列表** ([`/api/category/list`](categoryList.md))
   - 用途：获取所有分类，用于侧边栏导航

6. **获取筛选条件** ([`/api/archive/list`](archiveList.md))
   ```json
   {
    "moduleId": 2, // 商品模块ID
     "categoryId": 1,
     "type": "filter"
   }
   ```
   - 用途：获取当前分类下的筛选条件

#### 10.2.3 商品详情页面

商品详情页面展示单个商品的完整信息。

**主要接口调用：**

1. **获取商品详情** ([`/api/archive/detail`](archiveDetail.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取商品详细内容
   - 参数：id(商品ID) 或 filename(商品别名)

2. **获取商品参数** ([`/api/archive/params`](archiveParams.md))
   ```json
   {
     "id": 1,
     "sorted": true
   }
   ```
   - 用途：获取商品自定义参数
   - 参数：id(商品ID)、sorted(返回格式)

3. **获取商品SKU信息** ([`/api/archive/sku`](archiveSku.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取商品SKU规格信息
   - 参数：id(商品ID)

4. **获取上一个商品** ([`/api/archive/prev`](archivePrev.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取上一个商品信息

5. **获取下一个商品** ([`/api/archive/next`](archiveNext.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取下一个商品信息

6. **获取相关商品** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "type": "related",
     "limit": 5,
     "id": 1
   }
   ```
   - 用途：获取同分类的其他商品
   - 参数：type="related"(相关商品类型)、limit(数量)、id(当前商品)

7. **获取商品评论列表** ([`/api/comment/list`](commentList.md))
   ```json
   {
     "archive_id": 1,
     "limit": 10,
     "page": 1
   }
   ```
   - 用途：获取商品评论列表
   - 参数：archive_id(商品ID)、limit(每页数量)、page(页码)

8. **检查收藏状态** ([`/api/favorite/check`](favoriteCheck.md))
   ```json
   {
     "archive_id": 1
   }
   ```
   - 用途：检查当前用户是否收藏了该商品
   - 需要认证

9. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

10. **获取购物车商品数量** ([`/api/cart/list`](cartList.md))
    - 用途：获取当前用户购物车中的商品数量
    - 需要认证

#### 10.2.4 购物车页面

购物车页面展示用户已选择的商品。

**主要接口调用：**

1. **获取购物车列表** ([`/api/cart/list`](cartList.md))
   - 用途：获取当前用户的购物车商品列表
   - 需要认证

2. **更新购物车商品数量** ([`/api/cart/update`](cartUpdate.md))
   ```json
   {
     "id": 1,
     "quantity": 2
   }
   ```
   - 用途：更新购物车中某个商品的数量
   - 参数：id(购物车项目ID)、quantity(数量)
   - 需要认证

3. **从购物车移除商品** ([`/api/cart/remove`](cartRemove.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：从购物车中移除某个商品
   - 参数：id(购物车项目ID)
   - 需要认证

4. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

5. **获取优惠券列表** ([`/api/coupon/codes`](couponCodeList.md))
   - 用途：获取可用的优惠券列表
   - 需要认证

#### 10.2.5 订单确认页面

订单确认页面用于确认订单信息。

**主要接口调用：**

1. **获取购物车列表** ([`/api/cart/list`](cartList.md))
   - 用途：获取当前用户的购物车商品列表
   - 需要认证

2. **获取收货地址列表** ([`/api/order/addresses`](orderAddresses.md))
   - 用途：获取用户的收货地址列表
   - 需要认证

3. **获取默认收货地址** ([`/api/order/address`](orderAddress.md))
   - 用途：获取用户的默认收货地址
   - 需要认证

4. **获取商品结算信息** ([`/api/orders/checkout`](ordersCheckout.md))
   ```json
   {
     "cart_ids": [1, 2, 3]
   }
   ```
   - 用途：获取商品结算信息（价格、运费等）
   - 参数：cart_ids(购物车项目ID列表)
   - 需要认证

5. **获取优惠券列表** ([`/api/coupon/codes`](couponCodeList.md))
   - 用途：获取可用的优惠券列表
   - 需要认证

6. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

#### 10.2.6 订单支付页面

订单支付页面用于完成订单支付。

**主要接口调用：**

1. **创建订单** ([`/api/order/create`](orderCreate.md))
   ```json
   {
     "address_id": 1,
     "coupon_id": 2,
     "remark": "订单备注",
     "cart_ids": [1, 2, 3]
   }
   ```
   - 用途：创建新订单
   - 参数：address_id(收货地址ID)、coupon_id(优惠券ID)、remark(备注)、cart_ids(购物车项目ID列表)
   - 需要认证

2. **获取订单详情** ([`/api/order/detail`](orderDetail.md))
   ```json
   {
     "order_id": "202211232209080046"
   }
   ```
   - 用途：获取订单详情
   - 参数：order_id(订单ID)
   - 需要认证

3. **订单支付** ([`/api/order/payment`](orderPayment.md))
   ```json
   {
     "order_id": "202211232209080046",
     "pay_way": "alipay"
   }
   ```
   - 用途：发起订单支付
   - 参数：id(订单ID)、payment_method(支付方式)
   - 需要认证

4. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

#### 10.2.7 个人中心页面

个人中心页面展示用户个人信息和订单管理。

**主要接口调用：**

1. **获取用户详情** ([`/api/user/detail`](userDetail.md))
   - 用途：获取当前用户详细信息
   - 需要认证

2. **获取用户订单列表** ([`/api/orders`](orders.md))
   ```json
   {
     "limit": 5,
     "page": 1
   }
   ```
   - 用途：获取用户订单列表
   - 参数：limit(每页数量)、page(页码)
   - 需要认证

3. **获取用户收藏列表** ([`/api/favorite/list`](favorites.md))
   ```json
   {
     "limit": 5,
     "page": 1
   }
   ```
   - 用途：获取用户收藏的商品列表
   - 参数：limit(每页数量)、page(页码)
   - 需要认证

4. **获取用户愿望清单** ([`/api/wishlist`](wishlist.md))
   - 用途：获取用户愿望清单
   - 需要认证

5. **获取用户收货地址列表** ([`/api/order/addresses`](orderAddresses.md))
   - 用途：获取用户收货地址列表
   - 需要认证

6. **获取用户评论列表** ([`/api/comment/list`](commentList.md))
   ```json
   {
     "user_id": 1,
     "limit": 5,
     "page": 1
   }
   ```
   - 用途：获取用户发表的评论
   - 参数：user_id(用户ID)、limit(每页数量)、page(页码)
   - 需要认证

7. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

#### 10.2.8 订单详情页面

订单详情页面展示单个订单的详细信息。

**主要接口调用：**

1. **获取订单详情** ([`/api/order/detail`](orderDetail.md))
   ```json
   {
     "order_id": "202211232209080046"
   }
   ```
   - 用途：获取订单详细信息
   - 参数：order_id(订单ID)
   - 需要认证

2. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

3. **获取订单评价** ([`/api/review/list`](orderReviews.md))
   ```json
   {
     "order_id": "202211232209080046"
   }
   ```
   - 用途：获取订单商品的评价
   - 参数：order_id(订单ID)
   - 需要认证

#### 10.2.9 我的订单页面

我的订单页面展示用户的所有订单。

**主要接口调用：**

1. **获取用户订单列表** ([`/api/orders`](orders.md))
   ```json
   {
     "limit": 10,
     "page": 1,
     "status": "paid"
   }
   ```
   - 用途：获取用户订单列表
   - 参数：limit(每页数量)、page(页码)、status(订单状态)
   - 需要认证

2. **取消订单** ([`/api/order/cancel`](orderCancel.md))
   ```json
   {
     "order_id": "202211232209080046"
   }
   ```
   - 用途：取消订单
   - 参数：order_id(订单ID)
   - 需要认证

3. **完成订单** ([`/api/order/finished`](orderFinished.md))
   ```json
   {
     "order_id": "202211232209080046"
   }
   ```
   - 用途：完成订单
   - 参数：order_id(订单ID)
   - 需要认证

4. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

#### 10.2.10 收货地址页面

收货地址页面用于管理用户的收货地址。

**主要接口调用：**

1. **获取收货地址列表** ([`/api/order/addresses`](orderAddresses.md))
   - 用途：获取用户收货地址列表
   - 需要认证

2. **保存收货地址** ([`/api/order/address`](orderAddressSave.md))
   ```json
   {
     "name": "收货人姓名",
     "phone": "收货人电话",
     "province": "省份",
     "city": "城市",
     "country": "区域",
     "address": "详细地址",
     "is_default": 1
   }
   ```
   - 用途：保存收货地址
   - 参数：name(姓名)、phone(电话)、province(省份)、city(城市)、country(区域)、address(详细地址)、is_default(是否默认)
   - 需要认证

3. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

#### 10.2.11 商品搜索页面

商品搜索页面展示搜索关键词相关的商品。

**主要接口调用：**

1. **搜索商品列表** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "moduleId": 2, // 商品模块ID
     "q": "关键词",
     "limit": 10,
     "page": 1
   }
   ```
   - 用途：搜索包含关键词的商品
   - 参数：q(搜索关键词)、limit(每页数量)、page(页码)

2. **获取热门搜索** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "moduleId": 2, // 商品模块ID
     "order": "views desc",
     "limit": 10
   }
   ```
   - 用途：获取热门搜索内容

3. **获取搜索建议** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "moduleId": 2, // 商品模块ID
     "q": "关键词前缀",
     "limit": 5
   }
   ```
   - 用途：获取搜索建议

4. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

#### 10.2.12 促销活动页面

促销活动页面展示优惠券、秒杀等促销活动。

**主要接口调用：**

1. **获取优惠券列表** ([`/api/coupon/codes`](couponCodeList.md))
   ```json
   {
     "limit": 10,
     "page": 1
   }
   ```
   - 用途：获取优惠券列表
   - 参数：limit(每页数量)、page(页码)

2. **获取有效优惠券列表** ([`/api/coupon/valid`](couponValidList.md))
   - 用途：获取当前有效的优惠券列表

3. **获取优惠券码** ([`/api/coupon/code`](couponCodeGet.md))
   ```json
   {
     "id": 1
   }
   ```
   - 用途：获取优惠券码
   - 参数：id(优惠券ID)
   - 需要认证

4. **获取限时秒杀商品** ([`/api/archive/list`](archiveList.md))
   ```json
   {
     "moduleId": 2, // 商品模块ID
     "flag": "s",  // 秒杀标识
     "limit": 10,
     "page": 1
   }
   ```
   - 用途：获取秒杀商品列表

5. **获取系统设置** ([`/api/setting/system`](settingSystem.md))
   - 用途：获取网站基础信息

#### 10.2.13 用户相关页面

##### 10.2.13.1 登录页面

**主要接口调用：**

1. **用户登录** ([`/api/login`](login.md))
   ```json
   {
     "user_name": "用户名",
     "password": "密码"
   }
   ```
   - 用途：用户登录认证
   - 参数：user_name(用户名)、password(密码)、email(邮箱)、phone(手机号)

##### 10.2.13.2 注册页面

**主要接口调用：**

1. **用户注册** ([`/api/register`](register.md))
   ```json
   {
     "user_name": "用户名",
     "password": "密码",
     "email": "邮箱",
     "captcha_id": "验证码ID",
     "captcha": "验证码"
   }
   ```
   - 用途：新用户注册
   - 参数：user_name(用户名)、password(密码)、email(邮箱)、captcha(验证码)

2. **获取验证码** ([`/api/captcha`](captcha.md))
   - 用途：获取图形验证码

3. **发送邮箱验证** ([`/api/verify/email`](emailVerifySend.md))
   ```json
   {
     "email": "邮箱地址"
   }
   ```
   - 用途：发送邮箱验证码

##### 10.2.13.3 个人中心页面

**主要接口调用：**

1. **获取用户详情** ([`/api/user/detail`](userDetail.md))
   - 用途：获取当前用户详细信息
   - 需要认证

2. **更新用户信息** ([`/api/user/update`](userDetailUpdate.md))
   ```json
   {
     "real_name": "真实姓名",
     "email": "邮箱"
   }
   ```
   - 用途：更新用户信息
   - 需要认证

3. **更新用户头像** ([`/api/user/avatar`](userAvatarUpdate.md))
   - 用途：更新用户头像
   - 需要认证

4. **更新用户密码** ([`/api/user/password`](userPasswordUpdate.md))
   ```json
   {
     "old_password": "旧密码",
     "password": "新密码"
   }
   ```
   - 用途：更新用户密码
   - 需要认证

5. **重置用户密码** ([`/api/user/password/reset`](userPasswordReset.md))
   ```json
   {
     "email": "邮箱",
     "password": "新密码",
     "token": "验证token",
     "code": "验证码"
   }
   ```
   - 用途：重置用户密码

### 10.3 页面加载流程示例

以商品详情页为例，说明完整的API调用流程：

#### 10.3.1 页面初始化
1. 获取商品详情
2. 增加商品浏览量（通过后续请求或服务端处理）
3. 获取商品SKU信息

#### 10.3.2 侧边栏内容加载
1. 获取上一个/下一个商品
2. 获取相关商品推荐
3. 获取热门商品列表

#### 10.3.3 评论区域加载
1. 获取商品评论列表
2. 如果用户已登录，获取用户对当前商品的收藏状态

#### 10.3.4 购物车功能
1. 获取购物车商品数量（如果用户已登录）
2. 添加到购物车（需要认证）

#### 10.3.5 交互功能
1. 发布评论（需要认证）
2. 收藏/取消收藏（需要认证）
3. 评论点赞（需要认证）

### 10.4 常见页面组合调用

#### 10.4.1 首页 + 分类页组合
```javascript
// 并行请求多个接口
Promise.all([
  fetch('/api/archive/list', { params: { moduleId: 2, limit: 10, page: 1 } }),
  fetch('/api/category/list', { params: { moduleId: 2, limit: 10 } }),
  fetch('/api/tag/list', { params: { type: 'list', limit: 20 } }),
  fetch('/api/setting/system'),
  fetch('/api/coupon/codes', { params: { limit: 5 } })
]).then(responses => {
  // 处理所有响应数据
  const [products, categories, tags, settings, coupons] = responses;
  // 渲染页面
});
```

#### 10.4.2 商品详情页完整调用
```javascript
// 串行或并行调用多个接口
const productId = 1;
Promise.all([
  fetch(`/api/archive/detail`, { params: { id: productId } }),
  fetch(`/api/archive/params`, { params: { id: productId } }),
  fetch(`/api/archive/sku`, { params: { id: productId } }),
  fetch(`/api/archive/prev`, { params: { id: productId } }),
  fetch(`/api/archive/next`, { params: { id: productId } }),
  fetch(`/api/comment/list`, { params: { archive_id: productId, limit: 10 } }),
  fetch(`/api/setting/system`)
]).then(responses => {
  const [product, params, sku, prev, next, comments, settings] = responses;
  // 组合数据并渲染页面
});
```

#### 10.4.3 订单确认页完整调用
```javascript
// 订单确认页面的API调用
const cartIds = [1, 2, 3];
Promise.all([
  fetch('/api/cart/list'),
  fetch('/api/order/addresses'),
  fetch('/api/orders/checkout', { params: { cart_ids: cartIds } }),
  fetch('/api/coupon/codes'),
  fetch('/api/setting/system')
]).then(responses => {
  const [cart, addresses, checkout, coupons, settings] = responses;
  // 组合数据并渲染页面
});
```

可以看出一个完整的商城站点需要调用多个API接口来构建各个页面，开发者可以根据实际需求选择合适的接口组合，实现丰富的商城功能。

## 结语

通过本指南，您可以系统地了解和使用 AICMS API，从基础概念到高级用法，逐步掌握接口的使用方法。建议按照指南的顺序逐步学习，并结合实际项目进行练习。