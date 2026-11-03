# 获取文档分类接口

获取系统中所有文档分类信息，支持按模块类型筛选（文章或产品），用于内容导入或分类管理功能。

## 注意事项

- 该接口采用GET方法
- 需要提供有效的后台导入接口Token进行身份验证
- 必须指定模块ID来获取对应的分类类型
- 支持获取文章分类和产品分类两种类型
- 返回的分类信息包含层级关系（通过parent_id区分）

## 请求地址

```
{域名地址}/api/import/categories?token={token}
```

说明：`{域名地址}` 需要替换成你的域名地址，`{token}` 需要更换为后台内容导入接口功能里的 Token，如 `https://www.aicms.com/api/import/categories?token=xxx`

## 请求语法

```
GET {域名地址}/api/import/categories?token={token}&module_id={module_id}
```

## 请求参数

| 字段名    | 类型   | 必填 | 说明                                               |
| :-------- | :----- | :--- | :------------------------------------------------- |
| token     | string | 是   | 后台内容导入接口功能里的 Token                     |
| module_id | int    | 是   | 要获取的分类类型，填数字，支持的值：1 文章，2 产品 |

## 返回参数

| 字段名 | 类型   | 说明         |
| :----- | :----- | :----------- |
| code   | int    | 错误码       |
| msg    | string | 错误原因说明 |
| data   | array  | 分类列表     |

### data 参数

| 字段名    | 类型   | 说明           |
| :-------- | :----- | :------------- |
| id        | int    | 分类 ID        |
| parent_id | int    | 父级分类 ID    |
| title     | string | 分类标题       |

## 使用示例

### 请求示例

```
GET /api/import/categories?token=4712a54b4c456bb29b7816d241db69a7&module_id=1 HTTP/1.1
Host: www.aicms.com
```

### 响应示例

```json
{
  "code": 200,
  "data": [
    {
      "id": 1,
      "parent_id": 0,
      "title": "golang实战教程"
    },
    {
      "id": 10,
      "parent_id": 0,
      "title": "AICMS使用帮助"
    },
    {
      "id": 11,
      "parent_id": 10,
      "title": "AICMS基础"
    },
    {
      "id": 13,
      "parent_id": 10,
      "title": "AICMS模板制作"
    },
    {
      "id": 12,
      "parent_id": 10,
      "title": "AICMS后台操作教程"
    }
  ],
  "msg": "获取成功"
}
```

### 错误响应示例

```json
{
  "code": -1,
  "msg": "Token无效"
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