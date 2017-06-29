#coding:utf-8
import sys,unittest,time
sys.path.append("..")
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from pages.converged_page import ConvergedPage
from functions.sqlServerJDBC import Exce_SQLserver


class BuyProductScriptGreenHand(InterfaceCase):

    def setUp(self):
        self.logger=self.inital.logger

    # @unittest.skip('skip')
    def test_buy_greenHand(self):
        '''购买新手标脚本，和buy_prodouct_info.xlsx数据源对应'''

        user_phone = self.inital.buyProduct_info['greenHand']['phone']
        pwd = self.inital.buyProduct_info['greenHand']['pwd']
        amount = self.inital.buyProduct_info['greenHand']['amount']
        times = self.inital.buyProduct_info['greenHand']['times']
        exec_flag = self.inital.buyProduct_info['greenHand']['exec']
        load_create = self.inital.buyProduct_info['greenHand']['load_create']

        if amount=="" or times=="" or exec_flag=="" or load_create=="":
            self.logger.info("BuyProductScriptGreenHand.test_buy_greenHand: buy_info excel parms is wrong!")
            return "buy_info excel parms is wrong!"


        elif exec_flag=='N' or times=='0':
            self.logger.info('BuyProductScriptGreenHand.test_buy_greenHand: do not buy product greenHand!')
            return "do not buy product greenHand!"


        for i in xrange(int(times)):
            try:

                if load_create == "Y" and (user_phone == "" or pwd == ""):
                    self.logger.info(
                        "BuyProductScriptGreenHand.test_buy_greenHand: user_phone pwd value can not be null!")
                    return "BuyProductScriptGreenHand.test_buy_greenHand: user_phone pwd value can not be null!"

                elif load_create == 'N':


                    self.driver = self.inital.get_driver()
                    convergedPage = ConvergedPage(self.driver)
                    user_phone, pwd = convergedPage.register_customer()


                self.driver = self.inital.get_driver()
                startupPage = StartupPage(self.driver)
                homePage = startupPage.page_swipe()
                loginPage = homePage.logic_link_login_page()
                homePage = loginPage.logic_login(user_phone, pwd)
                # 点击一次理财产品元素，过滤蒙层
                homePage.el_product_btn.click()
                time.sleep(0.5)
                productListPage = homePage.logic_link_product()

                productGreenHandPage = productListPage.logic_link_greenHand()

                buyInsertMoneyPage = productGreenHandPage.logic_link_buy()

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

                self.logger.info("BuyProductScriptGreenHand.test_buy_greenHand:run {one} time;"
                                 "phone is {two};"
                                 "pwd is {three};"
                                 "product is {four};"
                                 "amount is {five}".format(one=(i+1),two=user_phone,three=pwd,four=sql_productNo,five=sql_amount))
            except Exception as e:
                self.logger.info("test_buy_greenHand failed!"+str(e))
            finally:
                self.driver.quit()




if __name__=="__main__":
    print range(4)