#coding=utf-8
from functions.HTMLTestRunner1 import  *
# from functions.appium_init import Initialization
from appium_init import *
import os


class exec_sutiecase():


    def __init__(self):
        # path = Initialization()
        self.result = appium_init.inital.project_path + "\\result\\"
        # 获取系统当前时间
        self.now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        self.day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # 定义个报告存放路径，支持相对路径
        self.tdresult = self.result + self.day


        # appium_init.inital.result_path=self.tdresult

    def get_html(self,stream,startTime, duration, status, success_count, failure_count, error_count):
        """
        :param startTime: 开始时间
        :param duration: 运行时长
        :param status: 状态
        :param success_count: 通过数量
        :param failure_count: 失败数量
        :param error_count：错误数量
        :return:
        """

        template = '''
        <h1 style="color:green;">quark—UFO自动化测试报告</h1>
        开始时间:{startTime}<br/>
        运行时长:{duration}<br/>
        状态:{status}<br/>
        <p style="color:blue;">结果概览 </p>
              <h2>详细数据，烦请点击查看附件</h2>
              <div align=center>
        <table border=1 cellspacing=0 cellpadding=0 style='border-collapse:collapse;border:none'>
            <tr>
                <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;background:#DBDBDB;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>用例总数</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
                <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;background:#DBDBDB;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>通过数量</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
                 <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;background:#DBDBDB;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>失败数量</span><span lang=EN-US><o:p></o:p></span></p>
                </td>
                <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;background:#DBDBDB;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>错误数量</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
            </tr>

            <tr>
               <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>{full_success}</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
                <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>{success_count}</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
                 <td  bgcolor="red"   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0p;padding:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>{failure_count}</span><span lang=EN-US><o:p></o:p></span></p>
                </td>
                <td   width=180 valign=top style='width:134.7pt;border:solid windowtext 1.0pt;background:0cm 5.4pt 0cm 5.4pt'>
                <p class=MsoNormal align=center style='text-align:center'>
                    <span style='font-family:宋体'>{error_count}</span><span lang=EN-US><o:p></o:p></span></p>
                    </td>
            </tr>
        </table>
        </div>
        '''.format(startTime=startTime, duration=duration, status=status,
                   full_success=success_count + failure_count + error_count, success_count=success_count,
                   failure_count=failure_count, error_count=error_count)
        stream.write(template)

        # save_html_file = '%s/test.html' % result_path




    def exec_cases(self,test_case):

        if os.path.exists(self.tdresult):
            filename = self.tdresult +"\\" + self.now + "_result.html"
            mail_name = self.tdresult + "\\" + self.now + "_send_mail.html"
            fp = file(filename, 'wb')
            fp1 = file(mail_name, 'wb')

            # 定义测试报告

            runner = HTMLTestRunner(stream=fp, title=u'quark—UFO自动化测试报告', description=u'用例详情：',verbosity=2)




            # 运行测试用例
            a=runner.run(test_case)

            self.get_html(fp1,  self.now,  1,"ss", a.success_count, a.failure_count, a.error_count)
            fp.close()  # 关闭报告文件
            fp1.close()

        else:
            os.mkdir(self.tdresult)
            filename = self.tdresult + "\\" + self.now + "_result.html"
            mail_name = self.tdresult + "\\" + self.now + "_send_mail.html"
            fp = file(filename, 'wb')
            fp1 = file(mail_name, 'wb')
            # 定义测试报告
            runner = HTMLTestRunner(stream=fp, title=u'quark—UFO自动化测试报告', description=u'用例详情：',verbosity=2)

            # 运行测试用例
            a=runner.run(test_case)

            self.get_html(fp1, a.startTime, self.now, 1,"ss", a.success_count, a.failure_count, a.error_count)
            fp.close()  # 关闭报告文件
            fp1.close()
