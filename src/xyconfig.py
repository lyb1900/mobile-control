'''
@Author: lyb1900
@Date: 2020-05-17 21:28:41
@LastEditTime: 2020-05-17 21:50:08
@LastEditors: lyb1900
@Description: 
@lyb.19@qq.com欢迎讨论优化
'''
import json
import threading

class Xyconfig():
    _instance_lock = threading.Lock()

    def __init__(self):
        with open(r"./config/conf.json",'r') as f:
            conf = f.read()
            f.close()
            self.paras = json.loads(conf)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Xyconfig, "_instance"):
            with Xyconfig._instance_lock:
                if not hasattr(Xyconfig, "_instance"):
                    Xyconfig._instance = object.__new__(cls)  
        return Xyconfig._instance

    def get_install(self):
        return self.paras['install']
