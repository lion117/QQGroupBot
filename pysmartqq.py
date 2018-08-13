# -*- coding: utf-8 -*-

import sys, os, time




def onQQMessage(bot, contact, member, content):
    bot.SendTo(contact, 'QQ机器人已关闭')
    bot.Stop()
    return








if __name__ == "__main__":
    print os.getcwd()