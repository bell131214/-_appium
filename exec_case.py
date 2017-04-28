#coding:utf-8
from functions.load_case import LoadCase
import unittest

if __name__=='__main__':
    testSuite = LoadCase.get_cases('testcase2')
    if testSuite != None:
        runner = unittest.TextTestRunner()
        runner.run(testSuite)