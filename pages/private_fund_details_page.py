#coding:utf-8

from functions.BasePage import BasePage
from functions.appium_init import *
from selenium.webdriver.common.by import By

class Private_Fund_Details_Page(BasePage):
    "私募详情页"



    @property
    def el_title_text(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/item_view")


    @property
    def el_input_password(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/edit_password")