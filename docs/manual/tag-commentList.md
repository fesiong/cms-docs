# 评论列表标签

说明：用于获取文档的评论列表、评论分页列表

使用方法：`{% commentList 变量名称 with archiveId="1" type="page|list" %}` 如将变量定义为 comments `{% commentList comments with archiveId="1" type="page" %}...{% endcommentList %}`

### commentList 支持的参数有：

- 评论文档 ID `archiveId`  
  `archiveId` 为指定的文档 ID；
- 评论排序 `order`  
  `order` 可以指定显示的排序规则，支持依据 id 正序排序 `order="id desc"`、按 id 倒叙排序 `order="id desc"`；
- 显示数量 `limit`数量的列表，比如`limit="10"`则只会显示 10 条，`limit` 在不是分页列表的时候，支持`offset`模式，也就是 `,`分隔模式，如想从第 2 条开始，获取 10 条数据，可以设置成 `limit="2,10"`；
- 列表类型 `type`  
  `type` 支持按 page、list 方式列出。默认值为 list，如果`type="page"` 后续可用 分页标签 `pagination` 来组织分页显示 `{% pagination pages with show="5" %}`。
- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

comments 是一个数组对象，因此需要使用 `for` 循环来输出

### item 为 for 循环体内的变量，可用的字段有：

- 评论 ID `Id`
- 类型内容 ID `ArchiveId`
- 用户名 `UserName`
- 用户 ID `UserId`
- 用户 IP `Ip`
- 点赞数量 `VoteCount`
- 评论内容 `Content`
- 上级评论 ID `ParentId`
- 审核状态 `Status` Status = 1 表示审核通过， status = 0 时审核中，不要显示出来
- 上级评论的对象数据 `Parent` Parent 包含上级评论的完整 item，字段和评论 item 相同
- 添加时间 `CreatedTime` 时间戳，需要使用格式化时间戳为日期格式 `{{stampToDate(item.CreatedTime, "2006-01-02")}}`

### 常规评论列表

```twig
{# list 列表展示 #}
<div>
{% commentList comments with archiveId=archive.Id type="list" limit="6" %}
    {% for item in comments %}
    <div>
      <div>
        <span>
          {% if item.Status != 1 %}
          审核中：{{item.UserName|truncatechars:6}}
          {% else %}
          {{item.UserName}}
          {% endif %}
        </span>
        {% if item.Parent %}
        <span>回复</span>
        <span>
          {% if item.Status != 1 %}
          审核中：{{item.Parent.UserName|truncatechars:6}}
          {% else %}
          {{item.Parent.UserName}}
          {% endif %}
        </span>
        {% endif %}
        <span>{{stampToDate(item.CreatedTime, "2006-01-02")}}</span>
      </div>
      <div>
        {% if item.Parent %}
        <blockquote>
          {% if item.Parent.Status != 1 %}
          该内容正在审核中：{{item.Parent.Content|truncatechars:9}}
          {% else %}
          {{item.Parent.Content|truncatechars:100}}
          {% endif %}
        </blockquote>
        {% endif %}
        {% if item.Status != 1 %}
          该内容正在审核中：{{item.Content|truncatechars:9}}
        {% else %}
        {{item.Content}}
        {% endif %}
      </div>
      <div class="comment-control" data-id="{{item.Id}}" data-user="{{item.UserName}}">
        <a class="item" data-id="praise">赞(<span class="vote-count">{{item.VoteCount}}</span>)</a>
        <a class="item" data-id=reply>回复</a>
      </div>
    </div>
    {% endfor %}
{% endcommentList %}
</div>
```

### 分页展示评论列表

```twig
{# page 分页列表展示 #}
<div>
{% commentList comments with archiveId=archive.Id type="page" limit="10" %}
    {% for item in comments %}
    <div>
      <div>
        <span>
          {% if item.Status != 1 %}
          审核中：{{item.UserName|truncatechars:6}}
          {% else %}
          {{item.UserName}}
          {% endif %}
        </span>
        {% if item.Parent %}
        <span>回复</span>
        <span>
          {% if item.Status != 1 %}
          审核中：{{item.Parent.UserName|truncatechars:6}}
          {% else %}
          {{item.Parent.UserName}}
          {% endif %}
        </span>
        {% endif %}
        <span>{{stampToDate(item.CreatedTime, "2006-01-02")}}</span>
      </div>
      <div>
        {% if item.Parent %}
        <blockquote>
          {% if item.Parent.Status != 1 %}
          该内容正在审核中：{{item.Parent.Content|truncatechars:9}}
          {% else %}
          {{item.Parent.Content|truncatechars:100}}
          {% endif %}
        </blockquote>
        {% endif %}
        {% if item.Status != 1 %}
          该内容正在审核中：{{item.Content|truncatechars:9}}
        {% else %}
        {{item.Content}}
        {% endif %}
      </div>
      <div class="comment-control" data-id="{{item.Id}}" data-user="{{item.UserName}}">
        <a class="item" data-id="praise">赞(<span class="vote-count">{{item.VoteCount}}</span>)</a>
        <a class="item" data-id=reply>回复</a>
      </div>
    </div>
    {% endfor %}
{% endcommentList %}
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

### 评论表单提交

评论使用 form 表单提交，提交后台接收的地址为：`/comment/publish` 。需要提交的字段有

| 字段       | 是否必填 | 说明                                                                |
| :--------- | :------: | :------------------------------------------------------------------ |
| archive_id |    是    | 对应的文档 ID                                                       |
| user_name  |    是    | 评论的用户名                                                        |
| content    |    是    | 评论内容                                                            |
| parent_id  |    否    | 上级评论 ID，当回复，某条评论的时候，要带上才会产生关联             |
| return     |    否    | 提交后，指定后端返回的格式，可选的值有：`html`、`json`，默认为 html |

表单代码示例

```twig
<form method="post" action="/comment/publish">
  <input type="hidden" name="return" value="html">
  <input type="hidden" name="archive_id" value="{% archiveDetail with name="Id" %}">
  <div>
    <label>用户名</label>
    <div>
      <input type="text" name="user_name" required lay-verify="required" placeholder="请填写您的昵称" autocomplete="off">
    </div>
  </div>
  <div>
    <label>评论内容</label>
    <div>
      <textarea name="content" placeholder="" id="comment-content-field" rows="5"></textarea>
    </div>
  </div>
  <div>
    <div>
      <button type="submit">提交评论</button>
      <button type="reset">重置</button>
    </div>
  </div>
</form>
```

### 评论内容点赞

可以给某条评论的内容点赞，点赞使用 form 表单提交，点赞提交后台接收地址为：`/comment/praise` 。点赞需要提交的字段有：

| 字段 | 是否必填 | 说明        |
| :--- | :------: | :---------- |
| id   |    是    | 评论内容 ID |

评论点赞只支持返回 json 格式的数据，因此需要用 js post 来提交。

示例代码

```twig
<div class="comment-control">
  <a class="item vote-comment" data-id="praise" data-id="{{item.Id}}">赞(<span class="vote-count">{{item.VoteCount}}</span>)</a>
</div>
```

```js
$(".vote-comment").click(function (e) {
  let that = $(this);
  let commentId = $(this).data("id");

  //赞
  $.ajax({
    url: "/comment/praise",
    method: "post",
    data: { id: commentId },
    dataType: "json",
    success: function (res) {
      if (res.code === 0) {
        alert(res.msg);
        that.find(".vote-count").text(res.data.vote_count);
      } else {
        alert(res.msg);
      }
    },
    error: function (err) {
      alert(res.msg);
    },
  });
});
```
