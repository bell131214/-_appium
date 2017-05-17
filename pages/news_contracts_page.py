#coding:utf-8
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *
from pages.news_contract_details_page import NewsContractDetailsPage

class NewsContractsPage(BasePage):
    """
     describe：消息中心合同页面
      """


   #查看电子合同
    @property
    def el_check_pact_btn(self):
        return self.base_find_elements(By.XPATH, "//android.widget.TextView[contains(@text,'点击查看')]")

    @property
    def el_Contracts_title(self):
        return self.base_find_elements(By.XPATH, "//android.widget.TextView[contains(@resource-id,'com.quarkfinance.ufo:id/tb_title')]")





    def click_el_check_pact_btn(self,index=0):
        """
        :param index: 列表索引
        :return:  NewsContractDetailsPage  合同详情页面
        """
        self.el_check_pact_btn[index].click()
        return NewsContractDetailsPage(self.driver)


    def get_el_Contracts_title(self):
        """
        :return: 合同详情页面 title
        """
        try:
            return self.el_Contracts_title.text
        except  AttributeError, e:
            self.logger.debug('LoginTest | exception is %s' % e)
            # self.driver.quit()


if __name__ == '__main__':
    from login_page import LoginPage
    Init()
    driver = appium_init.inital.get_driver()
    login = LoginPage(driver)
    a = login.logic_login('14488888098', 'qwe123')
    time.sleep(1.5)
    b=a.el_news_img_click()
    c=b.el_contract_message_btn_click()
    time.sleep(1.5)
    c.el_check_pact_btn_click()

