# 联系方式标签

说明：用于获取后台配置的联系方式信息

使用方法：`{% contact 变量名称 with name="字段名称" %}`，变量名称不是必须的，设置了变量名称后，后续可以通过变量名称来调用，而不设置变量名称，则是直接输出结果。

### contact 支持的参数有

- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

### name 参数可用的字段名称有：

- 联系人 `UserName`
- 联系电话 `Cellphone`
- 联系地址 `Address`
- 联系邮箱 `Email`
- 联系微信 `Wechat`
- 微信二维码 `Qrcode`
- QQ `QQ`
- WhatsApp `WhatsApp`
- Facebook `Facebook`
- Twitter `Twitter`
- Tiktok `Tiktok`
- Pinterest `Pinterest`
- Linkedin `Linkedin`
- Instagram `Instagram`
- Youtube `Youtube`
- 自定义参数 `后台自定义设置的参数名`

### 联系人 `UserName`

标签用法：`{% contact with name="UserName" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系人</span>
    <span>{% contact with name="UserName" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系人</span>
    <span>{% contact userName with name="UserName" %}{{userName}}</span>
</li>
```

### 联系电话 `Cellphone`

标签用法：`{% contact with name="Cellphone" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系电话</span>
    <span>{% contact with name="Cellphone" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系电话</span>
    <span>{% contact cellphone with name="Cellphone" %}{{cellphone}}</span>
</li>
```

### 联系地址 `Address`

标签用法：`{% contact with name="Address" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系地址</span>
    <span>{% contact with name="Address" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系地址</span>
    <span>{% contact address with name="Address" %}{{address}}</span>
</li>
```

### 联系邮箱 `Email`

标签用法：`{% contact with name="Email" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系邮箱</span>
    <span>{% contact with name="Email" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系邮箱</span>
    <span>{% contact contactEmail with name="Email" %}{{contactEmail}}</span>
</li>
```

### 联系微信 `Wechat`

标签用法：`{% contact with name="Wechat" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系微信</span>
    <span>{% contact with name="Wechat" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系微信</span>
    <span>{% contact contactWechat with name="Wechat" %}{{contactWechat}}</span>
</li>
```

### 微信二维码 `Qrcode`

标签用法：`{% contact with name="Qrcode" %}`

```twig
{# 默认用法 #}
<li>
    <span>微信二维码</span>
    <span>
        <img src="{% contact with name="Qrcode" %}" />
    </span>
</li>
{# 自定义名称调用 #}
<li>
    <span>微信二维码</span>
    <span>
        <img src="{% contact qrcode with name="Qrcode" %}{{qrcode|safe}}" />
    </span>
</li>
```

### 联系 QQ `QQ`

标签用法：`{% contact with name="QQ" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系QQ</span>
    <span>{% contact with name="QQ" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系QQ</span>
    <span>{% contact contactQQ with name="QQ" %}{{contactQQ}}</span>
</li>
```

### 联系 WhatsApp `WhatsApp`

标签用法：`{% contact with name="WhatsApp" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系WhatsApp</span>
    <span>{% contact with name="WhatsApp" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系WhatsApp</span>
    <span>{% contact contactWhatsApp with name="WhatsApp" %}{{contactWhatsApp}}</span>
</li>
```

### 联系 Facebook `Facebook`

标签用法：`{% contact with name="Facebook" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系Facebook</span>
    <span>{% contact with name="Facebook" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系Facebook</span>
    <span>{% contact contactFacebook with name="Facebook" %}{{contactFacebook}}</span>
</li>
```

### 联系 Twitter `Twitter`

标签用法：`{% contact with name="Twitter" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系Twitter</span>
    <span>{% contact with name="Twitter" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系Twitter</span>
    <span>{% contact contactTwitter with name="Twitter" %}{{contactTwitter}}</span>
</li>
```

### 联系 Tiktok `Tiktok`

标签用法：`{% contact with name="Tiktok" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系Tiktok</span>
    <span>{% contact with name="Tiktok" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系Tiktok</span>
    <span>{% contact contactTiktok with name="Tiktok" %}{{contactTiktok}}</span>
</li>
```

### 联系 Pinterest `Pinterest`

标签用法：`{% contact with name="Pinterest" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系Pinterest</span>
    <span>{% contact with name="Pinterest" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系Pinterest</span>
    <span>{% contact contactPinterest with name="Pinterest" %}{{contactPinterest}}</span>
</li>
```

### 联系 Linkedin `Linkedin`

标签用法：`{% contact with name="Linkedin" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系Linkedin</span>
    <span>{% contact with name="Linkedin" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系Linkedin</span>
    <span>{% contact contactLinkedin with name="Linkedin" %}{{contactLinkedin}}</span>
</li>
```

### 联系 Instagram `Instagram`

标签用法：`{% contact with name="Instagram" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系Instagram</span>
    <span>{% contact with name="Instagram" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系Instagram</span>
    <span>{% contact contactInstagram with name="Instagram" %}{{contactInstagram}}</span>
</li>
```

### 联系 Youtube `Youtube`

标签用法：`{% contact with name="Youtube" %}`

```twig
{# 默认用法 #}
<li>
    <span>联系Youtube</span>
    <span>{% contact with name="Youtube" %}</span>
</li>
{# 自定义名称调用 #}
<li>
    <span>联系Youtube</span>
    <span>{% contact contactYoutube with name="Youtube" %}{{contactYoutube}}</span>
</li>
```
