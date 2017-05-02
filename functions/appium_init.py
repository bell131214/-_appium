# coding:utf-8
import os,sys,time
#os.chdir('..')
sys.path.append('..')
from appium import webdriver
from configParser import Config
from functions.appium_logging import AppLog
from functions.adbConnon import AndroidDebugBridge
import appium_init

inital=None

class Initialization():
    """docstring for initialization"""

    def __init__(self):
        self.config=Config()
        path_list=os.getcwd().split('\\')
        self.config_path="E:\\quark_work\\config\\appium_config.ini"




        appLog = AppLog()
        self.logger = appLog.logger
        self.logger.info('Initialization | config_path is %s init is complate!' %
                         self.config_path)
        self.adbCall = AndroidDebugBridge()

    def get_project_path(self):
        return self.get_desired_caps()['project_path']

    def get_desired_caps(self):
        desired_caps_config = self.config.get_config(
            'desired_caps', self.config_path)
        # print desired_caps_config
        # self.logger.info('Initialization | loading desired_caps_config')
        # print desired_caps_config
        return desired_caps_config

    # @staticmethod
    def get_cases_info(self, case_ini):

        cases_info = self.config.get_config(case_ini, self.config_path)
        if cases_info != []:
            return cases_info
        else:
            self.logger.info(
                "Initialization | config is Null! plz check information!")

    def get_driver(self):
        """

        :return: driver
        """
        # 通过adb判断设备是否启动
        if self.adbCall.attached_devices():
            desired_caps_config = self.get_desired_caps()
            desired_caps = {}
            desired_caps['platformName'] = desired_caps_config['platformname']
            desired_caps['platformVersion'] = desired_caps_config[
                'platformversion']
            desired_caps['deviceName'] = desired_caps_config['devicename']
            desired_caps['appPackage'] = desired_caps_config['apppackage']
            desired_caps['appActivity'] = desired_caps_config['appactivity']

            time.sleep(1)
            # driver 实例化前，调用adb命令卸载和重新安装应用,保证每次测试用例执行的环境都是干净的
            self.adbCall.call_adb('uninstall ' + desired_caps['appPackage'])
            time.sleep(1)
            self.adbCall.call_adb(
                'install ' + desired_caps_config['project_path'] + "\\app\\" + desired_caps_config['app_name'])
            time.sleep(1)
            # print desired_caps.items()
            driver = webdriver.Remote(
                'http://localhost:4723/wd/hub', desired_caps)

            return driver

        else:
            self.logger.info('Initialization | 设备不存在 ')

class Init():
    def __init__(self):
        appium_init.inital=Initialization()


if __name__ == '__main__':
    if isinstance(appium_init.inital,Initialization)!=True:
        Init()
    print appium_init.inital.get_project_path()
