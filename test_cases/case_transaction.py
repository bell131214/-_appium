#coding=utf-8

import unittest,sys
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver
from functions.appium_init import *
from pages.all_pages import  AllPage
from pages.my_invset_record_page import MyAssetDetailsPage
from functions.BasePage import BasePage

class Transaction(InterfaceCase):
    """交易记录模块验证"""

    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger = self.inital.logger


    def test_transaction_list(self):
        """交易列表数据验证"""
        mytraderecordpage=self.into_transaction()
       # time.sleep(2)
        trade_list = mytraderecordpage.logic_trade_list()
        # 查询DB 获得理财中第一个理财的合同编号
        sql = Exce_SQLserver()
        txtinvestapply = sql.execSql_getList("SELECT  top 1 new_txtinvestapply from new_tradedetailBase WHERE new_account = '24004F6C-7C08-E711-80C9-00155D01F903'  ORDER BY new_paydate DESC")
       # print  txtinvestapply[0][0]
        #print  trade_list[0]
        sql = Exce_SQLserver()
        paymentno = sql.execSql_getList("SELECT top 1  new_paymentno from new_tradedetailBase WHERE new_account = '24004F6C-7C08-E711-80C9-00155D01F903'  ORDER BY new_paydate DESC")
        #print  paymentno[0][0]
        #print trade_list[1]

        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('transaction_list')
        self.assertEquals(trade_list[0],txtinvestapply[0][0])
        self.assertEquals(trade_list[1], paymentno[0][0])


    def into_transaction(self):
        startupPage = StartupPage(self.driver)
        homepage = startupPage.page_swipe()
        loginPage = homepage.logic_link_login_page()
        homepage = loginPage.logic_login()
        mypage = homepage.click_el_my_btn()
        mypage.el_tv_know.click()
        mytraderecordpage = mypage.logic_my_transactionRecord_btn_click()
        return  mytraderecordpage

    def tearDown(self):
        self.driver.quit()

        "14454839876 qwe123  回款成功"
        "14454635718 qwe123  回款成功"


if __name__ == '__main__':
    unittest.main(verbosity=2)