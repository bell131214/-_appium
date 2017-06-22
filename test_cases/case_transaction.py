#coding=utf-8

import unittest,sys
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver
from functions.appium_init import *
from pages.entry_page import Entry_page

class Transaction(InterfaceCase):
    """交易记录模块验证"""

    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger = self.inital.logger


    def test_transaction_list(self):
        """交易记录-交易列表数据验证"""
        #mytraderecordpage=self.into_transaction()

        entry_page = Entry_page(self.driver)
        mytradeRecordPage = entry_page.open_my_tradeRecord_page()

       # time.sleep(2)
        trade_list = mytradeRecordPage.logic_trade_list()
        # 查询DB 获得理财中第一个理财的合同编号
        sql = Exce_SQLserver()
        txtinvestapply = sql.execSql_getList("SELECT  top 1 new_txtinvestapply from new_tradedetailBase WHERE new_account = '24004F6C-7C08-E711-80C9-00155D01F903'  ORDER BY new_paydate DESC")
       # print  txtinvestapply[0][0]
        #print  trade_list[0]
        sql = Exce_SQLserver()
        paymentno = sql.execSql_getList("SELECT top 1  new_paymentno from new_tradedetailBase WHERE new_account = '24004F6C-7C08-E711-80C9-00155D01F903'  ORDER BY new_paydate DESC")
        #print  paymentno[0][0]
        #print trade_list[1]

        entry_page.saveScreenshot('transaction_list')
        self.assertEquals(trade_list[0],txtinvestapply[0][0])
        self.assertEquals(trade_list[1], paymentno[0][0])

    def test_transaction_consultation(self):
        """交易记录-咨询消息验证"""
        "14114444144"

        entry_page=Entry_page(self.driver)
        mytradeRecordPage=entry_page.open_my_tradeRecord_page()
        mytradeRecordPage.el_trade_Consultation_btn.click()
        mytradeRecordPage.el_trade_Consultation_list[0].click()
        #time.sleep(2)
        title=mytradeRecordPage.logic_get_inquiry_no_test()

        entry_page.saveScreenshot('transaction_consultation')
        #断言
        self.assertIsNotNone(title)


    def test_payment_record(self):
        """交易记录-回款记录验证"""

        entry_page = Entry_page(self.driver,phone="14454839876",pwd="qwe123")
        mytradeRecordPage = entry_page.open_my_tradeRecord_page()






    def tearDown(self):
        self.driver.quit()

        "14454839876 qwe123  回款成功"
        "14454635718 qwe123  回款成功"


if __name__ == '__main__':
    Init()
    unittest.main(verbosity=2)
