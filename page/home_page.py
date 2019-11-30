import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction



class HomePage(BaseAction):

    # 首页 我的 按钮
    me_button = By.ID,"com.yunmall.lc:id/tab_me"

    # 首页 分类 按钮
    category_button = By.ID, "com.yunmall.lc:id/tab_category"

    # 首页 购物车 按钮
    cart_button = By.ID, "com.yunmall.lc:id/tab_shopping_cart"

    # 首页 首页按钮
    home_buttom = By.ID, "com.yunmall.lc:id/tab_home"

    # 首页 搜索按钮
    search_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    # 点击 我的
    @allure.step(title='主页 点击 我')
    def click_me(self):
        self.click(self.me_button)

    # 点击 分类
    @allure.step(title='主页 点击 分类')
    def click_category(self):
        self.click(self.category_button)

    # 点击 购物车
    @allure.step(title='主页 点击 购物车')
    def click_cart(self):
        self.click(self.cart_button)

    # 点击 首页
    @allure.step(title='主页 点击 首页')
    def click_home(self):
        self.click(self.home_buttom)

    # 点击 搜索
    @allure.step(title='主页 点击 搜索')
    def click_search(self):
        self.click(self.search_button)

    @allure.step(title='主页 登录（如果没有登录的话）')
    def login_if_not(self, page):
        # 判断登录状态
        self.click_me()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
           return
        # 没有登录，就去登录
        # 点击 已有账号
        page.register.click_login()
        # 输入 用户名
        page.login.input_username("itheima_test")
        # 输入 密码
        page.login.input_password("itheima")
        # 点击 登录
        page.login.click_login()

    