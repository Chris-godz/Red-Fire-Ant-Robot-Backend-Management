import tornado.web
from tornado.web import RequestHandler
from UserService import UserService
import config
import os
import tornado.ioloop
import tornado.escape
from views import test
import json



class ChartsHandlers(RequestHandler):
    def get(self):
        resp_data = {}
        resp_data['current_user'] = config.options['current_user']
        self.render("charts.html", resp_data=resp_data)
    
       