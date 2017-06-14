#coding=utf-8

import unittest,sys,datetime
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver
from functions.appium_init import *
from pages.my_invset_record_page import MyAssetDetailsPage
from functions.BasePage import BasePage
from pages.entry_page import Entry_page


class InvestRecord(InterfaceCase):

    """投资记录模块验证"""


    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger = self.inital.logger


    def test_home_financial(self):
        "登录状态-首页进入资产详情"
        entry_page=Entry_page(self.driver)
        homepage=entry_page.open_login_home_page()
        time.sleep(2)
        myInvsetRecorePage=homepage.logic_click_el_invest_img()
        myInvsetRecorePage.el_tv_know.click()
        title_text=myInvsetRecorePage.logic_get_invest_title()

        #断言
        self.assertEquals(title_text,u"投资记录")

        #截图
        entry_page.saveScreenshot('home_financial')


    def test_product_financial(self):
        "登录状态—产品列表进入资产详情"
        entry_page = Entry_page(self.driver)
        productListPage = entry_page.open_login_productList_page()
        myInvsetRecorePage=productListPage.logic_financia_img_click()
        myInvsetRecorePage.el_tv_know.click()
        title_text=myInvsetRecorePage.logic_get_invest_title()
        # 断言
        self.assertEquals(title_text, u"投资记录")
        # 截图
        entry_page.saveScreenshot('home_financial')


    def test_my_financial(self):
        "登录状态-我的列表进入资产详情"
        entry_page = Entry_page(self.driver)
        mypage=entry_page.open_login_my_page()

        myInvsetRecorePage=mypage.logic_financial_img_click()
        myInvsetRecorePage.el_tv_know.click()

        title_text = myInvsetRecorePage.logic_get_invest_title()
        # 断言
        self.assertEquals(title_text, u"投资记录")
        # 截图
        entry_page.saveScreenshot('home_financial')


    def test_financial_list(self):
        "投资记录-理财中列表数据验证"

        entry_page = Entry_page(self.driver)
        myinvsetrecorepage=entry_page.open_my_invset_recore_Page()
        invest_list_value=myinvsetrecorepage.logic_get_invest_value()
        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList("SELECT  top 1 new_product_name,new_name,new_instreststartdate,new_quitdate,new_planmoney,new_planmoney_Base from new_investdetailBase WHERE new_accountname = '24004F6C-7C08-E711-80C9-00155D01F903' AND  new_status=100000000 order BY  new_paidon desc")


        #new_quitdate=(datetime.datetime.strptime(contract_number[0][2], "%Y-%m-%d %H:%M:%S").date()+datetime.timedelta(days = 1))
       # print new_quitdate

        #print  invest_list_value["invest_product_no"]

        entry_page.saveScreenshot('financial_data')
        #断言验证
        self.assertIn(invest_list_value["invest_text_name"],contract_number[0][0])
        self.assertIn(contract_number[0][1],invest_list_value["invest_product_no"])
        #self.assertIn(invest_list_value["start_income_day"], contract_number[0][1])

       # print  invest_list_value.items()





    def test_financial_data(self):
        """投资记录-理财中资产详情数据验证"""

        #allpage=AllPage(self.driver)
        #myinvsetrecorepage=allpage.openpage_myassetDetailsPage(MyAssetDetailsPage(self.driver))
        
        
        myinvsetrecorepage=self.logon()
        
        myinvsetrecorepage.el_my_financial_btn.click()
        time.sleep(1)
        MyAssetDetailsPage=myinvsetrecorepage.logic_invest_list_click()
        
        time.sleep(2)
        #获得资产详情页列表数据，默认获得第index=0 个
        assetdetails_list=MyAssetDetailsPage.get_assetdetails_list()

        pact_title=MyAssetDetailsPage.el_pact_title_btn.text

        #查询DB 获得理财中第一个理财的合同编号
        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList("SELECT  top 1 new_name from new_investdetailBase WHERE new_accountname = '24004F6C-7C08-E711-80C9-00155D01F903' AND  new_status=100000000 order BY  new_paidon desc")

        #查询DB 获得理财产品名称
        sql = Exce_SQLserver()
        product_name = sql.execSql_getList(
            "SELECT top 1  new_product_name from new_investdetailBase WHERE new_accountname = '24004F6C-7C08-E711-80C9-00155D01F903' AND  new_status=100000000 order BY  new_paidon desc")

        #断言
        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('financial_data')
        self.assertIn(assetdetails_list[0],product_name[0][0])
        self.assertIn(contract_number[0][0],assetdetails_list[1])
        self.assertEqual(pact_title,'资产详情')




    def test_quiting_data(self):
        """投资记录-退出中资产详情数据验证"""
        
        #allpage=AllPage(self.driver)
        #myinvsetrecorepage=allpage.openpage_myassetDetailsPage(MyAssetDetailsPage)
        
        myinvsetrecorepage=self.logon(phone='14477650717',pwd='qwe123')
        #点击理财中
        myinvsetrecorepage.el_drop_out_btn.click()
        time.sleep(1)
        MyAssetDetailsPage=myinvsetrecorepage.logic_invest_list_click()
        
        time.sleep(2)
        #获得资产详情页列表数据，默认获得第index=0 个
        assetdetails_list=MyAssetDetailsPage.get_assetdetails_list()

        pact_title=MyAssetDetailsPage.el_pact_title_btn.text

        #查询DB 获得理财中第一个理财的合同编号
        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList("SELECT  top 1 new_name from new_investdetailBase WHERE new_accountname = '331C4E9C-D93A-E711-80D3-00155D02B414' AND  new_status=100000003 order BY  new_instreststartdate desc")

        #查询DB 获得理财产品名称
        sql = Exce_SQLserver()
        product_name = sql.execSql_getList(
            "SELECT top 1  new_product_name from new_investdetailBase WHERE new_accountname = '331C4E9C-D93A-E711-80D3-00155D02B414' AND  new_status=100000003 order BY  new_instreststartdate desc")

        #断言

        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('quiting_data')
        self.assertIn(assetdetails_list[0],product_name[0][0])
        self.assertIn(contract_number[0][0],assetdetails_list[1])
        self.assertEqual(pact_title,'资产详情')


    def test_Exited_data(self):
        """投资记录-已退出资产详情数据验证"""
        
        #allpage=AllPage(self.driver)
        #myinvsetrecorepage=allpage.openpage_myassetDetailsPage(MyAssetDetailsPage)
        
        myinvsetrecorepage=self.logon(phone='17712345606',pwd='qwe123')
        #点击理财中
        myinvsetrecorepage.el_exited_btn.click()
        
        time.sleep(1)
        MyAssetDetailsPage=myinvsetrecorepage.logic_invest_list_click()
        
        time.sleep(1)
        #获得资产详情页列表数据，默认获得第index=0 个
        assetdetails_list=MyAssetDetailsPage.get_assetdetails_list()

        pact_title=MyAssetDetailsPage.el_pact_title_btn.text

        #查询DB 获得理财中第一个理财的合同编号
        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList("SELECT  top 1 new_name from new_investdetailBase WHERE new_accountname = 'F86EEE35-2940-E711-80D3-00155D02B414' AND  new_status=100000002 order BY  new_instreststartdate desc ")

        #查询DB 获得理财产品名称
        sql = Exce_SQLserver()
        product_name = sql.execSql_getList(
            "SELECT top 1  new_product_name from new_investdetailBase WHERE new_accountname = 'F86EEE35-2940-E711-80D3-00155D02B414' AND  new_status=100000002 order BY  new_instreststartdate desc")

        #断言
        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('Exited_data')
        self.assertIn(assetdetails_list[0],product_name[0][0])
        self.assertIn(contract_number[0][0],assetdetails_list[1])
        self.assertEqual(pact_title,'资产详情')
        
        

    def logon(self,phone='14488888098',pwd='qwe123'):
        
        #myinvsetrecorepage =AllPage.openpage(myinvsetrecorepage)
        
        startupPage = StartupPage(self.driver)
        homepage = startupPage.page_swipe()
        loginPage = homepage.logic_link_login_page()
        homepage = loginPage.logic_login(phone,pwd)

        mypage = homepage.click_el_my_btn()
        mypage.el_tv_know.click()
        myinvsetrecorepage=mypage.click_my_investmentRecord()
        myinvsetrecorepage.el_tv_know.click()
        return  myinvsetrecorepage


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    "月月付息 17712345602 qwe123"
