# 获取产品SKU接口

获取指定产品的SKU（库存量单位）信息，包括产品的规格属性、价格、库存、批发规则等详细信息。此接口适用于需要展示产品详细规格和购买选项的场景。

## 注意事项

- 接口支持通过产品 ID 或 URL 别名（filename）两种方式获取产品SKU信息
- 此接口为产品接口，适用于产品类型文档
- 返回数据包含产品的完整规格信息和SKU列表
- 如果产品不存在，接口会返回错误码

## 请求地址

```
{域名地址}/api/archive/sku
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/archive/sku`

## 请求语法

```
GET {域名地址}/api/archive/sku?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名   | 类型   | 必填 | 说明                                      |
| :------- | :----- | :--- | :---------------------------------------- |
| id       | int    | 是   | 文档 ID，如果传了 filename，可以不用传 ID |
| filename | string | 否   | 文档 URL 别名，文档 ID、filename 二选一   |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | object | 结果内容     |

#### data 参数

| 字段名        | 类型     | 说明      |
| :------------ | :------- | :------- |
| id       | int    | 产品 ID     |
| title | string | 产品标题     |
| currency | string | 货币名称     |
| curency_symbol | string | 货币符号     |
| price | float | 产品价格     |
| min_price | float | 产品最低价格 |
| max_price | float | 产品最高价格 |
| user_limit | int | 用户限购数量 |
| quota_used | int | 用户已购数量 |
| order_count | int | 销量 |
| stock | int | 库存数量 |
| options | object[] | 产品规格属性名称     |
| skus | object[] | 产品SKU信息     |
| wholesale_rules | object[] | 产品批发规则     |


##### option 产品规格属性名称

| 字段名       | 类型     | 说明                         |
| :----------- | :------- | :--------------------------- |
| id           | int      | 属性ID                      |
| title        | string   | 属性名称                     |
| values    | object[]   | 属性 value 列表                |

##### 属性 value

| 字段名  | 类型   | 说明         |
| :------ | :----- | :----------- |
| id      | int    | 分类 ID      |
| option_id | int  | 属性 ID      | 
| option_title | string   | 属性名称       |
| title | string | 属性 value 名称 |
| color | string | 颜色值 |
| price | float | 价格     |

##### sku 产品SKU信息

| 字段名  | 类型   | 说明         |
| :------ | :----- | :----------- |
| id      | int    | 分类 ID      |
| title | string | sku 名称 |
| symbol | string | 规格属性值id链接符号 |
| values | object[] | 属性 value 列表 |
| sku | string | sku 链接符号 |
| barcode | string | 条形码 |
| hs_code | string | 海关编码 |
| logo | string | logo |
| thumb | string | 缩略图 |
| stock | int | 库存数量 |
| price | int | 价格     |
| origin_price | int | 原价     |
| weight | int | 重量     |
| weight_unit | string | 重量单位 |
| sold_count | int | 销量 |

##### wholesale_rules 产品批发规则

| 字段名  | 类型   | 说明         |
| :------ | :----- | :----------- |
| id | int | 规则 ID |
| archive_id | int | 文档 ID |
| min_quantity | int | 最小数量 |
| max_quantity | int | 最大数量 |
| sku_id | int | sku ID |
| discount_rate | int | 折扣率， 0-100 |
| created_time | int | 创建时间 |
| updated_time | int | 更新时间 |

## 使用示例

### 请求示例

```
GET /api/archive/sku?id=1 HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

或

```
GET /api/archive/sku?filename=product-slug HTTP/1.1
Host: your-domain.com
Content-Type: application/json
```

### 响应示例

```json
{
  "code": 0,
  "data": {
    "id": 1,
    "title": "示例产品",
    "currency": "人民币",
    "currency_symbol": "¥",
    "price": 100.00,
    "min_price": 80.00,
    "max_price": 120.00,
    "user_limit": 10,
    "quota_used": 2,
    "order_count": 100,
    "stock": 998,
    "options": [
      {
        "id": 1,
        "title": "颜色",
        "values": [
          {
            "id": 1,
            "option_id": 1,
            "option_title": "颜色",
            "title": "红色",
            "color": "#FF0000",
            "price": 100.00
          },
          {
            "id": 2,
            "option_id": 1,
            "option_title": "颜色",
            "title": "蓝色",
            "color": "#0000FF",
            "price": 100.00
          }
        ]
      },
      {
        "id": 2,
        "title": "尺寸",
        "values": [
          {
            "id": 3,
            "option_id": 2,
            "option_title": "尺寸",
            "title": "大号",
            "color": "",
            "price": 100.00
          },
          {
            "id": 4,
            "option_id": 2,
            "option_title": "尺寸",
            "title": "小号",
            "color": "",
            "price": 100.00
          }
        ]
      }
    ],
    "skus": [
      {
        "id": 1,
        "title": "红色-大号",
        "symbol": "1-3",
        "values": [
          {
            "id": 1,
            "option_id": 1,
            "option_title": "颜色",
            "title": "红色",
            "color": "#FF0000",
            "price": 100.00
          },
          {
            "id": 3,
            "option_id": 2,
            "option_title": "尺寸",
            "title": "大号",
            "color": "",
            "price": 100.00
          }
        ],
        "sku": "SKU001",
        "barcode": "123456789",
        "hs_code": "",
        "logo": "",
        "thumb": "",
        "stock": 100,
        "price": 10000,
        "origin_price": 12000,
        "weight": 100,
        "weight_unit": "g",
        "sold_count": 50
      }
    ],
    "wholesale_rules": [
      {
        "id": 1,
        "archive_id": 1,
        "min_quantity": 1,
        "max_quantity": 10,
        "sku_id": 1,
        "discount_rate": 90,
        "created_time": 1630000000,
        "updated_time": 1630000000
      }
    ]
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
