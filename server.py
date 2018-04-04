#!/usr/bin/env Python
# coding=utf-8

import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application
from tornado.options import define, options

define("port", default=8000, type=int, help="default")

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print "端口 http://127.0.0.1:%s"%options.port
    print "使用Control+C退出server"

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()

