#coding:utf-8
import sys
sys.path.append('..')
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *
from pages.my_invset_record_page import MyInvsetRecorePage
from pages.my_trade_record_page import MyTradeRecordPage
from pages.my_personal_center_page import MyPersonalCenterPage
from pages.my_opinion_page import Opinionpage


class MyPage(BasePage):
    """
    describe：登录后个人信息页面
    """

    #个人中心
    @property
    def el_my_personalCenter(self):
        #return self.base_find_element(By.XPATH,"//android.widget.ImageView[contains(@resource-id,'com.quarkfinance.ufo:id/img_my')]")
       return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/img_my")

    #我的银行卡
    @property
    def el_my_bankCard(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'我的银行卡')]")

    #交易记录
    @property
    def el_my_transactionRecord_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'交易记录')]")

    #投资记录
    @property
    def el_my_investmentRecord(self):
         return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'投资记录')]")

    #我知道了 浮层
    @property
    def el_tv_know(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_know")

    #意见反馈
    @property
    def el_view_msg(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/re_feedback")


    #投资记录快捷入口
    @property
    def el_financial_img(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/return_money_btn")




    #点击投资记录
    def click_my_investmentRecord(self):
        self.el_my_investmentRecord.click()
        return MyInvsetRecorePage(self.driver)

     #投资记录快捷入口
    def logic_financial_img_click(self):
        self.el_financial_img.click()
        return MyInvsetRecorePage(self.driver)


    #点击交易记录
    def logic_my_transactionRecord_btn_click(self):
        self.el_my_transactionRecord_btn.click()
        return MyTradeRecordPage(self.driver)

    def logic_link_myCenter(self):
        self.el_my_personalCenter.click()
        return MyPersonalCenterPage(self.driver)

    def logic_view_msg_click(self):
        self.el_view_msg.click()
        return Opinionpage(self.driver)





if __name__ == '__main__':
    from login_page import LoginPage
    Init()
    driver = appium_init.inital.get_driver()
    login=LoginPage(driver)
    a=login.logic_login('14488888098','qwe123')
    b=a.click_el_my_btn()
    time.sleep(3)
    b.test_t()





