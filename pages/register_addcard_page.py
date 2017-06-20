#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.sms_verification import Message
import time

class RegisterAddCardPage(BasePage):

    context='register add card page'

    #持卡人姓名文本输入框
    @property
    def el_username_textfield(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_user_pass")

    #银行卡下拉列表
    @property
    def el_bankcard_list(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_bankname")

    #银行卡号文本输入框
    @property
    def el_cardNo_textfield(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_cradnum")

    #预留手机号文本输入框
    @property
    def el_phone_textfield(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_phone_num")

    #获取验证码按钮  元素
    @property
    def el_getsms_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_getverify")

    #验证码文本输入框
    @property
    def el_sms_textfield(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_yanzheng")

    #下拉列表中 建设银行 option
    @property
    def el_bankJS_option(self):
        return self.base_find_element(By.NAME,"中国建设银行")

    #确认按钮 元素
    @property
    def el_confirm_btn(self):
        return self.base_find_element(By.XPATH,"//*[contains(@resource-id,'com.quarkfinance.ufo:id/tv_nextstep')]")

    #点击获取验证码按钮，获取短信验证码
    def logic_getSMS(self):
        self.el_getsms_btn.click()





    #点击银行卡下拉列表，选择建设银行
    def logic_choose_bankcard_js(self):
        self.el_bankcard_list.click()
        time.sleep(1)
        self.el_bankJS_option.click()

    def logic_insert_jsbankCard_INFO(self,username,phone,cardNO):
        from pages.my_bankcard_page import MyBankCardPage
        self.el_username_textfield.send_keys(username)
        self.logic_choose_bankcard_js()
        self.el_cardNo_textfield.send_keys(cardNO)
        self.el_phone_textfield.send_keys(phone)

        self.el_getsms_btn.click()
        sms=Message()
        self.el_sms_textfield.send_keys(sms.get_sms(phone))
        self.el_confirm_btn.click()
        time.sleep(8)

        return MyBankCardPage(self.driver)






