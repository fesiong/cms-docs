# 对象（Objects）

### 关于对象

[对象](https://graphql.github.io/graphql-spec/June2018/#sec-Objects) 在 GraphQL 中代表您可以访问的资源。一个对象可以包含一系列字段，这些字段都有特定的类型。

GraphQL 对象类型定义了查询返回的数据结构，每个对象类型包含多个字段，每个字段都有其特定的数据类型。这些对象类型构成了 API 的数据模型，定义了客户端可以获取的数据结构和关系。

在本系统中，对象类型涵盖了内容管理、用户信息、产品数据、评论系统等多个方面的数据结构，为各种业务场景提供统一的数据访问接口。

### 对象类型分类

本系统中的对象类型主要包括：

- **内容相关对象**：如 [Archive](objects.md#archive)（文档详情）、[ArchiveList](objects.md#archivelist)（文档列表）、[Category](objects.md#category)（分类信息）等
- **用户相关对象**：如 [User](objects.md#user)（用户信息）、[UserGroup](objects.md#usergroup)（用户组）等
- **产品相关对象**：如 [Sku](objects.md#sku)（产品SKU信息）、[ArchiveSku](objects.md#archivesku)（产品规格SKU信息）等
- **系统设置对象**：如 [SystemSetting](objects.md#systemsetting)（系统设置）、[ContactSetting](objects.md#contactsetting)（联系方式）等
- **交互相关对象**：如 [Comment](objects.md#comment)（评论）、[Review](objects.md#review)（产品评价）等

每个对象类型都详细列出了其包含的字段和字段说明，便于客户端准确获取所需数据。

### Archive

文档详情，包括文章和产品

#### 字段

| 名称 | 说明 |
|------|-------------|
| **allow_oversold** ([Boolean](scalars.md#boolean)) | 是否支持超卖 |
| **amount** ([Int](scalars.md#int)) | 金额 |
| **brand** ([String](scalars.md#string)) | 品牌 |
| **canonical_url** ([String](scalars.md#string)) | 规范URL |
| **cart_id** ([Int](scalars.md#int)) | 购物车ID |
| **category** ([Category](objects.md#category)) | 分类信息 |
| **category_id** ([Int](scalars.md#int)) | 分类ID |
| **category_ids** ([Int](scalars.md#int)) | 分类ID列表 |
| **category_titles** ([String](scalars.md#string)) | 分类标题列表 |
| **comment_count** ([Int](scalars.md#int)) | 评论数量 |
| **content** ([String](scalars.md#string)) | 内容 |
| **cost_price** ([Int](scalars.md#int)) | 成本价 |
| **created_time** ([Int](scalars.md#int)) | 创建时间戳 |
| **description** ([String](scalars.md#string)) | 描述 |
| **extra** ([JSON](scalars.md#json)) | 扩展字段 |
| **favorable_price** ([Int](scalars.md#int)) | 优惠价格 |
| **favorite_count** ([Int](scalars.md#int)) | 收藏数量 |
| **fixed_link** ([String](scalars.md#string)) | 固定链接 |
| **flag** ([String](scalars.md#string)) | 标志 |
| **has_order_fields** ([Boolean](scalars.md#boolean)) | 是否有订单字段 |
| **has_ordered** ([Boolean](scalars.md#boolean)) | 是否已下单 |
| **has_password** ([Boolean](scalars.md#boolean)) | 是否有密码 |
| **has_pseudo** ([Int](scalars.md#int)) | 是否有虚拟销量 |
| **id** ([Int](scalars.md#int)) | 文档ID |
| **images** ([String](scalars.md#string)) | 图片列表 |
| **is_favorite** ([Boolean](scalars.md#boolean)) | 是否已收藏 |
| **is_free_shipping** ([Boolean](scalars.md#boolean)) | 是否包邮 |
| **is_wholesale** ([Boolean](scalars.md#boolean)) | 是否支持批发 |
| **keyword_id** ([Int](scalars.md#int)) | 关键词ID |
| **keywords** ([String](scalars.md#string)) | 关键词 |
| **link** ([String](scalars.md#string)) | 链接 |
| **logo** ([String](scalars.md#string)) | Logo |
| **module_id** ([Int](scalars.md#int)) | 模型ID |
| **module_name** ([String](scalars.md#string)) | 模型名称 |
| **need_logistics** ([Boolean](scalars.md#boolean)) | 是否需要物流 |
| **option_type** ([Int](scalars.md#int)) | 选项类型 |
| **options** ([ArchiveOption](objects.md#archiveoption)) | 规格选项列表 |
| **order_fields** ([CustomField](objects.md#customfield)) | 订单字段列表 |
| **order_extra** ([JSON](scalars.md#json)) | 订单扩展信息 |
| **origin_amount** ([Int](scalars.md#int)) | 原始金额 |
| **origin_id** ([Int](scalars.md#int)) | 原始ID |
| **origin_price** ([Int](scalars.md#int)) | 原始价格 |
| **origin_title** ([String](scalars.md#string)) | 原始标题 |
| **origin_url** ([String](scalars.md#string)) | 原始URL |
| **parent_id** ([Int](scalars.md#int)) | 上级ID |
| **password** ([String](scalars.md#string)) | 密码 |
| **password_valid** ([Boolean](scalars.md#boolean)) | 密码是否有效 |
| **price** ([Int](scalars.md#int)) | 价格 |
| **quantity** ([Int](scalars.md#int)) | 数量 |
| **read_level** ([Int](scalars.md#int)) | 阅读等级 |
| **review_count** ([Int](scalars.md#int)) | 评价数量 |
| **seo_title** ([String](scalars.md#string)) | SEO标题 |
| **sold_count** ([Int](scalars.md#int)) | 销售数量 |
| **sort** ([Int](scalars.md#int)) | 排序 |
| **stock** ([Int](scalars.md#int)) | 库存 |
| **skus** ([ArchiveSku](objects.md#archivesku)) | SKU列表 |
| **sku** ([Sku](objects.md#archivesku)) | 当前选中SKU信息 |
| **tags** ([Tag](objects.md#tag)) | 标签列表 |
| **template** ([String](scalars.md#string)) | 模板 |
| **thumb** ([String](scalars.md#string)) | 缩略图 |
| **title** ([String](scalars.md#string)) | 标题 |
| **type** ([String](scalars.md#string)) | 类型 |
| **updated_time** ([Int](scalars.md#int)) | 更新时间戳 |
| **url_token** ([String](scalars.md#string)) | URL标识符 |
| **user_id** ([Int](scalars.md#int)) | 用户ID |
| **video_url** ([String](scalars.md#string)) | 视频URL |
| **views** ([Int](scalars.md#int)) | 浏览量 |
| **weight** ([Float](scalars.md#float)) | 重量 |
| **weight_unit** ([String](scalars.md#string)) | 重量单位 |
| **wholesale_rule** ([WholesaleRule](objects.md#wholesalerule)) | 批发规则 |
| **wholesale_rules** ([WholesaleRule](objects.md#wholesalerule)) | 批发规则列表 |

---

### ArchiveList

文档、产品列表，产品的传 module_id=2

#### 字段

| 名称 | 说明 |
|------|-------------|
| **items** ([Archive](objects.md#archive)) | 文档/产品列表 |
| **page** ([Int](scalars.md#int)) | 页码 |
| **total** ([Int](scalars.md#int)) | 总数 |

---

### ArchiveOption

产品规格名称

#### 字段

| 名称 | 说明 |
|------|-------------|
| **archive_id** ([Int](scalars.md#int)) | 产品ID |
| **created_time** ([Int](scalars.md#int)) | 创建时间戳 |
| **id** ([Int](scalars.md#int)) | ID |
| **is_main** ([Int](scalars.md#int)) | 是否主选项 |
| **sort** ([Int](scalars.md#int)) | 排序 |
| **title** ([String](scalars.md#string)) | 标题 |
| **updated_time** ([Int](scalars.md#int)) | 更新时间戳 |
| **values** ([ArchiveOptionValue](objects.md#archiveoptionvalue)) | 规格值列表 |

---

### ArchiveOptionValue

产品规格选项

#### 字段

| 名称 | 说明 |
|------|-------------|
| **archive_id** ([Int](scalars.md#int)) | 产品ID |
| **color** ([String](scalars.md#string)) | 颜色 |
| **created_time** ([Int](scalars.md#int)) | 创建时间戳 |
| **id** ([Int](scalars.md#int)) | ID |
| **option_id** ([Int](scalars.md#int)) | 选项ID |
| **images** ([String](scalars.md#string)) | 图片列表 |
| **logo** ([String](scalars.md#string)) | Logo |
| **thumb** ([String](scalars.md#string)) | 缩略图 |
| **price** ([Int](scalars.md#int)) | 价格 |
| **sort** ([Int](scalars.md#int)) | 排序 |
| **title** ([String](scalars.md#string)) | 标题 |
| **updated_time** ([Int](scalars.md#int)) | 更新时间戳 |

---

### ArchiveSku

产品规格SKU信息

#### 字段

| 名称 | 说明 |
|------|-------------|
| **archive_id** ([Int](scalars.md#int)) | 产品ID |
| **barcode** ([String](scalars.md#string)) | 条形码 |
| **cost_price** ([Int](scalars.md#int)) | 成本价 |
| **created_time** ([Int](scalars.md#int)) | 创建时间戳 |
| **hs_code** ([String](scalars.md#string)) | 海关编码 |
| **id** ([Int](scalars.md#int)) | ID |
| **link** ([String](scalars.md#string)) | SKU的链接 |
| **images** ([String](scalars.md#string)) | 图片列表 |
| **logo** ([String](scalars.md#string)) | Logo |
| **origin_price** ([Int](scalars.md#int)) | 原价 |
| **price** ([Int](scalars.md#int)) | 价格 |
| **sku** ([String](scalars.md#string)) | SKU |
| **sold_count** ([Int](scalars.md#int)) | 销售数量 |
| **stock** ([Int](scalars.md#int)) | 库存 |
| **symbol** ([String](scalars.md#string)) | SKU符号 |
| **thumb** ([String](scalars.md#string)) | 缩略图 |
| **title** ([String](scalars.md#string)) | 标题 |
| **updated_time** ([Int](scalars.md#int)) | 更新时间戳 |
| **weight** ([Float](scalars.md#float)) | 重量 |
| **weight_unit** ([String](scalars.md#string)) | 重量单位 || **values** ([ArchiveOptionValue](objects.md#archiveoptionvalue)) | 规格值列表 |

---

### BannerItem

首页Banner

#### 字段

| 名称 | 说明 |
|------|-------------|
| **alt** ([String](scalars.md#string)) | 替代文本 |
| **description** ([String](scalars.md#string)) | 描述 |
| **id** ([Int](scalars.md#int)) | ID |
| **link** ([String](scalars.md#string)) | 链接 |
| **logo** ([String](scalars.md#string)) | Logo |
| **type** ([String](scalars.md#string)) | 类型 |

---

### Category

文档、产品分类

#### 字段

| 名称 | 说明 |
|------|-------------|
| **archive_count** ([Int](scalars.md#int)) | 文档/产品数量 |
| **content** ([String](scalars.md#string)) | 内容 |
| **description** ([String](scalars.md#string)) | 描述 |
| **detail_template** ([String](scalars.md#string)) | 详情模板 |
| **extra** ([JSON](scalars.md#json)) | 扩展字段 |
| **has_children** ([Boolean](scalars.md#boolean)) | 是否有子分类 |
| **id** ([Int](scalars.md#int)) | ID |
| **images** ([String](scalars.md#string)) | 图片列表 |
| **is_current** ([Boolean](scalars.md#boolean)) | 是否当前分类 |
| **is_inherit** ([Int](scalars.md#int)) | 是否继承 |
| **keywords** ([String](scalars.md#string)) | 关键词 |
| **link** ([String](scalars.md#string)) | 链接 |
| **logo** ([String](scalars.md#string)) | Logo |
| **module_id** ([Int](scalars.md#int)) | 模型ID |
| **parent_id** ([Int](scalars.md#int)) | 上级ID |
| **seo_title** ([String](scalars.md#string)) | SEO标题 |
| **sort** ([Int](scalars.md#int)) | 排序 |
| **spacer** ([String](scalars.md#string)) | 间隔符 |
| **status** ([Int](scalars.md#int)) | 状态 |
| **template** ([String](scalars.md#string)) | 模板 |
| **thumb** ([String](scalars.md#string)) | 缩略图 |
| **title** ([String](scalars.md#string)) | 标题 |
| **type** ([Int](scalars.md#int)) | 类型 |
| **url_token** ([String](scalars.md#string)) | URL标识符 |

---

### Comment

评论

#### 字段

| 名称 | 说明 |
|------|-------------|
| **active** ([Boolean](scalars.md#boolean)) | 是否活跃 |
| **archive_id** ([Int](scalars.md#int)) | 文档ID |
| **content** ([String](scalars.md#string)) | 评论内容 |
| **created_time** ([Int](scalars.md#int)) | 创建时间戳 |
| **id** ([Int](scalars.md#int)) | ID |
| **ip** ([String](scalars.md#string)) | IP地址 |
| **item_title** ([String](scalars.md#string)) | 文档标题 |
| **parent** ([Comment](objects.md#comment)) | 父评论 |
| **parent_id** ([Int](scalars.md#int)) | 父ID |
| **status** ([Int](scalars.md#int)) | 状态 |
| **to_uid** ([Int](scalars.md#int)) | 目标用户ID |
| **user_id** ([Int](scalars.md#int)) | 用户ID |
| **user_name** ([String](scalars.md#string)) | 用户名 |
| **vote_count** ([Int](scalars.md#int)) | 投票数量 |

---

### CommentList

评论列表

#### 字段

| 名称 | 说明 |
|------|-------------|
| **items** ([Comment](objects.md#comment)) | 评论列表 |
| **page** ([Int](scalars.md#int)) | 页码 |
| **total** ([Int](scalars.md#int)) | 总数 |

---

### ContactSetting

联系方式

#### 字段

| 名称 | 说明 |
|------|-------------|
| **address** ([String](scalars.md#string)) | 地址 |
| **cellphone** ([String](scalars.md#string)) | 手机号 |
| **email** ([String](scalars.md#string)) | 邮箱 |
| **extra_fields** ([ExtraField](objects.md#extrafield)) | 扩展字段列表 |
| **facebook** ([String](scalars.md#string)) | Facebook |
| **instagram** ([String](scalars.md#string)) | Instagram |
| **linkedin** ([String](scalars.md#string)) | LinkedIn |
| **pinterest** ([String](scalars.md#string)) | Pinterest |
| **qq** ([String](scalars.md#string)) | QQ |
| **qrcode** ([String](scalars.md#string)) | 二维码 |
| **tiktok** ([String](scalars.md#string)) | TikTok |
| **twitter** ([String](scalars.md#string)) | Twitter |
| **user_name** ([String](scalars.md#string)) | 用户名 |
| **wechat** ([String](scalars.md#string)) | 微信 |
| **whats_app** ([String](scalars.md#string)) | WhatsApp |
| **youtube** ([String](scalars.md#string)) | YouTube |

---

### CurrencySetting

货币设置

#### 字段

| 名称 | 说明 |
|------|-------------|
| **currency** ([String](scalars.md#string)) | 货币码 |
| **name** ([String](scalars.md#string)) | 货币名称 |
| **symbol** ([String](scalars.md#string)) | 货币符号 |

---

### CustomField

自定义字段

#### 字段

| 名称 | 说明 |
|------|-------------|
| **content** ([String](scalars.md#string)) | 内容 |
| **field_name** ([String](scalars.md#string)) | 字段名 |
| **follow_level** ([Boolean](scalars.md#boolean)) | 跟随用户组等级 |
| **is_filter** ([Boolean](scalars.md#boolean)) | 是否筛选 |
| **is_system** ([Boolean](scalars.md#boolean)) | 是否系统字段 |
| **items** ([String](scalars.md#string)) | 项目列表 |
| **name** ([String](scalars.md#string)) | 名称 |
| **required** ([Boolean](scalars.md#boolean)) | 是否必填 |
| **type** ([String](scalars.md#string)) | 类型 |

---

### ExtraField

文档扩展字段

#### 字段

| 名称 | 说明 |
|------|-------------|
| **content** ([String](scalars.md#string)) | 内容 |
| **name** ([String](scalars.md#string)) | 名称 |
| **remark** ([String](scalars.md#string)) | 备注 |
| **type** ([String](scalars.md#string)) | 类型 |
| **value** ([JSON](scalars.md#json)) | 值 |

---

### FilterGroup

文档、产品筛选组

#### 字段

| 名称 | 说明 |
|------|-------------|
| **field_name** ([String](scalars.md#string)) | 字段名 |
| **items** ([FilterItem](objects.md#filteritem)) | 筛选项列表 |
| **name** ([String](scalars.md#string)) | 名称 |
| **range** ([Range](objects.md#range)) | 范围 |

---

### FilterItem

文档、产品筛选项

#### 字段

| 名称 | 说明 |
|------|-------------|
| **is_current** ([Boolean](scalars.md#boolean)) | 是否当前项 |
| **label** ([String](scalars.md#string)) | 标签 |
| **link** ([String](scalars.md#string)) | 链接 |
| **total** ([Int](scalars.md#int)) | 总数 |

---

### FriendLink

友情链接

#### 字段

| 名称 | 说明 |
|------|-------------|
| **back_link** ([String](scalars.md#string)) | 反链 |
| **checked_time** ([Int](scalars.md#int)) | 检查时间戳 |
| **contact** ([String](scalars.md#string)) | 联系方式 |
| **id** ([Int](scalars.md#int)) | ID |
| **link** ([String](scalars.md#string)) | 链接 |
| **my_link** ([String](scalars.md#string)) | 我的链接 |
| **my_title** ([String](scalars.md#string)) | 我的标题 |
| **nofollow** ([Int](scalars.md#int)) | 是否nofollow |
| **remark** ([String](scalars.md#string)) | 备注 |
| **sort** ([Int](scalars.md#int)) | 排序 |
| **status** ([Int](scalars.md#int)) | 状态 |
| **title** ([String](scalars.md#string)) | 标题 |

---

### IndexSetting

首页TDK

#### 字段

| 名称 | 说明 |
|------|-------------|
| **seo_description** ([String](scalars.md#string)) | SEO描述 |
| **seo_keywords** ([String](scalars.md#string)) | SEO关键词 |
| **seo_title** ([String](scalars.md#string)) | SEO标题 |

---

### Module

模型信息

#### 字段

| 名称 | 说明 |
|------|-------------|
| **description** ([String](scalars.md#string)) | 描述 |
| **id** ([Int](scalars.md#int)) | ID |
| **is_system** ([Int](scalars.md#int)) | 是否系统模型 |
| **keywords** ([String](scalars.md#string)) | 关键词 |
| **link** ([String](scalars.md#string)) | 链接 |
| **name** ([String](scalars.md#string)) | 名称 |
| **status** ([Int](scalars.md#int)) | 状态 |
| **table_name** ([String](scalars.md#string)) | 表名 |
| **title** ([String](scalars.md#string)) | 标题 |
| **title_name** ([String](scalars.md#string)) | 标题名称 |
| **url_token** ([String](scalars.md#string)) | URL标识符 |

---

### MultiLangSite

多语言站点信息

#### 字段

| 名称 | 说明 |
|------|-------------|
| **base_url** ([String](scalars.md#string)) | 基础URL |
| **id** ([Int](scalars.md#int)) | ID |
| **is_current** ([Boolean](scalars.md#boolean)) | 是否当前站点 |
| **language** ([String](scalars.md#string)) | 语言 |
| **language_emoji** ([String](scalars.md#string)) | 语言表情符号 |
| **language_icon** ([String](scalars.md#string)) | 语言图标 |
| **language_name** ([String](scalars.md#string)) | 语言名称 |
| **link** ([String](scalars.md#string)) | 链接 |
| **name** ([String](scalars.md#string)) | 名称 |
| **parent_id** ([Int](scalars.md#int)) | 父ID |
| **status** ([Boolean](scalars.md#boolean)) | 状态 |
| **sync_time** ([Int](scalars.md#int)) | 同步时间戳 |

---

### Nav

导航信息

#### 字段

| 名称 | 说明 |
|------|-------------|
| **description** ([String](scalars.md#string)) | 描述 |
| **id** ([Int](scalars.md#int)) | ID |
| **is_current** ([Boolean](scalars.md#boolean)) | 是否当前导航 |
| **level** ([Int](scalars.md#int)) | 级别 |
| **link** ([String](scalars.md#string)) | 链接 |
| **logo** ([String](scalars.md#string)) | Logo |
| **nav_list** ([Nav](objects.md#nav)) | 导航列表 |
| **nav_type** ([Int](scalars.md#int)) | 导航类型 |
| **page_id** ([Int](scalars.md#int)) | 页面ID |
| **parent_id** ([Int](scalars.md#int)) | 父ID |
| **sort** ([Int](scalars.md#int)) | 排序 |
| **spacer** ([String](scalars.md#string)) | 间隔符 |
| **status** ([Int](scalars.md#int)) | 状态 |
| **style** ([String](scalars.md#string)) | 样式 |
| **sub_title** ([String](scalars.md#string)) | 副标题 |
| **thumb** ([String](scalars.md#string)) | 缩略图 |
| **title** ([String](scalars.md#string)) | 标题 |
| **type_id** ([Int](scalars.md#int)) | 类型ID |

---

### Page

单页信息

#### 字段

| 名称 | 说明 |
|------|-------------|
| **content** ([String](scalars.md#string)) | 内容 |
| **description** ([String](scalars.md#string)) | 描述 |
| **id** ([Int](scalars.md#int)) | ID |
| **images** ([String](scalars.md#string)) | 图片列表 |
| **is_current** ([Boolean](scalars.md#boolean)) | 是否当前页面 |
| **keywords** ([String](scalars.md#string)) | 关键词 |
| **link** ([String](scalars.md#string)) | 链接 |
| **logo** ([String](scalars.md#string)) | Logo |
| **seo_title** ([String](scalars.md#string)) | SEO标题 |
| **status** ([Int](scalars.md#int)) | 状态 |
| **thumb** ([String](scalars.md#string)) | 缩略图 |
| **title** ([String](scalars.md#string)) | 标题 |
| **url_token** ([String](scalars.md#string)) | URL标识符 |

---

### PageMeta

获取当前页面TDK信息

#### 字段

| 名称 | 说明 |
|------|-------------|
| **canonical_url** ([String](scalars.md#string)) | 规范URL |
| **current_page** ([Int](scalars.md#int)) | 当前页码 |
| **description** ([String](scalars.md#string)) | 描述 |
| **image** ([String](scalars.md#string)) | 图片 |
| **keywords** ([String](scalars.md#string)) | 关键词 |
| **module_id** ([Int](scalars.md#int)) | 模型ID |
| **nav_bar** ([Int](scalars.md#int)) | 导航栏 |
| **page_id** ([Int](scalars.md#int)) | 页面ID |
| **page_name** ([String](scalars.md#string)) | 页面名称 |
| **params** ([JSON](scalars.md#json)) | 参数 |
| **status_code** ([Int](scalars.md#int)) | 状态码 |
| **title** ([String](scalars.md#string)) | 标题 |
| **total_pages** ([Int](scalars.md#int)) | 总页数 |

---

### Range

筛选选项范围，price filter 用到

#### 字段

| 名称 | 说明 |
|------|-------------|
| **max** ([Int](scalars.md#int)) | 最大值 |
| **min** ([Int](scalars.md#int)) | 最小值 |
| **link** ([String](scalars.md#string)) | 链接 |

---

### Review

产品评价

#### 字段

| 名称 | 说明 |
|------|-------------|
| **archive_id** ([Int](scalars.md#int)) | 产品ID |
| **archive_sku_id** ([Int](scalars.md#int)) | 产品SKU ID |
| **archive_title** ([String](scalars.md#string)) | 产品标题 |
| **avatar_url** ([String](scalars.md#string)) | 头像URL |
| **content** ([String](scalars.md#string)) | 内容 |
| **created_time** ([Int](scalars.md#int)) | 创建时间戳 |
| **email** ([String](scalars.md#string)) | 邮箱 |
| **id** ([Int](scalars.md#int)) | ID |
| **images** ([String](scalars.md#string)) | 图片列表 |
| **ip** ([String](scalars.md#string)) | IP地址 |
| **order_id** ([String](scalars.md#string)) | 订单ID |
| **score** ([Int](scalars.md#int)) | 评分 |
| **sku_title** ([String](scalars.md#string)) | SKU标题 |
| **status** ([Int](scalars.md#int)) | 状态 |
| **user_id** ([Int](scalars.md#int)) | 用户ID |
| **user_name** ([String](scalars.md#string)) | 用户名 |

---

### ReviewList

产品评价列表

#### 字段

| 名称 | 说明 |
|------|-------------|
| **items** ([Review](objects.md#review)) | 评价列表 |
| **page** ([Int](scalars.md#int)) | 页码 |
| **total** ([Int](scalars.md#int)) | 总数 |

---

### Sku

获取产品SKU信息

#### 字段

| 名称 | 说明 |
|------|-------------|
| **currency** ([String](scalars.md#string)) | 货币 |
| **currency_symbol** ([String](scalars.md#string)) | 货币符号 |
| **has_sku** ([Boolean](scalars.md#boolean)) | 是否有SKU |
| **id** ([Int](scalars.md#int)) | ID |
| **max_price** ([Int](scalars.md#int)) | 最高价格 |
| **min_price** ([Int](scalars.md#int)) | 最低价格 |
| **options** ([ArchiveOption](objects.md#archiveoption)) | 选项列表 |
| **order_count** ([Int](scalars.md#int)) | 订单数量 |
| **price** ([Int](scalars.md#int)) | 价格 |
| **quota_used** ([Int](scalars.md#int)) | 已用配额 |
| **skus** ([ArchiveSku](objects.md#archivesku)) | SKU列表 |
| **stock** ([Int](scalars.md#int)) | 库存 |
| **thumb** ([String](scalars.md#string)) | 缩略图 |
| **title** ([String](scalars.md#string)) | 标题 |
| **user_limit** ([Int](scalars.md#int)) | 用户限购数量 |
| **wholesale_rules** ([WholesaleRule](objects.md#wholesalerule)) | 批发规则列表 |

---

### SystemSetting

系统设置

#### 字段

| 名称 | 说明 |
|------|-------------|
| **admin_url** ([String](scalars.md#string)) | 管理员URL |
| **ban_spider** ([Int](scalars.md#int)) | 禁止爬虫 |
| **base_url** ([String](scalars.md#string)) | 基础URL |
| **currency** ([String](scalars.md#string)) | 货币 |
| **default_site** ([Boolean](scalars.md#boolean)) | 默认站点 |
| **extra_fields** ([ExtraField](objects.md#extrafield)) | 扩展字段列表 |
| **favicon** ([String](scalars.md#string)) | 网站图标 |
| **language** ([String](scalars.md#string)) | 语言 |
| **mobile_url** ([String](scalars.md#string)) | 移动端URL |
| **site_close** ([Int](scalars.md#int)) | 站点关闭 |
| **site_close_tips** ([String](scalars.md#string)) | 站点关闭提示 |
| **site_copyright** ([String](scalars.md#string)) | 站点版权 |
| **site_icp** ([String](scalars.md#string)) | 站点ICP备案号 |
| **site_logo** ([String](scalars.md#string)) | 站点Logo |
| **site_name** ([String](scalars.md#string)) | 站点名称 |
| **template_name** ([String](scalars.md#string)) | 模板名称 |
| **template_type** ([Int](scalars.md#int)) | 模板类型 |
| **template_url** ([String](scalars.md#string)) | 模板URL |

---

### Tag

文档标签

#### 字段

| 名称 | 说明 |
|------|-------------|
| **category_id** ([Int](scalars.md#int)) | 分类ID |
| **category_title** ([String](scalars.md#string)) | 分类标题 |
| **content** ([String](scalars.md#string)) | 内容 |
| **description** ([String](scalars.md#string)) | 描述 |
| **extra** ([JSON](scalars.md#json)) | 扩展字段 |
| **first_letter** ([String](scalars.md#string)) | 首字母 |
| **id** ([Int](scalars.md#int)) | ID |
| **keywords** ([String](scalars.md#string)) | 关键词 |
| **link** ([String](scalars.md#string)) | 链接 |
| **logo** ([String](scalars.md#string)) | Logo |
| **seo_title** ([String](scalars.md#string)) | SEO标题 |
| **status** ([Int](scalars.md#int)) | 状态 |
| **template** ([String](scalars.md#string)) | 模板 |
| **thumb** ([String](scalars.md#string)) | 缩略图 |
| **title** ([String](scalars.md#string)) | 标题 |
| **url_token** ([String](scalars.md#string)) | URL标识符 |

---

### TagList

文档标签列表

#### 字段

| 名称 | 说明 |
|------|-------------|
| **items** ([Tag](objects.md#tag)) | 标签列表 |
| **page** ([Int](scalars.md#int)) | 页码 |
| **total** ([Int](scalars.md#int)) | 总数 |

---

### User

用户信息

#### 字段

| 名称 | 说明 |
|------|-------------|
| **avatar_url** ([String](scalars.md#string)) | 头像URL |
| **balance** ([Int](scalars.md#int)) | 余额 |
| **email** ([String](scalars.md#string)) | 邮箱 |
| **email_verified** ([Boolean](scalars.md#boolean)) | 邮箱是否已验证 |
| **expire_time** ([Int](scalars.md#int)) | 过期时间戳 |
| **extra** ([JSON](scalars.md#json)) | 扩展字段 |
| **full_avatar_url** ([String](scalars.md#string)) | 完整头像URL |
| **group** ([UserGroup](objects.md#usergroup)) | 用户组 |
| **group_id** ([Int](scalars.md#int)) | 用户组ID |
| **id** ([Int](scalars.md#int)) | ID |
| **introduce** ([String](scalars.md#string)) | 介绍 |
| **invite_code** ([String](scalars.md#string)) | 邀请码 |
| **is_retailer** ([Int](scalars.md#int)) | 是否分销员 |
| **last_login** ([Int](scalars.md#int)) | 最后登录时间戳 |
| **link** ([String](scalars.md#string)) | 链接 |
| **parent_id** ([Int](scalars.md#int)) | 上级ID |
| **phone** ([String](scalars.md#string)) | 电话 |
| **real_name** ([String](scalars.md#string)) | 真实姓名 |
| **status** ([Int](scalars.md#int)) | 状态 |
| **token** ([String](scalars.md#string)) | 登录令牌 |
| **total_reward** ([Int](scalars.md#int)) | 总奖励收益 |
| **url_token** ([String](scalars.md#string)) | URL标识符 |
| **user_name** ([String](scalars.md#string)) | 用户名 |

---

### UserGroup

用户组

#### 字段

| 名称 | 说明 |
|------|-------------|
| **description** ([String](scalars.md#string)) | 描述 |
| **favorable_price** ([Int](scalars.md#int)) | 优惠价格 |
| **id** ([Int](scalars.md#int)) | ID |
| **level** ([Int](scalars.md#int)) | 等级 |
| **price** ([Int](scalars.md#int)) | 价格 |
| **setting** ([UserGroupSetting](objects.md#usergroupsetting)) | 设置 |
| **status** ([Int](scalars.md#int)) | 状态 |
| **title** ([String](scalars.md#string)) | 用户组名称 |

---

### UserGroupSetting

用户组设置

#### 字段

| 名称 | 说明 |
|------|-------------|
| **content_no_captcha** ([Boolean](scalars.md#boolean)) | 发布内容无需验证码 |
| **content_no_verify** ([Boolean](scalars.md#boolean)) | 发布内容无需验证 |
| **discount** ([Int](scalars.md#int)) | 折扣 |
| **expire_day** ([Int](scalars.md#int)) | 过期天数 |
| **parent_reward** ([Int](scalars.md#int)) | 父级奖励(二级分销员奖励) |
| **share_reward** ([Int](scalars.md#int)) | 分享奖励(三级分销员奖励) |

---

### WholesaleRule

批发规则

#### 字段

| 名称 | 说明 |
|------|-------------|
| **archive_id** ([Int](scalars.md#int)) | 产品ID |
| **created_time** ([Int](scalars.md#int)) | 创建时间戳 |
| **discount_rate** ([Int](scalars.md#int)) | 折扣率 |
| **id** ([Int](scalars.md#int)) | ID |
| **max_quantity** ([Int](scalars.md#int)) | 最大数量 |
| **min_quantity** ([Int](scalars.md#int)) | 最小数量 |
| **sku_id** ([Int](scalars.md#int)) | SKU ID |
| **updated_time** ([Int](scalars.md#int)) | 更新时间戳 |

---