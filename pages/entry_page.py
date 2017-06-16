#coding:utf-8
from pages.my_page import MyPage
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from pages.banner_pages import BannerPages
from functions.appium_init import *
from pages.product_list_page import ProductListPage
from pages.news_page import NewsPage
from pages.my_invset_record_page import MyInvsetRecorePage
from pages.startup_page import StartupPage
from pages.my_page import MyPage
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Entry_page(BasePage):
    """
        启动入口paga,将APP中所有page入口整合在一起
    """

    """
    open_start_home_page  首次启动APP首页
    open_login_page  登录页
    open_login_home_page 登录状态首页
    open_login_my_page  登录状态个人信息页
    open_my_assetDetails_page 资产详情
    
    """


    def open_start_home_page(self):
        startupPage = StartupPage(self.driver)
        homepage = startupPage.page_swipe()
        return homepage


    def open_login_page(self):
        homepage=self.open_start_home_page()
        loginPage=homepage.logic_link_login_page()

        return loginPage

    def open_login_home_page(self):
        loginPage=self.open_login_page()
        homepage = loginPage.logic_login(self.phone,self.pwd)
        return homepage


    def open_login_my_page(self):
        homepage=self.open_login_home_page()
        mypage = homepage.click_el_my_btn()
        mypage.el_tv_know.click()
        return mypage



    #登录状态进去产品列表
    def open_login_productList_page(self):
        homepage = self.open_login_home_page()
        productListPage=homepage.logic_link_product()
        return  productListPage




        #登录状态进入投资记录页面
    def open_my_invset_recore_Page(self):
        mypage=self.open_login_my_page()
        myinvsetrecorepage = mypage.click_my_investmentRecord()
        myinvsetrecorepage.el_tv_know.click()
        return myinvsetrecorepage

        #退出中月月付息收益明细
    def open_My_Invest_Profit_Detailed_page(self):
        self.open_my_assetDetails_quiting_page()




        #登录状态，理财中资产详情
    def open_my_assetDetails_page(self):
        myinvsetrecorepage=self.open_my_invset_recore_Page()
        myAssetDetailsPage=myinvsetrecorepage.logic_invest_list_click()
        return myAssetDetailsPage

    # 登录状态，退出中资产详情
    def open_my_assetDetails_quiting_page(self):
        myinvsetrecorepage = self.open_my_invset_recore_Page()
        myinvsetrecorepage.el_drop_out_btn.click()
        time.sleep(1.5)
        myAssetDetailsPage = myinvsetrecorepage.logic_invest_list_click()
        return myAssetDetailsPage

    #登录状态，已退出资产详情
    def open_my_assetDetails_Exited_page(self):
        myinvsetrecorepage = self.open_my_invset_recore_Page()
        myinvsetrecorepage.el_exited_btn.click()
        time.sleep(1.5)
        myAssetDetailsPage = myinvsetrecorepage.logic_invest_list_click()
        return myAssetDetailsPage


        #登录状态，理财中资产详情合同页面
    def open_Electronic_contract_page(self):
        myAssetDetailsPage=self.open_my_assetDetails_page()
        time.sleep(1)
        electronic_contract_page=myAssetDetailsPage.click_pact()
        return  electronic_contract_page





