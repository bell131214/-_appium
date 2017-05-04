#coding=utf-8

import time
from selenium.webdriver.common.by import By

from functions.BasePage import BasePage
from functions.appium_init import *
from pages.my_page import MyPage


class Login_Test(BasePage):

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
        self.el_my_btn.click()
        self.el_phone_text_input.send_keys(phone)
        self.el_pwd_text_input.send_keys(pwd)
        self.el_login_btn.click()
        time.sleep(3)
        return MyPage(self.driver)



#old  PO
    #定位首页【我的】
    myInf_loc = (By.NAME, u"我的")

    # 定位【手机号输入框】
    phone_loc = (By.ID, "com.quarkfinance.ufo:id/edit_name")

    # 定位【密码框】
    password_loc = (By.ID, "com.quarkfinance.ufo:id/edit_password")

    # 定位【注册】
    register_loc = (By.NAME, "com.quarkfinance.ufo:id/tv_register")

    # 定位【忘记密码】

    tv_forget_pass_loc = (By.ID, "com.quarkfinance.ufo:id/tv_forget_pass")

    # 【登录】
    click_Sign_loc = (By.ID, "com.quarkfinance.ufo:id/tv_login")



    def click_My_button(self):
         self.clickElement(*self.myInf_loc)

        # 输入手机号
    def input_Number(self,phone_number):
        self.send_keys(self.phone_loc,phone_number)

    def input_password(self, password):
        self.send_keys(self.password_loc, password)

    def click_login(self):
        self.clickElement(*self.click_Sign_loc)

    def click_register(self):
        self.clickElement(*self.register_loc)

    def login_test(self,phon,password):
         self.page_swipe()
         time.sleep(3)
         self.click_My_button()
         self.input_Number(phon)
         self.input_password(password)
         time.sleep(3)
         self.click_login()
         return MyPage(self.driver)


    def page_swipe(self):
        time.sleep(2)
        self.swipe_to_right()
        time.sleep(2)
        self.swipe_to_right()
        time.sleep(2)
        self.swipe_to_right()
        time.sleep(2)
        self.press_TouchAction()
        time.sleep(5)


if __name__ == '__main__':
    # info = Initialization()
    Init()
    driver = appium_init.inital.get_driver()
    d = Login_Test(driver)
    d.login_test('18048444414','hele5201')
    time.sleep(2)