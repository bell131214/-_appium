#coding:utf-8
from functions.BasePage import BasePage
from pages.startup_page import StartupPage
from functions.random_data import Create_Data
import  time

class ConvergedPage(BasePage):


    def register_customer(self):
        user_phone=Create_Data().get_phone()
        user_name=Create_Data().get_name()
        user_id=Create_Data.get_identification()
        user_email=Create_Data.get_random_mail()
        user_card=Create_Data.get_bank_card_js()
        user_pwd='123456q'

        startupPage = StartupPage(self.driver)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        registerChoosePage = loginPage.logic_link_register()
        registerSmsPage = registerChoosePage.logic_link_new_user()
        registerPasswordPage = registerSmsPage.logic_entry_info(user_phone)
        registerReferencePage = registerPasswordPage.logic_entry_pwd()
        registerPatternlockPage = registerReferencePage.logic_link_hulue()
        registerIdentityAuthPage = registerPatternlockPage.logic_drawGestureCode()
        homePage = registerIdentityAuthPage.logic_entry_user_info(user_name, user_id, user_email)

        homePage.el_my_btn.click()
        myPage=homePage.click_el_my_btn()

        #点击浮层
        myPage.el_tv_know.click()
        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_jsbankCard_INFO(user_name,user_phone,user_card)
        self.driver.quit()

        return (user_phone,user_pwd)





