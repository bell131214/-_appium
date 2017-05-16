#coding:utf-8
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *

class NewsContractDetailsPage(BasePage):
    """
      describe：合同详情页
    """

    # 元素【出借咨询与服务协议】
    @property
    def el_service_agreement_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'出借咨询与服务协议')]")


    # 元素【授权委托书-出借确认和债权转让】
    @property
    def el_confirmation_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'授权委托书-出借确认和债权转让')]")


    # 元素【授权委托书-催收及诉讼】
    @property
    def el_litigation_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'授权委托书-催收及诉讼')]")


    # 元素【出借本金确认书】
    @property
    def el_capital_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'出借本金确认书')]")



if __name__ == '__main__':
    from login_page import LoginPage

    Init()
    driver = appium_init.inital.get_driver()
    login = LoginPage(driver)
    a = login.logic_login('14488888098', 'qwe123')
    time.sleep(1.5)
    b = a.el_news_img_click()
    c = b.el_contract_message_btn_click()
    time.sleep(1.5)
    d=c.el_check_pact_btn_click()
    #time.sleep(1.5)
    d.el_service_agreement_btn.click()