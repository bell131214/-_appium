#coding=utf-8
from pages.my_page import MyPage
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *
import time


class BannerPages(BasePage):
    """
    功能：首页 Banner页面的测试
    """

    #获取有多少Banner广告
    @property
    def BannerXpath(self):
        return self.base_find_elements(By.XPATH,"//android.widget.ImageView[contains(@resource-id,'com.quarkfinance.ufo:id/image_indicator')]")

    #定位Banne详情页面的title
    @property
    def child_page_Xpath(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@resource-id,'com.quarkfinance.ufo:id/tb_title')]")

    """
    
    """
    #根据传入的ID 点击对应的Banner index
    def banner_click(self,id=2):
            BasePage.page_swipe(self.driver)
            #self.page_swipe()
            self.BannerXpath[id-1].click()
            time.sleep(0.5)
            self.saveScreenshot('banner_click')
            print self.child_page_Xpath.text
            return self.child_page_Xpath.text



if __name__ == '__main__':

    Init()
    driver = appium_init.inital.get_driver()
    d = BannerPages(driver)
    d.banner_click()




