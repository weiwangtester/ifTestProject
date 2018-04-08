#!/usr/bin/env python
# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Base:
    PHONE = 'xxxxxx'
    PASSWORD = 'xxxx'
    # HOST = '0.0.0.0'
    URL_START = 'https://xxxx.xxxx.xxx'
    URL_END = 'xxxxx'
    HEADERS = {
        'Content-Type': 'application/json',
        # 'Content-Type': 'application/x-www-form-urlencoded ',
        # 'Content-Type': 'multipart/form-data',
        # 'User-Agent': '填写IOS-User-Agent',
        # 'User-Agent': '填写Android-User-Agent',
        'Connection': 'keep-alive',
    }
    TOKEN = None
    SESSION = None
    RESULT_NAME = None

    @staticmethod
    def set_base_session(gb_session):
        Base.SESSION = gb_session

    @staticmethod
    def get_base_session():
        return Base.SESSION

    @staticmethod
    def send_mail(new_result_path):
        with open(new_result_path, 'r', encoding='utf-8') as result_file:
            mail_body = result_file.read()
        sender = '发件人@xxx.com'
        receivers = ['收件人1@xx.com', '收件人2@xxx.com', '等等等等']
        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header('接口自动化测试报告', 'utf-8')
        msg['From'] = sender
        msg['To'] = ','.join(receivers)
        try:
            smtp = smtplib.SMTP()
            # 或其他邮箱
            smtp.connect('smtp.163.com')
            smtp.login('发件人@xxx.com', '发件人邮箱密码')
            smtp.sendmail(sender, receivers, msg.as_string())
            smtp.quit()
        except Exception as e:
            print(e)
        return
