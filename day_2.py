# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:48:55 2018

@author: lenovo
"""

import urllib.request as r
city_pinyin = input("请输入城市拼音：")
address = 'http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print("该城市未来五天的天气情况：")
#json(dict)各式工具包
import json
data = json.loads(info)
for i in range(5):
    print("今天是："+str(data['list'][8*i+1]['dt_txt']))
    print("当前温度是："+str(data['list'][8*i+1]['main']['temp'])+"华氏度")
    print("当前天气情况："+str(data['list'][8*i+1]['weather'][0]['description']))
    print("今天的最高温度是："+str(data['list'][8*i+1]['main']['temp_max'])+"华氏度")
    print("气压是："+str(data['list'][8*i+1]['main']['pressure'])+"P"+'\n')