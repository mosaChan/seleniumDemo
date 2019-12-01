# coding=utf-8
from HTMLTestRunner_cn import HTMLTestRunner
import os
import unittest
import time
import sys
sys.path.append(os.path.dirname(os.path.abspath('.')))

#设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/report/'
#获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

#设置报告名称格式
HtmlFile = report_path + now +" HTMLtemplate.html"
fp = open(HtmlFile,"wb")

#构建suite
suite = unittest.TestLoader().discover("testModule")

if __name__ == '__main__':
    runner = HTMLTestRunner(
        title="自动化测试报告",
        description="",
        tester="mosa",
        stream=fp,
        verbosity=2, retry=0, save_last_try=True)
    runner.run(suite)
    fp.close()