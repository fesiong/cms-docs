# GraphQL API 参考

查看参考文档，了解 GraphQL API 架构中可用的数据类型。


- [查询](queries.md)
- [对象](objects.md)
- [标量](scalars.md)

## 使用指南

### 快速开始

GraphQL API 提供了统一的数据访问接口，支持查询（Queries）、变更（Mutations）和对象类型定义。本系统涵盖了内容管理、用户信息、产品数据、评论系统等多个方面的功能。

### 查询操作（Queries）

查询操作用于从服务器获取数据，支持丰富的参数选项和灵活的数据筛选。

#### 内容管理查询
- **archive** - 获取单个文档或产品详情，支持ID、URL别名、密码验证等方式定位内容
- **archives** - 获取文档列表，支持分页、筛选、排序、搜索等功能
- **archiveParams** - 获取文档自定义字段，便于处理扩展信息
- **page** / **pages** - 获取单页面详情或列表
- **category** / **categories** - 获取分类详情或列表
- **tag** / **tags** - 获取标签详情或列表

#### 系统配置查询
- **system** - 获取系统设置信息
- **contact** - 获取联系方式信息
- **currency** - 获取货币信息
- **index** - 获取首页TDK信息
- **languages** - 获取多语言站点信息

#### 用户与交互查询
- **user** - 获取用户信息
- **comments** - 获取评论列表
- **reviews** - 获取产品评价列表
- **metadata** - 获取页面元信息

#### 导航与展示查询
- **navs** - 获取导航列表
- **banners** - 获取首页轮播图
- **friendLinks** - 获取友情链接
- **filters** - 获取筛选字段

### 变更操作（Mutations）

变更操作用于修改服务器数据。

#### 评价管理
- **createReview** - 创建产品评价，支持评分、内容、图片等评价信息

### 对象类型（Objects）

对象类型定义了API返回的数据结构，包含以下主要类型：

#### 内容相关对象
- **Archive** - 文档详情，包含文章和产品信息
- **ArchiveList** - 文档列表
- **Category** - 分类信息
- **Tag** - 标签信息
- **Page** - 单页面信息

#### 用户相关对象
- **User** - 用户信息
- **UserGroup** - 用户组信息
- **UserGroupSetting** - 用户组设置

#### 产品相关对象
- **Sku** - 产品SKU信息
- **ArchiveSku** - 产品规格SKU信息
- **ArchiveOption** - 产品规格选项
- **WholesaleRule** - 批发规则

#### 交互相关对象
- **Comment** - 评论信息
- **CommentList** - 评论列表
- **Review** - 产品评价
- **ReviewList** - 产品评价列表

#### 系统相关对象
- **SystemSetting** - 系统设置
- **ContactSetting** - 联系方式
- **CurrencySetting** - 货币设置
- **IndexSetting** - 首页TDK设置

### 标量类型（Scalars）

基础数据类型：
- **String** - 文本数据
- **Int** - 整数值
- **Float** - 浮点数值
- **Boolean** - 布尔值
- **JSON** - JSON数据结构
- **ID** - 唯一标识符

### 常用查询示例

#### 获取文章详情
```graphql
query GetArticle {
  archive(id: 1, render: true) {
    id
    title
    content
    description
    category {
      name
    }
    tags {
      name
    }
    views
    created_time
  }
}
```

#### 获取文章列表
```graphql
query GetArticles {
  archives(limit: 10, page: 1, category_id: 1) {
    items {
      id
      title
      description
      thumb
      created_time
    }
    page
    total
  }
}
```

#### 获取分类及其文章
```graphql
query GetCategoryWithArticles {
  category(id: 1) {
    id
    title
    description
    archives(limit: 5) {
      items {
        id
        title
        description
      }
      total
    }
  }
}
```

#### 创建评价
```graphql
mutation CreateReview {
  createReview(
    content: "很好的产品！"
    score: 5
    user_name: "用户名"
    email: "user@example.com"
  ) {
    id
    content
    score
    user_name
    created_time
  }
}
```