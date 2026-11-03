# 产品评价列表标签

说明：用于获取产品、订单的评价列表、评价分页列表

使用方法：`{% reviewList 变量名称 with archiveId="1" type="page|list" %}` 如将变量定义为 comments `{% reviewList reviews with archiveId="1" type="page" %}...{% endreviewList %}`

### reviewList 支持的参数有：

- 产品 ID `archiveId`  
  `archiveId` 为指定的文档 ID；
- 产品 ID `userId`  
  `userId` 为指定的用户 ID；
- 排序 `order`  
  `order` 可以指定显示的排序规则，支持依据 id 正序排序 `order="id desc"`、按 id 倒叙排序 `order="id desc"`；
- 显示数量 `limit`数量的列表，比如`limit="10"`则只会显示 10 条，`limit` 在不是分页列表的时候，支持`offset`模式，也就是 `,`分隔模式，如想从第 2 条开始，获取 10 条数据，可以设置成 `limit="2,10"`；
- 列表类型 `type`  
  `type` 支持按 page、list 方式列出。默认值为 list，如果`type="page"` 后续可用 分页标签 `pagination` 来组织分页显示 `{% pagination pages with show="5" %}`。
- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

comments 是一个数组对象，因此需要使用 `for` 循环来输出

### item 为 for 循环体内的变量，可用的字段有：

- ID `Id`
- 产品 ID `ArchiveId`
- 产品规格 ID `ArchiveSkuId`
- 产品名称 `ArchiveTitle`
- 产品规格名称 `SkuTitle`
- 订单 ID `OrderId`
- 用户名 `UserName`
- 用户 ID `UserId`
- 用户 IP `Ip`
- 评分 `Score`
- 评价内容 `Content`
- 评价图片列表 `Images`
- 用户名 `UserName`
- 用户头像 `AvatarURL`
- Email `Email`
- 审核状态 `Status` Status = 1 表示审核通过， status = 0 时审核中，不要显示出来
- 添加时间 `CreatedTime` 时间戳，需要使用格式化时间戳为日期格式 `{{stampToDate(item.CreatedTime, "2006-01-02")}}`

### 常规评价列表

```twig
{# list 列表展示 #}
<div>
{% reviewList reviews with archiveId=archive.Id type="list" limit="6" %}
    {% for item in reviews %}
    <div>
      <div>
        <span>
          {% if item.Status != 1 %}
          审核中：{{item.UserName|truncatechars:6}}
          {% else %}
          {{item.UserName}}
          {% endif %}
        </span>
        <span>{{stampToDate(item.CreatedTime, "2006-01-02")}}</span>
      </div>
      <div>
        <div>评分：{{item.Score}}</div>
        {% if item.Status != 1 %}
          该内容正在审核中：{{item.Content|truncatechars:9}}
        {% else %}
        {{item.Content}}
        {% endif %}
        <div>
          {% for item in item.Images %}
            <img src="{{item}}" alt="">
          {% endfor %}
        </div>
      </div>
    </div>
    {% endfor %}
{% endreviewList %}
</div>
```

### 分页展示评价列表

```twig
{# page 分页列表展示 #}
<div>
{% reviewList reviews with archiveId=archive.Id type="list" limit="6" %}
    {% for item in reviews %}
    <div>
      <div>
        <span>
          {% if item.Status != 1 %}
          审核中：{{item.UserName|truncatechars:6}}
          {% else %}
          {{item.UserName}}
          {% endif %}
        </span>
        <span>{{stampToDate(item.CreatedTime, "2006-01-02")}}</span>
      </div>
      <div>
        <div>评分：{{item.Score}}</div>
        {% if item.Status != 1 %}
          该内容正在审核中：{{item.Content|truncatechars:9}}
        {% else %}
        {{item.Content}}
        {% endif %}
        <div>
          {% for item in item.Images %}
            <img src="{{item}}" alt="">
          {% endfor %}
        </div>
      </div>
    </div>
    {% endfor %}
{% endreviewList %}
</div>

<div>
    {% pagination pages with show="5" %}
    <ul>
        <li>总数：{{pages.TotalItems}}条，总共：{{pages.TotalPages}}页，当前第{{pages.CurrentPage}}页</li>
        <li class="{% if pages.FirstPage.IsCurrent %}active{% endif %}"><a href="{{pages.FirstPage.Link}}">{{pages.FirstPage.Name}}</a></li>
        {% if pages.PrevPage %}
            <li><a href="{{pages.PrevPage.Link}}">{{pages.PrevPage.Name}}</a></li>
        {% endif %}
        {% for item in pages.Pages %}
            <li class="{% if item.IsCurrent %}active{% endif %}"><a href="{{item.Link}}">{{item.Name}}</a></li>
        {% endfor %}
        {% if pages.NextPage %}
            <li><a href="{{pages.NextPage.Link}}">{{pages.NextPage.Name}}</a></li>
        {% endif %}
        <li class="{% if pages.LastPage.IsCurrent %}active{% endif %}"><a href="{{pages.LastPage.Link}}">{{pages.LastPage.Name}}</a></li>
    </ul>
    {% endpagination %}
</div>
```

### 评价表单提交

评价使用 JSON 格式提交，提交后台接收的地址为：`/api/review/publish` 。 请查阅产品/订单评价API接口文档。