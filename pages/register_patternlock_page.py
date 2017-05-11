#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import  By
from pages.register_identity_auth_page import RegisterIdentityAuthPage

class RegisterPatternlockPage(BasePage):
    context="register patternlock page"


    #跳转至register_identity_auth_page
    def logic_link_dingding(self):

        #复制鼎鼎滑屏代码
        return RegisterIdentityAuthPage(self.driver)

