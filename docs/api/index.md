# AICMS接口文档

[API 接口使用指南](api-guide.md)

## 导入

- [导入文档接口](importArchive.md)
- [检查文档是否存在接口](importArchiveCheck.md)
- [获取文档分类接口](importCategories.md)
- [添加友情链接接口](importLink.md)
- [删除友情链接接口](importLinkDel.md)
- [检查友情链接是否可用接口](importLinkCheck.md)
- [导入图片资源接口](importAttachment.md)
- [手动Sitemap更新接口](importMakeSitemap.md)


## 文档接口
- [获取文档列表接口](archiveList.md)
- [获取文档详情接口](archiveDetail.md)
- [获取上一个文档接口](archivePrev.md)
- [获取下一个文档接口](archiveNext.md)
- [获取文档参数筛选条件接口](archiveFilters.md)
- [获取文档参数接口](archiveParams.md)
- [验证文档密码接口](archivePasswordCheck.md)
- [获取收藏列表接口](favorites.md)
- [添加收藏接口](favoriteAdd.md)
- [删除收藏接口](favoriteRemove.md)
- [检查是否收藏接口](favoriteCheck.md)
- [发布文档接口](archivePublish.md)
- [获取产品SKU接口](archiveSku.md)

## 文档标签接口
- [获取标签列表接口](tagList.md)
- [获取标签详情接口](tagDetail.md)
- [获取标签文档列表接口](tagDataList.md)

## 城市分站接口
- [获取城市分站详情接口](placeDetail.md)
- [获取城市分站列表接口](placeList.md)

## 分类页面接口
- [获取分类列表接口](categoryList.md)
- [获取分类详情接口](categoryDetail.md)
- [获取单页详情接口](pageDetail.md)
- [获取单页列表接口](pageList.md)
- [获取模型列表接口](moduleList.md)
- [获取模型详情接口](moduleDetail.md)

## 用户接口
- [用户登录接口](login.md)
- [用户注册接口](register.md)
- [用户信息接口](userDetail.md)
- [更新用户信息接口](userDetailUpdate.md)
- [更新用户头像接口](userAvatarUpdate.md)
- [获取用户组列表接口](userGroups.md)
- [获取用户组详情接口](userGroupDetail.md)
- [用户退出接口](logout.md)
- [发送Email验证接口](emailVerifySend.md)
- [验证Email地址接口](emailVerify.md)
- [更新用户密码接口](userPasswordUpdate.md)
- [重置用户密码接口](userPasswordReset.md)
- [获取谷歌登录跳转地址接口](googleUrl.md)

## 订单接口
- [获取订单列表接口](orders.md)
- [获取订单统计数据接口](ordersStatistic.md)
- [获取订单统计图表接口](ordersChart.md)
- [获取商品Checkout信息接口](ordersCheckout.md)
- [创建订单接口](orderCreate.md)
- [获取订单详情接口](orderDetail.md)
- [取消订单接口](orderCancel.md)
- [订单申请退款接口](orderRefund.md)
- [订单确认收货接口](orderFinished.md)
- [订单创建支付接口](orderPayment.md)
- [订单检查支付结果接口](paymentCheck.md)
- [检查指定文档是否支付了接口](archiveOrderCheck.md)
- [获取产品/订单评价列表接口](orderReviews.md)
- [发表产品/订单评价接口](orderReviewPublish.md)

## 订单地址与地区接口
- [获取订单地址列表接口](orderAddresses.md)
- [获取订单地址详情接口](orderAddress.md)
- [保存订单地址接口](orderAddressSave.md)
- [地址自动补全接口](placeAutocomplete.md)
- [获取国家列表接口](placeCountries.md)
- [获取城市列表接口](placeCountryCities.md)
- [获取国家省份/州列表接口](placeCountryStates.md)

## 沟通订单接口
- [获取沟通定制订单字段接口](orderCommunicationFields.md)
- [获取沟通定制订单列表](orderCommunicationList.md)
- [创建沟通定制订单接口](orderCommunicationCreate.md)
- [获取沟通定制订单详情接口](orderCommunicationDetail.md)
- [更新沟通定制订单接口](orderCommunicationUpdate.md)
- [沟通定制订单接受报价接口](orderCommunicationAcceptQuote.md)
- [获取沟通定制订单沟通信息列表接口](orderCommunicationMessages.md)
- [发送沟通定制订单信息接口](orderCommunicationMessageSend.md)

## 购物车接口
- [获取购物车列表接口](cartList.md)
- [添加购物车接口](cartAdd.md)
- [移除购物车商品接口](cartRemove.md)
- [更新购物车接口](cartUpdate.md)

## 优惠券接口
- [获取可用优惠券列表接口](couponValidList.md)
- [获取我的优惠券列表接口](couponCodeList.md)
- [领取优惠券接口](couponCodeGet.md)

## 愿望清单接口
- [获取愿望清单列表接口](wishlist.md)
- [添加愿望清单接口](wishlistAdd.md)
- [移除愿望清单接口](wishlistRemove.md)

## 活动与营销接口
- [获取活动详情接口](activityDetail.md)
- [获取活动列表接口](activityList.md)
- [获取商品活动信息接口](archiveActivity.md)

## 订单扩展接口
- [获取订单自定义表单接口](orderCustomForm.md)
- [保存订单自定义表单接口](orderCustomFormSave.md)
- [获取订单服务列表接口](orderServices.md)
- [获取配送信息接口](shippingInfo.md)

## 分销接口
- [获取分销员详情接口](retailerInfo.md)
- [获取分销员统计信息接口](retailerStatistics.md)
- [更新分销员真实姓名接口](retailerUpdate.md)
- [获取分销订单列表接口](retailerOrders.md)
- [获取提现列表接口](retailerWithdraws.md)
- [申请提现接口](retailerWithdraw.md)
- [获取分销团队列表接口](retailerMembers.md)
- [获取分销员收益列表接口](retailerCommissions.md)

## 留言与评论接口
- [获取评论列表接口](commentList.md)
- [发布评论接口](commentPublish.md)
- [评论点赞接口](commentPraise.md)
- [获取留言表单字段接口](guestbookFields.md)
- [添加留言接口](guestbook.md)

## 微信相关接口
- [生成微信小程序码接口](weappQrcode.md)
- [微信授权接口](wechatAuth.md)
- [微信消息接收接口](wechat.md)

## 其他接口
- [获取友情链接列表接口](friendlinkList.md)
- [获取系统设置接口](settingSystem.md)
- [获取联系方式接口](settingContact.md)
- [获取自定义字段接口](settingDiy.md)
- [获取首页TDK接口](settingIndex.md)
- [获取导航列表接口](navList.md)
- [上传图片资源接口](attachmentUpload.md)
- [获取多语言列表接口](languages.md)
- [调用图形验证码接口](captcha.md)
- [首页幻灯片列表接口](bannerList.md)
- [邮件订阅接口](subscription.md)
- [统计页面访问数据](logStatistic.md)
- [公共 HTTP 头定义](api-header.md)
- [页面元数据接口](metadata.md)

## GraphQL接口
- [GraphQL 概览](graphql/README.md)
- [查询 Queries](graphql/queries.md)
- [变更 Mutations](graphql/mutations.md)
- [对象 Objects](graphql/objects.md)
- [标量 Scalars](graphql/scalars.md)