# 获取产品SKU标签

获取指定产品的SKU（库存量单位）信息，包括产品的规格属性、价格、库存、批发规则等详细信息。此接口适用于需要展示产品详细规格和购买选项的场景。

使用方法：`{% archiveSku 变量名 with id=1 %}` 如将变量定义为 tags `{% archiveSku productSku with id=1 %}...{% endarchiveSku %}`

### tagList 支持的参数有：

- 文档 ID `id`
  `id` 如果没有指定，默认读取当前产品的 ID，也可以手工指定，读取指定的产品的SKU信息
- 站点 ID `siteId`
  `siteId` 一般不需要填写，如果你使用后台的多站点管理创建了多个站点，并且想调用其他站点的数据，则可以通过指定 `siteId` 来实现调用指定站点的数据。

productSku 是一个对象，包含的字段有：

| 字段名        | 类型     | 说明      |
| :------------ | :------- | :------- |
| Id       | int    | 产品 ID     |
| Title | string | 产品标题     |
| Currency | string | 货币名称     |
| CurencySymbol | string | 货币符号     |
| Price | float | 产品价格     |
| MinPrice | float | 产品最低价格 |
| MaxPrice | float | 产品最高价格 |
| UserLimit | int | 用户限购数量 |
| QuotaUsed | int | 用户已购数量 |
| OrderCount | int | 销量 |
| Stock | int | 库存数量 |
| Pptions | object[] | 产品规格属性名称     |
| Skus | object[] | 产品SKU信息     |
| WholesaleRules | object[] | 产品批发规则     |


##### option 产品规格属性名称

| 字段名       | 类型     | 说明                         |
| :----------- | :------- | :--------------------------- |
| Id           | int      | 属性ID                      |
| Title        | string   | 属性名称                     |
| Values    | object[]   | 属性 value 列表                |

##### 属性 value

| 字段名  | 类型   | 说明         |
| :------ | :----- | :----------- |
| Id      | int    | 分类 ID      |
| OptionId | int  | 属性 ID      | 
| OptionTitle | string   | 属性名称       |
| Title | string | 属性 value 名称 |
| Logo | string | logo |
| Color | string | 颜色值 |
| Price | float | 价格     |

##### sku 产品SKU信息

| 字段名  | 类型   | 说明         |
| :------ | :----- | :----------- |
| Id      | int    | 分类 ID      |
| Title | string | sku 名称 |
| Symbol | string | 规格属性值id链接符号 |
| Values | object[] | 属性 value 列表 |
| Sku | string | sku 链接符号 |
| Barcode | string | 条形码 |
| HsCode | string | 海关编码 |
| Logo | string | logo |
| Thumb | string | 缩略图 |
| Stock | int | 库存数量 |
| Price | int | 价格     |
| OriginPrice | int | 原价     |
| Weight | int | 重量     |
| WeightUnit | string | 重量单位 |
| SoldCount | int | 销量 |

##### WholesaleRules 产品批发规则

| 字段名  | 类型   | 说明         |
| :------ | :----- | :----------- |
| Id | int | 规则 ID |
| ArchiveId | int | 文档 ID |
| MinQuantity | int | 最小数量 |
| MaxQuantity | int | 最大数量 |
| SkuId | int | sku ID |
| DiscountRate | int | 折扣率， 0-100 |
| CreatedTime | int | 创建时间 |
| UpdatedTime | int | 更新时间 |

## 示例代码

```twig
<div>
{% archiveSku productSku %}
  <div>价格：{{productSku.MinPrice/100}} ~ {{productSku.MaxPrice/100}}</div>
  ...
{% endarchiveSku %}
</div>
```