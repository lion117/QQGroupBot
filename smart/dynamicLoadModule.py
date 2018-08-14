# -*- coding: utf-8 -*-
"""
@author: Leo
Date:  2018/8/13
Email:	lion_117@126.com
All Rights Reserved Licensed under the Apache License
"""

import os
import importlib


imp_module = 'parseSmart'
imp_class = ''
imp_func = 'onSmartParse'

def onDynamicLoad(contact, member, content):
    ip_module = importlib.import_module( imp_module,'smart')
    ip_module_cls = getattr(ip_module, imp_func)
    return ip_module_cls(contact, member, content)



if __name__ == '__main__':
    pass
