#coding=utf-8

import unittest,sys
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver
from functions.appium_init import *
from pages.all_pages import  AllPage
from pages.my_invset_record_page import MyAssetDetailsPage
from functions.BasePage import BasePage

class MyPage(InterfaceCase):
    """登录状态下我的模块验证"""


    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger = self.inital.logger


    def test_view_msg(self):
        """意见反馈"""

        strmeg=u"意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈意见反馈"
        opinionpage=self.logic_login()
        opinionpage.logic_input_data(strmeg)
        opinionpage.logic_Submit_meg_click()
        time.sleep(2)
        #opinionpage.logic_jurisdiction_click()
        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('test_view_msg')


    def logic_login(self):
        startupPage = StartupPage(self.driver)
        homepage = startupPage.page_swipe()
        loginPage = homepage.logic_link_login_page()
        homepage = loginPage.logic_login()
        mypage = homepage.click_el_my_btn()
        mypage.el_tv_know.click()
        opinionpage = mypage.logic_view_msg_click()
        return  opinionpage

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    Init()
    unittest.main()