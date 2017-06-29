#coding:utf-8
import sys,unittest,time
sys.path.append("..")
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from pages.converged_page import ConvergedPage
from functions.sqlServerJDBC import Exce_SQLserver


class BuyProductScriptBeauti(InterfaceCase):

    def setUp(self):
        self.logger=self.inital.logger

    # @unittest.skip('skip')
    def test_buy_beauti(self):
        '''购买夸客美丽脚本，和buy_prodouct_info.xlsx数据源对应'''

        user_phone = self.inital.buyProduct_info['beauti']['phone']
        pwd = self.inital.buyProduct_info['beauti']['pwd']
        amount = self.inital.buyProduct_info['beauti']['amount']
        times = self.inital.buyProduct_info['beauti']['times']
        exec_flag = self.inital.buyProduct_info['beauti']['exec']
        load_create = self.inital.buyProduct_info['beauti']['load_create']

        if amount=="" or times=="" or exec_flag=="" or load_create=="":
            self.logger.info("BuyProductScriptBeauti.test_buy_beauti: buy_info excel parms is wrong!")
            return "buy_info excel parms is wrong!"


        elif exec_flag=='N' or times=='0':
            self.logger.info('BuyProductScriptBeauti.test_buy_beauti: do not buy product beauti')
            return "do not buy product beauti!"


        for i in xrange(int(times)):
            try:

                if load_create == "Y" and (user_phone == "" or pwd == ""):
                    self.logger.info(
                        "BuyProductScriptBeauti.test_buy_beauti: user_phone pwd value can not be null!")
                    return "BuyProductScriptBeauti.test_buy_beauti: user_phone pwd value can not be null!"

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
                time.sleep(3)
                productListPage.swipe_to_up()

                productBeautiPage = productListPage.logic_link_beauti()

                buyInsertMoneyPage = productBeautiPage.logic_link_buy()

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

                self.logger.info("BuyProductScriptBeauti.test_buy_beauti:run {one} time;"
                                 "phone is {two};"
                                 "pwd is {three};"
                                 "product is {four};"
                                 "amount is {five}".format(one=(i+1),two=user_phone,three=pwd,four=sql_productNo,five=sql_amount))
            except Exception as e:
                self.logger.info("test_buy_beauti failed!"+str(e))
            finally:
                self.driver.quit()




if __name__=="__main__":
    print range(4)