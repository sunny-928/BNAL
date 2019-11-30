import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegisterPage(BaseAction):
    # 登录 按钮
    login_button = By.XPATH, "//*[@text='已有账号，去登录']"

    # 点击登录 按钮
    @allure.step(title='注册 点击 登录')
    def click_login(self):
        self.click(self.login_button)