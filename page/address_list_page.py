import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    # 新建地址
    add_new_button = By.ID, "com.yunmall.lc:id/address_add_new_btn"

    # 编辑
    edit_button = By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn"

    # 修改
    modify_button = By.ID, "com.yunmall.lc:id/modify"

    # 删除
    delete_button = By.ID, "com.yunmall.lc:id/delete"

    # 确认
    commit_button = By.XPATH, "//*[@text='确认']"

    # 保存
    save_button = By.ID, "com.yunmall.lc: id / ymtitlebar_right_btn"

    # 默认标记 特征
    is_default_feature = By.ID, "com.yunmall.lc:id/address_is_default"

    # 默认的姓名和电话的信息的特征
    default_receipt_name_text_view = By.ID, "com.yunmall.lc:id/receipt_name"

    # 点击 新建地址
    @allure.step(title='地址管理 点击 新增地址')
    def click_add_new(self):
        self.click(self.add_new_button)

    # 点击 编辑
    @allure.step(title='地址管理 点击 编辑')
    def click_edit(self):
        self.click(self.edit_button)

    # 点击 修改
    @allure.step(title='地址管理 点击 修改')
    def click_modify(self):
        self.click(self.modify_button)

    # 点击 删除
    @allure.step(title='地址管理 点击 删除')
    def click_delete(self):
        self.click(self.delete_button)

    # 点击 确认
    @allure.step(title='地址管理 点击 确认')
    def click_commit(self):
        self.click(self.commit_button)

    # 点击 保存
    @allure.step(title='地址管理 点击 保存')
    def click_save(self):
        self.click(self.save_button)

    # 点击 默认地址
    @allure.step(title='地址管理 点击 默认地址')
    def click_default_address(self):
        self.click(self.is_default_feature)

    # 获取 默认的姓名和电话的文字信息
    @allure.step(title='地址管理 获取 默认的姓名和电话的文字信息是否存在')
    def is_default_receipt_name_text(self):
        return self.get_text(self.default_receipt_name_text_view)

    # 获取  默认标记 是否存在
    @allure.step(title='地址管理 获取 默认标记是否存在')
    def is_default_feature_exist(self):
        return self.is_feature_exist(self.is_default_feature)

    # 获取  删除标记 是否存在
    @allure.step(title='地址管理 获取 删除标记是否存在')
    def is_delete_feature_exist(self):
        return self.is_feature_exist(self.delete_button)