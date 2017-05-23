#coding:utf-8

#首先安装扩展库pip install pymssql
from functions.appium_init import *
import pymssql

class Exce_SQLserver():
	"""docstring for ClassName"""
	def __init__(self):
		databaseINFO=appium_init.inital.get_cases_info('database')
		self.conn=pymssql.connect(host=databaseINFO['host'],user=databaseINFO['user'],password=databaseINFO['password'],database=databaseINFO['databasename'])
	def test_connect(self):
		cur=self.conn.cursor()
		if not cur:
			print "连接失败"
		else:
			print "连接成功"
		cur.close()
		self.conn.close()

	def execSql_getOne(self,SQL):
		cur=self.conn.cursor()
		cur.execute(SQL)

		#查询第一条记录
		result=cur.fetchone()
		cur.close()
		self.conn.close()
		appium_init.inital.logger.info("Exce_SQLserver | execSql_getOne() have get result!")
		return result

	def execSql_getList(self,SQL):
		cur=self.conn.cursor()
		cur.execute(SQL)

		#执行SQL，获取所有数据results是list，而其中的每个元素是 tuple
		results=cur.fetchall()
		cur.close()
		self.conn.close()
		appium_init.inital.logger.info("Exce_SQLserver | execSql_getList() have get results!")
		return results


if __name__ == '__main__':
	Init()
	sql_conn=Exce_SQLserver()
	#测试代码，查询一条记录
	# print sql_conn.execSql_getOne("SELECT * from dbo.new_product")

	#测试代码，查询结果集
	#results=sql_conn.execSql_getList("SELECT * from dbo.new_product")

	results = sql_conn.execSql_getList("SELECT top 1  new_name,new_investdate,new_financeterm from new_investdetailBase WHERE new_accountname = '24004F6C-7C08-E711-80C9-00155D01F903' order BY  new_investdate DESC")

	a=list(results)
	for i in a:
		print i