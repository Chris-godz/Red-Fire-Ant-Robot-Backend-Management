
# 路由映射子表
import tornado.web
import config
from views import index
from views import account
from views import User, Command, Stat, Eye,charts,Map,Map_yichao

# 引入数据库
from usrSQL import usrSQL
from interceptor import Interceptor

class Application(tornado.web.Application):
    def __init__(self):
        # 映射路由表
        handlers = [

            # 登录入口
            (r'/login', index.LoginHandlers),
            # 后台首页
            (r'/', index.IndexHandlers),
            # 分页路由
            (r'/map/(\w+)', Map.MapHandlers),
            (r'/map_yichao/(\w+)', Map_yichao.Map_yichaoHandlers),
            (r'/charts', charts.ChartsHandlers),
            (r'/account/(\w+)', account.AccountHandlers),
            (r'/user/(\w+)', User.UserHandlers),
            (r'/command/(\w+)', Command.CommandHandlers),
            (r'/stat/(\w+)', Stat.StatHandlers),
            (r'/eye/(\w+)', Eye.EyeHandlers),
         
           

        ]

        super(Application, self).__init__(handlers, **config.settings)
        self.db = usrSQL(config.mysql["host"], config.mysql["user"], config.mysql["password"], config.mysql["database"])
        self.inter = Interceptor(config.options['url'])




