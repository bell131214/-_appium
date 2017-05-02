#coding:utf-8
import smtplib,os
from email.mime.text import MIMEText
from email.header import Header

class SendMail(object):
	"""docstring for send_mail"""

	def get_report(self,result_path):
		reportName=sorted(os.listdir(result_path),
			key=lambda filename:(os.path.getmtime(result_path+"\\"+filename)))[-1]
		return (result_path+'\\'+reportName)

	def post_mail(self,report_file):
		f=open(report_file,'rb')
		mail_body=f.read()
		f.close()


		sender="276476197@qq.com"
		to_mail=["276476197@qq.com"]
		username="276476197@qq.com"

		#QQ授权码
		mail_pwd="gujttwszbatpbieh"
		# #第一种写法  使用plain格式发送
		# msg=MIMEText("邮件测试",'plain','utf-8')


		#第二种写法  使用html格式发送
		# msg=MIMEText("<html><h1>邮件测试！</h1></html>","html","utf-8")
		msg=MIMEText(mail_body,"html","utf-8")

		msg['To'] =";".join(to_mail)
		msg['From']='hello<'+username+'>'
		msg['Subject']=Header(u'quark—UFO自动化测试报告','utf-8')
		try:
			smtp=smtplib.SMTP_SSL()
			smtp.connect("smtp.qq.com")
			smtp.login(username, mail_pwd)
			smtp.sendmail(sender, to_mail, msg.as_string())
			smtp.close()
			return True
		except Exception, e:
			print str(e).encode('GBK')
			return False


# #邮件正文
# msg=MIMEText("<html><h1>邮件测试！</h1></html>","html","utf-8")
# msg["Subject"]=Header("python email test","utf-8")


# smtp=smtplib.SMTP()
# smtp.connect("smtp.qq.com")
# smtp.login(username, password)
# smtp.sendmail(sender, to_addrs, msg.as_string())

# smtp.quit()


if __name__ == '__main__':
	mail=SendMail()
	# if mail.post_mail():
	# 	print "发送成功"
	# else:
	# 	print "发送失败"
	report_file=mail.get_report("D:\\quarkscript\\UFO_appium\\result\\2017-04-27")
	mail.post_mail(report_file)
