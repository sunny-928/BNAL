import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AboutPage(BaseAction):

    # 版本更新 按钮
    version_update_button = By.ID, "com.yunmall.lc:id/about_version_update"

    # 点击版本更新
    @allure.step(title='关于百年奥莱 点击 版本更新')
    def click_version_update(self):
        self.click(self.version_update_button)