#coding:utf-8
import configparser

class Config():
	"""docstring for Config"""

	def __init__(self):
		self.config=configparser.ConfigParser()

	def get_config(self,section,path):
		self.config.read(path)
		values=self.config.options(section)
		parameter_dict={}
		for i in values:
			parameter_dict[i]=self.config.get(section, i)
		return parameter_dict





if __name__ == '__main__':
	config=Config()
	path="D:\\quarkscript\\auto_appium\\config\\appium_config.ini"
	parameter_dict=config.get_config('desired_caps', path)
	print parameter_dict