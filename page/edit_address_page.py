import time
import random

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):

    # 收件人
    receipt_name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"
    # 手机号
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"
    # 详细地址
    detail_info_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
    # 邮编
    post_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"
    # 设为默认
    address_default = By.ID, "com.yunmall.lc:id/address_default"
    # 保存
    save_button = By.ID, "com.yunmall.lc:id/button_send"
    # 所在地区
    region_button = By.ID, "com.yunmall.lc:id/address_province"
    # 地区特征
    area_feature = By.ID, "com.yunmall.lc:id/area_title"

    # 输入收件人
    @allure.step(title='编辑地址 输入 收件人')
    def input_receipt_name(self, text):
        self.input(self.receipt_name_edit_text, text)
    # 输入手机号
    @allure.step(title='编辑地址 输入 手机号')
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)
    # 输入详细地址
    @allure.step(title='编辑地址 输入 详细地址')
    def input_detail_info(self, text):
        self.input(self.detail_info_edit_text, text)
    # 输入邮编
    @allure.step(title='编辑地址 输入 邮编')
    def input_post_code(self, text):
        self.input(self.post_code_edit_text, text)
    # 点击保存
    @allure.step(title='编辑地址 点击 保存')
    def click_save(self):
        self.click(self.save_button)
    # 点击所在地区
    @allure.step(title='编辑地址 点击 地区')
    def click_region(self):
        self.click(self.region_button)
    # 进入 所在地区 并且选择一个随机的区域
    @allure.step(title='编辑地址 随机点击 区域')
    def choose_region(self):
        self.click_region()
        time.sleep(1)
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            areas = self.find_elements(self.area_feature)
            areas_count = len(areas)
            area_index = random.randint(0, areas_count - 1)
            areas[area_index].click()
            time.sleep(1)

    # 点击设为默认
    @allure.step(title='编辑地址 点击 设为默认')
    def click_address_default(self):
        self.click(self.address_default)



