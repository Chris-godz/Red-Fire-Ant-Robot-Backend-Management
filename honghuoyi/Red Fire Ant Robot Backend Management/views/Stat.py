import tornado.web
from tornado.web import RequestHandler
from UserService import UserService
import config

class StatHandlers(RequestHandler):
    def get(self, h):
        if h == "index":
            resp_data = {}
            resp_data['current_user'] = config.options['current_user']

            self.render("stat/index.html", resp_data=resp_data)

        pass
