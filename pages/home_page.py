#coding:utf-8
#from pages.base_page import BasePage
from pages.my_page import MyPage
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.banner_pages import BannerPages
from functions.appium_init import *

import time



class HomePage(BasePage):

    context='im home page'


    #banner
    @property
    def home_banner(self):
        return  self.base_find_elements(By.XPATH,)

    #获取有多少Banner广告  ;这里获取的页面的元素属性，命名还是一个el开头。返回的是一个元素，而不是xpath,稍作修改
    @property
    def el_Banner(self):
        return self.base_find_elements(By.XPATH,"//android.widget.ImageView[contains(@resource-id,'com.quarkfinance.ufo:id/image_indicator')]")



    @property
    def el_my_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'我的')]")



    """

    """

    # 根据传入的ID 点击对应的Banner index
    def banner_click(self, id=2):
        try:
            time.sleep(2.5*(id-1))
            self.el_Banner[id].click()
            time.sleep(0.5)
            self.saveScreenshot('banner_click')
            return BannerPages(self.driver)
        except Exception,e:
            self.logger.info('HomePage | Exception  is %s %s'%e %(sys._getframe().f_back.f_lineno))
            self.saveScreenshot('banner_click')
