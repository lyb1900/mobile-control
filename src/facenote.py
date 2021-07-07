'''
Description: 电子书打卡
version: 
Author: lyb1900
Date: 2020-08-16 20:52:00
LastEditTime: 2020-08-23 21:39:53
'''

import unittest

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time
import re
import random
import sqlite3           
import traceback
from tkinter import messagebox
import tkinter
import tkinter.simpledialog
# 
class Xyfn():
    dev_index = 0
  
    def __init__(self, dev, db,poco = ""):
        self.dev = dev
        self.db = db
        if (poco != ""):
            self.dev.poco = poco # 测试用字段
        pass
        

        
    def __str__(self):  # 其实一般可能都是这样简单用一下的
        pass


    def goHome(self):
        '''
        @description: 用于各种异常情况回到主页
        @param {type} 
        @return: 
        '''   
        if self.dev.isApp("com.tencent.mm") == False:
            self.dev.runApp("com.tencent.mm")
            sleep(3)
            node = self.dev.poco(text="微信")
            if node.exists():
                node.click()
                sleep(1)
            else:    
                print("找不到微信")
    def askname(self,titlestr):
        # 获取字符串（标题，提示，初始值）
        result = tkinter.simpledialog.askstring(title = '获取信息',prompt=titlestr,initialvalue = '可以设置初始值')
        # 打印内容
        print(result)  
    def atme(self):
        times = 40000
        #self.goHome()
        while(times):
            sleep(2)
            times = times - 1
            node = self.dev.poco(name = "com.tencent.mm:id/cyv",textMatches="\[有人@我\].+")
            if node.exists():
                word = node.get_text()
                print(word)
                #messagebox.showinfo("提示",node.get_text())
                node.click()
                self.askname(word)
                sleep(1)
                self.dev.poco("com.tencent.mm:id/rs").click()

            
    def dianzan(self, times):
        self.goHome()
        while(times):
            times = times - 1
            index = random.randint(0,7)
            sleep(index)
            node = self.dev.poco("com.tencent.mm:id/g2s").child("android.widget.FrameLayout").child("android.widget.LinearLayout")\
            .offspring("com.te0n0cent.mm:id/fol").child("com.tencent.mm:id/fn9")
            if node.exists():
                node = node[0].offspring("com.tencent.mm:id/fn8").offspring("com.tencent.mm:id/ik")
                if node.exists():
                    node.click()
                    zannode = self.dev.poco("com.tencent.mm:id/i9")
                    if zannode.exists():
                        if zannode.get_text() == "赞":
                            zannode.click()
                        else:
                            print("是取消不要点")
                    else:
                        node = self.dev.poco(text="拍摄") #防出错处理
                        if node.exists():
                            self.dev.clickBack()
            else:
                print("node no find")
            swipe(self.dev.rToA(0.5,0.8),self.dev.rToA(0.5,0.5))
 
def fnmain():
    auto_setup(__file__)
    dev = connect_device("android:///")
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    vxdb = "no db"
    #xyvx = Xyfn(dev,vxdb,poco)
    #xyvx.atme()
    #xyvx.dianzan(100)
    while(1):
        index = random.randint(0,7)
        sleeptime = 10 + index
        print("sleep time is " +str(sleeptime))
        sleep(sleeptime)
            
        keyevent("KEYCODE_VOLUME_DOWN")
    #     xylp.huntnew()
    #     #poco.swipe([-0.0352, -0.5879])
    #     swipe(xylp.rToA(0.5,0.8),xylp.rToA(0.5,0.1))

# main()
if __name__ == '__main__':
    #unittest.main()
    fnmain()

