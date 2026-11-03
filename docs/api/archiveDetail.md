# 获取文档详情接口

获取AICMS 系统中单个文档的详细信息，包括文档的基本信息、分类信息、内容详情及其他自定义字段信息。此接口同时适用于文档和产品类型的内容。

## 注意事项

- 接口支持通过文档 ID 或 URL 别名（filename）两种方式获取文档详情
- 可通过本接口获取上一篇、下一篇文档
- 部分字段如价格、库存、SKU 等仅在产品类型文档中有效
- 响应中包含 SEO 相关字段，便于 SEO 优化
- 如果文档不存在，接口会返回错误码

## 请求地址

```
{域名地址}/api/archive/detail
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/archive/detail`

## 请求语法

```
GET {域名地址}/api/archive/detail?{参数}
```
## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名   | 类型   | 必填 | 说明                                      |
| :------- | :----- | :--- | :---------------------------------------- |
| id       | int    | 是   | 文档 ID，如果传了 filename，可以不用传 ID |
| filename | string | 否   | 文档 URL 别名，文档 ID、filename 二选一，如果传了ID，并且 filename 的值是 prev/next，则返回上一篇或下一篇文档 |   |
| password | string | 否   | 文档密码，如果文档设置了密码，则需要填写密码获取完整内容 |
| render    | bool   | 否   | 是否渲染Markdown内容，默认为 true |

