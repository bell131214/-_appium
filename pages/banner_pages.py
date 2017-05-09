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

    #定位Banne详情页面的title
    @property
    def child_page_Xpath(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@resource-id,'com.quarkfinance.ufo:id/tb_title')]")







if __name__ == '__main__':
    Init()
    driver = appium_init.inital.get_driver()
    d = BannerPages(driver)





