#coding=utf-8
from functions.HTMLTestRunner1 import  *
# from functions.appium_init import Initialization
from appium_init import *
import os
import GetHtml


class exec_sutiecase():


    def __init__(self):
        # path = Initialization()
        self.result = appium_init.inital.project_path + "\\result\\"
        # 获取系统当前时间
        self.now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        self.day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # 定义个报告存放路径，支持相对路径
        self.tdresult = self.result + self.day


        # appium_init.inital.result_path=self.tdresult



    def exec_cases(self,test_case):

        if os.path.exists(self.tdresult):
            filename = self.tdresult +"\\" + self.now + "_result.html"
            mail_name = self.tdresult + "\\" + self.now + "_send_mail.html"
            fp = file(filename, 'wb')
            fp1 = file(mail_name, 'wb')

            # 定义测试报告

            runner = HTMLTestRunner(stream=fp, title=u'quark—UFO自动化测试报告', description=u'用例详情：',verbosity=2)


            # 运行测试用例
            a=runner.run(test_case)
            startTime = datetime.datetime.now()
            startTime = str(startTime)[:19]

            GetHtml.get_html(fp1, startTime, a.success_count, a.failure_count, a.error_count)
            fp.close()  # 关闭报告文件
            fp1.close()

        else:
            os.mkdir(self.tdresult)
            filename = self.tdresult + "\\" + self.now + "_result.html"
            mail_name = self.tdresult + "\\" + self.now + "_send_mail.html"
            fp = file(filename, 'wb')
            fp1 = file(mail_name, 'wb')
            # 定义测试报告
            runner = HTMLTestRunner(stream=fp, title=u'quark—UFO自动化测试报告', description=u'用例详情：',verbosity=2)

            # 运行测试用例
            a=runner.run(test_case)

            startTime = datetime.datetime.now()
            startTime = str(startTime)[:19]
            GetHtml.get_html(fp1, startTime,a.success_count, a.failure_count, a.error_count)
            fp.close()  # 关闭报告文件
            fp1.close()
