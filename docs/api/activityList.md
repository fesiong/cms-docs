# 获取活动列表接口

获取当前启用的营销活动列表，支持分页查询。

## 请求地址

```
{域名地址}/api/activity/list
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/activity/list`

## 请求语法

```
GET {域名地址}/api/activity/list?{参数}
```

## 请求头

此接口仅涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名            | 类型    | 必填 | 说明            |
| :---------------- | :------ | :--- | :-------------------- |
| current  | int  | 否   | 获取指定分页数据，当前页码 |
| pageSize | int  | 否   | 显示数量，每页数量         |

## 响应头

此接口仅涉及公共相应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型     | 说明                  |
| :----- | :------- | :-------------------- |
| code   | int      | 错误码                |
| msg    | string   | 错误原因说明          |
| data   | object[] | 活动列表              |
| total  | int      | 活动总数量            |

#### data 结果 item 参数

| 字段名         | 类型    | 说明                  |
| :------------- | :------ | :-------------------- |
| id             | int     | 活动 ID               |
| name           | string  | 活动名称              |
| title          | string  | 活动标题              |
| description    | string  | 活动描述              |
| goods_id       | int     | 关联商品 ID           |
| type           | int     | 活动类型              |
| price          | int     | 活动价格，单位分      |
| original_price | int     | 原始价格，单位分      |
| start_time     | int     | 活动开始时间戳        |
| end_time       | int     | 活动结束时间戳        |
| status         | int     | 活动状态              |
| min_quantity   | int     | 最小购买数量          |
| max_quantity   | int     | 最大购买数量          |
| can_use_coupon | bool    | 是否可使用优惠券      |
| stock          | int     | 活动库存              |
| sold_count     | int     | 已售数量              |
| created_time   | int     | 创建时间戳            |
| updated_time   | int     | 更新时间戳            |

## 使用示例

### 请求示例

```
GET /api/activity/list?current=1&pageSize=20 HTTP/1.1
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
      "name": "限时特惠",
      "title": "夏季大促",
      "description": "全场商品8折优惠",
      "goods_id": 123,
      "type": 0,
      "price": 2999,
      "original_price": 3999,
      "start_time": 1607308159,
      "end_time": 1607912759,
      "status": 1,
      "min_quantity": 1,
      "max_quantity": 10,
      "can_use_coupon": true,
      "stock": 100,
      "sold_count": 15,
      "created_time": 1607308159,
      "updated_time": 1662717106
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