#coding:utf-8
import yagmail,os
from datetime import  datetime
from appium_init import *
from email.mime.text import MIMEText
#上传附件需要的类
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header

class SendMail(object):
    """docstring for send_mail"""
        #入参测试报告文件路径，查询文件夹，选取最新的文件，返回“文件路径+最新的文件名”

    def get_report(self,result_path):
        reportName=sorted(os.listdir(result_path),key=lambda filename:(os.path.getmtime(result_path+"\\"+filename)))[-1]
        return (result_path+'\\'+reportName)

    def get_mail_body(self,report_file):
        f = open(report_file, 'rb')
        mail_body = f.read()
        f.close()
        return mail_body

    def post_mail(self,to_mail_list,resultFile,logFile):

        mail = yagmail.SMTP(user='276476197@qq.com', password='gujttwszbatpbieh', host='smtp.qq.com', port='587')
        contents = self.get_mail_body(resultFile)
        mail.send(to=to_mail_list,subject=u'quark—UFO自动化测试报告',
                  contents=[contents,resultFile,logFile])

    def send(self):
        to_mail_list=appium_init.inital.desired_caps['to_mail_list'].split(',')
        project_path=appium_init.inital.project_path

        log_path=project_path+"\\log\\"+datetime.now().strftime("%Y_%m_%d")
        result_path=project_path+ "\\result\\" +time.strftime('%Y-%m-%d', time.localtime(time.time()))

        logFile=self.get_report(log_path)
        resultFile=self.get_report(result_path)

        self.post_mail(to_mail_list,resultFile,logFile)


        # yag.send(to=['276476197@qq.com', 'FanGu@quarkfinance.com'], subject=u'quark—UFO自动化测试报告',
        #          contents=[contents,
        #                    "D:\\quarkscript\\UFO_appium\\result\\2017-05-01\\2017-05-01-07_54_03_result.html",
        #                    "D:\\quarkscript\\UFO_appium\\log\\2017_05_01\\appium 2017_05_01 00-07-08.log"])




    # def post_mail(self,report_file):
    #     msg=MIMEMultipart()
    #     f=open(report_file,'rb')
    #     mail_body=f.read()
    #     f.close()
    #     sender="276476197@qq.com"
    #     to_mail=["276476197@qq.com"]
    #     username="276476197@qq.com"
    #
    #     #QQ授权码
    #     mail_pwd="gujttwszbatpbieh"
    #
    #     #实例化父类
    #     msg=MIMEMultipart()
    #     msg['To'] = ";".join(to_mail)
    #     msg['From'] = 'hello<' + username + '>'
    #     msg['Subject'] = Header(u'quark—UFO自动化测试报告', 'utf-8')
    #
    #     #创建正文部分并加载
    #     text_part = MIMEText(mail_body, _subtype="html", _charset="utf-8")
    #     msg.attach(text_part)
    #     #
    #     #创建附件部分并加载
    #     upload_part=MIMEApplication(mail_body)
    #     upload_part.add_header('Content-Disposition', 'attachment', filename="UFO_appium_report.html")
    #     msg.attach(upload_part)
    #
    #     try:
    #     	smtp=smtplib.SMTP_SSL()
    #     	smtp.connect("smtp.qq.com")
    #     	smtp.login(username, mail_pwd)
    #     	smtp.sendmail(sender, to_mail, msg.as_string())
    #     	smtp.close()
    #     	return True
    #     except Exception, e:
    #     	print str(e).encode('GBK')
    #     	return False




if __name__ == '__main__':
    Init()
    mail=SendMail()
    mail.send()