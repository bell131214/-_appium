#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.register_addcard_page import RegisterAddCardPage
from pages.bankcard_info_page import BankCardInfoPage
import time

class MyBankCardPage(BasePage):

    context='my bankcard page'

    #我的银行卡页面新增银行卡按钮 元素
    @property
    def el_addCard_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tb_right")

    @property
    def el_bankcard_list(self):
        return self.base_find_elements(By.ID,"com.quarkfinance.ufo:id/ll_bank_layout")

    @property
    def el_bankcard_js(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'中国建设银行')]")

    @property
    def el_bankcard_gf(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'广发银行')]")

    @property
    def el_bankcard_jt(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'交通银行')]")

    @property
    def el_bankcard_pa(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'平安银行')]")

    @property
    def el_bankcard_js(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'建设银行')]")

    @property
    def el_bankcard_zs(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'招商银行')]")

    @property
    def el_bankcard_zx(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'中信银行')]")

    @property
    def el_bankcard_zg(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'中国银行')]")

    @property
    def el_bankcard_ny(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'中国农业银行')]")


    @property
    def el_bankcard_ms(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'中国民生银行')]")

    #银行卡列表第一个元素
    @property
    def el_bankName_listOne(self):
        return self.base_find_elements(By.ID,"com.quarkfinance.ufo:id/tv_bankname")[0]

    #银行卡尾号第一个元素
    @property
    def el_bankWeihao_listOne(self):
        return self.base_find_elements(By.ID,"com.quarkfinance.ufo:id/tv_weihao")[0]


    def logic_addCard_click(self):
        self.el_addCard_btn.click()
        return RegisterAddCardPage(self.driver)

    def logic_link_bankcardInfo_page(self):
        self.el_bankName_listOne.click()
        return BankCardInfoPage(self.driver)




