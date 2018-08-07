# -*- coding: utf-8 -*-

import sys, os, time
from work.PyLogPro import  g_logger


g_help = '''
1. [帮助1](baidu.com)
2. [帮助2](youdao.com)
3. [帮助3](mi.com)
.....
'''


def onMsgParse(bot, contact, member, content):
    lInfo = str.format("user: %s content: %s"%(contact, content))
    g_logger.info( lInfo)
    return g_help



if __name__ == "__main__":
    print(os.getcwd())