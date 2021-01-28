from tools.test_db_connect import db_conn

db = db_conn()
class TestcaseElement(object):
        # ----------------------------------------登录模块----------------------------------------- #
        xpathHomePageLoginMod = db.check_sql("首页模块的登录按钮")    # 首页模块的登录按钮
        xpathCodeLoginMod = db.check_sql("登录模块的验证码登录")    # 登录模块的验证码登录
        xpathIdPwsLoginMod = db.check_sql("登录模块的账号密码登录")    # 登录模块的账号密码登录
        xpathEnterPhonenum = db.check_sql("验证码登录模块的输入手机号码")    # 验证码登录模块的输入手机号码
        xpathEnterCode = db.check_sql("验证码登录模块的输入验证码")    # 验证码登录模块的输入验证码
        xpathCodeLoginBtn = db.check_sql("验证码登录模块的登陆按钮")    # 验证码登录模块的登陆按钮
        xpathIdEnterPhonenum = db.check_sql("账号密码登录模块的输入手机号码")    # 账号密码登录模块的输入手机号码
        xpathIdEnterPws = db.check_sql("账号密码登录模块的输入密码")    # 账号密码登录模块的输入密码
        xpathIdEnterImg = db.check_sql("账号密码登录模块的验证码图片")    # 账号密码登录模块的验证码图片
        xpathIdEnterCode = db.check_sql("账号密码登录模块的输入验证码")    # 账号密码登录模块的输入验证码
        xpathIdPwsLoginBtn = db.check_sql("账号密码登录模块的登录按钮")    # 账号密码登录模块的登录按钮
        xpathHomePageId = db.check_sql("首页右上角的账号名称")    # 首页右上角的账号名称
        xpathSafeExit = db.check_sql("安全退出按钮")    # 安全退出按钮
        xpathPopUpBtn = db.check_sql("登录模块登录弹窗的确定按钮")    # 登录模块登录弹窗的确定按钮
        xpathPopUpTest = db.check_sql("登录模块登录弹窗中的内容")    # 登录模块登录弹窗中的内容
        xpathPhoneNumFormat = db.check_sql("请输入正确的手机号格验证码登录")    # 请输入正确的手机号格式(验证码登录)
        xpathPhoneNumFormatID = db.check_sql("请输入正确的手机号格账号密码登录")    # 请输入正确的手机号格式(账号密码登录)
        xpathCodeFormat = db.check_sql("请输入正确的验证码格式")    # 请输入正确的验证码格式
        xpathPwdLimit = db.check_sql("密码不能小于6位且不能大于20位")    # 密码不能小于6位且不能大于20位

        # ----------------------------------------支付流程----------------------------------------- #
        xpathHomePageBtn = db.check_sql("登录之后的首页按钮")    # 登录之后的首页按钮
        xpathAllWares = db.check_sql("全部商品分类")    #全部商品分类
        xpathHomeOddsBtn = db.check_sql("首页的特惠产品按钮")    # 首页的特惠产品按钮
        # xpathTopSortList = db.check_sql("商品分类一级列表")    # 商品分类一级列表
        # xpathSecondSortList = db.check_sql("商品分类二级列表")  # 商品分类二级列表
        # xpathThirdSortList = db.check_sql("商品分类三级列表")  # 商品分类三级列表
        xpathTopSort = db.check_sql("商品分类一级")    # 商品分类一级
        xpathSecondSort = db.check_sql("商品分类二级")    # 商品分类二级
        xpathThirdSort = db.check_sql("商品分类三级")    # 商品分类三级
        xpathWaresMag = db.check_sql("产品翻页信息")    # 产品翻页信息
        xpathWaresBtn = db.check_sql("点击产品")    # 点击产品
        xpathWaresName = db.check_sql("产品名称")    # 产品名称
        xpathNomsBtn = db.check_sql("点击规格")    # 点击规格
        xpathShopCarBtn = db.check_sql("加入购物车按钮")    # 加入购物车按钮
        xpathBuyNowBtn = db.check_sql("立即购买按钮")    # 立即购买按钮
        xpathJoinCarImg = db.check_sql("加入购物车图标")    # 加入购物车图标
        xpathCheckWareMag = db.check_sql("查看商品详情按钮")    # 查看商品详情按钮
        xpathGoCarWareMag = db.check_sql("购物车中查看商品详情")    # 购物车中查看商品详情
        xpathGoShopCarPay = db.check_sql("去购物车结算按钮")    # 去购物车结算按钮
        xpathAllCheck = db.check_sql("全选框")    # 全选框
        xpathGoPay = db.check_sql("去结算按钮")    # 去结算按钮
        xpathConsigneeMag = db.check_sql("收货人信息默认文本")    # 收货人信息默认文本(暂无收货地址~)
        xpathAddConsignee = db.check_sql("新增收获人地址")    # 新增收获人地址
        xpathConsignee = db.check_sql("收货人")    # 收货人
        xpathPhoneNum = db.check_sql("手机号")    # 手机号
        xpathAddr_Province = db.check_sql("收货地址省")    # 收货地址(省)
        xpathAddr_City = db.check_sql("收货地址市")  # 收货地址(市)
        xpathAddr_Area = db.check_sql("收货地址区")  # 收货地址(区)
        xpathDetailAddr = db.check_sql("详细地址")    # 详细地址
        xpathDetailHelp = db.check_sql("详细地址提示信息")    # 详细地址提示信息(请填写详细地址)
        xpathCheckBox = db.check_sql("检查框")    # 检查框(设为默认地址)
        xpathWaresValue = db.check_sql("商品的总价格")    # 商品的总价格
        xpathFare = db.check_sql("运费")    # 运费
        xpathAllValue = db.check_sql("应付的总金额")    # 应付的总金额
        xpathPlaceOrder = db.check_sql("提交订单")    # 提交订单
        xpathTips = db.check_sql("弹窗的提示信息")    # 弹窗的提示信息(请选择收货地址)
        xpathCPMBtn = db.check_sql("弹窗的按钮")    # 弹窗的按钮
        xpathSaveBtn = db.check_sql("保存按钮")    # 保存按钮
        xpathChooseAddr = db.check_sql("选择一个地址")    # 选择一个地址
        xpathBalancePay = db.check_sql("选择支付方式(余额支付)")    # 选择支付方式(余额支付)
        xpathInputCode = db.check_sql("输入4位数短信验证码")    # 输入4位数短信验证码
        xpathSendCode = db.check_sql("发送验证码")    # 发送验证码
        xpathPayBtn = db.check_sql("立即支付按钮")    # 立即支付按钮
        xpathAddrDel = db.check_sql("删除收货人地址按钮")    # 删除收货人地址按钮
        xpathSetDefAddr = db.check_sql("设为默认地址按钮")    # 设为默认地址按钮
        xpathPopAccBtn = db.check_sql("弹窗的确定按钮")    # 弹窗的确定按钮
        xpathPopCanBtn = db.check_sql("弹窗的取消按钮")    # 弹窗的取消按钮
        xpathMoreAddrBtn = db.check_sql("更多地址按钮")    # 更多地址按钮
        xpathAddrList = db.check_sql("地址的列表")    # 地址的列表
        xpathConsigneeMagCheck = db.check_sql("收货人信息选中框")    # 收货人信息选中框

        # ----------------------------------------后台管理----------------------------------------- #
        xpathBackstageUser = db.check_sql("用户名")    # 用户名
        xpathBackstagePwd = db.check_sql("密码")    # 密码
        xpathBackstageCode = db.check_sql("验证码")    # 验证码
        xpathLoginBtn = db.check_sql("登陆按钮")    # 登陆按钮
        xpathSysBtn = db.check_sql("系统按钮")    # 系统按钮
        xpathSysDaily = db.check_sql("系统日志按钮")    # 系统日志按钮
        xpathNoteDaily = db.check_sql("短信日志按钮")    # 短信日志按钮
        xpathNoteMsg = db.check_sql("短信内容")    # 短信内容
        xpathUserBtn = db.check_sql("用户按钮")    # 用户按钮
        xpathExitBtn = db.check_sql("退出按钮")    # 退出按钮