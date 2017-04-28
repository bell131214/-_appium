#coding:utf-8
import logging
from datetime import  datetime
import os
# print os.getcwd()

class AppLog():

    def __init__(self):
        time=datetime.now().strftime("%Y_%m_%d %H-%M-%S")
        path="D:\\quarkscript\\quarkUFO\\log"
        log_name=path+"\\appium "+time+".log"
        #print log_name

        self.logger=logging.Logger('appium_logger')

        #创建写日志句柄
        fh1=logging.FileHandler(log_name)
        fh1.setLevel(logging.INFO)

        #创建控制台输出句柄
        fh2=logging.StreamHandler()
        fh2.setLevel(logging.DEBUG)

        #定义日志输出规则
        formatter=logging.Formatter('%(levelname)s| %(asctime)s |%(message)s')

        #日志句柄绑定规则
        fh1.setFormatter(formatter)
        fh2.setFormatter(formatter)

        #给logger添加句柄
        self.logger.addHandler(fh1)
        self.logger.addHandler(fh2)









if __name__ == '__main__':
    log=AppLog()
