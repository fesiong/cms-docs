# 查询（Queries）

### 关于查询

查询（Queries）是GraphQL API的核心组成部分，用于从服务器获取数据。通过定义的查询字段，客户端可以精确地请求所需的数据，避免获取不必要的信息。本系统提供了丰富的查询接口，涵盖了内容管理、用户信息、产品数据、评论系统等多个方面，满足各种应用场景的数据获取需求。

查询接口支持多种参数，允许对数据进行筛选、排序、分页等操作，使数据获取更加灵活高效。每个查询都有明确的返回类型，确保客户端能够准确预期返回的数据结构。

### archive

#### 类型: [Archive](objects.md#archive)

获取文档或产品详情

该查询用于获取单个文档或产品的详细信息，支持通过多种方式定位目标文档，包括ID、URL别名等。可以用于获取文章、产品等具体内容，支持密码保护内容的验证访问，以及Markdown内容的HTML渲染功能。

#### 参数

| 名称 | 说明 |
|------|-------------|
| password ([String](scalars.md#string)) | 有密码保护的文档，需要传入password进行验证才能获取完整内容 |
| id ([Int](scalars.md#int)) | 文档ID |
| filename ([String](scalars.md#string)) | 文件名，等同于url_token |
| url_token ([String](scalars.md#string)) | 文档别名。特殊值：上一篇：prev，下一篇：next |
| render ([Boolean](scalars.md#boolean)) | 如果是Markdown编辑器，传render为true将内容渲染成HTML格式 |
| variant ([Int](scalars.md#int)) | SKU ID |

---

### archiveParams

#### 类型: [[CustomField]](objects.md#customfield)

获取文档自定义字段

该查询用于获取特定文档的自定义字段信息。在内容管理系统中，不同的文档可能需要包含特定的自定义属性或扩展字段，此接口允许客户端获取这些附加的字段数据，以便更好地展示或处理文档的扩展信息。

自定义字段通常用于存储文档的额外属性，如SEO设置、特殊配置项、业务相关的扩展数据等，使文档系统具有更好的灵活性和可扩展性。

#### 参数

| 名称 | 说明 |
|------|-------------|
| filename ([String](scalars.md#string)) | 文件名，等同于url_token |
| url_token ([String](scalars.md#string)) | 文档别名 |
| render ([Boolean](scalars.md#boolean)) | 是否渲染内容 |
| id ([Int](scalars.md#int)) | 文档ID |

---

### archives

#### 类型: [ArchiveList](objects.md#archivelist)

获取文档列表

该查询用于获取文档或产品的列表数据，支持多种筛选和排序方式。通过此接口，客户端可以获取文章、产品等文档的集合，适用于首页展示、分类页面、搜索结果页面等需要展示多个文档的场景。

此查询接口提供了丰富的参数选项，可以实现分页、筛选、排序、搜索等功能，满足各种业务场景下的文档列表展示需求。

#### 参数

| 名称 | 说明 |
|------|-------------|
| parent_id ([Int](scalars.md#int)) | 父级ID |
| exclude_category_id ([Int](scalars.md#int)) | 排除的分类ID |
| exclude_category_ids ([[Int]](scalars.md#int)) | 排除的分类ID列表 |
| module_id ([Int](scalars.md#int)) | 模型ID |
| user_id ([Int](scalars.md#int)) | 用户ID |
| show_flag ([Boolean](scalars.md#boolean)) | 是否显示标志 |
| draft ([Boolean](scalars.md#boolean)) | 是否显示草稿 |
| author_id ([Int](scalars.md#int)) | 作者ID |
| q ([String](scalars.md#string)) | 搜索关键词 |
| like ([String](scalars.md#string)) | 模糊搜索关键词 |
| keywords ([String](scalars.md#string)) | 关键词搜索 |
| type ([String](scalars.md#string)) | 类型筛选 |
| limit ([Int](scalars.md#int)) | 限制返回数量 |
| render ([Boolean](scalars.md#boolean)) | 是否渲染内容 |
| category_id ([Int](scalars.md#int)) | 分类ID |
| tag_id ([Int](scalars.md#int)) | 标签ID |
| tag_ids ([[Int]](scalars.md#int)) | 标签ID列表 |
| flag ([String](scalars.md#string)) | 标志筛选 |
| page ([Int](scalars.md#int)) | 页码 |
| category_ids ([[Int]](scalars.md#int)) | 分类ID列表 |
| show_content ([Boolean](scalars.md#boolean)) | 是否显示内容 |
| show_extra ([Boolean](scalars.md#boolean)) | 是否显示扩展字段 |
| child ([Boolean](scalars.md#boolean)) | 是否包含子分类 |
| order ([String](scalars.md#string)) | 排序方式 |
| tag ([String](scalars.md#string)) | 标签筛选 |
| offset ([Int](scalars.md#int)) | 偏移量 |
| id ([Int](scalars.md#int)) | 特定ID |

---

### banners

#### 类型: [[BannerItem]](objects.md#banneritem)

获取首页轮播图

#### 参数

| 名称 | 说明 |
|------|-------------|
| type ([String](scalars.md#string)) | 轮播图类型 |

---

### categories

#### 类型: [[Category]](objects.md#category)

获取分类列表

#### 参数

| 名称 | 说明 |
|------|-------------|
| parent_id ([Int](scalars.md#int)) | 父分类ID |
| module_id ([Int](scalars.md#int)) | 模型ID |
| all ([Boolean](scalars.md#boolean)) | 是否获取所有分类 |
| limit ([Int](scalars.md#int)) | 限制返回数量 |
| offset ([Int](scalars.md#int)) | 偏移量 |

---

### category

#### 类型: [Category](objects.md#category)

获取分类详情

#### 参数

| 名称 | 说明 |
|------|-------------|
| id ([Int](scalars.md#int)) | 分类ID |
| filename ([String](scalars.md#string)) | 文件名，等同于url_token |
| catname ([String](scalars.md#string)) | 分类名称 |
| url_token ([String](scalars.md#string)) | 分类别名 |
| render ([Boolean](scalars.md#boolean)) | 是否渲染内容 |

---

### comments

#### 类型: [CommentList](objects.md#commentlist)

获取评论列表

#### 参数

| 名称 | 说明 |
|------|-------------|
| order ([String](scalars.md#string)) | 排序方式 |
| page ([Int](scalars.md#int)) | 页码 |
| limit ([Int](scalars.md#int)) | 限制返回数量 |
| offset ([Int](scalars.md#int)) | 偏移量 |
| render ([Boolean](scalars.md#boolean)) | 是否渲染内容 |
| id ([Int](scalars.md#int)) | 评论ID |
| user_id ([Int](scalars.md#int)) | 用户ID |

---

### contact

#### 类型: [ContactSetting](objects.md#contactsetting)

获取联系方式信息

---

### currency

#### 类型: [CurrencySetting](objects.md#currencysetting)

获取货币信息

---

### diy

#### 类型: [[ExtraField]](objects.md#extrafield)

获取系统自定义字段

#### 参数

| 名称 | 说明 |
|------|-------------|
| render ([Boolean](scalars.md#boolean)) | 是否渲染内容 |

---

### filters

#### 类型: [[FilterGroup]](objects.md#filtergroup)

获取文档、产品筛选字段

#### 参数

| 名称 | 说明 |
|------|-------------|
| module_id ([Int](scalars.md#int)) | 模型ID |
| show_all ([Boolean](scalars.md#boolean)) | 是否显示全部筛选项 |
| all_text ([String](scalars.md#string)) | "全部"显示文本 |
| show_price ([Boolean](scalars.md#boolean)) | 是否显示价格筛选 |
| show_category ([Boolean](scalars.md#boolean)) | 是否显示分类筛选 |
| parent_id ([Int](scalars.md#int)) | 分类筛选中上级分类ID，默认为 `0` |
| category_id ([Int](scalars.md#int)) | 当前分类的ID，默认为 `0` |

---

### friendLinks

#### 类型: [[FriendLink]](objects.md#friendlink)

获取友情链接

---

### guestbookFields

#### 类型: [[CustomField]](objects.md#customfield)

获取留言字段配置

---

### index

#### 类型: [IndexSetting](objects.md#indexsetting)

获取首页TDK信息

---

### languages

#### 类型: [[MultiLangSite]](objects.md#multilangsite)

获取多语言站点信息

---

### metadata

#### 类型: [PageMeta](objects.md#pagemeta)

获取当前页面元信息

#### 参数

| 名称 | 说明 |
|------|-------------|
| path ([String](scalars.md#string)) | 页面路径 |
| params ([JSON](scalars.md#json)) | 页面参数 |

---

### module

#### 类型: [Module](objects.md#module)

获取模块详情

#### 参数

| 名称 | 说明 |
|------|-------------|
| filename ([String](scalars.md#string)) | 文件名，等同于url_token |
| url_token ([String](scalars.md#string)) | 模块别名 |
| id ([Int](scalars.md#int)) | 模块ID |

---

### modules

#### 类型: [[Module]](objects.md#module)

获取模块列表

---

### navs

#### 类型: [[Nav]](objects.md#nav)

获取导航列表

#### 参数

| 名称 | 说明 |
|------|-------------|
| type_id ([Int](scalars.md#int)) | 导航类型ID |
| show_type ([String](scalars.md#string)) | 显示类型 |

---

### page

#### 类型: [Page](objects.md#page)

获取单页面详情

#### 参数

| 名称 | 说明 |
|------|-------------|
| render ([Boolean](scalars.md#boolean)) | 是否渲染内容 |
| id ([Int](scalars.md#int)) | 页面ID |
| filename ([String](scalars.md#string)) | 文件名，等同于url_token |
| url_token ([String](scalars.md#string)) | 页面别名 |

---

### pages

#### 类型: [[Page]](objects.md#page)

获取单页面列表

#### 参数

| 名称 | 说明 |
|------|-------------|
| limit ([Int](scalars.md#int)) | 限制返回数量 |
| offset ([Int](scalars.md#int)) | 偏移量 |

---

### reviews

#### 类型: [ReviewList](objects.md#reviewlist)

获取产品评价列表

#### 参数

| 名称 | 说明 |
|------|-------------|
| user_id ([Int](scalars.md#int)) | 用户ID |
| order ([String](scalars.md#string)) | 排序方式 |
| page ([Int](scalars.md#int)) | 页码 |
| limit ([Int](scalars.md#int)) | 限制返回数量 |
| offset ([Int](scalars.md#int)) | 偏移量 |
| render ([Boolean](scalars.md#boolean)) | 是否渲染内容 |
| id ([Int](scalars.md#int)) | 评价ID |

---

### sku

#### 类型: [Sku](objects.md#sku)

获取产品SKU信息

#### 参数

| 名称 | 说明 |
|------|-------------|
| id ([Int](scalars.md#int)) | 产品ID |
| filename ([String](scalars.md#string)) | 文件名，等同于url_token |
| url_token ([String](scalars.md#string)) | 产品别名 |

---

### system

#### 类型: [SystemSetting](objects.md#systemsetting)

获取系统设置信息

---

### tag

#### 类型: [Tag](objects.md#tag)

获取文档、产品标签详情

#### 参数

| 名称 | 说明 |
|------|-------------|
| url_token ([String](scalars.md#string)) | 标签别名 |
| render ([Boolean](scalars.md#boolean)) | 是否渲染内容 |
| id ([Int](scalars.md#int)) | 标签ID |
| filename ([String](scalars.md#string)) | 文件名，等同于url_token |

---

### tags

#### 类型: [TagList](objects.md#taglist)

获取标签列表

#### 参数

| 名称 | 说明 |
|------|-------------|
| letter ([String](scalars.md#string)) | 首字母筛选 |
| page ([Int](scalars.md#int)) | 页码 |
| item_id ([Int](scalars.md#int)) | 项目ID |
| category_id ([Int](scalars.md#int)) | 分类ID |
| type ([String](scalars.md#string)) | 类型筛选 |
| order ([String](scalars.md#string)) | 排序方式 |
| limit ([Int](scalars.md#int)) | 限制返回数量 |
| offset ([Int](scalars.md#int)) | 偏移量 |
| category_ids ([[Int]](scalars.md#int)) | 分类ID列表 |

---

### user

#### 类型: [User](objects.md#user)

获取用户信息

#### 参数

| 名称 | 说明 |
|------|-------------|
| id ([Int](scalars.md#int)) | 用户ID |

## 使用示例


### 获取单个文档详情
```graphql
query GetArchive {
  archive(id: 1, render: true) {
    id
    title
    content
    category {
      name
    }
    tags {
      name
    }
  }
}
```

### 获取文档列表
```graphql
query GetArchives {
  archives(limit: 10, page: 1, category_id: 1) {
    list {
      id
      title
      summary
      created_at
    }
    pagination {
      total
      page
      limit
    }
  }
}
```

### 获取分类信息
```graphql
query GetCategory {
  category(id: 1) {
    id
    name
    description
    archives(limit: 5) {
      list {
        id
        title
      }
    }
  }
}
```

### 获取评论列表
```graphql
query GetComments {
  comments(page: 1, limit: 20, order: "created_at desc") {
    list {
      id
      content
      author
      created_at
    }
    pagination {
      total
      page
      limit
    }
  }
}
```

### 获取自定义字段
```graphql
query GetArchiveParams {
  archiveParams(id: 1) {
    name
    value
    type
  }
}
```

### 获取导航菜单
```graphql
query GetNavs {
  navs(type_id: 1) {
    id
    name
    url
    children {
      id
      name
      url
    }
  }
}
```

### 获取系统设置
```graphql
query GetSystemInfo {
  system {
    site_name
    site_url
    site_logo
    seo_title
    seo_keywords
    seo_description
  }
}
```