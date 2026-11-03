# 更新用户信息接口

更新当前登录用户的基本信息，包括用户名、真实姓名、个人介绍、邮箱和手机号等个人信息。

## 注意事项

- 该接口采用POST方法，需要以application/json格式提交数据
- 需要用户登录后才能调用此接口
- 所有参数都是可选的，可以只更新需要修改的字段
- 用户名、邮箱和手机号可能需要唯一性验证
- 更新成功后会返回操作结果

## 请求地址

```
{域名地址}/api/user/detail
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/user/detail`

## 请求语法

```
POST {域名地址}/api/user/detail
Content-Type: application/json
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
| :----- | :----- | :--- | :--- |
| user_name | string | 否 | 用户名，如不提供则不更新此项 |
| real_name | string | 否 | 真实姓名，如不提供则不更新此项 |
| introduce | string | 否 | 用户介绍，如不提供则不更新此项 |
| email | string | 否 | 邮箱地址，如不提供则不更新此项 |
| phone | string | 否 | 手机号码，如不提供则不更新此项 |

## 响应头

此接口仅涉及公共响应头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

### 返回参数

| 字段名 | 类型 | 说明 |
| :----- | :----- | :--- |
| code | int | 错误码 |
| msg | string | 错误原因说明 |

## 使用示例

### 请求示例

#### 更新用户名和真实姓名
```
POST /api/user/detail HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "user_name": "new_username",
  "real_name": "张三"
}
```

#### 更新邮箱和手机号
```
POST /api/user/detail HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "email": "newemail@example.com",
  "phone": "13800138000"
}
```

#### 更新个人介绍
```
POST /api/user/detail HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "introduce": "这是一段新的个人介绍"
}
```

#### 同时更新多个字段
```
POST /api/user/detail HTTP/1.1
Host: www.aicms.com
Content-Type: application/json

{
  "user_name": "updated_user",
  "real_name": "李四",
  "email": "updated@example.com",
  "phone": "13900139000",
  "introduce": "更新后的个人介绍"
}
```

### 响应示例

#### 成功响应
```json
{
  "code": 0,
  "msg": "保存成功"
}
```

#### 失败响应
```json
{
  "code": -1,
  "msg": "用户名已存在"
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