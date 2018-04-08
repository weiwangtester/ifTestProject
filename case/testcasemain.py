#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sys
import case.myunit as myunit
import case.base as base


class intertest(myunit.MyTest):
    '''xxx模块/功能/etc接口测试
    self.session:用例中使用该session发送请求.注意:如果self.session不生效,则在case中获取及保存session
    intertest.DATA:接口测试的相关数据
    '''
    with open('./data/testdata.csv', 'r', encoding='utf-8-sig') as cf:
        cf_d = csv.DictReader(cf)
        DATA = []
        for row in cf_d:
            DATA.append(row)

    def test_1(self):
        '''测试用例1: xxx'''
        num = int(sys._getframe().f_code.co_name.split('_')[-1]) - 1
        datadict = intertest.DATA[num]
        # print(datadict)
        Url = base.Base.URL_START + datadict['Url']  # + base.Base.URL_END
        # Method = intertest.DATA[num]['Method']
        # Parameter = intertest.DATA[num]['Parameter']
        # TCode = datadict['TCode']

        Parameter = eval("{'token': '%s'}" % base.Base.TOKEN)
        response = self.session.post(url=Url, json=Parameter)
        responseJson = response.json()

        # print(responseJson['code'])
        self.assertEquals(responseJson['code'], '0000')

    # def test_2(self):
    #     '''测试用例2: '''

    # def test_3(self):
    #     '''测试用例3的标题'''


if __name__ == '__main__':
    pass
