# !/usr/bin/env Python
# conding=utf-8
import tornado.escape
import tornado.web
import methods.readdb as mrd
from base import BaseHandler
class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        username = self.get_argument('user')
        username2 = tornado.escape.json_decode(self.current_user)
        if username2 == username:
            user_infos = mrd.select_table(table="users", column='*', condition='username', value=username)
            self.render('user.html', users=user_infos)
        else:
            self.render('user.html', users=0)