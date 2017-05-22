#coding:utf-8
import unittest,sys
sys.path.append('..')
from functions.appium_init import *
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
class LoginTest(InterfaceCase):
    '''
    登录操作相关测试用例集合
    '''

    def setUp(self):
        self.driver=self.inital.get_driver()
        self.logger=self.inital.logger

    #非登录态点击“立即投资”按钮
    def test_non_login_state_clickBuy(self):
        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        productListPage=homePage.logic_link_product()
        productQuarkzxPage=productListPage.logic_link_quarkZX()
        loginPage=productQuarkzxPage.logic_noLogin_state_buy()

        self.assertEqual('im login page',loginPage.context)

    #非登录状态点击“我的”按钮
    def test_non_login_state_clickMyPage(self):
        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        self.assertEqual('im login page',loginPage.context)

    #登录成功用例
    def test_login_success(self):
        user_phone='14488888098'
        pwd='qwe123'

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,pwd)

        myPage=homePage.click_el_my_btn()
        # 点击浮层
        time.sleep(1)
        myPage.el_tv_know.click()
        # 断言代码
        myPersonalCenterPage = myPage.logic_link_myCenter()
        phone_text = myPersonalCenterPage.el_phone_text.text
        phone_secret = user_phone[:3] + '****' + user_phone[7:]
        self.assertEqual(phone_text, phone_secret)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    Init()
    unittest.main()

