import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 昵称
    nick_name_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    # 设置
    setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    # 加入VIP
    add_vip_button = By.ID, "com.yunmall.lc:id/tv_my_shop_text"

    # 获取昵称
    @allure.step(title='我 获取 昵称')
    def get_nick_name_text(self):
        return self.find_element(self.nick_name_text_view).text

    # 点击左上角设置按钮
    @allure.step(title='我 点击 设置')
    def click_setting(self):
        self.click(self.setting_button)

    # 点击加入vip
    @allure.step(title='我 点击 加入VIP')
    def click_add_vip(self):
        self.find_element_with_scroll(self.add_vip_button).click()