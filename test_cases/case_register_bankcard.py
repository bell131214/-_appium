#coding:utf-8
import sys,unittest,time
sys.path.append("..")
from functions.interface_case import InterfaceCase
from pages.converged_page import ConvergedPage
from pages.startup_page import StartupPage
from functions.random_data import Create_Data

class RegisterBankCard(InterfaceCase):
    '''绑卡相关测试集'''

    def setUp(self):
        self.logger=self.inital.logger
        self.driver=self.inital.get_driver()

    # @unittest.skip('skip')
    def test_register_JS(self):
        '''绑定建行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('JS')
        self.logger.info('run case:RegisterBankCard.test_register_JS user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"中国建设银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_JS')


    # @unittest.skip('skip')
    def test_register_GF(self):
        '''绑定广发卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('GF')
        self.logger.info('run case:RegisterBankCard.test_register_GF user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"广发银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_GF')

    # @unittest.skip('skip')
    def test_register_JT(self):
        '''绑定交通卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('JT')
        self.logger.info('run case:RegisterBankCard.test_register_JT user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"交通银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_JT')

    # @unittest.skip('skip')
    def test_register_PA(self):
        '''绑定平安银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('PA')
        self.logger.info('run case:RegisterBankCard.test_register_PA user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"平安银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_PA')

    # @unittest.skip('skip')
    def test_register_ZS(self):
        '''绑定招商银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('ZS')
        self.logger.info('run case:RegisterBankCard.test_register_ZS user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"招商银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_ZS')

    # @unittest.skip('skip')
    def test_register_ZX(self):
        '''绑定中信银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('ZX')
        self.logger.info('run case:RegisterBankCard.test_register_ZX user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"中信银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_ZX')

    # @unittest.skip('skip')
    def test_register_ZG(self):
        '''绑定中国银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('ZG')
        self.logger.info('run case:RegisterBankCard.test_register_ZG user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"中国银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_ZG')

    # @unittest.skip('skip')
    def test_register_NY(self):
        '''绑定中国农业银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('NY')
        self.logger.info('run case:RegisterBankCard.test_register_NY user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"中国农业银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_NY')

    # @unittest.skip('skip')
    def test_register_MS(self):
        '''绑定中国民生银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('MS')
        self.logger.info('run case:RegisterBankCard.test_register_MS user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"中国民生银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_MS')

    # @unittest.skip('skip')
    def test_delete_bankcard_JS(self):
        '''删除建设银行测试用例'''
        user_name='ufo83'
        user_phone='14488888083'
        user_pwd='123456q'
        cardNO=Create_Data.get_bank_card_js()
        bankType='JS'

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,user_pwd)

        myPage = homePage.click_el_my_btn()
        # 点击浮层
        time.sleep(1)
        myPage.el_tv_know.click()

        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_bankCard_INFO(user_name,user_phone,cardNO,bankType)
        bankName=myBankCardPage.el_bankName_listOne.text
        self.logger.info('run case:RegisterBankCard.test_delete_bankcard_JS bankName={one}  cardNo={two}'.format(one=bankName,two=cardNO))
        self.assertEqual(bankName,u'中国建设银行')

        bankCardInfoPage=myBankCardPage.logic_link_bankcardInfo_page()
        myBankCardPage=bankCardInfoPage.logic_delete_bankcard(user_pwd)
        myBankCardPage.saveScreenshot("RegisterBankCard.test_delete_bankcard_JS")
        self.assertEqual(myBankCardPage.el_bankcard_js, None)

    # @unittest.skip('skip')
    def test_delete_bankcard_GF(self):
        '''删除广发银行测试用例'''
        user_name='ufo83'
        user_phone='14488888083'
        user_pwd='123456q'
        cardNO=Create_Data.get_bank_card_gf()
        bankType='GF'

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,user_pwd)

        myPage = homePage.click_el_my_btn()
        # 点击浮层
        time.sleep(1)
        myPage.el_tv_know.click()

        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_bankCard_INFO(user_name,user_phone,cardNO,bankType)
        bankName=myBankCardPage.el_bankName_listOne.text
        self.logger.info('run case:RegisterBankCard.test_delete_bankcard_GF bankName={one}  cardNo={two}'.format(one=bankName,two=cardNO))
        self.assertEqual(bankName,u'广发银行')

        bankCardInfoPage=myBankCardPage.logic_link_bankcardInfo_page()
        myBankCardPage=bankCardInfoPage.logic_delete_bankcard(user_pwd)
        myBankCardPage.saveScreenshot("RegisterBankCard.test_delete_bankcard_GF")
        self.assertEqual(myBankCardPage.el_bankcard_gf, None)

    @unittest.skip('skip')
    def test_delete_bankcard_JT(self):
        '''删除交通银行测试用例'''
        user_name='ufo83'
        user_phone='14488888083'
        user_pwd='123456q'
        cardNO=Create_Data.get_bank_card_jt()
        bankType='JT'

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,user_pwd)

        myPage = homePage.click_el_my_btn()
        # 点击浮层
        time.sleep(1)
        myPage.el_tv_know.click()

        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_bankCard_INFO(user_name,user_phone,cardNO,bankType)
        bankName=myBankCardPage.el_bankName_listOne.text
        self.logger.info('run case:RegisterBankCard.test_delete_bankcard_JT bankName={one}  cardNo={two}'.format(one=bankName,two=cardNO))
        self.assertEqual(bankName,u'交通银行')

        bankCardInfoPage=myBankCardPage.logic_link_bankcardInfo_page()
        myBankCardPage=bankCardInfoPage.logic_delete_bankcard(user_pwd)
        myBankCardPage.saveScreenshot("RegisterBankCard.test_delete_bankcard_JT")
        self.assertEqual(myBankCardPage.el_bankcard_jt, None)

    @unittest.skip('skip')
    def test_delete_bankcard_PA(self):
        '''删除平安银行测试用例'''
        user_name='ufo83'
        user_phone='14488888083'
        user_pwd='123456q'
        cardNO=Create_Data.get_bank_card_pa()
        bankType='PA'

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,user_pwd)

        myPage = homePage.click_el_my_btn()
        # 点击浮层
        time.sleep(1)
        myPage.el_tv_know.click()

        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_bankCard_INFO(user_name,user_phone,cardNO,bankType)
        bankName=myBankCardPage.el_bankName_listOne.text
        self.logger.info('run case:RegisterBankCard.test_delete_bankcard_PA bankName={one}  cardNo={two}'.format(one=bankName,two=cardNO))
        self.assertEqual(bankName,u'平安银行')

        bankCardInfoPage=myBankCardPage.logic_link_bankcardInfo_page()
        myBankCardPage=bankCardInfoPage.logic_delete_bankcard(user_pwd)
        myBankCardPage.saveScreenshot("RegisterBankCard.test_delete_bankcard_PA")
        self.assertEqual(myBankCardPage.el_bankcard_pa, None)

    # @unittest.skip('skip')
    def test_delete_bankcard_ZS(self):
        '''删除招商银行测试用例'''
        user_name='ufo83'
        user_phone='14488888083'
        user_pwd='123456q'
        cardNO=Create_Data.get_bank_card_zs()
        bankType='ZS'

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,user_pwd)

        myPage = homePage.click_el_my_btn()
        # 点击浮层
        time.sleep(1)
        myPage.el_tv_know.click()

        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_bankCard_INFO(user_name,user_phone,cardNO,bankType)
        bankName=myBankCardPage.el_bankName_listOne.text
        self.logger.info('run case:RegisterBankCard.test_delete_bankcard_ZS bankName={one}  cardNo={two}'.format(one=bankName,two=cardNO))
        self.assertEqual(bankName,u'招商银行')

        bankCardInfoPage=myBankCardPage.logic_link_bankcardInfo_page()
        myBankCardPage=bankCardInfoPage.logic_delete_bankcard(user_pwd)
        myBankCardPage.saveScreenshot("RegisterBankCard.test_delete_bankcard_ZS")
        self.assertEqual(myBankCardPage.el_bankcard_zs, None)

    # @unittest.skip('skip')
    def test_delete_bankcard_ZX(self):
        '''删除中信银行测试用例'''
        user_name='ufo83'
        user_phone='14488888083'
        user_pwd='123456q'
        cardNO=Create_Data.get_bank_card_zx()
        bankType='ZX'

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,user_pwd)

        myPage = homePage.click_el_my_btn()
        # 点击浮层
        time.sleep(1)
        myPage.el_tv_know.click()

        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_bankCard_INFO(user_name,user_phone,cardNO,bankType)
        bankName=myBankCardPage.el_bankName_listOne.text
        self.logger.info('run case:RegisterBankCard.test_delete_bankcard_ZX bankName={one}  cardNo={two}'.format(one=bankName,two=cardNO))
        self.assertEqual(bankName,u'中信银行')

        bankCardInfoPage=myBankCardPage.logic_link_bankcardInfo_page()
        myBankCardPage=bankCardInfoPage.logic_delete_bankcard(user_pwd)
        myBankCardPage.saveScreenshot("RegisterBankCard.test_delete_bankcard_ZX")
        self.assertEqual(myBankCardPage.el_bankcard_zx, None)

    # @unittest.skip('skip')
    def test_delete_bankcard_ZG(self):
        '''删除中国银行测试用例'''
        user_name='ufo83'
        user_phone='14488888083'
        user_pwd='123456q'
        cardNO=Create_Data.get_bank_card_zg()
        bankType='ZG'

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,user_pwd)

        myPage = homePage.click_el_my_btn()
        # 点击浮层
        time.sleep(1)
        myPage.el_tv_know.click()

        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_bankCard_INFO(user_name,user_phone,cardNO,bankType)
        bankName=myBankCardPage.el_bankName_listOne.text
        self.logger.info('run case:RegisterBankCard.test_delete_bankcard_ZG bankName={one}  cardNo={two}'.format(one=bankName,two=cardNO))
        self.assertEqual(bankName,u'中国银行')

        bankCardInfoPage=myBankCardPage.logic_link_bankcardInfo_page()
        myBankCardPage=bankCardInfoPage.logic_delete_bankcard(user_pwd)
        myBankCardPage.saveScreenshot("RegisterBankCard.test_delete_bankcard_ZG")
        self.assertEqual(myBankCardPage.el_bankcard_zg, None)

    # @unittest.skip('skip')
    def test_delete_bankcard_NY(self):
        '''删除中国农业银行测试用例'''
        user_name='ufo83'
        user_phone='14488888083'
        user_pwd='123456q'
        cardNO=Create_Data.get_bank_card_ny()
        bankType='NY'

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,user_pwd)

        myPage = homePage.click_el_my_btn()
        # 点击浮层
        time.sleep(1)
        myPage.el_tv_know.click()

        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_bankCard_INFO(user_name,user_phone,cardNO,bankType)
        bankName=myBankCardPage.el_bankName_listOne.text
        self.logger.info('run case:RegisterBankCard.test_delete_bankcard_NY bankName={one}  cardNo={two}'.format(one=bankName,two=cardNO))
        self.assertEqual(bankName,u'中国农业银行')

        bankCardInfoPage=myBankCardPage.logic_link_bankcardInfo_page()
        myBankCardPage=bankCardInfoPage.logic_delete_bankcard(user_pwd)
        myBankCardPage.saveScreenshot("RegisterBankCard.test_delete_bankcard_NY")
        self.assertEqual(myBankCardPage.el_bankcard_ny, None)

    def test_delete_bankcard_MS(self):
        '''删除中国民生银行测试用例'''
        user_name='ufo83'
        user_phone='14488888083'
        user_pwd='123456q'
        cardNO=Create_Data.get_bank_card_ms()
        bankType='MS'

        startupPage=StartupPage(self.driver)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,user_pwd)

        myPage = homePage.click_el_my_btn()
        # 点击浮层
        time.sleep(1)
        myPage.el_tv_know.click()

        myBankCardPage=myPage.logic_my_bankCard_click()
        registerAddCardPage=myBankCardPage.logic_addCard_click()
        myBankCardPage=registerAddCardPage.logic_insert_bankCard_INFO(user_name,user_phone,cardNO,bankType)
        bankName=myBankCardPage.el_bankName_listOne.text
        self.logger.info('run case:RegisterBankCard.test_delete_bankcard_MS bankName={one}  cardNo={two}'.format(one=bankName,two=cardNO))
        self.assertEqual(bankName,u'中国民生银行')

        bankCardInfoPage=myBankCardPage.logic_link_bankcardInfo_page()
        myBankCardPage=bankCardInfoPage.logic_delete_bankcard(user_pwd)
        myBankCardPage.saveScreenshot("RegisterBankCard.test_delete_bankcard_MS")
        self.assertEqual(myBankCardPage.el_bankcard_ms,None)


    def tearDown(self):
        self.driver.quit()