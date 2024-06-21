import tornado.web
from tornado.web import RequestHandler
from UserService import UserService
import config

class UserHandlers(RequestHandler):
    def get(self, h):
        # 退出
        if h == "logout":
            self.redirect(config.domain_url['url'])
        #     print(self.get_cookie(name=config.cookies_name['name'], default='test'))
        # #     清空缓存
        #     print(config.cookies_name['name'])
        #     self.set_header("Set-Cookie", "name={0};Path=/".format(config.cookies_name['name']))
        #     print("***********************")
        #     print(self.get_cookie(name=config.cookies_name['name'], default='test'))



    def post(self):
        pass
