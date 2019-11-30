import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):

    # 搜索输入框
    keyword_edit_tex = By.ID, "com.yunmall.lc:id/text_search_keyword"

    # 搜索按钮
    search_button = By.ID, "com.yunmall.lc:id/button_search"

    # 删除按钮
    delete_button = By.ID, "com.yunmall.lc:id/search_del"

    # 输入搜索关键字
    @allure.step(title='搜索 输入 关键字')
    def input_keyword(self, text):
        self.input(self.keyword_edit_tex, text)

    # 点击搜索
    @allure.step(title='搜索 点击 搜索')
    def click_search_button(self):
        self.click(self.search_button)

    # 点击删除
    @allure.step(title='搜索 点击 删除')
    def click_delete(self):
        self.click(self.delete_button)

    # 判断搜索的关键字是否存在
    @allure.step(title='搜索 获取 搜索的关键字是否存在')
    def is_search_keyword_exist(self, keyword):
        xpath = By.XPATH, "//*[@resource-id= 'com.yunmall.lc:id/keyayout']/*/*[@text = '%s']"  % keyword
        return self.is_feature_exist(xpath)

    # 判断搜索的历史记录是否为空
    @allure.step(title='搜索 获取 搜索的历史记录是否为空')
    def is_search_record_empty(self):
        xpath = By.XPATH, "//*[@text ='暂无搜索历史']"
        return self.is_feature_exist(xpath)