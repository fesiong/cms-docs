# 获取购物车列表接口

获取当前用户购物车中的商品列表，支持分页功能，返回商品详细信息及购物车相关数据。

## 注意事项

- 接口支持登录用户和未登录用户（通过 cart token 识别）
- 支持分页查询，可通过 current 和 pageSize 参数控制分页
- 返回的商品信息包含购物车中的数量、价格等信息
- total 字段返回购物车中商品的总数量

## 请求地址

```
{域名地址}/api/cart/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/cart/list`

## 请求语法

```
GET {域名地址}/api/cart/list?{参数}
```

## 请求头

| 字段名 | 类型 | 必填 | 说明 |
| :---------------- | :------ | :--- | :-------------------- |
| cart | string | 否 | 当没有登录的时候，用此token作为用户判断 |

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名            | 类型    | 必填 | 说明            |
| :---------------- | :------ | :--- | :-------------------- |
| current  | int  | 否   | 获取指定分页数据，当前页码 |
| pageSize | int  | 否   | 显示数量，每页数量         |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明                                  |
| :----- | :------- | :------------------------------------ |
| code   | int      | 错误码                                |
| msg    | string   | 错误原因说明                          |
| data   | object[] | 结果内容，购物车商品列表               |
| total  | int      | 购物车商品总数量                      |

#### data 结果 item 参数

| 字段名        | 类型            | 说明                                                                   |
| :------------ | :-------------- | :--------------------------------------------------------------------- |
| id            | int             | 购物车 ID                                                              |
| archive_id    | int             | 商品 ID                                                                |
| sku_id        | int             | SKU ID，为 0 则表示无规格                                              |
| sku_values    | array           | SKU 选项值列表                                                        |
| quantity      | int             | 购买数量                                                               |
| origin_price  | int             | 加入购物车时的价格，单位分                                            |
| status        | int             | 状态                                                                  |
| user_id       | int             | 用户 ID                                                                |
| token         | string          | 购物车 token，用于未登录用户识别                                       |
| created_time  | int             | 加入购物车时间戳                                                      |
| updated_time  | int             | 更新时间戳                                                            |
| order_extra   | object          | 订单扩展信息                                                          |
| price         | int             | 当前计算价格，单位分（已考虑 SKU、加价属性、批发价等因素）             |
| amount        | int             | 小计金额，单位分（quantity × price）                                   |
| origin_amount | int             | 原始金额，单位分（quantity × origin_price）                             |
| archive       | object          | 商品详细信息                                                           |
| sku           | object          | SKU 信息（仅在有规格时返回）                                           |

##### archive 商品对象

| 字段名          | 类型     | 说明                                                                   |
| :-------------- | :------- | :--------------------------------------------------------------------- |
| id              | int      | 商品 ID                                                                |
| title           | string   | 商品标题                                                               |
| seo_title       | string   | SEO 标题                                                               |
| url_token       | string   | URL 别名                                                               |
| keywords        | string   | 关键词                                                                 |
| description     | string   | 简介                                                                   |
| module_id       | int      | 模型 ID                                                                |
| category_id     | int      | 分类 ID                                                                |
| views           | int      | 浏览量                                                                 |
| comment_count   | int      | 评论量                                                                 |
| images          | array    | 商品组图                                                               |
| logo            | string   | 商品 Logo                                                              |
| thumb           | string   | 商品缩略图                                                             |
| flag            | string   | 推荐属性：头条[h]推荐[c]幻灯[f]特荐[a]滚动[s]加粗[b]图片[p]跳转[j]     |
| canonical_url   | string   | 规范链接                                                               |
| fixed_link      | string   | 固定链接                                                               |
| created_time    | int      | 发布时间戳                                                             |
| updated_time    | int      | 更新时间戳                                                             |
| status          | int      | 状态                                                                   |
| user_id         | int      | 用户 ID                                                                |
| price           | int      | 商品价格，单位分                                                       |
| stock           | int      | 库存量                                                                 |
| wholesale_rule  | object   | 适用的批发规则（当商品为批发类型且达到起订量时返回）                      |

##### sku_values 选项值对象

| 字段名       | 类型   | 说明                    |
| :---------- | :----- | :---------------------- |
| id          | int    | 选项值 ID                |
| option_id   | int    | 所属规格 ID              |
| title       | string | 选项值名称（如"红色"）   |
| option_title| string | 规格名称（如"颜色"）    |
| price       | int    | 加价金额，单位分        |
| stock       | int    | 库存量                  |

##### sku SKU对象

| 字段名       | 类型   | 说明                    |
| :---------- | :----- | :---------------------- |
| id          | int    | SKU ID                  |
| title       | string | SKU 名称（如"红色-L"）  |
| price       | int    | SKU 价格，单位分        |
| stock       | int    | SKU 库存量              |
| thumb       | string | SKU 缩略图              |
| sku         | string | 货号                    |
| barcode     | string | 条形码                  |

##### wholesale_rule 批发规则对象

| 字段名        | 类型 | 说明                        |
| :------------ | :--- | :-------------------------- |
| id            | int  | 规则 ID                     |
| min_quantity  | int  | 最小起订量                  |
| max_quantity  | int  | 最大数量限制                |
| discount_rate | int  | 折扣率（百分比）            |

## 使用示例

### 请求示例

```
GET /api/cart/list?current=1&pageSize=20 HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": [
    {
      "id": 123,
      "archive_id": 456,
      "sku_id": 789,
      "sku_values": [
        {
          "id": 1,
          "option_id": 10,
          "title": "红色",
          "option_title": "颜色",
          "price": 0,
          "stock": 100
        },
        {
          "id": 5,
          "option_id": 11,
          "title": "L",
          "option_title": "尺码",
          "price": 0,
          "stock": 50
        }
      ],
      "user_id": 1,
      "token": "abc123-def456",
      "quantity": 2,
      "origin_price": 2999,
      "status": 0,
      "created_time": 1607308159,
      "updated_time": 1662717106,
      "order_extra": {},
      "price": 2999,
      "amount": 5998,
      "origin_amount": 5998,
      "archive": {
        "id": 456,
        "title": "AICMS 限量版 T 恤",
        "seo_title": "",
        "url_token": "AICMS-tshirt",
        "keywords": "T桖,周边,限量",
        "description": "AICMS 官方限量版 T 恤，纯棉材质，舒适透气",
        "module_id": 1,
        "category_id": 5,
        "views": 1338,
        "comment_count": 10,
        "images": [],
        "status": 1,
        "user_id": 0,
        "price": 2999,
        "stock": 100,
        "wholesale_rule": {
          "id": 1,
          "min_quantity": 10,
          "max_quantity": 0,
          "discount_rate": 90
        }
      },
      "sku": {
        "id": 789,
        "title": "红色-L",
        "price": 3299,
        "stock": 50,
        "thumb": "https://www.example.com/uploads/thumb_sku.webp",
        "sku": "TSHIRT-RED-L",
        "barcode": "1234567890123"
      }
    }
  ],
  "msg": "",
  "total": 1
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
