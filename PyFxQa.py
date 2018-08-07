# -*- coding: utf-8 -*-

import sys, os, time

from  work.FxWork import onMsgParse

g_User = '@何思远'


def onQQMessage(bot, contact, member, content):
    if g_User not in content:
        return
    else:
        if '-stop 8888' in content:
            bot.SendTo(contact, 'QQ机器人已关闭')
            bot.Stop()
            return
        else:
            linfo = onMsgParse(bot,contact, member, content)
            lResp = str.format('%s\r\n@%s'%(linfo,member))
            bot.SendTo(contact ,lResp)





if __name__ == "__main__":
    print(os.getcwd())