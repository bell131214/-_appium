#coding:utf-8

from functions.BasePage import BasePage
from functions.appium_init import *
from selenium.webdriver.common.by import By

class Private_Offering_Fund_Page(BasePage):
    """私募预约"""



    #私募预约列表
    @property
    def el_private_fund_list(self):
        return self.base_find_elements(By.ID, "com.quarkfinance.ufo:id/item_view")

    #首次进入弹窗
    @property
    def el_Popup_btn(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/text_confirm_btn")

