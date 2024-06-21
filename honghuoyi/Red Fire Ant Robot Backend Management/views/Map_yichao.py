 
# -*- coding: utf-8 -*-
from decimal import Decimal
from tornado.web import RequestHandler
from Helper import iPagination
import config
import json
from datetime import datetime
import base64
import io
from PIL import Image

class Map_yichaoHandlers(RequestHandler):
    def get(self, h):  
        # 处理HTTP GET请求
        resp_data = {}
        # 前端账户展示
        if h == "index":  
            # 如果h等于"index"
            resp_data = {}
            resp_data['status_mapping'] = config.STATUS_MAPPING
            resp_data['current_user'] = config.options['current_user']
            self.render("map_yichao/index2.html", resp_data=resp_data)
            # 渲染account/index.html模板并传入resp_data参数

        
        if h == "api_yicaho":
            yichao_list = self.application.db.get_all_obj("select * from yichao","yichao")
            def convert_to_json_compatible(value):
                if isinstance(value, Decimal):
                    return float(value)
                elif isinstance(value, datetime):
                    return value.strftime('%Y-%m-%d %H:%M:%S')
                else:
                    return value

            if len(yichao_list)==1:
                for k,v in yichao_list:
                    yichao_list[k] = convert_to_json_compatible(v) 
            elif len(yichao_list) > 1:
                for i in range(len(yichao_list)):
                    yichao = yichao_list[i]
                    keys_list = ['id', 'longitude', 'latitude', 'image', 'date', 'is_sanitized']  # 使用不同的变量名
                    for k in keys_list:
                        yichao[k] = convert_to_json_compatible(yichao[k])
                    yichao_list[i] = yichao

            # 更新原响应数据中的'data'部分
            resp_data['yichao'] = yichao_list #resp_data['yichao'] 是所有的蚁巢信息
            resp_data['current_user'] = config.options['current_user']  # 设置当前用户的信息
            json_str = json.dumps(resp_data, ensure_ascii=True)
            self.write(json_str)  