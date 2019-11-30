import random

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class CategoryPage(BaseAction):
    # 商品列表 按钮
    goods_list_button = By.ID, "com.yunmall.lc:id/iv_img"

    # 随机点击商品
    @allure.step(title='商品列表 随机点击 商品')
    def click_goods_list(self):
        goods_list = self.find_elements(self.goods_list_button)
        goods_list_count = len(goods_list)
        goods_list_index = random.randint(0, goods_list_count - 1)
        goods_list[goods_list_index].click()