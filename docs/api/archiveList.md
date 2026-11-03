# 获取文档列表接口

获取系统中指定条件的文档列表，支持多种筛选和排序方式，可以获取指定模型、分类、推荐属性等条件下的文档列表。此接口同时适用于文档和产品类型的内容。

## 注意事项

- 接口支持多种类型的数据获取（page、list、related），不同类型的参数效果可能不同
- 当 type="page" 时，支持分页功能和搜索功能
- 支持自定义筛选参数，可根据模型中配置的字段进行筛选
- 部分字段如价格、库存等仅在产品类型文档中有效
- total 字段仅在 type=page 时返回


## 请求地址

```
{域名地址}/api/archive/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/archive/list`

## 请求语法

```
GET {域名地址}/api/archive/list?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id | int | 否 | 文档 ID，当要获取 type=related 的时候需要指定 |
| moduleId | int | 否 | 模型 ID |
| parentId | int | 否 | 上级文档 ID |
| categoryId | string | 否 | 文档分类 ID，多个分类 ID 可用,隔开 |
| excludeCategoryId | string | 否 | 排除的文档分类 ID，多个分类 ID 可用,隔开 |
| order | string | 否 | 排序方式，如：`id desc`，支持的字段有：`id`、`views`、`category_id`、`created_time`、`updated_time`等 |
| type | int | 否 | 支持按 `page`、`list`、`related` 方式列出。默认值为`list`，type="list" 时，只会显示 指定的 limit 指定的数量，如果 type="page" 则可获取文档数量 total |
| flag | string | 否 | 推荐属性 `flag` 支持的属性值有 头条[h]、推荐[c]、幻灯[f]、特荐[a]、滚动[s]、加粗[h]、图片[p]、跳转[j]。如要显示 flag 属性为推荐的，则标签为 flag="c" |
| showFlag | boolean | 否 | 是否显示推荐属性，支持的属性值有 false\|true，默认 false |
| showContent | boolean | 否 | 是否显示文档内容，支持的属性值有 false\|true，默认 false |
| showExtra | boolean | 否 | 是否显示文档的额外内容，支持的属性值有 false\|true，默认 false |
| showOptions | boolean | 否 | 是否显示文档的规格属性选项，支持的属性值有 false\|true，默认 false |
| showSkus | boolean | 否 | 是否显示文档的规格列表，支持的值有 false\|true，默认 false |
| showWholesaleRules | boolean | 否 | 是否显示批发规则，支持的属性值有 false\|true，默认 false |
| showCategory | boolean | 否 | 是否显示文档分类，支持的属性值有 false\|true，默认 true |
| child | boolean | 否 | 是否显示所有子分类的文档，支持的属性值有 false\|true，默认 true。如只想显示属于当前分类的文档，而不包括子分类的文档，则需指定 child=false |
| page | int | 否 | 指定获取第几页内容，仅当 type="page"时候生效 |
| limit | int | 否 | 显示数量，limit 可以指定显示数量，按多少数量来分页，比如 limit="10"则只会显示 10 条，limit 在不是分页列表的时候，支持 offset 模式，也就是 ,分隔模式，如想从第 2 条开始，获取 10 条数据，可以设置成 limit="2,10"。 |
| q | string | 否 | 搜索关键词，可以指定搜索内容，如果需要搜索内容，可以通过参数 q 来展示指定包含关键词的标题搜索内容如 q="seo" 呈现结果将只显示标题包含 seo 关键词的列表。也可以不指定，如果 url 中存在 q=关键词 的 query 参数，则在分页列表中会自动读取 q 关键词内容并用于搜索。 |
| 自定义筛选参数 | string | 否 | 筛选参数，如在文档额外自动配置中，配置了可筛选的字段，可以通过这些参数，来完成对文档进行参数是筛选。如你的文档中设置了筛选自动为 gender,默认值有 男，女，保密，则你可以通过 url 的 query 参数 gender=男 来搜索文档 gender 字段是男的文档内容。筛选条件支持多选，多个条件用 , 分割，如 gender=男,女 |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :------- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | [array[object]](#data结果item参数) | 结果内容 |
| total | int | 文档数量，仅当 type=page 的时候会返回 |

#### data结果item参数

| 字段名        | 类型     | 说明                                                                   |
| :------------ | :------- | :--------------------------------------------------------------------- |
| id            | int      | 文档 ID                                                                |
| is_wholesale | bool | 是否是批发商品 |
| wholesale_rules | object[] | 批发规则列表 |
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
| extra         | [object#extra](#extra文档其他字段信息)   | 文档其他字段信息                                                       |

##### extra文档其他字段信息

extra 根据模型设置的字段显示，字段结构为 key => item：
key 表单字段调用名，item 为内容：

|字段名|类型|说明|
|:---|:---|:---|
|name|string|字段名称|
|value|string|填写的值|
|default|string|默认值|

### 请求数据示例

| 参数     | 值   |
| :------- | :--- |
| moduleId | 1    |
| type     | page |

## 使用示例

### 请求示例

```
GET /api/archive/list?moduleId=1&type=page HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": 1,
      "created_time": 1607308159,
      "updated_time": 1662717106,
      "title": "关于AICMS",
      "seo_title": "",
      "url_token": "design",
      "keywords": "",
      "description": "AI内容管理系统(AICMS)，是一款使用 GoLang 开发的企业站内容管理系统，它部署简单，软件安全，界面优雅，小巧，执行速度飞快，使用 AICMS 搭建的网站可以防止众多安全问题发生。",
      "module_id": 1,
      "category_id": 1,
      "views": 1338,
      "comment_count": 0,
      "images": null,
      "template": "",
      "status": 1,
      "canonical_url": "",
      "fixed_link": "",
      "flag": "",
      "user_id": 0,
      "price": 0,
      "stock": 9999999,
      "has_pseudo": 0,
      "keyword_id": 0,
      "origin_url": "",
      "origin_title": "",
      "category": null,
      "module_name": "",
      "data": null,
      "logo": "https://www.aicms.com/uploads/202012/7/bd36c37ef742c7be.webp",
      "thumb": "https://www.aicms.com/uploads/202012/7/thumb_bd36c37ef742c7be.webp",
      "extra": {
        "author": {
          "name": "作者",
          "value": "AICMS",
          "default": null
        },
        "certificate": {
          "name": "学历",
          "value": null,
          "default": null
        },
        "city": {
          "name": "城市",
          "value": null,
          "default": null
        }
      },
      "link": "https://www.aicms.com/design"
    },
    {
      "id": 2,
      "created_time": 1607308247,
      "updated_time": 1611373941,
      "title": "AICMS使用帮助",
      "seo_title": "",
      "url_token": "help",
      "keywords": "",
      "description": "AICMS常见问题汇总",
      "module_id": 1,
      "category_id": 1,
      "views": 1655,
      "comment_count": 0,
      "images": null,
      "template": "",
      "status": 1,
      "canonical_url": "",
      "fixed_link": "",
      "flag": "",
      "user_id": 0,
      "price": 0,
      "stock": 9999999,
      "has_pseudo": 0,
      "keyword_id": 0,
      "origin_url": "",
      "origin_title": "",
      "category": null,
      "module_name": "",
      "data": null,
      "logo": "https://www.aicms.com/uploads/202012/7/bd36c37ef742c7be.webp",
      "thumb": "https://www.aicms.com/uploads/202012/7/thumb_bd36c37ef742c7be.webp",
      "extra": null,
      "link": "https://www.aicms.com/help"
    }
  ],
  "msg": "",
  "total": 2
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
