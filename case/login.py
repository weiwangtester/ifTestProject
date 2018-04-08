#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import case.base as base


def login():
    # 设置登录的post的url
    url = base.Base.URL_START + '/登录的路由'  # + base.Base.URL_END
    # 设置post的数据,登录的账号和密码等等
    data = {'phone': base.Base.PHONE, 'password': base.Base.PASSWORD}
    # 新建一个session
    session = requests.session()
    # 发送请求并获取返回值
    response = session.post(url=url, headers=base.Base.HEADERS, json=data)
    # 取出返回的json
    responseJson = response.json()
    # 如果登录成功,则返回True,保存session
    if responseJson['msg'] == 'success':
        # 将全局session绑定当前session
        base.Base.set_base_session(session)
        # 保存登录返回的token
        base.Base.TOKEN = responseJson['data']['token']
        return True
    else:
        return False


def logout():
    # TODO 3.1设置登出的post的url
    url = base.Base.URL_START + '链接待定'  # + base.Base.URL_END
    # TODO 3.2设置登出的data
    data = ''
    # 获取全局session
    session = base.Base.get_base_session()
    # 发送请求并获取返回值
    response = session.post(url=url, json=data)
    responseJson = response.json()
    # TODO 3.3指定登出的返回值
    if responseJson['xxxx'] == "xxxx":
        print("登出成功,即将关闭session")
        session.close()
        return True
    else:
        print("登出失败,强行关闭session")
        session.close()
        return False


if __name__ == '__main__':
    login()
