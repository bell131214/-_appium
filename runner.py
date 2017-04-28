#coding=utf-8

import  unittest,os,time
from functions.exec_Suitecase import exec_sutiecase
from functions.appium_init import Init

case_path="test_cases"
# result = "D:\\CodeWork\\quarkUFO\\result\\"


def Creatsuite():
    #定义单元测试容器
    testunit = unittest.TestSuite()

    #定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern='cases_*.py', top_level_dir=None)

    #将测试用例加入测试容器中
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
        print testunit
    return testunit

test_case = Creatsuite()



if __name__ == '__main__':
    Init()
    exec_result=exec_sutiecase()
    exec_result.exec_cases(test_case)




