
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
from UserService import UserService  # 导入UserService模块
from Helper import iPagination
import config

class AccountHandlers(RequestHandler):
    def get(self, h):  
        # 处理HTTP GET请求
        resp_data = {}
        # 前端账户展示
        if h == "index":  
            # 如果h等于"index"
            resp_data = {}

            page = self.get_query_argument("p", default="1")  
            # 获取查询参数p的值，默认为1
            mix_kw = self.get_query_argument('mix_kw', default='')  
            # 获取查询参数mix_kw的值，默认为空字符串
            status = self.get_query_argument('status', default='-1')  
            # 获取查询参数status的值，默认为-1

            req = {
                'status': status,
                'mix_kw': mix_kw,
                'p': page
            }
            user_data = []

            # 参数有效性查询
            if status:
                sql = "select * from user where status='%s'" % (status)
                user_data = self.application.db.get_all_obj(sql, "user")
                print("222222")
                print(user_data)
                print("222222")

            # 混合查询
            if mix_kw:
                sql = "select * from user where nickname like %s or mobile like %s"
                params = [('%' + mix_kw + '%'), ('%' + mix_kw + '%')]
                data = self.application.db.or_(sql, params)
                print("11111")
                print(data)
                print("11111")
                user_data = []
                for item in data:
                    tmp = {
                        'uid':item[0],
                        'nickname': item[1],
                        'mobile': item[2],
                        'email': item[3],
                        'sex': item[4],
                        'avatar': item[5],
                        'login_name': item[6],
                        'login_pwd': item[7],
                        'login_salt': item[8],
                        'status': item[9],
                    }
                    user_data.append(tmp)

            page_params = {
                'total': len(user_data),
                'page_size': config.page['PAGE_SIZE'],
                'page': page,
                'display': config.page['PAGE_DISPLAY'],
                'url': self.request.uri.replace("&p={}".format(page), "")
            }
            print(self.request.uri)

            pages = iPagination(page_params)

            offset = (int(page) - 1) * config.page['PAGE_SIZE']
            limit = config.page['PAGE_SIZE'] * page

            list = []

            if user_data != []:
                list = user_data

            else:
                if status == -1:
                    list = self.application.db.get_all_obj("select * from user order by uid desc limit %s offset %s" % (limit, offset), "user")
                else:
                    list = self.application.db.get_all_obj("select * from user where status=0 order by uid desc limit %s offset %s" % (limit, offset), "user")

            if status == '-1' and mix_kw == '': #默认状态显示的数据（默认：未选择状态，未搜索）
                list = self.application.db.get_all_obj("select * from user order by uid desc limit %s offset %s" % (limit, offset), "user")

            if status == '0':
                print("I am coming")
                list = self.application.db.get_all_obj("select * from user where status==0 order by uid desc limit %s offset %s" % (limit, offset), "user")

            resp_data['list'] = list
            print("list如下：")
            print(list)
            resp_data['pages'] = pages
            resp_data['search_con'] = req
            resp_data['status_mapping'] = config.STATUS_MAPPING

            resp_data['current_user'] = config.options['current_user']
            self.render("account/index.html", resp_data=resp_data)
            # 渲染account/index.html模板并传入resp_data参数

        if h == "set":  # 如果h等于"set"
            resp_data = {}
            resp_data['current_user'] = config.options['current_user']  # 设置当前用户的信息

            uid = self.get_query_argument("id", default=None)  # 获取查询参数id的值，默认为None
            info = {
                'id': uid,
                'nickname': '',
                'mobile': '',
                'email': '',
                'login_name': '',
                'login_pwd': ''
            }
            print(uid)
            if not uid:  # 如果uid为None
                self.render("account/set.html", info=info, resp_data=resp_data)
                # 渲染account/set.html模板并传入info和resp_data参数

            query_info = self.application.db.get_one("select * from user where uid=%s" % (uid))

            print(query_info)
            info = {
                'id': uid,
                'nickname': query_info[1],
                'mobile': query_info[2],
                'email': query_info[3],
                'login_name': query_info[6],
                'login_pwd': '******'
            }

            self.render("account/set.html", info=info, resp_data=resp_data)
            # 渲染account/set.html模板并传入info和resp_data参数

        if h == "test":  # 如果h等于"test"
            data = self.application.db.get_all_obj("select * from user", "user")
            print(data)
            self.write("successfully")

        if h == "info":  # 如果h等于"info"
            resp_data['current_user'] = config.options['current_user']  # 设置当前用户的信息
            self.render("account/info.html", resp_data=resp_data)
            # 渲染account/info.html模板并传入resp_data参数

    def post(self, h):  # 处理HTTP POST请求
        # 添加账号操作
        if h == "set":  # 如果h等于"set"
            default_pwd = "******"  # 设置默认密码
            resp = {
                'code': 200,
                'msg': "操作成功",
                'data': {}
            }

            nickname = self.get_body_argument("nickname", default="")  # 获取表单参数nickname的值，默认为空字符串
            mobile = self.get_body_argument("mobile", default="")  # 获取表单参数mobile的值，默认为空字符串
            email = self.get_body_argument("email", default="")  # 获取表单参数email的值，默认为空字符串
            login_name = self.get_body_argument("login_name", default="")  # 获取表单参数login_name的值，默认为空字符串
            login_pwd = self.get_body_argument("login_pwd", default="")  # 获取表单参数login_pwd的值，默认为空字符串

            uid = self.get_body_argument("id", default="0")  # 获取表单参数id的值，默认为0

            if nickname is None or len(nickname) < 1:  # 如果nickname为None或长度小于1
                resp['code'] = -1
                resp['msg'] = "请输入符合的姓名"
                self.write(resp)  # 将resp作为HTTP响应返回

            if mobile is None or len(mobile) < 1:  # 如果mobile为None或长度小于1
                resp['code'] = -1
                resp['msg'] = "请输入符合的电话"
                self.write(resp)  # 将resp作为HTTP响应返回

            if email is None or len(email) < 1:  # 如果email为None或长度小于1
                resp['code'] = -1
                resp['msg'] = "请输入符合的邮箱"
                self.write(resp)  # 将resp作为HTTP响应返回

            if login_name is None or len(login_name) < 1:  # 如果login_name为None或长度小于1
                resp['code'] = -1
                resp['msg'] = "请输入符合的登录用户名"
                self.write(resp)  # 将resp作为HTTP响应返回

            if login_pwd is None or len(login_pwd) < 1:  # 如果login_pwd为None或长度小于1
                resp['code'] = -1
                resp['msg'] = "请输入符合的登录密码"
                self.write(resp)  # 将resp作为HTTP响应返回

            has_in = self.application.db.get_one("select * from user where login_name='%s' and uid!='%s'" % (login_name, uid))
            if has_in:  # 如果已经存在该用户
                resp['code'] = -1
                resp['msg'] = "该用户已经存在"
                self.write(resp)  # 将resp作为HTTP响应返回

            user_info = self.application.db.get_one("select * from user where uid='%s'" % (uid))

            if user_info:  # 如果用户信息已存在
                login_salt = user_info[8]
                if login_pwd != default_pwd:  # 如果登录密码不等于默认密码
                    login_pwd = UserService.genePwd(login_pwd, login_salt)  # 根据登录密码和盐值生成新的密码
                self.application.db.update("UPDATE user SET nickname='%s',mobile='%s',email='%s',login_name='%s',login_pwd='%s' where uid='%s'" % (nickname, mobile, email, login_name, login_pwd, uid))
            else:  # 如果用户信息不存在
                login_salt = UserService.geneSalt()  # 生成盐值

                if login_pwd != default_pwd:  # 如果登录密码不等于默认密码
                    login_pwd = UserService.genePwd(login_pwd, login_salt)  # 根据登录密码和盐值生成新的密码

                self.application.db.insert("insert into user (nickname,mobile,email,login_name,login_pwd,login_salt) values ('%s','%s','%s','%s','%s','%s')" % (nickname, mobile, email, login_name, login_pwd, login_salt))

            print("successfully")
            self.write(resp)  # 将resp作为HTTP响应返回
