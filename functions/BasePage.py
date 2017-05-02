#coding=utf-8
import time,os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from functions.appium_init import *

class BasePage(object):
	"""
	封装关于Appium中操作元素对象的方法
	"""
#new PO
	def __init__(self, driver):
	#	print driver
		self.driver = driver

	def base_find_element(self,locator,value):
		try:
			return self.driver.find_element(locator,value)
		except NoSuchElementException,e:
			if isinstance(appium_init.inital,Initialization)!=True:
				Init()
			appium_init.inital.logger.info('BasePage | NoSuchElementException error is%s; %s,%s' %(e,locator,value))
			raise e



#old PO
	def __str__(self):
		return "APP"



	# def find_element(self, *loc):
	# 	"""
	# 	定位元素,定位正确后返回元素的信息,外部调用传入元组参数必须有*,
	# 	例如:
	# 	find_element(*self.native_caixun)
	# 	:param loc: 元组类型,结构必须是(By.NAME, u'财讯')
	# 	:return: element
	# 	"""
	# 	try:
	# 		print loc
	# 		element = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(*loc))
	# 		return element
	# 	except NoSuchElementException, e:
	# 		print e
	# 		print ('Error details :%s' % (e.args[0]))
	# 	#print loc
	# 	#return  self.driver.find_element(*loc)
	# 	#try:
	# 		#WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
	# 		#return self.driver.find_element(*loc)
	# 	#except:
	# 		#print u"%s 页面中未能找到 %s 元素" % (self, loc)


	def find_elements(self, *loc):
		"""
		定位元素,定位正确后返回元素的信息,外部调用传入元组参数必须有*,
		例如:
		find_elements(*self.native_caixun)

		:param loc: 元组类型,结构必须是(By.NAME, u'财讯')
		:return: elements
		"""
		try:
			elements = WebDriverWait(self.driver, 30).until(lambda x: x.find_elements(*loc))
			return elements
		except NoSuchElementException, e:
			print ('Error details :%s' % (e.args[0]))

	def checkElementIsShown(self, *loc):
		"""
		判断某个控件是否显示

		:param loc: 元组类型,结构必须是(By.NAME, u'财讯')
		"""
		try:
			self.find_element(*loc)
			return True
		except:
			return False

	def waitForElementNotPresent(self, period, *loc):
		"""
		等待某个控件不再显示

		:param loc: 元组类型,结构必须是(By.NAME, u'财讯')
		:param period：等待的秒数
		"""
		for i in range(0, period):
			time.sleep(1)
			if not self.checkElementIsShown(*loc):
				return True
			else:
				continue
		raise Exception("Cannot find Element seconds")

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
		self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

	def swipe_to_right(self):
		"""
		从左往右滑动
		:return: None
		"""
		window_size = self.get_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

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

	def clickElement(self, *loc):
		"""
		点击某一个控件，如果改控件不存在则会抛出异常

		:param loc: 元组类型,结构必须是(By.NAME, u'财讯')
		"""
		element = self.find_element(*loc)
		element.click()


	def getTextOfElement(self, *loc):
		"""
		获取某个控件显示的文本，如果该控件不能找到则会抛出异常

		:param loc: 元组类型,结构必须是(By.NAME, u'财讯')
		:Return: str, 返回该控件显示的文本

		:Usage:
			self.getTextOfElement(elementInfo)
		"""
		element = self.find_element(*loc)
		return element.text

	def clearTextEdit(self, *loc):
		"""
		清除文本框里面的文本

		:Usage:
			self.clearTextEdit(*loc)
		"""
		element = self.find_element(*loc)
		element.clear()

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
		TouchAction(self.driver).press(x=359,y=1074).release().perform()



	def waitActivity(self, activity, timeout=5):
		"""
		等待指定的Activity,5秒超时
		:param activity: 等待的Activity
		:param timeout: 超时时间
		:return:True or False
		"""
		result = self.driver.wait_activity(activity, timeout)
		return result

	def send_keys(self, loc, value, clear_first=True, click_first=True):
		try:
			if click_first:
				self.find_element(*loc).click()
			if clear_first:
				self.find_element(*loc).clear()
			self.find_element(*loc).send_keys(value)
		except AttributeError,WebDriverException:
			print "%s 页面未能找到 %s 元素" % (self, loc)



class WebUI(BasePage):
	def __str__(self):
		return 'WEB UI'


class AppUI(BasePage):
	def __str__(self):
		return 'App UI'
