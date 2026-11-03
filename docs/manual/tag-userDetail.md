# 用户详情标签

说明：用于获取用户详情数据

使用方法：`{% userDetail 变量名称 with name="字段名称" id="1" %}` 变量名称不是必须的，设置了变量名称后，后续可以通过变量名称来调用，而不设置变量名称，则是直接输出结果。

### userDetail 支持的参数有：

- 用户 ID `id`。  
  `id` 必须的，用于指定获取哪个用户 ID 的详情。

### name 参数可用的字段有：

- 用户 ID `Id`
- 上级用户 Id `ParentId`
- 用户名 `UserName`
- 真实姓名 `RealName`
- 用户介绍 `Introduce`
- 用户头像 `AvatarURL`
- 用户头像 `FullAvatarURL`
- 用户 Email `Email`
- 用户手机号 `Phone`
- 用户组 ID `GroupId`
- 是否是分销员 `IsRetailer`
- 账户余额 `Balance`
- 累计收益 `TotalReward`
- 邀请码 `InviteCode`
- 最近登录时间 `LastLogin` 时间戳，需要使用格式化时间戳为日期格式 `{% userDetail lastLogin with name="LastLogin" id="1" %}{{stampToDate(lastLogin, "2006-01-02")}}`
- VIP 过期时间 `ExpireTime` 时间戳，需要使用格式化时间戳为日期格式 `{% userDetail expireTime with name="ExpireTime" id="1" %}{{stampToDate(expireTime, "2006-01-02")}}`
- 用户链接 `Link`

### 用户 ID `Id`

标签用法：`{% userDetail with name="Id" %}`

```twig
{# 默认用法，自动获取当前当前页面用户ID #}
<div>UserID：{% userDetail with name="Id" %}</div>
{# 获取指定用户ID #}
<div>UserID：{% userDetail with name="Id" id="1" %}</div>
{# 自定义字段名称 #}
<div>UserID：{% userDetail getId with name="Id" %}{{getId}}</div>
<div>UserID：{% userDetail getId with name="Id" id="1" %}{{getId}}</div>
```

### 用户名 `UserName`

标签用法：`{% userDetail with name="UserName" %}`

```twig
{# 默认用法，自动获取当前当前页面用户ID #}
<div>用户名：{% userDetail with name="UserName" %}</div>
{# 获取指定Tagid的Tag字段 #}
<div>用户名：{% userDetail with name="TiUserNametle" id="1" %}</div>
{# 自定义字段名称 #}
<div>用户名：{% userDetail userName with name="UserName" %}{{userName}}</div>
<div>用户名：{% userDetail userName with name="UserName" id="1" %}{{userName}}</div>
```

### 用户链接 `Link`

标签用法：`{% userDetail with name="Link" %}`

```twig
{# 默认用法，自动获取当前当前页面用户ID #}
<div>用户链接：{% userDetail with name="Link" %}</div>
{# 获取指定Tagid的Tag字段 #}
<div>用户链接：{% userDetail with name="Link" id="1" %}</div>
{# 自定义字段名称 #}
<div>用户链接：{% userDetail userLink with name="Link" %}{{userLink}}</div>
<div>用户链接：{% userDetail userLink with name="Link" id="1" %}{{userLink}}</div>
```
