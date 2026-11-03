# 统计页面访问数据接口

用于统计页面访问数据，包括文档访问量统计和其他访问记录，支持多种记录类型和访问路径统计。

## 注意事项

- 该接口采用GET方法
- 用于统计页面访问量和记录访问数据
- 支持文档访问量统计和其他类型的访问记录
- HTML模板默认会自动注入此接口调用
- 如果使用Next.js等前端框架，需要手动调用此接口
- 必须提供HTTP状态码和访问路径参数

## 请求地址

```
{域名地址}/api/log
```

说明：`{域名地址}` 需要替换成你的域名地址，如 `https://www.aicms.com/api/log`

## 请求语法

```
GET {域名地址}/api/log
```

## 请求参数

| 字段名 | 类型   | 必填 | 说明            |
| :----- | :----- | :--- | :-------------------- |
| action | string | 否   | 记录类型，支持的值：views: 文档访问,会统计文档访问量，other：其他值 |
| id     | int    | 否   | 文档ID |
| type   | string | 否   | 记录类型，支持的值：archive: action=views 时需要 |
| code   | int    | 是   | http状态码 |
| path   | string | 是   | 访问路径 |

## 返回参数

无

## 使用示例

### 文档访问统计请求示例

```
GET /api/log?action=views&id=1&type=archive&code=200&path=/article/1.html HTTP/1.1
Host: www.aicms.com
```

### 其他类型访问记录请求示例

```
GET /api/log?action=other&code=404&path=/nonexistent-page.html HTTP/1.1
Host: www.aicms.com
```

### 500错误页面统计请求示例

```
GET /api/log?action=other&code=500&path=/error-page HTTP/1.1
Host: www.aicms.com
```

### 前端JavaScript调用示例

```javascript
// 统计文档访问
function trackPageView(articleId, path) {
  const url = `/api/log?action=views&id=${articleId}&type=archive&code=200&path=${encodeURIComponent(path)}`;
  // 使用fetch发送请求，不等待响应
  fetch(url, { method: 'GET' })
    .catch(err => console.error('统计请求失败:', err));
}

// 统计其他页面访问
function trackOtherPage(path, statusCode = 200) {
  const url = `/api/log?action=other&code=${statusCode}&path=${encodeURIComponent(path)}`;
  // 使用图片方式发送请求，避免CORS问题
  new Image().src = url;
}

// 页面加载完成后统计访问
document.addEventListener('DOMContentLoaded', function() {
  const currentPath = window.location.pathname;
  const articleId = getArticleIdFromPath(currentPath); // 自定义函数获取文章ID
  
  if (articleId) {
    trackPageView(articleId, currentPath);
  } else {
    trackOtherPage(currentPath);
  }
});
```

### Next.js中使用示例

```javascript
import { useEffect } from 'react';
import { useRouter } from 'next/router';

export default function LogTracker() {
  const router = useRouter();
  
  useEffect(() => {
    const trackPageView = () => {
      const path = router.asPath;
      const articleId = extractArticleId(path); // 自定义函数提取文章ID
      
      let logUrl = `/api/log?code=200&path=${encodeURIComponent(path)}`;
      if (articleId) {
        logUrl += `&action=views&id=${articleId}&type=archive`;
      } else {
        logUrl += '&action=other';
      }
      
      // 发送统计请求
      fetch(logUrl).catch(err => console.error('统计请求失败:', err));
    };
    
    // 路由变化时统计
    trackPageView();
    router.events.on('routeChangeComplete', trackPageView);
    
    return () => {
      router.events.off('routeChangeComplete', trackPageView);
    };
  }, [router]);
}
```
