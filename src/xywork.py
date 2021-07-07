
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *

from tkinter import *
import  tkinter #导入TKinter模块

import traceback
import random
import threading
from poco.proxy import UIObjectProxy
from aip import AipOcr
import re

sys.path.append('D:\\code\\mobile-control')
from xydb import *
from mail import *
from xytalker import *
from xydev import *
import time
import json

# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()

# def get_screen_content():
#     snapshot(r"D:\code\autodo\xywork.air\tmp_screen.png")
#     image = get_file_content(r"D:\code\autodo\xywork.air\tmp_screen.png")
#     ret = client.general(image)
#     print(ret)


def init():
    global lock
    global xyDevs
    lock = threading.Lock()
    xyDevs = []
    auto_setup(__file__)
    #配置文件加载
    f = open(r"./config/conf.json",'r')
    conf = f.read()
    f.close()
    paras = json.loads(conf)
    print( paras['dbpath'])
    Mail.mail_init(paras)
    #设备连接
    XyDev.devs_init()
    XyDev.printdevs()
    for devsno in XyDev.devs_getsno():
        xyDevs.append(XyDev(devsno))
        print(devsno)

def getuser(user_text):
    lock.acquire()
    # xyxyapp = xyDeve2.xyxy
    text=user_text.get() #获取文本框内容
    print(text)
    if text == "qd":
        #qianDao()
        #guanQian()
        pass
    elif text == "gq":
        for dev in xyDevs:
            dev.xyxy.guanQian()
    elif text == "find":
        #xyxyapp.collect_relategoods("honor7",False)
        # xyxyapp.collect_relategoods("m30", True)
        # xyxyapp.collect_relategoods("v10", True)
        # xyxyapp.collect_relategoods("u1", False)
        # xyxyapp.collect_relategoods("lephonet7a", False)
        pass
    elif text == "yq":
        pass
        # guanyq()
    elif text == "leave":
        for dev in xyDevs:
            dev.xyxy.collectgoods("XXX", "XXX", 1,3000,True, justsearch=True, message = "加入我的程序员互助鱼塘，置顶你的宝贝，复制这条消息后，打开闲鱼€bSrS1pgx2DS€后打开闲鱼(若是你已经收到过了，那打扰了)",towant = True)
  
    else:

        #collect_relategoods("honor7")
        #collect_relategoods("m30",False)
        
        # collect_relategoods("v10", False)
        # collect_relategoods("u1", False)
        
        #report = analyze_goods()
        #mail_send(report)
        print("不知道做什么")
    lock.release()

def test():
    for dev in xyDevs:
        dev.xyxy.collectgoods("XX", "XXXX", 1,3000,True, justsearch=True, message = "加入我的程序员互助鱼塘，置顶你的宝贝，复制这条消息后，打开闲鱼€bSrS1pgx2DS€后打开闲鱼(帮宣传，若已经收到过，那打扰了)",towant = True)
def talk_everytime():
    while(1):
        sleep(10)
        lock.acquire() 
        # xyDeve2.xyxy.brushup()
        # for dev in xyDevs:
        #     dev.xyxy.detection()
        #     dev.xyxy.goHome()
        #     dev.talker.talk()
        for dev in xyDevs:
            dev.xyxy.collectgoods("XXXX", "XXX", 1,3000,True, justsearch=True, message = "加入我的程序员互助鱼塘，置顶你的宝贝，复制这条消息后，打开闲鱼€bSrS1pgx2DS€后打开闲鱼(若是你已经收到过了，那打扰了)",towant = True)
        lock.release()

#=============界面主程序开始==============
def main():
    init()    
    t1 =threading.Thread(target=talk_everytime)
    t1.setName("talker")
    t1.start()
    ytm=tkinter.Tk() #创建Tk对象
    ytm.title("手机控制智能助手") #设置窗口标题
    ytm.geometry("600x600") #设置窗口尺寸
    l1=tkinter.Label(ytm,text="目前开放闲鱼自动聊天功能，其他功能未开放使用") #标签
    l1.pack() #指定包管理器放置组件
    l2=tkinter.Label(ytm,text="手机序列号") #标签
    l2.pack() #指定包管理器放置组件
    theLB = tkinter.Listbox(ytm,width = 50)
    theLB.pack(side='top', anchor='sw')
    # 往列表里添加数据
    for dev in xyDevs:
        theLB.insert("end", dev.sno)
    l1=tkinter.Label(ytm,text="操作命令") #标签
    l1.pack() #指定包管理器放置组件
    user_text=tkinter.Entry() #创建文本框
    user_text.pack()
    tkinter.Button(ytm,text="确定执行",command=lambda arg = user_text:getuser(arg)).pack() #command绑定获取文本框内容方法
    # user_assign_text = tkinter.Entry()
    # user_assign_text.pack()
    # tkinter.Button(ytm,text="查找",command=lambda arg=user_assign_text:xyDevV10.xyxy.user_find_assign(arg)).pack() #command绑定获取文本框内容方法
    ytm.mainloop() #进入主循环

if __name__ == '__main__':
    #main()
    init() 
    test()











































































