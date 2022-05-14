from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
from airtest.core.android.adb import *

import unittest
import traceback
import time
import re
class XyUtil():
    def findAndClickPic(pic,resolution):
        try:
            touch(Template(pic, resolution))
            print("在手机屏幕找到" + pic)
            return 0
        except TargetNotFoundError:
            print("没找到"+ pic)
            return 1
        except :
            print("未知")

    def findPicArea(pic, x, y, resolution):
        ret = exists(Template(pic, record_pos=(x, y), resolution = resolution))
        if ret == False: 
            return 1
        else:
            return 0

