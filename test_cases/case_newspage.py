#coding=utf-8

import unittest,sys
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.login_page import LoginPage as login
from pages.banner_pages import BannerPages
from functions.appium_init import Initialization as inital
from pages.startup_page import StartupPage
from pages.home_page import HomePage

class NewsPage(InterfaceCase):
    """消息中心"""

    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger = self.inital.logger
        login_=login(self.driver)
        homepage=login_.logic_login()
        time.sleep(1)
        self.newspage=homepage.click_el_news_img()

    def test_check_title(self):
        """page 验证"""
        title_=self.newspage.get_el_newspage_title()
        self.assertEqual(title_,u"消息中心")

    def test_check_contract(self):
        """合同消息 跳转验证"""
        contractpage=self.newspage.click_el_contract_message_btn()
        title=contractpage.get_el_Contracts_title()
        self.assertEqual(title,u"合同消息")





    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



