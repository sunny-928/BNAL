import time

from base.base_driver import init_driver
from page.page import Page


class TestClear(object):

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_clear(self):
        # 如果没有登录 就去登录
        self.page.home.login_if_not(self.page)
        # 我 点击设置
        self.page.me.click_setting()
        # 设置 点击清理缓存
        self.page.setting.click_clear_cache()
        time.sleep(2)
        # 断言
        assert self.page.setting.is_toast_exist("清理成功")