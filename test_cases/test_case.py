#coding=utf-8

import unittest,sys
sys.path.append('..')

from pages.login_page import LoginPage

from functions.interface_case import InterfaceCase



class LoginTest(InterfaceCase):


    def setUp(self):
        # info = Initialization()
        self.driver = self.inital.get_driver()
        self.logger=self.inital.logger

    def test_add(self):
        self.assertEqual(self.inital.project_path,'D:\\quarkscript\\UFO_appium')


    def test_new_PO_test(self):
        u"""验证登录"""
        try:
            username = '18048444414'
            password = 'hele5201'
            self.driver.implicitly_wait(5)
            login=LoginPage(self.driver)
            login.logic_login(username, password)
            self.assertEqual(1, 1)


        except Exception,e:

            self.logger.info(e)




    @unittest.skip
    def test_Skip(self):
        print "不执行用例"


    def tearDown(self):
       #self.devices.close_app()
        #self.devices.close()
        self.driver.quit()








if __name__ == '__main__':
     unittest.main(verbosity =2)