# -*- coding: utf-8 -*-

import sys, os, time

from  work.FxWork import onMsgParse

g_User = '@雨淋淋'
g_List = [ '@梁衍鹏', '@何思远', '@黎振佳','@汤伯超']


def onQQMessage(bot, contact, member, content):
    for itor in g_List:
        if itor not in content:
            continue
        else:
            if '-stop 8888' in content:
                bot.SendTo(contact, 'QQ机器人已关闭')
                bot.Stop()
                return
            else:
                linfo = onMsgParse(bot,contact, member, content)
                lResp = str.format('%s\r\n'%(linfo))
                bot.SendTo(contact ,lResp)





if __name__ == "__main__":
    print(os.getcwd())