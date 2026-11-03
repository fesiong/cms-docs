# 获取用户分组列表接口

获取系统中所有用户分组的列表信息，包括各分组的名称、等级、价格、配置等详细信息。

## 注意事项

- 该接口采用GET方法
- 无需登录即可访问此接口
- 返回系统中所有可用的用户分组信息
- 包含分组的基本信息和配置信息
- 配置信息包括分享收益、上级收益、折扣和过期天数等设置

## 请求地址

```
{域名地址}/api/user/groups
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/user/groups`

## 请求语法

```
GET {域名地址}/api/user/groups
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

无

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |
| data | object[] | 用户分组列表数据 |

#### data item 参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| id | int | 分组ID |
| title | string | 分组名称 |
| description | string | 分组简介 |
| level | int | 分组等级 |
| price | int | 分组价格 |
| setting | object | 配置信息 |
| status | int | 显示状态 |
| favorable_price | int | 优惠价，当用户登录时可显示 |
| created_time | int | 创建时间戳 |
| updated_time | int | 更新时间戳 |

##### setting 配置信息参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| share_reward | int | 分享收益百分比 |
| parent_reward | int | 上级收益百分比 |
| discount | int | 用户购买折扣 |
| expire_day | int | 过期天数 |

## 使用示例

### 请求示例

```
GET /api/user/groups HTTP/1.1
Host: www.aicms.com
```

### 响应示例

#### 成功响应
```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "id": 1,
      "title": "普通用户",
      "description": "<ul> <li>有效期不限制</li>  <li>最多管理2个站点</li> <li>最多2个/1万关键词导出任务</li> <li>最多2个采集文章任务</li> <li>最多2个文章组合任务</li> <li>最多2个文章监控任务</li> <li>整站采集/下载不可用</li>  <li>累计AI写作额度 10 篇<div class=\"extra\">超出数量 10 积分一篇</div> </li> </ul>",
      "level": 0,
      "price": 0,
      "setting": {
        "share_reward": 20,
        "parent_reward": 0,
        "discount": 95,
        "expire_day": 0
      },
      "status": 1,
      "favorable_price": 0,
      "created_time": 0,
      "updated_time": 1696919880
    },
    {
      "id": 2,
      "title": "VIP用户",
      "description": "<ul> <li>一年有效期</li>  <li>不限制管理站点数量</li> <li>不限制关键词任务</li> <li>不限制采集文章任务</li> <li>不限制文章组合任务</li> <li>不限制文章监控任务</li> <li>可用整站采集/下载</li> <li>每天AI写作额度 100 篇<div class=\"extra\">超出数量 10 积分一篇</div> </ul>",
      "level": 1,
      "price": 68800,
      "setting": {
        "share_reward": 30,
        "parent_reward": 0,
        "discount": 95,
        "expire_day": 365
      },
      "status": 1,
      "favorable_price": 0,
      "created_time": 0,
      "updated_time": 1696919899
    }
  ]
}
```

#### 空列表响应
```json
{
  "code": 0,
  "msg": "",
  "data": []
}
```

### 错误代码

| 错误码 | 说明 |
| :----- | :--- |
| 0 | OK |
| -1 | 错误，错误原因在 msg 中指出 |
| 1001 | 未登录 |
| 1002 | 未授权 |
| 200 | API 请求 OK |