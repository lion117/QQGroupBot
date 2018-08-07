# -*- coding: utf-8 -*-

import sys, os, time
from work.PyLogPro import  g_logger


g_help = '''
常见问题解决方案:
[无法打开/启动伴侣](http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138740)
[直播伴侣安装失败](http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138724)
[检测到设备被占用](http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138717)
[检测到尚未安装酷狗直播伴侣](http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138712)
[播歌正在连接](http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138721)
[乐库/伴奏显示空白](http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138734)
.....
'''


def onMsgParse(bot, contact, member, content):
    lInfo = str.format("user: %s content: %s"%(contact, content))
    g_logger.error( lInfo)
    return g_help



if __name__ == "__main__":
    print(os.getcwd())
    #onMsgParse(None, 'good','new', 'hello')