# 页面元数据接口文档

## 接口概述
该接口用于根据传入的页面路径（URI）获取对应页面的元数据信息，帮助Next.js动态路由确定应该请求哪个具体的后端接口。

## 接口地址
```
{域名地址}/api/metadata
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/metadata`

## 请求语法

```
GET {域名地址}/api/metadata
```

## 请求头

此接口还涉及公共请求头。更多信息，请参见[公共请求头（Common Request Headers）](api-header.md)。

## 请求参数

### Query Parameters
| 参数名 | 类型 | 必填 | 描述 | 示例 |
|--------|------|------|------|------|
| path | string | 是 | 需要获取元数据的页面路径 | `/collections/full-length-catsuit.html` |

## 响应格式
JSON

## 响应示例
```json
{
    "code": 0,
    "data": {
        "title": "Full-Length Catsuit",
        "keywords": "",
        "description": "",
        "image": "https://www.aicms.com/uploads/202601/05/155e089bfb3dda0b.jpg",
        "nav_bar": 13,
        "page_id": 56,
        "module_id": 2,
        "page_name": "archiveDetail",
        "canonical_url": "https://www.aicms.com/collections/full-length-catsuit.html",
        "total_pages": 0,
        "current_page": 0,
        "status_code": 200,
        "params": {
            "": "",
            "combine": "",
            "filename": "full-length-catsuit",
            "match": "archive",
            "module": "collections",
            "page": "",
            "pattern": "^([^\/]+?)\/([^\/]+?)(\/c\\-([^\/]+?))?(_([\\d]+))?\\.html$",
            "route": "collections/full-length-catsuit.html"
        }
    },
    "msg": ""
}
```

## 响应字段说明

### 顶层字段
| 字段名 | 类型 | 描述 |
|--------|------|------|
| code | integer | 响应状态码，0表示成功 |
| data | object | 页面元数据对象 |
| msg | string | 响应消息，成功时为空字符串 |

### data字段说明
| 字段名 | 类型 | 描述 |
|--------|------|------|
| title | string | 页面标题 |
| keywords | string | 页面关键词 |
| description | string | 页面描述 |
| image | string | 页面主图URL |
| nav_bar | integer | 导航栏ID |
| page_id | integer | 页面ID |
| module_id | integer | 模块ID |
| page_name | string | 页面名称（用于标识页面类型） |
| canonical_url | string | 规范URL |
| total_pages | integer | 总页数（用于分页） |
| current_page | integer | 当前页码 |
| status_code | integer | HTTP状态码 |
| params | object | 路径解析参数 |

### params字段说明
| 字段名 | 类型 | 描述 |
|--------|------|------|
| filename | string | 文件名（从路径中提取） |
| match | string | 匹配类型（如"archive"表示归档页面） |
| module | string | 模块名称（如"collections"表示产品集合） |
| pattern | string | 用于匹配路径的正则表达式 |
| route | string | 原始路由路径 |

## 页面类型说明
根据`page_name`字段的值，可以确定页面的类型，从而决定后续的数据请求：

| page_name | 页面类型 | 说明 |
|-----------|----------|------|
| archiveDetail | 详情页 | 产品分类或集合详情页 |
| archiveList | 列表页 | 产品分类或集合列表页 |
| archiveIndex | 模型封面页 | 产品分类或集合封面页 |
| pageDetail | 单页面 | 独立页面（如关于我们） |
| userDetail | 用户详情页 | 用户详情页 |
| tagIndex | 标签列表页 | 标签列表页 |
| tag | 标签详情 | 标签详情页 |
| comments | 评论列表 | 评论列表页 |
| guestbook | 留言页 | 留言页 |
| index | 首页 | 网站首页 |
| search | 搜索页 | 搜索 |

## 使用示例

### Next.js动态路由中使用
```javascript
// pages/[...slug].js
import { useRouter } from 'next/router'

export async function getServerSideProps(context) {
  const { slug } = context.params
  const path = '/' + slug.join('/')
  
  // 调用元数据接口
  const res = await fetch(`https://www.aicms.com/api/metadata?path=${path}`)
  const metadata = await res.json()
  
  // 根据page_name决定后续请求
  const pageName = metadata.data.page_name
  let apiEndpoint = ''
  
  switch(pageName) {
    case 'archiveDetail':
      apiEndpoint = `/api/collection/${metadata.data.params.filename}`
      break
    case 'pageDetail':
      apiEndpoint = `/api/page/${metadata.data.page_id}`
      break
    // ... 其他页面类型
  }
  
  // 调用对应的后端接口获取页面数据
  // const data = await fetch(apiEndpoint)
  
  return {
    props: {
      metadata: metadata.data,
      // pageData: data
    }
  }
}
```

## 错误处理
接口可能返回以下状态码：
- 0：请求成功

## 注意事项
1. path参数必须以斜杠(`/`)开头
2. 接口主要用于Next.js的服务端渲染（SSR）场景
3. 可以根据`page_name`字段的值判断页面类型，从而确定后续的数据请求接口
4. `params`字段中的`module`和`filename`可用于构建具体的API请求路径