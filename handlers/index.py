#!/usr/bin/env Python
# coding=utf-8
import tornado.web
import tornado.escape
import methods.readdb as mrd
from base import BaseHandler

# import json
class IndexHandler(BaseHandler):
    def get(self):
        usernames = mrd.select_column(table='users', column='username')
        one_username = usernames[0][0]
        self.render('index.html', user=one_username)
    def post(self):
        username = self.get_argument('username');
        password = self.get_argument('password');
        userInfos = mrd.select_table(table='users', column='*', condition='username', value=username)
        if userInfos:
            # self.write(json.dumps(userInfos))
            db_pws = userInfos[0][2]
            if db_pws == password:
                self.set_current_user(username)
                self.write(username)
            else:
                self.set_current_user(0)
                self.write('-1')
        else:
            self.set_current_user(0)
            self.write('-1')
    def set_current_user(self, user):
        if user:
            self.set_secure_cookie('user', tornado.escape.json_encode(user))    #注意这里使用了 tornado.escape.json_encode() 方法
        else:
            self.clear_cookie("user")

class ErrorHandler(BaseHandler):    #增加了一个专门用来显示错误的页面
        def get(self):                                        #但是后面不单独讲述，读者可以从源码中理解
            self.render("error.html")

