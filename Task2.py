__author__ = 'yuhenghu@uic.edu'
#this is as a reference for IDS 566 Spring 2022 Homework #1 only#
#do not use it for other purposes#


import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


count = 0
url = 'https://www.zillow.com/graphql/'

headers = {'authority': 'www.zillow.com', 'method':'POST',
 'path': '/graphql/?zpid=19620225&timePeriod=TEN_YEARS&metricType=LOCAL_HOME_VALUES&forecast=true&useNewChartAPI=false&operationName=HomeValueChartDataQuery',
  'scheme': 'https', 'accept-encoding': 'gzip, deflate, br', 'content-length': '598', 'content-type': 'text/plain', 'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
  'cookie': 'zguid=23|%24963002dd-3ad8-44e5-88f2-9bcd6ba5ff8f; zjs_user_id=null; _ga=GA1.2.141287144.1642024957; _gac_UA-21174015-56=1.1642024957.CjwKCAiAlfqOBhAeEiwAYi43F5gy07g3ODX7wYJlAjlTpGGTw3HkBl2OQ0RouLNjTyuxbPUJrNv3SBoCKtoQAvD_BwE; zjs_anonymous_id=%22963002dd-3ad8-44e5-88f2-9bcd6ba5ff8f%22; _pxvid=5b0c8c55-73f3-11ec-aa60-7064675a6558; _gcl_aw=GCL.1642024958.CjwKCAiAlfqOBhAeEiwAYi43F5gy07g3ODX7wYJlAjlTpGGTw3HkBl2OQ0RouLNjTyuxbPUJrNv3SBoCKtoQAvD_BwE; _gcl_au=1.1.820592105.1642024958; __pdst=c20b1b80be2b42b5afb4831583b6c845; _fbp=fb.1.1642024958254.44808872; _pin_unauth=dWlkPU1HSTVaalF6TlRndE1qbGlOaTAwWVdOaUxXSTBOVGN0TVRNMU5tSTVZV1ZoTkRVeg; __gads=ID=7c693bcb19adc050:T=1642025028:S=ALNI_MbEH5I6_cf1MrenJ1Zl-ixtr3vbGg; JSESSIONID=4A3B5E0B37AA7A82BAC8A54FDA000513; zgsession=1|55caeb04-c811-4606-83db-c5d08ae59ca3; _gid=GA1.2.1510085412.1643144514; _pxff_bsco=1; KruxPixel=true; DoubleClickSession=true; g_state={"i_p":1643230920575,"i_l":2}; utag_main=v_id:017e505078d7001f13b7a07a874a0507300e006b00978$_sn:2$_se:1$_ss:1$_st:1643146318042$dc_visit:2$ses_id:1643144518042%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:us-east-1%3Bexp-session$ttd_uuid:9e1b40eb-a54c-4b5c-8dc2-7f27ea277e82%3Bexp-session; KruxAddition=true; _px3=b0e8e96d4da9f5286755b72cd647913c95139f95a78a68b6d9058a4fd9aeedbb:r7TI77ftqX/o63l1oF4/0ShuIUfxnhktqaDGlL+SjQGes7aEGYj/nMgIJzqKdlF3511m51vVJYANJsBpWBKKWw==:1000:TNRjJ5VRX0GorcSEOErUf16N1CV0pSpRARalJUUL1W+sMTwnR4YZDUtugHtM2ZDrtetM5KCliWeieVFo/78DOS6LjGPHjv+0PTWll5Q101p6d6gD8gZGxTO3U1TliPL6WB7UfbhJPvVjTZ508k1ZDCBHAz0E7E1ZUZaDq9FnldFG9vHSZv7FK4jKf/VhffRp284OO4rwVz6+7DO8oK5qjA==; _uetsid=08a865c07e2211ecb62f4ffe5d078de2; _uetvid=5af5185073f311ecb248e9c2233feeab; search=6|1645736656191%7Crect%3D37.35357976469194%252C-121.97802543640137%252C37.29897803021096%252C-122.08102226257324%26zpid%3D19620225%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%09%09%09%09%09%09%09%09; _gat=1; AWSALB=qnWG29aLjUIOyPj3LwSLrwV7lGRVF038m4bZ0dE7Xb6cpHc2cBnCZ7LhAX7SwBPlhsvoCQUXv88pewb9gGbHnu0WPTpkr2tqUlO001SvDtPFTjT8LAJEFKY04chf; AWSALBCORS=qnWG29aLjUIOyPj3LwSLrwV7lGRVF038m4bZ0dE7Xb6cpHc2cBnCZ7LhAX7SwBPlhsvoCQUXv88pewb9gGbHnu0WPTpkr2tqUlO001SvDtPFTjT8LAJEFKY04chf',
  'origin': 'https://www.zillow.com','user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

def json_zestimatehistory(zpid):
    #this is payload, i.e., the query sent to zillow server
    chartData = {"operationName":"HomeValueChartDataQuery","variables":{"zpid":00000},"query":"query HomeValueChartDataQuery($zpid: ID!, $metricType: HomeValueChartMetricType, $timePeriod: HomeValueChartTimePeriod, $useNewChartAPI: Boolean) {\n  property(zpid: $zpid) {\n    homeValueChartData(metricType: $metricType, timePeriod: $timePeriod, useNewChartAPI: $useNewChartAPI) {\n      points {\n        x\n        y\n      }\n      name\n    }\n  }\n}\n"}

    chartData['variables']['zpid']=zpid

    return chartData

def get_json_zestimate(zpid):
    #get json query ready, zpid as input
    chartData = json_zestimatehistory(zpid)
    ZestimateScore = []
    
    try:
        chart_req = requests.post(url=url, json=chartData, headers=headers) #send request to zillow server

        chart_out = json.loads(chart_req.text) #get the response from zillow server and load as json object
        #print(len(chart_out))
        #parse the json object to extract scores
        #pd.read_json('chart_out')

        for each in chart_out['data']['property']['homeValueChartData'][0]['points']:
            x = each['x']
            x = str(x)
            x = int(x[:10])
            d = datetime.fromtimestamp(x).strftime('%m/%Y')
            date = (d,each['y'])
            #print(date)
            ZestimateScore.append(date)
        #print(*ZestimateScore, sep = "\n")

        f = pd.DataFrame(ZestimateScore, columns = ['Date','Price'])
        print(f)

        ax = f.plot()
        ax.set_xlim(xmin=0,xmax=120)
        ax.ticklabel_format(style='plain')
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
        ax.legend().set_visible(False)
        DF = f.set_index('Date')
        plt.locator_params(axis='y', nbins=5)
        plt.ylim(0, 2000000)
        plt.grid(color='grey', linestyle='-', linewidth=1)
        plt.plot(DF,color='blue')
        ax.set_xticks(range(0,121,24))
        plt.gcf().autofmt_xdate()
        plt.show()

        '''ax = f.plot()
        ax.ticklabel_format(style='plain')
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
        DF = f.set_index('Date')
        plt.locator_params(axis='y', nbins=5)
        plt.ylim(0, 2000000)
        plt.plot(DF,color="b")
        plt.gcf().autofmt_xdate()
        plt.show()'''


    except Exception as e:
        print ('error not 200, ZestimateScore, try again', e)
        return ZestimateScore



#for ids 566 demo


get_json_zestimate(19620225)
