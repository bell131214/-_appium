#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *

class MyAssetDetailsPage(BasePage):
    """
    describe:资产详情页面
    """


    # 合同编号
    @property
    def el_pact_number_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@resource-id,'com.quarkfinance.ufo:id/text_reinvest_contract_no')]")


    #电子合同
    @property
    def el_Asset_pact_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'电子合同查询')]")


    def click_pact(self):
        self.el_Asset_pact_btn.click()


if __name__ == '__main__':
    from login_page import LoginPage
    Init()
    driver = appium_init.inital.get_driver()
    login = LoginPage(driver)
    a = login.logic_login('14488888098', 'qwe123')
    b = a.click_el_my_btn()
    time.sleep(3)
    e = b.test_t()
    time.sleep(2)
    e.press_TouchAction()
    e.el_my_financial.click()
    time.sleep(1)
    f=e.invest_list_click()
    time.sleep(3)
    print f.el_pact_number.text
    f.el_Asset_pact.click()
