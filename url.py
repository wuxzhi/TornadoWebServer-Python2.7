#!/usr/bin/env Python
# coding=utf-8

"""
网站架构
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.sleep import SleepHandler
from handlers.sleep import SeeHandler
url = [
    (r'/', IndexHandler),
    (r'/user', UserHandler),
    (r'/sleep', SleepHandler),
    (r'/see', SeeHandler)
    ]


