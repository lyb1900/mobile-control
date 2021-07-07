import unittest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.core.android.adb import *
from xyxy import *
from xydb import *
from xytalker import *
from xyvx import *
import os
import subprocess
import re

class XyDev():
    dev_index = 0
    devsinfo = []
    devs_sno = []
    @classmethod
    def devs_init(cls):
        # devices = subprocess.Popen(
        # 'adb devices'.split(),
        # stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE
        # ).communicate()[0]       
        # before = "" 
        # for item in devices.split():
        #     before = item
        #     if item.lower()  == "device":
        #         if before is not "":
        #             cls.serial_sno.append(before)
        cls.devsinfo = ADB().devices(state="device")
        for dev in cls.devsinfo:
             cls.devs_sno.append(dev[0]) 
    @classmethod
    def devs_get(cls):
        return cls.devsinfo
    @classmethod
    def devs_getsno(cls):
        return cls.devs_sno

    @classmethod
    def printdevs(cls):
        print(cls.devsinfo)
    def __init__(self, sno):
        uri = 'Android://127.0.0.1:5037/' + sno
        self.sno = sno
        self.uri = uri
        self.dev = connect_device(uri)
        self.dev_index = XyDev.dev_index
        XyDev.dev_index = XyDev.dev_index + 1
        #dbpath = r"D:\code\mobile-control\{0}.db".format(self.sno)
        dbpath = r"D:\code\mobile-control\common.db"
        XyDev.db = Xydb(dbpath)
        print("connect dev:" + uri + str(self.dev_index))
        self.poco = AndroidUiautomationPoco(self.dev)
        self.xyxy = XyXy(self,XyDev.db)
        self.xyvx = Xyvx(self,XyDev.db)
        self.width, self.height = self.dev.get_current_resolution()
        self.resolution = (self.width, self.height)
        #self.dev.shell("am startservice ca.zgrs.clipper/.ClipboardService")
        #self.talker = XyTalker(self,self.poco)
    def devairop(self,op, str):
        set_current(self.sno)
        op(str)
        # start_app("com.taobao.idlefish")

    def updatepoco(self):
        set_current(self.sno)
        ##self.dev = device()
        self.poco = AndroidUiautomationPoco(self.dev)

    def get_top_activity(self):
        set_current(self.sno)
        ##self.dev = device()
        return self.dev.get_top_activity()

    def isApp(self,str):
        set_current(self.sno)

        app = self.dev.get_top_activity()
        if app is not None:
            return app[0] == str
        return False

    def shell(self,str):
        set_current(self.sno)
        #self.dev = device()
        self.dev.shell(str)
    def touch(self, v):
        try:
            set_current(self.sno)
            #self.dev = device()
            touch(v)
        except:
            print("no find pic")

    def text(self,str):
        set_current(self.sno)
        #self.dev = device()
        text(str)

    def __str__(self):  # 其实一般可能都是这样简单用一下的
        return self.uri

    def key(self, key):
        set_current(self.sno)
        keyevent(key)

    def runApp(self, appName):
        set_current(self.sno)
        #self.dev = device()
        start_app(appName)


    def clickPosDelay1s(self,pos):
        if pos.exists():
            pos.click()
            time.sleep(1)

    def clickPosDelay2s(self,pos):
        if pos.exists():
            pos.click()
            time.sleep(2)

    def clickDelay1s(self,x, y):
        click(x,y)
        time.sleep(1)

    def clickDelay2s(self,x, y):
        click(x,y)
        time.sleep(2)

    def clickBack(self):
        set_current(self.sno)
        #self.dev = device()
        keyevent("BACK")
        time.sleep(1)

    def clickBack2S(self):
        set_current(self.sno)
        #self.dev = device()
        keyevent("BACK")
        time.sleep(2)

    def relativeToAbsolute(self,x,y):
        x = self.width * x
        y = self.height * y
        return x,y

    def rToA(self,x,y):
        x = self.width * x
        y = self.height * y
        return x,y


    def movePageUp(self):
        set_current(self.sno)
        #self.dev = device()
        swipe(self.rToA(0.5,0.8),self.rToA(0.5,0.1))

    def devswipe(self, list):
        set_current(self.sno)
        swipe(list[0],list[1])

    def movePageDown(self):
        set_current(self.sno)
        #self.dev = device()
        swipe(self.rToA(0.5,0.1),self.rToA(0.5,0.8))

    # def findAndClickPic(pic):
    #     try:
    #         touch(Template(pic, resolution))
    #         print("在手机屏幕找到" + pic)
    #         return 0
    #     except TargetNotFoundError:
    #         print("没找到"+ pic)
    #         return 1

    # def findPicArea(pic, x, y):
    #     ret = exists(Template(pic, record_pos=(x, y), resolution = resolution))
    #     if ret == False: 
    #         return 1
    #     else:
    #         return 0



