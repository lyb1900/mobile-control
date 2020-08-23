'''
@Author: lyb1900
@Date: 2020-05-23 17:59:32
@LastEditTime: 2020-05-24 21:02:10
@LastEditors: lyb1900
@Description: 
@lyb.19@qq.com欢迎讨论优化
'''

import unittest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
import time
import re
import random
import sqlite3           
import traceback


class HuntUser():
    def __init__(self):
        self.label =""
        self.company=""
        self.state=""
        self.email=""
        self.sex=""
        self.salary=""
                
    def __str__(self):
        print(self.name)


class HuntUserDb():
    
    def __init__(self, file):
        self.file = file
        #数据库初始化
        #创建一个连接对象，连接到本地数据库
        self.conn=sqlite3.connect(file)
        self.conn.execute("""create table if not exists user_info (
        id integer PRIMARY KEY AUTOINCREMENT, 
        name text, 
        label text,
        realname text,
        job_state text,
        sex text, 
        age text,
        email text,
        company text, 
        salary text,
        work_dese text, 
        update_date DATE, 
        insert_date DATE)""")



    def find_same_name(self,huntuser):
        cursor = self.conn.cursor()
        cursor.execute("select * from user_info where name ='{}' and label = '{}'".format(huntuser.name,huntuser.label))
        result = cursor.fetchall()
        if len(result) == 0:
            print("no find")
            cursor.close()
            return 1
        else:
            return 0

    def insert(self,huntuser):
        if self.find_same_name(huntuser) != 0:
            # 插入一条数据
            nowdate = time.strftime("%Y-%m-%d", time.localtime())
            dbstr = 'insert into user_info (name, label, company, job_state, email, work_dese, insert_date, sex, salary) values ("{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
                huntuser.name,
                huntuser.label,
                huntuser.company,
                huntuser.state, 
                huntuser.email,
                huntuser.state,
                nowdate,
                huntuser.sex,
                huntuser.salary
                )
            #print(dbstr)
            self.conn.execute(dbstr)
            self.conn.commit()
            print("insert" + huntuser.name + "success")
        else:
            print("has the same")
            #self.update(str(price),star,des,url,leavemessage)
# v4.32.0
class XyLp():
    dev_index = 0
  
    def __init__(self, dev, db,poco = ""):
        self.dev = dev
        self.db = db
        if (poco != ""):
            self.dev.poco = poco # 测试用字段
        pass
        self.width, self.height = self.dev.get_current_resolution()
        
    def rToA(self,x,y):
        x = self.width * x
        y = self.height * y
        return x,y
        
    def __str__(self):  # 其实一般可能都是这样简单用一下的
        pass


    def goHome(self):
        '''
        @description: 用于各种异常情况回到主页
        @param {type} 
        @return: 
        '''   
        if self.dev.isApp("com.lietou.mishu") == False:
            self.dev.runApp("com.lietou.mishu")

    def huntnew(self):
        node = self.dev.poco(name = "com.lietou.mishu:id/user_name")
        for user in node:
            huntuser = HuntUser()
           
            huntuser.name = user.get_text()
            
            # other_info_node = user.sibling("com.lietou.mishu:id/user_other_info")
            # other_info_node.wait_for_appearance()
            # if other_info_node.exists():
            #     huntuser.label = other_info_node.get_text()
            # sex_node = user.sibling("com.lietou.mishu:id/user_sex")
            # sex_node.wait_for_appearance()
            # if sex_node.exists():
            #     huntuser.sex = sex_node.get_text()
            # salary_node = user.sibling("com.lietou.mishu:id/salary")
            # salary_node.wait_for_appearance()
            # if salary_node.exists():
            #     huntuser.salary = salary_node.get_text()

            # if 0 == self.db.find_same_name(huntuser):
            #     print("find same user" + huntuser.name)
            # else:    
            user.click()

            sleep(1)
            company_node = self.dev.poco("com.lietou.mishu:id/aoto_company_positon")
            if company_node.exists():
                huntuser.company = company_node.get_text()
            state_node =  self.dev.poco("com.lietou.mishu:id/tv_job_state")
            if state_node.exists():
                huntuser.state =state_node.get_text()
            email_node = self.dev.poco("com.lietou.mishu:id/tv_email")
            if email_node.exists():
                huntuser.email = email_node .get_text()
            work_node = self.dev.poco("com.lietou.mishu:id/tv_work_dese")
            if work_node.exists():
                huntuser.des = work_node.get_text()
            for onelabel in self.dev.poco("com.lietou.mishu:id/tv_label_text"):
                huntuser.label = huntuser.label+ " " + onelabel.get_text()
            
            self.dev.poco("com.lietou.mishu:id/btn_submit").click()
            sleep(1)
            self.dev.poco("com.lietou.mishu:id/chat_left_group").click()
            sleep(1)
            self.dev.poco("com.lietou.mishu:id/ib_menu_back").click()
            sleep(1)
            self.db.insert(huntuser)
            print(user.get_text())
        # for user in nodelist:


class XyLpTest(unittest.TestCase):
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
        pass

    def test_add(self):
        auto_setup(__file__)
        dev = connect_device("android:///")
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        lpdb = HuntUserDb("d://huntuser.db")
        xylp = XyLp(dev,lpdb,poco)
        while(1):
            sleep(10)
            xylp.huntnew()
            #poco.swipe([-0.0352, -0.5879])
            swipe(xylp.rToA(0.5,0.8),xylp.rToA(0.5,0.1))

        pass

    def test_sub(self):
        pass

def main():
    auto_setup(__file__)
    dev = connect_device("android:///")
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    lpdb = HuntUserDb("d://huntuser.db")
    xylp = XyLp(dev,lpdb,poco)
    while(1):
        sleep(10)
        xylp.huntnew()
        #poco.swipe([-0.0352, -0.5879])
        swipe(xylp.rToA(0.5,0.8),xylp.rToA(0.5,0.1))

# main()
if __name__ == '__main__':
    #unittest.main()
    main()


