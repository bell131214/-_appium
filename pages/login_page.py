#coding=utf-8

import time
from selenium.webdriver.common.by import By
from functions.BasePage import BasePage
from functions.appium_init import *
from pages.my_page import MyPage
from pages.startup_page import StartupPage


class LoginPage(BasePage):

#new  PO  return element

    @property
    def el_my_btn(self):
        return self.base_find_element(By.NAME,u'我的')

    @property
    def el_phone_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_name")

    @property
    def el_pwd_text_input(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_password")

    @property
    def el_login_btn(self):
        return  self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_login")


    def logic_login(self,phone,pwd):
        startuppage=StartupPage(self.driver)
        str
        self.el_my_btn.click()
        self.el_phone_text_input.send_keys(phone)
        self.el_pwd_text_input.send_keys(pwd)
        self.el_login_btn.click()
        time.sleep(3)
        return MyPage(self.driver)



if __name__ == '__main__':
    # info = Initialization()
    Init()
    driver = appium_init.inital.get_driver()
    d = LoginPage(driver)
    d.logic_login('18048444414','hele5201')
    time.sleep(2)