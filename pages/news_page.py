#coding:utf-8
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *
from pages.news_contracts_page import NewsContractsPage
from pages.news_consults_page import NewsConsultsPage


class NewsPage(BasePage):
    """
    describe：消息中心
    """

    #合同消息
    @property
    def el_contract_message_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'合同消息')]")

    #咨询消息
    @property
    def el_consult_message_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'咨询消息')]")


    #点击 合同中心，返回 NewsContractsPage
    def el_contract_message_btn_click(self):
        self.el_contract_message_btn.click()
        return NewsContractsPage(self.driver)


    def el_consult_message_btn_click(self):
        self.el_consult_message_btn.click()
        return NewsConsultsPage(self.driver)




if __name__ == '__main__':
    from login_page import LoginPage
    Init()
    driver = appium_init.inital.get_driver()
    login = LoginPage(driver)
    a = login.logic_login('14488888098', 'qwe123')
    time.sleep(1.5)
    b=a.el_news_img_click()
    b.el_contract_message_btn_click()

