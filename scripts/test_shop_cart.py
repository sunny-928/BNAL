import time


from base.base_driver import init_driver
from page.page import Page


class TestShopCart(object):
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_add_shop_cart(self):
        # 如果没有登录 去登陆
        self.page.home.login_if_not(self.page)
        # 首页 点击分类
        self.page.home.click_category()
        # 分类 点击商品列表
        self.page.category.click_goods_list()
        # 商品列表 点击商品详情
        self.page.goods_list.click_goods()
        # 商品详情 获取商品标题
        goods_title = self.page.goods_detail.get_goods_title_text()
        # 商品详情 点击加入购物车
        self.page.goods_detail.click_add_shop_cart()
        # 商品详情 点击规格
        self.page.goods_detail.click_spec()
        # 商品详情 点击购物车
        self.page.goods_detail.click_shop_cart()
        time.sleep(2)
        # 断言 是否成功添加购物车
        assert self.page.goods_detail.is_goods_title_exist(goods_title)

    def test_shop_cart_price(self):
        # 如果没有登录 去登陆
        self.page.home.login_if_not(self.page)
        # 首页 点击购物车
        self.page.home.click_cart()
        # 购物车 点击全选
        self.page.shop_cart.click_select_all()
        # 购物车 获取总价
        all_price = self.page.shop_cart.get_all_price()
        # 购物车 点击编辑
        self.page.shop_cart.click_edit()
        # 购物车 点击加号
        self.page.shop_cart.click_add()
        # 购物车 点击完成
        self.page.shop_cart.click_commit()
        # 购物车 获取单价
        price = self.page.shop_cart.get_price()
        # 断言 新的总价=总价+单价
        assert self.page.shop_cart.get_all_price() == all_price + price

    def test_del_shop_cart(self):
        # 如果没有登录 去登陆
        self.page.home.login_if_not(self.page)
        # 首页 点击购物车
        self.page.home.click_cart()
        # 购物车 - 判断是否有商品，如果没有则添加
        if self.page.shop_cart.is_shop_cart_empty():
            # 首页 点击分类
            self.page.home.click_category()
            # 分类 点击商品列表
            self.page.category.click_goods_list()
            # 商品列表 点击商品详情
            self.page.goods_list.click_goods()
            # 商品详情 获取商品标题
            goods_title = self.page.goods_detail.get_goods_title_text()
            # 商品详情 点击加入购物车
            self.page.goods_detail.click_add_shop_cart()
            # 商品详情 点击规格
            self.page.goods_detail.click_spec()
            self.page.goods_detail.press_back()
            self.page.goods_detail.press_back()
            # 商品详情 点击购物车
            self.page.home.click_cart()
        # 购物车 点击全选
        self.page.shop_cart.click_select_all()
        # 购物车 点击编辑
        self.page.shop_cart.click_edit()
        # 购物车 点击删除
        self.page.shop_cart.click_delete()
        # 购物车 点击确认
        self.page.shop_cart.click_confirm()
        # 断言 是不是删除成功
        assert self.page.shop_cart.is_toast_exist("删除成功")
        # 断言 能够找到购物车还是空的提示
        assert self.page.shop_cart.is_shop_cart_empty()