class XyDevTest(unittest.TestCase):
    def setUp(self):
        '''
        测试之前的准备工作
        :return:
        '''
        print("setup")
        pass

    def tearDown(self):
        '''
        测试之后的收尾
        如关闭数据库
        :return:
        '''
        print("teardown")
        pass
    
    def test_init(self):
        #xyDeve2 = XyDev('Android://127.0.0.1:5037/741AEDQK25YX7')
        #xyDevv10 = XyDev('Android://127.0.0.1:5037/P7C0217C08001294')
        xyDevt10a = XyDev('Android://127.0.0.1:5037/ST52HZCMB7C07FB11565')
        # adb = ADB()
        # devicesList = adb.devices()
        # print(devicesList)
        #print(xyDeve2)
        print(xyDevt10a)
        #xyDevt10a.devairop(start_app,"com.taobao.idlefish")
        xyDevt10a.xyxy.goHome()

    def test_add(self):
        pass

    def test_sub(self):
        pass

# def main():
#     db = Xydb("e:\\xy1.db")
#     db.upgrade1()

# main()
if __name__ == '__main__':
    unittest.main()



# PACKAGE = "com.when.coco"
# START_ACTIVITY = "Login"
# INSTALL_PATH = "/Users/blue/Downloads/test.apk"

# # 获得当前设备列表
# adb = ADB()
# devicesList = adb.devices()
# # 连几台基本上是知道的,也可以判断一下是否满足需要,如果不够就报个错
# devicesNum = len(devicesList) > 1
# assert_equal(devicesNum,True,"设备连接数量至少为2")

# # 连接手机 默认连接方式
# connect_device("android:///")
# # 指定设备号连接
# connect_device("android:///" + devicesList[0][0])

# android = Android()
# #判断手机上是否安装包
# try:
#     android.check_app(PACKAGE)
# except AirtestError:
#     # 安装应用,是否同意覆盖安装,默认否
#     android.install_app(INSTALL_PATH,False)
    
#     # 有的手机不能直接安装,有个弹窗需要点,比如小米.
#     # 我通过刷开发版,开启root,关闭了这个弹窗,还有应用权限监控
#     # 除了安装特别慢之外,一切还算正常了
    
#     # 覆盖安装举个例子
#     android.install_app(INSTALL_PATH,True)
        
# # 清空包数据,有的手机没有权限,相当尴尬
# try:
#     clear_app(PACKAGE)
# except:
#     # 卸载App
#     uninstall(PACKAGE)
#     # 安装应用
#     install(INSTALL_PATH)

# # 启动应用,可以带Acitvity,也可以不带   
# start_app(PACKAGE, START_ACTIVITY)
# # 休眠两秒
# sleep(2)
# # 停止应用
# stop_app(PACKAGE)

# # 切换手机
# connect_device("android:///" + devicesList[1][0])

# clear_app(PACKAGE)
# uninstall(PACKAGE)
# install(INSTALL_PATH)
# # 启动App,不带Activity
# start_app(PACKAGE)
# sleep(2)
# stop_app(PACKAGE)    