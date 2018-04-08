#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
import os
import HTMLTestRunner
import case.login as lg
import case.base as base
import case.testcasemain as tcm

if __name__ == '__main__':
    login_result = lg.login()
    if login_result:
        # 构造测试集
        suite = unittest.TestSuite()
        # TODO 1.按需添加测试用例
        # suite.addTest(tcm.intertest('test_1'))
        suite.addTest(unittest.makeSuite(tcm.intertest))
        # 获取当前时间,生成测试报告文件名称
        file_path = os.getcwd() + '\\result\\' + time.strftime('%Y-%m-%d-%H-%M', time.localtime()) + '.html'
        # 新建测试报告文件并准备写入测试结果
        with open(file_path, 'wb') as fp:
            # 初始化unittest执行器
            runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='接口自动化测试',
                # TODO 2.确定测试报告的副标题
                description='这是测试报告的副标题'
            )
            # 执行测试集
            runner.run(suite)
        # TODO 3.退出登录
        # lg.logout()
        base.Base.send_mail(file_path)
        print('测试完毕,已生成测试报告并用邮件发送')
    else:
        print('登录失败,结束当前测试')
