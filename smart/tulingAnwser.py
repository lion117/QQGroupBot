# -*- coding: utf-8 -*-

import sys, os, time
import json
import urllib2



g_appid= '3c640db2e63742cab7c46d856d1a4eb1'
g_key = '9e594598f880744e'
g_urlV1 ='http://www.tuling123.com/openapi/api'
g_urlV2 ='http://openapi.tuling123.com/openapi/api/v2'
g_timeout = 10


def autoAnwser(tText, tUser ='default'):
    req = {
        "perception":
            {
                "inputText":
                    {
                        "text": tText
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
                "userId": tUser
            }
    }
    req = json.dumps(req).encode('utf8')
    lRequest = urllib2.Request(g_urlV2, data=req, headers={'content-type': 'application/json'})
    response = urllib2.urlopen(lRequest, timeout=g_timeout)
    response_str = response.read().decode('utf8')
    response_dic = json.loads(response_str)
    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    return  results_text



class MainRun():
    @classmethod
    def runInteractiate(cls):
        print(u"please input your text")
        while True:
            lText = raw_input()
            if lText == 'q':
                print(u"quit from loop")
                return
            lResp = autoAnwser(lText)
            print(lResp)

        print(u'end auto respon')





if __name__ == "__main__":
    print os.getcwd()
    MainRun.runInteractiate()