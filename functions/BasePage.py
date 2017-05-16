#coding=utf-8
import time,os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from functions.appium_init import *
import sys

class BasePage(object):
	"""
	封装关于Appium中操作元素对象的方法
	"""
#new PO
	def __init__(self, driver):
	#	print driver
		self.driver = driver
		self.logger=appium_init.inital.logger


	#根据何乐获取的方法名、方法行数对日志异常修改完善
	def base_find_element(self,locator,value):
		try:
			WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(locator,value).is_displayed())
			return self.driver.find_element(locator,value)
			#return self.driver.find_element(locator,value)
		except NoSuchElementException,e:
			if isinstance(appium_init.inital,Initialization)!=True:
				Init()
			self.logger.info('BasePage | NoSuchElementException error occur at %s;function name is %s;locator is %s %s Exception: %s;'
							 %(sys._getframe().f_back.f_lineno,sys._getframe().f_back.f_code.co_name,locator,value,e))
			self.saveScreenshot(sys._getframe().f_back.f_code.co_name)


	def base_find_elements(self,locator,value):
		try:
			if len(self.driver.find_elements(locator, value)):
				return self.driver.find_elements(locator, value)
		except NoSuchElementException,e:
			if isinstance(appium_init.inital,Initialization)!=True:
				Init()
			self.logger.info('BasePage | NoSuchElementException error occur at %s;function name is %s;locator is %s %s Exception: %s;'
							 %(sys._getframe().f_back.f_lineno,sys._getframe().f_code.co_name,locator,value,e))
			self.saveScreenshot(sys._getframe().f_back.f_code.co_name)





	def get_size(self):
		"""
		获取当前屏幕的分辨率
		:return: int, x*y
		"""
		size = self.driver.get_window_size()
		return size

	def swipe_to_up(self):
		"""
		从下往上滑动
		:return: None
		"""
		window_size = self.get_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

	def swipe_to_down(self):
		"""
		从上往下滑动
		:return: None
		"""
		window_size = self.get_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

	def swipe_to_left(self):
		"""
		从右往左滑动
		:return: None
		"""
		window_size = self.get_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width / 8, height / 2, width * 7 / 8, height / 2, 500)

	def swipe_to_right(self):
		"""
		从左往右滑动
		:return: None
		"""
		window_size = self.get_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width * 7 / 8, height / 2, width / 8, height / 2, 500)

	def reLoadApp(self):
		"""
		重启app
		:return:None
		"""
		self.driver.close_app()
		self.driver.launch_app()

	def longPress(self, x, y, peroid):
		"""
		长按点击操作
		:Args:
		 - x,y： 长按点的坐标
		 - peroid: 多长时间内完成该操作,单位是毫秒

		:Usage:
		 self.longPress(50, 50, 500)
		"""
		self.driver.tap([(x, y)], peroid)



	def pressBackKey(self):
		"""
		按返回键
		"""
		# code码参考Android的官网的keycode
		self.driver.keyevent(4)

	def hideKeyboard(self):
		"""
		收起键盘
		"""
		self.driver.hide_keyboard()


	def press_TouchAction(self):
		window_size = self.get_size()
		width = window_size.get("width")
		height = window_size.get("height")
		TouchAction(self.driver).press(x=int(width * 0.5), y=int(height*0.9)).release().perform()



	def waitActivity(self, activity, timeout=5):
		"""
		等待指定的Activity,5秒超时
		:param activity: 等待的Activity
		:param timeout: 超时时间
		:return:True or False
		"""
		result = self.driver.wait_activity(activity, timeout)
		return result


	# savePngName:生成图片的名称
	def savePngName(self, name):
			"""
			name：自定义图片的名称
			"""
			# 每次实例化Initalization太浪费内存，已经定义好的全局变量就是为了减少初始化类反复实例化
			if isinstance(appium_init.inital,Initialization)!=True:
				Init()
			inital=appium_init.inital
			day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
			fp = inital.project_path+"\\result\\" + day + "\\image\\" + day
			tm = self.saveTime()
			type = ".png"
			if os.path.exists(fp):
				filename = fp + "\\" + tm + "_" + name + type
				# print filename
				# print "True"
				return filename
			else:
				os.makedirs(fp)
				filename = fp + "\\" + tm + "_" + name + type
				# print filename
				# print "False"
				return filename

	# 获取系统当前时间
	def saveTime(self):
			"""
			返回当前系统时间以括号中（2014-08-29-15_21_55）展示
			"""
			return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

	# saveScreenshot:通过图片名称，进行截图保存
	def saveScreenshot(self, name):
			"""
			快照截图
			name:图片名称
			"""
			# 获取当前路径
			# print os.getcwd()
			image = self.driver.save_screenshot(self.savePngName(name))
			return image




class WebUI(BasePage):
	def __str__(self):
		return 'WEB UI'


class AppUI(BasePage):
	def __str__(self):
		return 'App UI'


if __name__ == '__main__':
	a=Initialization()
	d=a.get_driver()
	c=BasePage(d)
	c.saveScreenshot("test")