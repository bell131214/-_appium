#coding:utf-8
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *


class MyTradeRecordPage(BasePage):

    """
      describe：交易记录页面
    """

    #交易
    @property
    def el__trade_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'交易')]")
        #return self.base_find_element(By.XPATH, "//com.quarkfinance.ufo:id/tab_layout[contains(@resource-id,'com.quarkfinance.ufo:id/tab_layout')]/android.widget.LinearLayout/android.support.v7.a.a$c[0]/android.widget.TextView[0]")



    #咨询
    @property
    def el_trade_Consultation_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'咨询')]")





if __name__ == '__main__':
    from login_page import LoginPage
    Init()
    driver = appium_init.inital.get_driver()
    login = LoginPage(driver)
    a = login.logic_login('14488888098', 'qwe123')
    time.sleep(1.5)
    b=a.click_el_my_btn()
    b.test_t()
    c=MyTradeRecordPage(driver)
    c.el_trade_Consultation_btn.click()
    time.sleep(3)
    c.el__trade_btn.click()

