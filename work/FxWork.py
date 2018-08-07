# -*- coding: utf-8 -*-

import sys, os, time
from work.PyLogPro import  g_logger


g_help1 = '''常见问题解决方案:
无法打开/启动伴侣http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138740)
直播伴侣安装失败http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138724
网页开播检测到设备被占用http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138717
检测到尚未安装酷狗直播伴侣http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138712
播歌正在连接http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138721
乐库/伴奏显示空白http://c.fxwork.kugou.net/pages/viewpage.action?pageId=25138734
其他问题解决方案http://c.fxwork.kugou.net/pages/viewpage.action?pageId=6917757
'''

g_help ='''网页开播检测到设备被占用
检测到尚未安装酷狗直播伴侣
无法搜索下载和播歌
乐库/伴奏显示空白
无法打开/启动伴侣
直播伴侣安装失败
限制第三方播歌异常情况解决方案
主播开播不符合流畅度要求,无法开播
其他问题解决方案
解决方案文档路径: 群文件---酷狗直播伴侣-2018**.doc
'''

def onMsgParse(bot, contact, member, content):
    lInfo = str.format("user: %s content: %s"%(contact, content))
    g_logger.error( lInfo)
    return g_help



if __name__ == "__main__":
    print(os.getcwd())
    #onMsgParse(None, 'good','new', 'hello')