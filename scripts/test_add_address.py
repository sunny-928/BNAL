import time

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver

from page.page import Page


class TestAddAddress(object):

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)

        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("address_data.yaml", "test_add_address"))
    def test_add_address(self, args):
        name = args["name"]
        phone = args["phone"]
        info = args["info"]
        post_code = args["post_code"]
        toast = args["toast"]

        # 如果没有登录就去登录
        self.page.home.login_if_not(self.page)
        # 我 点击设置
        self.page.me.click_setting()
        # 设置 点击地址管理
        self.page.setting.click_address()
        # 地址管理 新增地址
        self.page.address_list.click_add_new()
        # 新增地址 输入收件人
        self.page.edit_address.input_receipt_name(name)
        # 新增地址 输入电话
        self.page.edit_address.input_phone(phone)
        # 新增地址 输入详细地址
        self.page.edit_address.input_detail_info(info)
        # 新增地址 输入邮编
        self.page.edit_address.input_post_code(post_code)
        # 新增地址 设置默认
        self.page.edit_address.click_address_default()
        # 新增地址 选择一个随机的区域
        self.page.edit_address.choose_region()
        # 新增地址 保存
        self.page.edit_address.click_save()
        if toast is None:
            assert self.page.address_list.is_default_receipt_name_text() == "%s  %s" % (name, phone)
        else:
            assert self.page.address_list.is_toast_exist(toast)

    def test_edit_address(self):
        # 如果没有登录就去登录
        self.page.home.login_if_not(self.page)
        # 我 点击设置
        self.page.me.click_setting()
        # 设置 点击地址管理
        self.page.setting.click_address()
        # 地址管理 判断默认标记是否存在
        if not self.page.address_list.is_default_feature_exist():
            # 地址管理 新增地址
            self.page.address_list.click_add_new()
            # 新增地址 输入收件人
            self.page.edit_address.input_receipt_name("zhangsan")
            # 新增地址 输入电话
            self.page.edit_address.input_phone("18888888888")
            # 新增地址 输入详细地址
            self.page.edit_address.input_detail_info("三单元 504")
            # 新增地址 输入邮编
            self.page.edit_address.input_post_code("100000")
            # 新增地址 设置默认
            self.page.edit_address.click_address_default()
            # 新增地址 选择一个随机的区域
            self.page.edit_address.choose_region()
            # 新增地址 保存
            self.page.edit_address.click_save()
        # 进入 默认地址
        self.page.address_list.click_default_address()
        # 重新输入 收件人
        self.page.edit_address.input_receipt_name("李四")
        # 重新输入 手机号
        self.page.edit_address.input_phone("16666666666")
        # 重新输入 详细地址
        self.page.edit_address.input_detail_info("302 二单元")
        # 重新输入 邮编
        self.page.edit_address.input_post_code("222222")
        # 重新输入 所在地区
        self.page.edit_address.choose_region()
        # 保存
        self.page.edit_address.click_save()
        # 断言，是否出现 "保存成功" 的toast信息
        assert self.page.address_list.is_toast_exist("保存成功")

    def test_delete_address(self):
        # 首页，如果没有登录就登录
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 地址管理
        self.page.setting.click_address()
        # 地址管理 判断是否有地址可以删除
        assert self.page.address_list.is_default_feature_exist()
        for i in range(10):
            self.page.address_list.click_edit()
            # 判断 删除是否存在
            if not self.page.address_list.is_delete_feature_exist():
                # 如果不存在，break
                break
            # 如果存在，则点击
            self.page.address_list.click_delete()
            self.page.address_list.click_commit()
        # 如果存在，则点击
        self.page.address_list.click_edit()
        # 断言 删除按钮 是否存在，如果不存在则通过，如果存在则有问题
        assert not self.page.address_list.is_delete_feature_exist()


