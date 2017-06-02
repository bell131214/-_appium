#coding:utf-8
import unittest,sys,time
sys.path.append('..')
from functions.interface_case import InterfaceCase
from functions.BasePage import BasePage
from pages.startup_page import StartupPage
from pages.home_page import HomePage
import unittest
from functions.appium_init import *



class GFtest(InterfaceCase):
    '''截图对比测试集'''

    def setUp(self):

        self.driver = self.inital.get_driver()
        self.logger = self.inital.logger


    def test_procedure(self):
        '''我的按钮截图对比测试用例'''

        startuppage=StartupPage(self.driver)
        time.sleep(3)
        homepage=startuppage.page_swipe()
        homepage.el_product_btn.click()
        # homepage.get_screenshot_by_element(homepage,"el_home_btn",False)
        result=homepage.get_screenshot_by_element(homepage,"el_my_btn").same_as(30)
       # self.driver.save_screenshot("E:\\quark_work\\result\\2017-05-31\\image\\2017-05-31\\" +"test_procedure11"+'.png')

        self.basepage = BasePage(self.driver)
       # if result != False:
        self.basepage.saveScreenshot('procedure')
        time.sleep(2)
        #self.assertTrue(result)
        #self.assertTrue(result)



    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
    