#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.register_addcard_page import RegisterAddCardPage
import time

class MyBankCardPage(BasePage):

    context='my bankcard page'

    #我的银行卡页面新增银行卡按钮 元素
    @property
    def el_addCard_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tb_right")

    def logic_addCard_click(self):
        self.el_addCard_btn.click()
        return RegisterAddCardPage(self.driver)




