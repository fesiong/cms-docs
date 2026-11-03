# 标量(Scalars)

### 关于标量

[Scalars](https://graphql.github.io/graphql-spec/June2018/#sec-Scalars) 是基本值类型：`Int`、`Float`、`String`、`Boolean` 或 `ID`。

在调用 GraphQL API 时，必须指定嵌套的子字段，直到只返回标量值为止。

### Boolean

<p><code>Boolean</code> 标量类型表示 <code>true</code> 或 <code>false</code>。</p>

---

### Float

<p><code>Float</code> 标量类型表示有符号双精度浮点数值，符合 <a href="http://en.wikipedia.org/wiki/IEEE_floating_point">IEEE 754</a> 标准。</p>

---

### ID

<p><code>ID</code> 标量类型表示唯一标识符，通常用于重新获取对象或作为缓存的键。在 JSON 响应中，ID 类型显示为字符串；但它并非设计为人类可读。当作为输入类型时，任何字符串（例如 "4"）或整数（例如 4）都可以被接受为 ID。</p>

---

### Int

<p><code>Int</code> 标量类型表示非小数的有符号整数值。Int 可以表示从 -(2^31) 到 2^31 - 1 之间的值。</p>

---

### JSON

<p><code>JSON</code> 标量类型表示任意的 JSON 数据结构。它可以包含对象、数组、字符串、数字、布尔值和 null 值的任意组合。该类型通常用于传递动态的或结构不固定的数据。</p>

---

### String

<p><code>String</code> 标量类型表示文本数据，以 UTF-8 字符序列形式呈现。String 类型最常被 GraphQL 用来表示自由格式的人类可读文本。</p>

---