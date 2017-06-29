#coding:utf-8
import sys,unittest,time
sys.path.append("..")
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from pages.converged_page import ConvergedPage
from functions.sqlServerJDBC import Exce_SQLserver


class BuyProductScriptMonthlyInterest(InterfaceCase):

    def setUp(self):
        self.logger=self.inital.logger

    # @unittest.skip('skip')
    def test_buy_monthly_interest180(self):
        '''购买月月付息180天脚本，和buy_prodouct_info.xlsx数据源对应'''

        user_phone = self.inital.buyProduct_info['monthly_interest180']['phone']
        pwd = self.inital.buyProduct_info['monthly_interest180']['pwd']
        amount = self.inital.buyProduct_info['monthly_interest180']['amount']
        times = self.inital.buyProduct_info['monthly_interest180']['times']
        exec_flag = self.inital.buyProduct_info['monthly_interest180']['exec']
        load_create = self.inital.buyProduct_info['monthly_interest180']['load_create']

        if amount=="" or times=="" or exec_flag=="" or load_create=="":
            self.logger.info("BuyProductScriptMonthlyInterest.test_buy_monthly_interest180: buy_info excel parms is wrong!")
            return "buy_info excel parms is wrong!"


        elif exec_flag=='N' or times=='0':
            self.logger.info('BuyProductScriptMonthlyInterest.test_buy_monthly_interest180: do not buy product monthly_interest180!')
            return "do not buy product monthly_interest180!"

        if load_create=='N':
            self.driver = self.inital.get_driver()
            convergedPage=ConvergedPage(self.driver)
            user_phone,pwd=convergedPage.register_customer()

        elif load_create=="Y" and (user_phone=="" or pwd==""):
            self.logger.info("BuyProductScriptMonthlyInterest.test_buy_monthly_interest180: user_phone pwd value can not be null!")
            return  "BuyProductScriptMonthlyInterest.test_buy_monthly_interest180: user_phone pwd value can not be null!"

        for i in xrange(int(times)):
            try:
                self.driver = self.inital.get_driver()
                startupPage = StartupPage(self.driver)
                homePage = startupPage.page_swipe()
                loginPage = homePage.logic_link_login_page()
                homePage = loginPage.logic_login(user_phone, pwd)
                # 点击一次理财产品元素，过滤蒙层
                homePage.el_product_btn.click()
                time.sleep(0.5)
                productListPage = homePage.logic_link_product()
                productMonthlyInterestPage = productListPage.logic_link_monthly_interest()
                productMonthlyInterestPage.logic_choose_product_type(3)

                buyInsertMoneyPage = productMonthlyInterestPage.logic_link_buy()

                buyConfirmPage = buyInsertMoneyPage.logic_buy_product(amount)
                buyTradeResultPage = buyConfirmPage.logic_confirm_info(pwd)
                time.sleep(20)
                homePage = buyTradeResultPage.logic_link_buy()
                myPage = homePage.logic_buy_my_btn()
                SQL="select top(1) m.new_managemoney,m.new_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" % (
                    user_phone)
                sql_conn = Exce_SQLserver()

                sql_result = sql_conn.execSql_getOne(SQL)
                sql_amount = int(sql_result[0])
                sql_productNo = str(sql_result[1])

                self.logger.info("BuyProductScriptMonthlyInterest.test_buy_monthly_interest180:run {one} time;"
                                 "phone is {two};"
                                 "pwd is {three};"
                                 "product is {four};"
                                 "amount is {five}".format(one=(i+1),two=user_phone,three=pwd,four=sql_productNo,five=sql_amount))
            except Exception as e:
                self.logger.info("buy_monthly_interest180 failed!"+str(e))
            finally:
                self.driver.quit()

    # @unittest.skip('skip')
    def test_buy_monthly_interest360(self):
        '''购买月月付息360天脚本，和buy_prodouct_info.xlsx数据源对应'''

        user_phone = self.inital.buyProduct_info['monthly_interest360']['phone']
        pwd = self.inital.buyProduct_info['monthly_interest360']['pwd']
        amount = self.inital.buyProduct_info['monthly_interest360']['amount']
        times = self.inital.buyProduct_info['monthly_interest360']['times']
        exec_flag = self.inital.buyProduct_info['monthly_interest360']['exec']
        load_create = self.inital.buyProduct_info['monthly_interest360']['load_create']

        if amount=="" or times=="" or exec_flag=="" or load_create=="":
            self.logger.info("BuyProductScriptMonthlyInterest.test_buy_monthly_interest360: buy_info excel parms is wrong!")
            return "buy_info excel parms is wrong!"


        elif exec_flag=='N' or times=='0':
            self.logger.info('BuyProductScriptMonthlyInterest.test_buy_monthly_interest360: do not buy product monthly_interest360!')
            return "do not buy product monthly_interest360!"

        if load_create=='N':
            self.driver = self.inital.get_driver()
            convergedPage=ConvergedPage(self.driver)
            user_phone,pwd=convergedPage.register_customer()

        elif load_create=="Y" and (user_phone=="" or pwd==""):
            self.logger.info("BuyProductScriptMonthlyInterest.test_buy_monthly_interest360: user_phone pwd value can not be null!")
            return  "BuyProductScriptMonthlyInterest.test_buy_monthly_interest360: user_phone pwd value can not be null!"

        for i in xrange(int(times)):
            try:
                self.driver = self.inital.get_driver()
                startupPage = StartupPage(self.driver)
                homePage = startupPage.page_swipe()
                loginPage = homePage.logic_link_login_page()
                homePage = loginPage.logic_login(user_phone, pwd)
                # 点击一次理财产品元素，过滤蒙层
                homePage.el_product_btn.click()
                time.sleep(0.5)
                productListPage = homePage.logic_link_product()
                productMonthlyInterestPage = productListPage.logic_link_monthly_interest()
                productMonthlyInterestPage.logic_choose_product_type(4)

                buyInsertMoneyPage = productMonthlyInterestPage.logic_link_buy()

                buyConfirmPage = buyInsertMoneyPage.logic_buy_product(amount)
                buyTradeResultPage = buyConfirmPage.logic_confirm_info(pwd)
                time.sleep(20)
                homePage = buyTradeResultPage.logic_link_buy()
                myPage = homePage.logic_buy_my_btn()
                SQL="select top(1) m.new_managemoney,m.new_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" % (
                    user_phone)
                sql_conn = Exce_SQLserver()

                sql_result = sql_conn.execSql_getOne(SQL)
                sql_amount = int(sql_result[0])
                sql_productNo = str(sql_result[1])

                self.logger.info("BuyProductScriptMonthlyInterest.test_buy_monthly_interest360:run {one} time;"
                                 "phone is {two};"
                                 "pwd is {three};"
                                 "product is {four};"
                                 "amount is {five}".format(one=(i+1),two=user_phone,three=pwd,four=sql_productNo,five=sql_amount))
            except Exception as e:
                self.logger.info("buy_monthly_interest360 failed!"+str(e))
            finally:
                self.driver.quit()



if __name__=="__main__":
    print range(4)