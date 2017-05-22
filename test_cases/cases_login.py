#coding=utf-8
#coding=utf-8

import unittest,sys
# sys.path.append('..')

from pages.login_page import LoginPage as login
from functions.interface_case import InterfaceCase
from functions.appium_init import Initialization




class LoginTest(InterfaceCase):


    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger = self.inital.logger
        self.login_ = login(self.driver)


    def test_Login_def(self):
       """验证成功登录"""
       try:
           username = '14488888098'
           password = 'qwe123'
           self.logger.info(username+password)
           homepage=self.login_.logic_login(username,password)
           self.logger.info('LoginTest | exec test_Login_def1 name{name},password:{password}'.format(name=username,password=password))
           #self.assertTrue(homepage.proving_el_invest_img())
       except Exception,e:
           self.logger.debug('LoginTest | exception is %s' %e)
       self.assertTrue(homepage.proving_el_invest_img())




       def tearDown(self):
           self.driver.quit()


if __name__ == '__main__':
     unittest.main()

