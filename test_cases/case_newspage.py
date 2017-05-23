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



    def test_newspage_contract(self):
        """消息中心-合同消息-本金确认书验证"""


        #客户登录并进入消息中心列表
        newspage = self.logon()
        #点击合同列表页面
        NewsContractsPage=newspage.click_el_contract_message_btn()
        #点击合同详情页
        NewsContractDetailsPage=NewsContractsPage.click_el_check_pact_btn()
        #点击出借本金确认书 el_capital_btn
        NewsContractDetailsPage.clcik_el_capital_btn()

        #bool1 = NewsContractDetailsPage.get_screenshot_by_element(NewsContractDetailsPage, 'el_capital_img',isexist=False)  #第一次截图时
        #进行截图对比
        bool1= NewsContractDetailsPage.get_screenshot_by_element(NewsContractDetailsPage,'el_capital_img',isexist=True).same_as()

        #断言判断
        title=NewsContractDetailsPage.el_capitalt_title.text
        self.assertTrue(bool1)
        self.assertEqual(title,'出借本金确认书')


    def test_contract_list(self):
        """消息中心-合同消息-展示本金确认书合同列表"""
        # 客户登录并进入消息中心列表
        newspage = self.logon()
        # 点击合同列表页面
        NewsContractsPage = newspage.click_el_contract_message_btn()







    def logon(self):
        startupPage = StartupPage(self.driver)
        homepage = startupPage.page_swipe()
        loginPage = homepage.logic_link_login_page()
        homepage = loginPage.logic_login()
        time.sleep(1)
        newspage = homepage.click_el_news_img()
        return  newspage

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()



