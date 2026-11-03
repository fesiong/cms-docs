# 文档参数标签

说明：用于获取指定文档的后台设置的参数

使用方法：`{% archiveParams 变量名称 with id="1" sorted=true %}` 如将变量定义为 params `{% archiveParams params with id="1" sorted=true %}...{% endarchiveParams %}`

### archiveParams 支持的参数有：

- 文档 ID `id`  
  `id` 参数根据文档 id 获取指定的文档参数，默认获取当前文档页面的文档 id。
- 是否排序 `sorted`  
  支持 的值有： `false|true`，`sorted=false` 时，获取的是一个无序的 map 对象，需要用`.`的形式获取数据。`sorted=true` 时，获取是一个固定排序的数组对象。默认是 `true` 固定排序的数组对象，因此需要使用 `for` 循环来获取并输出。
- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

具体的可用字段根据后台设置的文档附加字段来决定。

单个字段内的结构是：

- 字段名称 `Name`
- 字段数据 `Value`

### 代码示例

```twig
{# 固定排序的数组 #}
<div>
    {% archiveParams params %}
    {% for item in params %}
    <div>
        <span>{{item.Name}}：</span>
        <span>{{item.Value}}</span>
    </div>
    {% endfor %}
    {% endarchiveParams %}
</div>
指定文档ID
{# 固定排序的数组 #}
<div>
    {% archiveParams params with id="1" %}
    {% for item in params %}
    <div>
        <span>{{item.Name}}：</span>
        <span>{{item.Value}}</span>
    </div>
    {% endfor %}
    {% endarchiveParams %}
</div>
{# 无序的map对象 #}
<div>
    {% archiveParams params with sorted=false %}
        <div>{{params.yuedu.Name}}:{{params.yuedu.Value}}</div>
        <div>{{params.danxuan.Name}}:{{params.danxuan.Value}}</div>
        <div>{{params.duoxuan.Name}}:{{params.duoxuan.Value}}</div>
    {% endarchiveParams %}
</div>
```
