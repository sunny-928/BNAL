import time

from base.base_driver import init_driver
from page.page import Page


class TestUpdate(object):

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_update(self):
        # 如果没有登录 去登陆
        self.page.home.login_if_not(self.page)
        # 我 点击设置
        self.page.me.click_setting()
        # 设置 点击关于百年奥莱
        self.page.setting.click_about()
        # 关于百年奥莱 点击版本更新
        self.page.about.click_version_update()
        # 断言
        assert self.page.about.is_toast_exist("立即更新")
