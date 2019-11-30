import time

import pytest
from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestSearch(object):

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("search_data.yaml", "test_search"))
    def test_search(self, args):
        keyword = args["keyword"]
        # 如果没有登录 去登陆
        self.page.home.login_if_not(self.page)
        # 首页 点击首页
        self.page.home.click_home()
        # 首页 点击搜索
        self.page.home.click_search()
        # 搜索 输入关键字
        self.page.search.input_keyword(keyword)
        # 搜索 点击搜索按钮
        self.page.search.click_search_button()
        # 搜索 点击返回
        self.page.search.press_back()
        time.sleep(2)
        # 断言 这个页面中能够找到
        assert self.page.search.is_keyword_in_page_source(keyword)

    def test_del_search(self):
        # 如果没有登录 去登陆
        self.page.home.login_if_not(self.page)
        # 首页 点击首页
        self.page.home.click_home()
        # 首页 点击搜索
        self.page.home.click_search()
        # 搜索 点击删除
        self.page.search.click_delete()
        # 断言
        assert self.page.search.is_toast_exist("暂无搜索历史")