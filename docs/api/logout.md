# 退出登录接口

用户退出登录，清除当前登录状态和会话信息，支持返回HTML页面或JSON数据格式。

## 注意事项

- 该接口采用GET方法
- 需要提供随机字符串防止接口被缓存
- 支持返回HTML页面或JSON数据格式
- 退出登录后会清除用户会话信息
- 适用于网站前端用户退出功能

## 请求地址

```
{域名地址}/logout
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/logout`

## 请求语法

```
GET {域名地址}/logout
```

## 请求参数

| 字段名 | 类型   | 必填 | 说明            |
| :----- | :----- | :--- | :-------------------- |
| return | string | 否   | 支持：html|json,默认：html,将返回html内容 |
| nonce  | string | 是   | 随机字符串，防止接口被缓存 |

## 返回参数

根据请求参数不同，返回内容也不同：

- 当 `return=json` 时，返回JSON格式数据：
  - code: int - 错误码
  - msg: string - 错误原因说明

- 当 `return=html` 或不指定时，返回HTML页面内容

## 使用示例

### JSON格式返回请求示例

```
GET /logout?return=json&nonce=1234567890 HTTP/1.1
Host: www.aicms.com
```

### JSON格式返回响应示例

```json
{
  "code": 0,
  "msg": "退出成功"
}
```

### HTML格式返回请求示例

```
GET /logout?nonce=0987654321 HTTP/1.1
Host: www.aicms.com
```

### HTML格式返回响应示例

```
HTTP/1.1 302 Found
Location: /
```

### 前端JavaScript调用示例

```javascript
// 退出登录并返回JSON结果
$.get("/logout", {
  return: "json",
  nonce: Date.now()
}, function(res) {
  if (res.code === 0) {
    console.log('退出成功');
    window.location.href = '/'; // 跳转到首页
  } else {
    console.error('退出失败', res.msg);
  }
}, 'json');

// 直接跳转退出（HTML返回）
function logout() {
  window.location.href = '/logout?nonce=' + Date.now();
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