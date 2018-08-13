# -*- coding: utf-8 -*-

import sys, os, time
import smart.dynamicLoadModule


g_qq = ''
g_debug = False


def onQQMessage(bot, contact, member, content):
    if member.qq == '1902115681':
        if g_debug :
            lret = smart.dynamicLoadModule.onDynamicLoad(contact, member, content)
            bot.SendTo(contact, lret)
        else:
            import smart.parseSmart
            bot.SendTo(contact, smart.parseSmart.onSmartParse(contact,member, content))









if __name__ == "__main__":
    print os.getcwd()
    import smart.parseSmart
    smart.parseSmart.onSmartParse('test', 'test', 'content')
