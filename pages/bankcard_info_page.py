#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
import time

class BankCardInfoPage(BasePage):

    context=' bankcard  info page'

    #删除银行卡按钮
    @property
    def el_delete_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_deletecard")

    #密码输入框文本
    @property
    def el_password_textfeild(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/et_password")


    #确定按钮
    @property
    def el_comfirm_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_confirm")

    def logic_delete_bankcard(self,user_pwd):
        from pages.my_bankcard_page import MyBankCardPage
        time.sleep(1)
        self.el_delete_btn.click()
        self.el_password_textfeild.send_keys(user_pwd)
        self.el_comfirm_btn.click()
        return MyBankCardPage(self.driver)






