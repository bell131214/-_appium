#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.register_password_page import RegisterPasswordPage
class RegisterSmsPage(BasePage):
    context='register sms page'

    #"手机号"文本输入框 元素
    @property
    def el_phone_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_phone")

    #"验证码"文本输入框 元素
    @property
    def el_verification_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_yanzheng")

    #获取"验证码"按钮 元素
    @property
    def el_verification_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_getverify")

    #"下一步"按钮 元素
    @property
    def el_next_step_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_nextstep")

    #跳转至register_password_page页面
    def logic_link_next(self):
        self.el_next_step_btn.click()
        return RegisterPasswordPage(self.driver)
