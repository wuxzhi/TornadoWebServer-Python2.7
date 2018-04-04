# !/usr/bin/env Python
# coding=utf-8
from base import BaseHandler
import tornado.web
import tornado.gen

import time

class SleepHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 5)
        #yield tornado.gen.sleep(17)
        self.render("sleep.html")

class SeeHandler(BaseHandler):
    def get(self):
        self.render("see.html")
