# -*- coding: utf-8 -*-
import logging
import sys, os, time
import smart.dynamicLoadModule
import smart.parseSmart
g_group  = 'group'
g_discuss = 'discuss'
g_buddy = 'buddy'




def onQQMessage(bot, contact, member, content):
    if contact.ctype == g_group:
        (lIsSend , lContent) = smart.parseSmart.onSmartParseGroup(contact,member, content)
        if lIsSend :
            bot.SendTo(contact, lContent)

    elif contact.ctype == g_discuss:
        pass
    elif contact.ctype == g_buddy:
        pass








if __name__ == "__main__":
    print os.getcwd()
