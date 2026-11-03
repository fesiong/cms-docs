# 留言表单标签

说明：用于获取后台设置的留言表单

使用方法：`{% guestbook 变量名称 %}` 如将变量定义为 fields `{% guestbook fields %}...{% endguestbook %}`

### guestbook 支持的参数有

- 站点 ID `siteId`  
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

fields 是一个数组对象，因此需要使用 `for` 循环来输出

### item 为 for 循环体内的变量，可用的字段有:

- 表单名称 `Name`
- 表单变量 `FieldName`
- 表单类型 `Type`
  表单类型有 6 种可能的值：文本类型 `text`、数字类型 `number`、多行文本类型 `textarea`、单项选择类型 `radio`、多项选择类型 `checkbox`、下拉选择类型 `select`。
- 是否必填 `Required`
  Required 值为 true 时，表示必填，Required 值为 false 时，表示可以不填。
- 表单默认值 `Content`
- 分割成数组的默认值 `Items`
  当表单类型为 单项选择类型 `radio`、多项选择类型 `checkbox`、下拉选择类型 `select` 时，它们的每一个选择项构成了一个 Items 数组，可以通过 for 循环输出。

### 留言表单提交

留言表单提交需要使用 form 表单提交， 提交后台接收地址为：`/guestbook.html`，需要提交的字段有

| 字段           |   是否必填   | 说明                                                                |
| :------------- | :----------: | :------------------------------------------------------------------ |
| user_name      |      是      | 留言的用户名                                                        |
| contact        |      是      | 联系方式，如手机，电话，微信，QQ 等                                 |
| content        |      是      | 留言内容                                                            |
| 其他自定义字段 | 根据设置决定 | 后台添加表单额外字段设置的字段，根据设置是否为必填                  |
| return         |      否      | 提交后，指定后端返回的格式，可选的值有：`html`、`json`，默认为 html |

### 代码示例

通过下面的代码，可以循环输出所有的设置的字段。

```twig
<form method="post" action="/guestbook.html">
{% guestbook fields %}
    {% for item in fields %}
    <div>
        <label>{{item.Name}}</label>
        <div>
            {% if item.Type == "text" || item.Type == "number" %}
            <input type="{{item.Type}}" name="{{item.FieldName}}" {% if item.Required %}required lay-verify="required"{% endif %} placeholder="{{item.Content}}" autocomplete="off">
            {% elif item.Type == "textarea" %}
            <textarea name="{{item.FieldName}}" {% if item.Required %}required lay-verify="required"{% endif %} placeholder="{{item.Content}}" rows="5"></textarea>
            {% elif item.Type == "radio" %}
            {%- for val in item.Items %}
            <input type="{{item.Type}}" name="{{item.FieldName}}" value="{{val}}" title="{{val}}">
            {%- endfor %}
            {% elif item.Type == "checkbox" %}
            {%- for val in item.Items %}
            <input type="{{item.Type}}" name="{{item.FieldName}}[]" value="{{val}}" title="{{val}}">
            {%- endfor %}
            {% elif item.Type == "select" %}
            <select name="{{item.FieldName}}">
                {%- for val in item.Items %}
                <option value="{{val}}">{{val}}</option>
                {%- endfor %}
            </select>
            {% endif %}
        </div>
    </div>
    {% endfor %}
    <div>
        <div>
            <button type="submit">提交留言</button>
            <button type="reset">重置</button>
        </div>
    </div>
{% endguestbook %}
</form>
```

如果你想自定义表单显示，你也可以使用常规的 input 来组织显示，如：

```twig
<form method="post" action="/guestbook.html">
  <input type="hidden" name="return" value="html">
  <div>
    <label>用户名</label>
    <div>
      <input type="text" name="user_name" required lay-verify="required" placeholder="请填写您的昵称" autocomplete="off">
    </div>
  </div>
  <div>
    <label>联系方式</label>
    <div>
      <input type="text" name="contact" required lay-verify="required" placeholder="请填写您的手机号或微信" autocomplete="off">
    </div>
  </div>
  <div>
    <label>留言内容内容</label>
    <div>
      <textarea name="content" placeholder="" id="comment-content-field" rows="5"></textarea>
    </div>
  </div>
    <div>
        <div>
            <button type="submit">提交留言</button>
            <button type="reset">重置</button>
        </div>
    </div>
</form>
```
