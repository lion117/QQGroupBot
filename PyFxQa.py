# -*- coding: utf-8 -*-

import sys, os, time

g_User = '@何思远'




def onQQMessage(bot, contact, member, content):
    if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()
    elif contact == 'leo_nardo':
        bot.SendTo(contact,'your are my master')






if __name__ == "__main__":
    print(os.getcwd())