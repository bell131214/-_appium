#coding=utf-8

import unittest,sys
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.banner_pages import BannerPages
from functions.appium_init import *
from pages.startup_page import StartupPage



class hometest(InterfaceCase):
    u"""验证首页banner获取加载页内容"""


    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger=self.inital.logger




    #id:输入需要验证的banner 索引ID
    #assertEqual 输入预期的banner详情的title

    def test_click_banner1(self):
        u"""验证点击banner[1]"""
        try:
            startUp=StartupPage(self.driver)
            homepage=startUp.page_swipe()
            b=homepage.banner_click(id=1)
            time.sleep(3)
            self.logger.info(b.child_page_Xpath.text)
        except Exception,e:
              self.logger.info(e)

        self.assertEqual(str(b.child_page_Xpath.text), "系统维护")

        # id:输入需要验证的banner 索引ID
        # assertEqual 输入预期的banner详情的title
    def test_click_banner3(self):
       u"""验证点击banner[3]"""
       try:
        startUp=StartupPage(self.driver)
        homepage=startUp.page_swipe()
        b=homepage.banner_click(id=3)
        time.sleep(3)
        self.logger.info(b.child_page_Xpath.text)

       except Exception,e:
        self.logger.info(e)

        self.assertEqual(str(b.child_page_Xpath.text), u"夸客美丽增值计划")


        # id:输入需要验证的banner 索引ID
        # assertEqual 输入预期的banner详情的title
    def test_click_banner5(self):
        u"""验证点击banner[5]"""
        try:
            startUp = StartupPage(self.driver)
            homepage = startUp.page_swipe()
            b = homepage.banner_click(id=5)
            time.sleep(3)
            self.logger.info(b.child_page_Xpath.text)
        except Exception, e:
            self.logger.info(e)

        self.assertEqual(str(b.child_page_Xpath.text), u"新春心意")


    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    Init()
    unittest.main()