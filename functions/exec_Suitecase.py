#coding=utf-8
from functions.HTMLTestRunner import  *
# from functions.appium_init import Initialization
from appium_init import *
import os


class exec_sutiecase():


    def __init__(self):
        # path = Initialization()
        self.result = appium_init.inital.get_project_path() + "\\result\\"
        # 获取系统当前时间
        self.now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        self.day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # 定义个报告存放路径，支持相对路径
        self.tdresult = self.result + self.day


    def exec_cases(self,test_case):

        if os.path.exists(self.tdresult):
            filename = self.tdresult +"\\" + self.now + "_result.html"
            fp = file(filename, 'wb')

            # 定义测试报告

            runner = HTMLTestRunner(stream=fp, title=u'hele', description=u'用例详情：')


            # 运行测试用例
            runner.run(test_case)
            fp.close()  # 关闭报告文件
        else:
            os.mkdir(self.tdresult)
            filename = self.tdresult + "\\" + self.now + "_result.html"
            fp = file(filename, 'wb')
            # 定义测试报告
            runner = HTMLTestRunner(stream=fp, title=u'hele', description=u'用例详情：')

            # 运行测试用例
            runner.run(test_case)
            fp.close()  # 关闭报告文件
