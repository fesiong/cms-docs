# 用户分组详情标签

说明：用于获取用户分组详情数据

使用方法：`{% userGroupDetail 变量名称 with name="字段名称" id="1" %}` 变量名称不是必须的，设置了变量名称后，后续可以通过变量名称来调用，而不设置变量名称，则是直接输出结果。

### userGroupDetail 支持的参数有：

- 用户组 ID `id`。  
  `id` level 和 id 二选一，用于指定获取哪个用户组 ID 的详情。
- 用户组等级 `level`。  
  `level` level 和 id 二选一，用于指定获取哪个用户组等级的详情。

### name 参数可用的字段有：

- 用户组 ID `Id`
- 用户组名称 `Title`
- 用户组介绍 `Description`
- 用户组等级 `Level`
- 用户组购买价格 `Price`
- 优惠价 `FavorablePrice`
- 用户组设置 `Setting` 用户组设置为键值对。

### 用户组 ID `Id`

标签用法：`{% userGroupDetail with name="Id" %}`

```twig
{# 默认用法，自动获取当前当前页面用户组ID #}
<div>UserID：{% userGroupDetail with name="Id" %}</div>
{# 获取指定用户组ID #}
<div>UserID：{% userGroupDetail with name="Id" id="1" %}</div>
{# 自定义字段名称 #}
<div>UserID：{% userGroupDetail getId with name="Id" %}{{getId}}</div>
<div>UserID：{% userGroupDetail getId with name="Id" id="1" %}{{getId}}</div>
```

### 用户组名称 `Title`

标签用法：`{% userGroupDetail with name="Title" %}`

```twig
{# 默认用法，自动获取当前当前页面用户组ID #}
<div>用户组名称：{% userGroupDetail with name="Title" %}</div>
{# 获取指定Tagid的Tag字段 #}
<div>用户组名称：{% userGroupDetail with name="Title" id="1" %}</div>
{# 自定义字段名称 #}
<div>用户组名称：{% userGroupDetail groupName with name="Title" %}{{groupName}}</div>
<div>用户组名称：{% userGroupDetail groupName with name="Title" id="1" %}{{groupName}}</div>
```

### 用户组介绍 `Description`

标签用法：`{% userGroupDetail with name="Description" %}`

```twig
{# 默认用法，自动获取当前当前页面用户组ID #}
<div>用户组介绍：{% userGroupDetail with name="Description" %}</div>
{# 获取指定Tagid的Tag字段 #}
<div>用户组介绍：{% userGroupDetail with name="Description" id="1" %}</div>
{# 自定义字段名称 #}
<div>用户组介绍：{% userGroupDetail groupDescription with name="Description" %}{{groupDescription}}</div>
<div>用户组介绍：{% userGroupDetail groupDescription with name="Description" id="1" %}{{groupDescription}}</div>
```
