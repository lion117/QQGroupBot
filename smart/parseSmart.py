# -*- coding: utf-8 -*-
"""
@author: Leo
Date:  2018/8/13
Email:	lion_117@126.com
All Rights Reserved Licensed under the Apache License
"""

import os, sys,time
import  tulingAnwser
import work.FxWork

g_groupFxFeedbk = '酷狗直播伴侣问题反馈'
g_groupTest = '测试群'
g_worker = '值班经理'
g_workerTest = 'leo_nardo'
g_disCoupleStream = '双流问题反馈'
g_list = [ '@梁衍鹏', '@何思远', '@黎振佳','@汤伯超']


def onSmartParseTest(contact, member, content):
    # lRet =
    lJson = {
        "member":
            {
                "ctype": member.ctype,
                "qq": member.qq,
                "uin": member.uin,
                "nick": member.nick,
                "mark": member.mark,
                "name": member.name,
                "card": member.card,
                # "join_time": contact.join_time,
                # "last_speak_time": contact.last_speak_time,
                # "role": contact.role,
                # "role_id": contact.role_id,
                # "is_buddy": contact.is_buddy,
                # "level": contact.level,
                # "levelname": contact.levelname,
                # "point": contact.point
            } ,
        "contacnt":
            {
                "ctype": contact.ctype,
                "qq": contact.qq,
                "uin": contact.uin,
                "nick": contact.nick,
                "mark": contact.mark,
                "name": contact.name,
                #"join_time": contact.join_time,
                # "last_speak_time":contact.last_speak_time,
                # "role":contact.role,
                # "role_id":contact.role_id,
                # "is_buddy":contact.is_buddy,
                # "level":contact.level,
                # "levelname": contact.levelname,
                # "point":contact.point
            }
    }
    import  json
    return (True,json.dumps(lJson))


def onSmartParseGroup(contact, member, content):
    lDefault = (False, None)
    if contact.name == g_groupFxFeedbk or contact.name == g_groupTest:
        lNow = time.localtime(time.time())
        if lNow.tm_hour > 20 or lNow.tm_hour < 9 :
            # doing normal task
            for itor in g_list:
                if itor not in content:
                    continue
                else:
                    linfo = work.FxWork.onMsgParse(None, contact, member, content)
                    Resp = str.format('%s\r\n' % (linfo))
                    return (True, linfo)
        else:
            if member.nick == g_worker or member.nick == g_workerTest:
                return tulingAnwser.doTulingTask(content,member.nick)
        return lDefault



def onSmartParseDiscuss(contact, member, content):
    if contact.name == g_groupFxFeedbk:
        pass


class RunMain():
    @classmethod
    def runTime(cls):
        lTime = time.localtime(time.time())
        print (lTime.tm_hour)
        print (lTime.tm_wday)
        import  datetime
        lDate  = datetime.datetime.now()
        print (lDate.hour, lDate.weekday())


if __name__ == '__main__':
    print (os.getcwd())
    RunMain.runTime()
    pass
