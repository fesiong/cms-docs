# 获取订单列表接口

获取用户的订单列表，支持按订单状态筛选和分页查询。

## 注意事项

- 该接口采用GET方法
- 需要用户登录验证
- 支持按订单状态筛选（待付款、已付款、已发货、已完成等）
- 支持分页查询，默认每页数量由pageSize参数决定
- 只返回当前登录用户的订单信息

## 请求地址

```
{域名地址}/api/orders
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/orders`

## 请求语法

```
GET {域名地址}/api/orders
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :------------------- | :------- | :--- | :---------------------- |
| status | string | 否 | 订单状态，默认为空，支持的值有：空值、waiting（待付款）、paid（已付款）、delivery（已发货）、finished（已完成）、refunding（退款中） |
| current | int | 否 | 当前页码，默认为1 |
| pageSize | int | 否 | 每页显示数量，默认为10 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :----------- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 订单列表数组 |
| total | int | 订单总数 |

#### data 结果 item 参数

| 字段名 | 类型 | 说明 |
| :------------------- | :------- | :-------------------------- |
| id | int | 订单ID |
| order_id | string | 订单号 |
| payment_id | string | 支付流水ID |
| user_id | int | 用户ID |
| remark | string | 订单备注 |
| type | string | 订单类型 |
| origin_amount | int | 订单原始总价（单位：分） |
| amount | int | 订单实际总价（单位：分） |
| paid_time | int | 支付时间戳，未支付为0 |
| end_time | int | 订单预计自动完成时间戳 |
| deliver_time | int | 发货时间戳，未发货为0 |
| finished_time | int | 订单完成时间戳，未完成为0 |
| discount_amount | int | 优惠金额（单位：分） |
| seller_id | int | 卖家ID |
| seller_amount | int | 卖家可得收益（单位：分） |
| share_user_id | int | 推广者ID |
| share_parent_user_id | int | 推广者上级ID |
| share_amount | int | 推广者可得收益（单位：分） |
| share_parent_amount | int | 推广者上级可得收益（单位：分） |
| express_company | string | 快递公司 |
| tracking_number | string | 快递运单号 |
| user | object | 买家用户信息 |
| details | object[] | 订单详情信息列表 |
| created_time | int | 下单时间戳 |
| status | int | 订单状态：-1 取消，0 待付款，1 已付款，2 已发货，3 已完成，8 退款中，9 已退款 |
| refund_status | int | 退款状态：-1 退款失败，0 无或退款中，1 已退款 |

#### user 买家用户信息参数

| 字段名 | 类型 | 说明 |
| :----------- | :----- | :-------------------------- |
| id | int | 用户ID |
| parent_id | int | 上级用户ID |
| user_name | string | 用户名 |
| real_name | string | 真实姓名 |
| avatar_url | string | 用户头像地址 |
| email | string | 邮箱地址 |
| phone | string | 手机号 |
| group_id | int | 用户组ID |
| is_retailer | int | 是否是分销员 |
| balance | int | 用户余额（单位：分） |
| total_reward | int | 分销员累计收益（单位：分） |
| invite_code | string | 用户邀请码 |
| last_login | int | 最近一次登录时间戳 |
| expire_time | int | 过期时间戳 |
| created_time | int | 注册时间戳 |
| updated_time | int | 更新时间戳 |
| status | int | 用户显示状态 |

#### details 订单详情信息参数

| 字段名 | 类型 | 说明 |
| :------------ | :----- | :-------------------------- |
| id | int | 订单详情ID |
| order_id | string | 订单号 |
| user_id | int | 用户ID |
| goods_id | int | 商品ID |
| goods_item_id | int | 商品SKU ID |
| price | int | 商品价格（单位：分） |
| origin_price | int | 商品原价（单位：分） |
| amount | int | 商品实际总价（单位：分） |
| origin_amount | int | 商品原始总价（单位：分） |
| quantity | int | 商品数量 |
| status | int | 状态 |
| goods | object | 商品详细信息 |

#### goods 商品详细信息参数

| 字段名 | 类型 | 说明 |
| :------------ | :------- | :-------------------------- |
| id | int | 文档ID |
| title | string | 文档标题 |
| seo_title | string | 文档SEO标题 |
| url_token | string | 文档URL别名 |
| keywords | string | 文档关键词 |
| description | string | 文档简介 |
| module_id | int | 文档模型ID |
| category_id | int | 文档分类ID |
| views | int | 文档浏览量 |
| comment_count | int | 文档评论量 |
| images | string[] | 文档组图 |
| logo | string | 文档Logo |
| thumb | string | 文档缩略图 |
| canonical_url | string | canonical URL |
| fixed_link | string | 文档固定链接 |
| created_time | int | 文档发布时间戳 |
| updated_time | int | 文档更新时间戳 |
| status | int | 文档显示状态 |
| user_id | int | 用户ID |
| price | int | 价格（单位：分） |
| stock | int | 库存量 |

## 使用示例

### 请求示例

```
GET /api/orders?status=paid&current=1&pageSize=10 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 46,
      "created_time": 1669212548,
      "updated_time": 1669212548,
      "order_id": "202211232209080046",
      "payment_id": "202211232209080016",
      "user_id": 1000,
      "address_id": 0,
      "remark": "英文外贸响应式通用主题wzl-008等",
      "type": "goods",
      "status": 0,
      "refund_status": 0,
      "origin_amount": 9900,
      "amount": 9900,
      "paid_time": 0,
      "end_time": 0,
      "deliver_time": 0,
      "finished_time": 0,
      "discount_amount": 0,
      "seller_id": 15,
      "seller_amount": 7920,
      "share_user_id": 0,
      "share_parent_user_id": 0,
      "share_amount": 0,
      "share_parent_amount": 0,
      "express_company": "",
      "tracking_number": "",
      "user": {
        "id": 1000,
        "created_time": 1669012062,
        "updated_time": 1679536756,
        "parent_id": 0,
        "user_name": "sinclair",
        "real_name": "",
        "avatar_url": "uploads/202211/21/14f56760596b5328.webp",
        "email": "",
        "phone": "",
        "group_id": 2,
        "status": 1,
        "is_retailer": 0,
        "balance": 0,
        "total_reward": 0,
        "invite_code": "1dzil93",
        "last_login": 1702912236,
        "expire_time": 1997404800,
        "integral": 9968520,
        "ai_remain": 30,
        "extra": null,
        "token": "",
        "group": null,
        "full_avatar_url": "",
        "link": ""
      },
      "is_updated": 0,
      "details": [
        {
          "id": 16,
          "created_time": 1669212548,
          "updated_time": 1669212548,
          "order_id": "202211232209080046",
          "user_id": 1000,
          "goods_id": 188,
          "goods_item_id": 0,
          "price": 9900,
          "origin_price": 9900,
          "amount": 9900,
          "origin_amount": 9900,
          "quantity": 1,
          "status": 1,
          "goods": {
            "id": 188,
            "created_time": 1669122751,
            "updated_time": 1669122751,
            "title": "英文外贸响应式通用主题wzl-008",
            "seo_title": "",
            "url_token": "ywwmxystyztw0-7",
            "keywords": "英文外贸响应式通用主题wzl-008",
            "description": "英文主题，外贸主题，响应式主题，通用英文企业站主题",
            "module_id": 3,
            "category_id": 36,
            "views": 158,
            "comment_count": 0,
            "images": [
              "https://www.aicms.com/uploads/202211/22/6315f8a943b979a4.webp",
              "https://www.aicms.com/uploads/202211/22/c705ba844eb51aec.webp"
            ],
            "template": "",
            "status": 1,
            "canonical_url": "",
            "fixed_link": "",
            "flag": "",
            "user_id": 15,
            "price": 9900,
            "stock": 9999999,
            "read_level": 0,
            "password": "",
            "sort": 0,
            "has_pseudo": 0,
            "keyword_id": 0,
            "origin_url": "",
            "origin_title": "",
            "origin_id": 0,
            "category": null,
            "module_name": "",
            "data": null,
            "logo": "https://www.aicms.com/uploads/202211/22/6315f8a943b979a4.webp",
            "thumb": "https://www.aicms.com/uploads/202211/22/thumb_6315f8a943b979a4.webp",
            "extra": null,
            "link": "https://www.aicms.com/endesign/188.html",
            "has_ordered": false,
            "favorable_price": 0,
            "has_password": false,
            "category_titles": null,
            "category_ids": null
          },
          "group": null
        }
      ]
    }
  ],
  "total": 1
}
```

### 错误代码

| 错误码 | 说明 |
| :----- | :-------------------------- |
| 0 | OK |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求 OK |