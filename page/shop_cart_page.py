import random
import time

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ShopCartPage(BaseAction):

     # 编辑 按钮
     edit_button = By.XPATH, "//*[@text='编辑']"

     # 完成 按钮
     commit_button = By.XPATH, "//*[@text= '完成']"

     # 加号 按钮
     add_button = By.ID, "com.yunmall.lc:id/iv_add"

     # 删除 按钮
     delete_button = By.ID, "com.yunmall.lc:id/tv_del_all"

     # 确认 按钮
     confirm_button = By.ID, "com.yunmall.lc:id/ymdialog_right_button"

     # 全选 按钮
     select_all_button = By.ID, "com.yunmall.lc:id/tv_select_all"

     # 获取商品单价
     price_feature = By.ID, "com.yunmall.lc:id/tv_price"

     # 获取商品总价
     all_price_feature = By.ID, "com.yunmall.lc:id/tv_count_money"

     # 点击 编辑
     @allure.step(title='购物车 点击 编辑')
     def click_edit(self):
         self.click(self.edit_button)

     # 点击 完成
     @allure.step(title='购物车 点击 完成')
     def click_commit(self):
         self.click(self.commit_button)

     # 点击 加号
     @allure.step(title='购物车 点击 加号')
     def click_add(self):
         self.click(self.add_button)

     # 点击 全选
     @allure.step(title='购物车 点击 全选')
     def click_select_all(self):
         self.click(self.select_all_button)

     # 点击 删除
     @allure.step(title='购物车 点击 删除')
     def click_delete(self):
         self.click(self.delete_button)

     # 点击 确认
     @allure.step(title='购物车 点击 确认')
     def click_confirm(self):
         self.click(self.confirm_button)

     # 处理价格 去掉前面的人民币符号，并且转化成float类型
     @allure.step(title='购物车 处理价格')
     def deal_with_price(self, price):
         return float(price[2:])

     # 获取单价文字
     @allure.step(title='购物车 获取 商品单价')
     def get_price(self):
         price_text = self.get_text(self.price_feature)
         return self.deal_with_price(price_text)

     # 获取总价文字
     @allure.step(title='购物车 获取 商品总价')
     def get_all_price(self):
         all_price_text =  self.get_text(self.all_price_feature)
         return self.deal_with_price(all_price_text)

     # 判断购物车是否为空
     @allure.step(title='购物车 获取 购物车是否为空')
     def is_shop_cart_empty(self):
         xpath = By.XPATH, "//*[contains(@text, '购物车还是空的')]"
         return self.is_feature_exist(xpath)