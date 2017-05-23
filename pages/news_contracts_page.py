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
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@resource-id,'com.quarkfinance.ufo:id/tb_title')]")





    def click_el_check_pact_btn(self,index=0):
        """
        :param index: 列表索引
        :return:  NewsContractDetailsPage  合同详情页面
        """
        #if self.element_is_exsit(self.el_check_pact_btn):
        if self.proving_element('点击查看'):
             self.el_check_pact_btn[index].click()

        else:
            self.click_el_check_pact_btn()

        return NewsContractDetailsPage(self.driver)




    def get_el_Contracts_title(self):
        """
        :return: 合同列表页面 title
        """
        try:
            return self.el_Contracts_title.text
        except  AttributeError, e:
            self.logger.debug('LoginTest | exception is %s' % e)
            # self.driver.quit()


if __name__ == '__main__':
    Init()
    driver = appium_init.inital.get_driver()
    from pages.startup_page import StartupPage
    startupPage = StartupPage(driver)
    homepage = startupPage.page_swipe()

    loginPage = homepage.logic_link_login_page()
    homepage = loginPage.logic_login()
    time.sleep(1)
    newspage = homepage.click_el_news_img()

    NewsContractsPage=newspage.click_el_contract_message_btn()
    NewsContractsPage.click_el_check_pact_btn()





