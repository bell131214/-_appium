#coding:utf-8
#from pages.base_page import BasePage
from pages.my_page import MyPage
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.banner_pages import BannerPages
import time


class HomePage(BasePage):

    context='im home page'


    #banner
    @property
    def home_banner(self):
        return  self.base_find_elements(By.XPATH,)

    #获取有多少Banner广告
    @property
    def BannerXpath(self):
        return self.base_find_elements(By.XPATH,"//android.widget.ImageView[contains(@resource-id,'com.quarkfinance.ufo:id/image_indicator')]")

    #定位Banne详情页面的title
    @property
    def child_page_Xpath(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@resource-id,'com.quarkfinance.ufo:id/tb_title')]")


    #定位器:首页
    @property
    def home_btn(self):
        return self.by_name(u'首页')

    #定位器：我的
    @property
    def my_btn(self):
        return self.by_name(u'我的')

    #定位器：产品列表
    @property
    def product_btn(self):
        return self.by_name(u'产品列表')



    #逻辑key_word:跳转到"我的"页面
    def my_page(self):
        self.my_btn.click()
        return MyPage(self.driver)

    #逻辑key_word:跳转到"产品列表"页面
    def product_page(self):
        self.product_btn.click()

    """

    """

    # 根据传入的ID 点击对应的Banner index
    def banner_click(self, id=2):
        # BasePage.page_swipe()
        # self.page_swipe
        time.sleep(3*(id-1))

        self.BannerXpath[id - 1].click()
        time.sleep(0.5)
        self.saveScreenshot('banner_click')

        return BannerPages(self.driver)
       # print self.child_page_Xpath.text
       # return self.child_page_Xpath.text