# 变更操作（Mutations）

### 关于变更操作

### createReview（创建评价）

#### 输入字段

- order_id ([Int](scalars.md#int)) - 订单ID
- user_name ([String](scalars.md#string)) - 用户名
- email ([String](scalars.md#string)) - 邮箱
- content ([String!](scalars.md#string)) - 评价内容（必填）
- score ([Int!](scalars.md#int)) - 评分（必填）
- images ([[String]](scalars.md#string)) - 图片列表
- id ([Int](scalars.md#int)) - ID

#### 返回值

| 名称 | 说明 |
|------|-------------|
| archive_id ([Int](scalars.md#int)) | 商品ID |
| archive_sku_id ([Int](scalars.md#int)) | 商品SKU ID |
| archive_title ([String](scalars.md#string)) | 商品标题 |
| avatar_url ([String](scalars.md#string)) | 头像URL |
| content ([String](scalars.md#string)) | 评价内容 |
| created_time ([Int](scalars.md#int)) | 创建时间戳 |
| email ([String](scalars.md#string)) | 邮箱 |
| id ([Int](scalars.md#int)) | 评价ID |
| images ([[String]](scalars.md#string)) | 图片列表 |
| ip ([String](scalars.md#string)) | IP地址 |
| order_id ([String](scalars.md#string)) | 订单ID |
| score ([Int](scalars.md#int)) | 评分 |
| sku_title ([String](scalars.md#string)) | SKU标题 |
| status ([Int](scalars.md#int)) | 状态 |
| user_id ([Int](scalars.md#int)) | 用户ID |
| user_name ([String](scalars.md#string)) | 用户名 |