**注意** 本接口也可以获取指定文档的上一篇文档或下一篇文档，使用方法是：参数id和filename同时传时，filename的值为prev/next，则返回上一篇或下一篇文档

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | [object#archive](#data文档信息) | 结果内容     |

#### data文档信息

| 字段名        | 类型     | 说明                                                                   |
| :------------ | :------- | :--------------------------------------------------------------------- |
| id            | int      | 文档 ID                                                                |
| is_wholesale | bool | 是否是批发商品 |
| wholesale_rule | object | 适用批发规则 |
| wholesale_rules | object[] | 批发规则列表 |
| sku | object | 单个，选择的一个sku，比如收藏夹，购物车，愿望清单等读取时用到 |
| skus | object[] | sku列表 |
| options | object[] | 规格选项信息 |
| is_favorite | bool | 是否收藏 |
| brand | string | 商品品牌 |
| video_url | string | 视频地址 |
| need_logistics | bool | 是否需要物流 |
| is_free_shipping | bool | 是否包邮 |
| sold_count | int | 已售数量 |
| review_count | int | 评价数量 |
| favorite_count | int | 收藏数量 |
| option_type | int | 规格类型, 0 无SKU，1 组合SKU，2 加价SKU |
| weight | int | 重量 |
| weight_unit | string | 重量单位 |
| allow_oversold | bool | 是否允许超卖 |
| has_order_fields | bool | 是否有订单扩展字段 |
| order_fields | object[] | 订单扩展字段 |
| title         | string   | 文档标题                                                               |
| seo_title     | string   | 文档 SEO 标题                                                          |
| url_token     | string   | 文档 URL 别名                                                          |
| keywords      | string   | 文档关键词                                                             |
| description   | string   | 文档简介                                                               |
| module_id     | int      | 文档模型 ID                                                            |
| category_id   | int      | 文档分类 ID                                                            |
| views         | int      | 文档浏览量                                                             |
| comment_count | int      | 文档评论量                                                             |
| images        | string[] | 文档组图                                                               |
| logo          | string   | 文档 Logo                                                              |
| thumb         | string   | 文档缩略图                                                             |
| flag          | string   | 文档推荐属性，头条[h]推荐[c]幻灯[f]特荐[a]滚动[s]加粗[h]图片[p]跳转[j] |
| canonical_url | string   | canonical url                                                          |
| fixed_link    | string   | 文档固定链接                                                           |
| created_time  | int      | 文档发布时间戳                                                         |
| updated_time  | int      | 文档更新时间戳                                                         |
| status        | int      | 文档显示状态                                                           |
| user_id       | int      | 用户 ID                                                                |
| price         | int      | 价格，单位分                                                           |
| stock         | int      | 库存量                                                                 |
| user_id       | int      | 用户 ID                                                                |
| category      | [object#category](#category文档分类信息)   | 文档分类信息                                                           |
| data          | [object#content](#content文档内容信息)   | 文档内容信息                                                           |
| extra         | [object#map](#extra文档其他字段信息)   | 文档其他字段信息                                                       |

##### category文档分类信息

| 字段名       | 类型     | 说明                         |
| :----------- | :------- | :--------------------------- |
| id           | int      | 分类 ID                      |
| parent_id    | int      | 分类上级 ID                  |
| title        | string   | 分类名称                     |
| seo_title    | string   | 分类 SEO 标题                |
| url_token    | string   | 分类 URL 别名                |
| keywords     | string   | 分类关键词                   |
| description  | string   | 分类简介                     |
| module_id    | int      | 模型 ID                      |
| content      | string   | 分类内容详情                 |
| type         | int      | 分类属性值，1 分类，3 单页面 |
| sort         | int      | 分类排序值                   |
| images       | string[] | 分类 Banner 图               |
| logo         | string   | 分类缩略图                   |
| thumb        | string   | 分类缩略图                   |
| created_time | int      | 文档发布时间戳               |
| updated_time | int      | 文档更新时间戳               |
| status       | int      | 文档显示状态                 |

##### content文档内容信息

| 字段名  | 类型   | 说明         |
| :------ | :----- | :----------- |
| id      | int    | 分类 ID      |
| content | string | 文档内容详情 |

##### extra文档其他字段信息

extra 根据模型设置的字段显示，字段结构为 key => item：
key 表单字段调用名，item 为内容：
|字段名|类型|说明|
|:---|:---|:---|
|name|string|字段名称|
|value|string|填写的值|
|default|string|默认值|

### 请求数据示例

```
GET /api/archive/detail?id=1 HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

或

```
GET /api/archive/detail?filename=AICMS HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```


### 返回数据示例

```json
{
  "code": 0,
  "data": {
    "id": 1,
    "created_time": 1607308159,
    "updated_time": 1662717106,
    "title": "欢迎使用AICMS",
    "seo_title": "",
    "url_token": "AICMS",
    "keywords": "",
    "description": "欢迎使用AICMS",
    "module_id": 1,
    "category_id": 1,
    "views": 1338,
    "comment_count": 0,
    "images": null,
    "status": 1,
    "canonical_url": "",
    "fixed_link": "",
    "flag": "",
    "user_id": 0,
    "price": 0,
    "stock": 9999999,
    "category": {
      "id": 1,
      "created_time": 1607308159,
      "updated_time": 1657761249,
      "title": "AICMS帮助",
      "seo_title": "",
      "keywords": "",
      "url_token": "goruning",
      "description": "",
      "content": "<p>欢迎使用AICMS</p>",
      "module_id": 1,
      "parent_id": 0,
      "type": 1,
      "sort": 1,
      "images": [],
      "logo": "https://www.aicms.com/uploads/202012/7/bd36c37ef742c7be.webp",
      "status": 1,
      "thumb": "https://www.aicms.com/uploads/202012/7/thumb_bd36c37ef742c7be.webp"
    },
    "data": {
      "id": 1,
      "content": "<p>欢迎使用AICMS</p>"
    },
    "logo": "https://www.aicms.com/uploads/202012/7/bd36c37ef742c7be.webp",
    "thumb": "https://www.aicms.com/uploads/202012/7/thumb_bd36c37ef742c7be.webp",
    "extra": {
      "author": {
        "name": "作者",
        "value": "AICMS",
        "default": ""
      }
    },
    "link": ""
  },
  "msg": ""
}
```

### 错误代码

| 错误码 | 说明                        |
| :----- | :-------------------------- |
| 0      | OK                          |
| -1     | 错误，错误原因在 msg 中指出 |
| 1001   | 未登录                      |
| 1002   | 未授权                      |
| 200    | API 请求 OK                 |
