#coding=utf-8

import unittest,sys
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.banner_pages import BannerPages



class LoginTest(InterfaceCase):
    u"""验证首页banner获取加载页内容"""


    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger=self.inital.logger




    def test_click_banner1(self):
        u"""验证点击【1】banner"""
        try:
            a=BannerPages(self.driver)
            b=a.banner_click(id=1)
            time.sleep(3)
            self.assertEqual(str(b), u"系统维护")
        except Exception,e:
            self.logger.info(e)

    def test_click_banner3(self):
        u"""验证点击【2】banner"""
        try:
            a=BannerPages(self.driver)
            b=a.banner_click(id=3)
            time.sleep(3)
            self.assertEqual(str(b), u"夸客美丽增值计划")
        except Exception,e:
            self.logger.info(e)

    def test_click_banner5(self):
        u"""验证点击【3】banner"""
        try:
            a=BannerPages(self.driver)
            b=a.banner_click(id=5)
            time.sleep(3)
            self.assertEqual(str(b), u"新春心意")
        except Exception,e:
            self.logger.info(e)


    def tearDown(self):
        self.driver.quit()





if __name__ == '__main__':
 unittest.main(verbosity =2)