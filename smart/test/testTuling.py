# -*- coding: utf-8 -*-

import sys, os, time


g_appid= '3c640db2e63742cab7c46d856d1a4eb1'
g_key = '9e594598f880744e'
g_urlV1 ='http://www.tuling123.com/openapi/api'
g_urlV2 ='http://openapi.tuling123.com/openapi/api/v2'




import json
import urllib2

api_url = "http://openapi.tuling123.com/openapi/api/v2"
text_input = '我的天'

req = {
    "perception":
    {
        "inputText":
        {
            "text": text_input
        },

        "selfInfo":
        {
            "location":
            {
                "city": "上海",
                "province": "上海",
                "street": "文汇路"
            }
        }
    },

    "userInfo":
    {
        "apiKey": g_appid,
        "userId": "OnlyUseAlphabet"
    }
}
# print(req)
# 将字典格式的req编码为utf8
req = json.dumps(req).encode('utf8')
# print(req)

http_post = urllib2.Request(api_url, data=req, headers={'content-type': 'application/json'})
response = urllib2.urlopen(http_post)
response_str = response.read().decode('utf8')
# print(response_str)
response_dic = json.loads(response_str)
# print(response_dic)

intent_code = response_dic['intent']['code']
results_text = response_dic['results'][0]['values']['text']
print(u'Turing的回答：')
print(u'code：' + unicode(intent_code))
print(u'text：' + results_text)



# if __name__ == "__main__":
#     print os.getcwd()