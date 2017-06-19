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
    def el_trade_btn(self):
        return self.base_find_elements(By.XPATH, "//android.widget.TextView[contains(@text,'交易')]")

    #我知道了 确认按钮
    @property
    def el_tv_know(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_know")

    #咨询
    @property
    def el_trade_Consultation_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'咨询')]")


    #咨询列表
    @property
    def el_trade_Consultation_list(self):
        return self.base_find_elements(By.ID,"com.quarkfinance.ufo:id/layout_item_head")

    # 预约编号
    @property
    def el_trade_Consultation_inquiry_no(self):
            return self.base_find_elements(By.XPATH, "//*[@resource-id='com.quarkfinance.ufo:id/text_inquiry_no']/android.widget.TextView[2]")

    #点击列表
    @property
    def el_trade_list_image(self):

        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/layout_item_head")
        #return  self.base_find_elements(By.XPATH,"//android.widget.RelativeLayout[contains(@id,'com.quarkfinance.ufo:id/layout_item_head')]")



    def logic_get_Consultation_list(self):
        self.el_trade_Consultation_list[0].click()

    #获取私募预约编号
    def logic_get_inquiry_no_test(self):
        inquiry_no=self.el_trade_Consultation_inquiry_no[0].text
        return  inquiry_no




    @property
    def el_trade_Consultation_btn111(self):
        self.logic_trade_btn_click()
        self.el_trade_list_image[1].click()
        time.sleep(2)

        #el_trade_list_image1=self.el_trade_list_image
        #el_trade_list_image1[1].click()
        #a=self.base_find_element(By.XPATH,"//android.widget.LinearLayout[{index}]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView".format(index=1))

        #b=self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_name_and_amount'][{id}]/android.widget.TextView".format(id=2))
        b = self.base_find_elements(By.XPATH,
                                    "//android.widget.LinearLayout[{id}]/android.widget.RelativeLayout/android.widget.TextView".format(id=2))
        return  b[0].text

        #return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'咨询')]")


    #进入交易list
    def logic_trade_btn_click(self):
          self.el_trade_btn[0].click()


    def logic_trade_list(self,index=0):
        #self.logic_trade_btn_click
        self.el_trade_list_image.click()
        time.sleep(2)
        trade_dict={}
        txtinvestapply =self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_contract_no']/android.widget.TextView")[1].text
        paymentno = self.base_find_elements(By.XPATH, "//*[@resource-id='com.quarkfinance.ufo:id/text_transaction_flowing']/android.widget.TextView")[1].text
        trade_list=[txtinvestapply,paymentno]

       # trade_dict[u'产品名称']=self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_name_and_amount'][{id}]/android.widget.TextView".format(id=index))[0].text
       # trade_dict[u'金额'] = self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_name_and_amount']/android.widget.TextView")[1].text

        #print txtinvestapply,paymentno
        return trade_list





if __name__ == '__main__':

    from pages.startup_page import StartupPage
    from functions.appium_init import Initialization
    Init()
    driver = appium_init.inital.get_driver()
    startupPage = StartupPage(driver)
    homepage = startupPage.page_swipe()
    loginPage = homepage.logic_link_login_page()
    homepage = loginPage.logic_login()
    mypage = homepage.click_el_my_btn()
    mypage.el_tv_know.click()
    mytraderecordpage=mypage.logic_my_transactionRecord_btn_click()
    time.sleep(2)
    a=mytraderecordpage.logic_trade_list()

   # print a.items()





