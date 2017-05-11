#coding:utf-8
__author__ = 'FanGu'

import unittest,sys,time
sys.path.append('..')
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from pages.home_page import HomePage
class GFtest(InterfaceCase):

    def setUp(self):
        self.driver=self.inital.get_driver()
        self.logger=self.inital.logger

    def test_procedure(self):
        startuppage=StartupPage(self.driver)
        time.sleep(3)
        homepage=startuppage.page_swipe()
        homepage.el_my_btn.click()

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()