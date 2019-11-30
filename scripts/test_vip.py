import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestVip(object):

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("vip_data.yaml", "test_vip"))
    def test_vip(self, args):
        # 解析 yaml 的数据
        keyword = args["keyword"]
        toast = args["toast"]
        # 脚本流程
        # 如果没有登录 去登陆
        self.page.home.login_if_not(self.page)
        # 我 点击加入vip
        self.page.me.click_add_vip()
        time.sleep(2)
        # 打印所有的环境
        print(self.driver.contexts)
        # 切换web环境
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        time.sleep(2)
        # vip 输入邀请码
        self.page.vip.input_invite(keyword)
        # vip 点击加入vip
        self.page.vip.click_be_vip()
        # 断言
        assert self.page.vip.is_keyword_in_page_source(toast)
        time.sleep(2)
        # 切换回原生环境
        self.driver.switch_to.context("NATIVE_APP")
