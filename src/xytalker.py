# -*- encoding=utf8 -*-
__author__ = "lyb19"

from airtest.core.api import *

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import re
import random
import traceback
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# auto_setup(__file__)
# dev = connect_device("android:///")


# ---- 这才是ChatterBot的业务逻辑
from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
# Create a new chat bot named Charlie




# trainer = ChatterBotCorpusTrainer(my_bot)

# trainer.train(
#     "chatterbot.corpus.chinese"
# )

# trainerlist = ListTrainer(my_bot)


# trainerlist.train([
#     "在",
#     "在的"
# ])

# ret = my_bot.get_response("在")
# print(ret)


# dev.shell("am start service ca.zgrs.clipper/.ClipboardService")
# dev.shell("am broadcast -a clipper.set -e text abc")
# url = dev.shell("am broadcast -a clipper.get")
# print("%%%%%%%%%%%%%%")
# print(url)
# #keyevent("BACK")

class XyTalker():
    def __init__(self,dev,poco):
        self.m30robot = ChatBot("m30robot", storage_adapter="chatterbot.storage.SQLStorageAdapter",database_uri='sqlite:///d:\\m30robot.db')
        self.v10robot = ChatBot("v10robot", storage_adapter="chatterbot.storage.SQLStorageAdapter",database_uri='sqlite:///d:\\v10robot.db')
        self.u1robot = ChatBot("u1robot", storage_adapter="chatterbot.storage.SQLStorageAdapter",database_uri='sqlite:///d:\\u1robot.db')
        self.poco = poco
        self.dev = dev

    def get_new_message(self):
        element = self.poco("com.taobao.idlefish:id/fnml_list").children()
        last = None
        if element.exists() == False:
            return None
        for e in element:
            node =e.offspring("com.taobao.idlefish:id/cell_stub").child("android.widget.LinearLayout").offspring("com.taobao.idlefish:id/fl_content").child("com.taobao.idlefish:id/cell_text")
            if (node.exists()):    
                word = node.get_text()
                print("find word" + word)
            else:
                print("word no find")
                continue
            my = e.offspring("com.taobao.idlefish:id/cell_stub").offspring("com.taobao.idlefish:id/iv_pic_right")
            if my.exists():
                last = "me"
            else:
                last = "other"
                username_node =  e.offspring("com.taobao.idlefish:id/cell_stub").child("android.widget.LinearLayout").child("android.widget.LinearLayout").offspring("com.taobao.idlefish:id/chat_username")
                
                if username_node.exists():
                    print("find name" + username_node.get_text())
                else:
                    print("username no find")
        if (last == "other"):
            return word
        else:
            return None
    
    def send_new_message(self,word):
        debug = True
        if debug == True:
                self.poco("com.taobao.idlefish:id/pond_chat_box_content").click()
                
                message = ["可以加到XXXX",
                "XXXXX1",
                "XXXXX2",
                "XXXXX3"]
                index = random.randint(0,len(message) - 1)
                self.dev.text("[自动回答]" + message[index])
                self.poco("com.taobao.idlefish:id/chat_send_button").click()
                self.dev.key("BACK")
        else:
            price = self.poco("com.taobao.idlefish:id/tv_price").get_text()
            robot = None
            match = re.search(r"(¥\s)(\d+)", price)
            if match:
                matchprice = match.groups(0)[1]
                print(match.groups(0)[1])
            else:
                matchprice = 0
                print("no match")
            if (int(matchprice) < 120):
                robot = self.m30robot
            else:
                self.poco("com.taobao.idlefish:id/pond_chat_box_content").click()
                index = random.randint(0,7)
                message = ["有的,可以拍",
                "走平台交易保证安全",
                "已经很优惠了，不用犹豫",
                "还等什么呢",
                "有货的，可以直接拍下",
                "机子功能都是好的",
                "可以看下描述",
                "东西还不错的呢"]
                self.dev.text("[自动回答]" + message[index])
                self.poco("com.taobao.idlefish:id/chat_send_button").click()
                self.dev.key("BACK")
            if robot != None:
                self.poco("com.taobao.idlefish:id/pond_chat_box_content").click()
                rep = robot.get_response(word)
                print("回答"+ rep.text)
                self.dev.text("[自动回答]" + rep.text)
                self.poco("com.taobao.idlefish:id/chat_send_button").click()
                self.dev.key("BACK")
    
    def talk(self):
        try:
            messagenum = 0
            message_node_un = self.poco("android:id/content").offspring("消息，未选中状态")
            if message_node_un.exists():
                message_node_un.offspring("com.taobao.idlefish:id/tab_icon").click()
            else:
                message_node = self.poco("android:id/content").offspring("消息，选中状态")
                if message_node.exists():
                    messagenum_node = message_node.offspring("com.taobao.idlefish:id/msg_tag_debug_text_id")
                    if messagenum_node.exists():
                        messagenum = messagenum_node.get_text()
            print("find message num :", messagenum)
            #有时可能找不到messagenum_node，所以无论如何也要尝试在fnml_list中找下
            if int(messagenum) >= 0:
                messagelist_node = self.poco("android:id/content").offspring("com.taobao.idlefish:id/id_pager").child("android.widget.FrameLayout").offspring("com.taobao.idlefish:id/fnml_list")
                if messagelist_node.exists():
                    for msg_node in messagelist_node.child("android.widget.RelativeLayout"):
                    #msg_node.offspring("com.taobao.idlefish:id/vmmici_item_logo").click()
                        one_persion_msg = msg_node.offspring("com.taobao.idlefish:id/msg_tag_debug_text_id")
                        if one_persion_msg.exists():
                                msgnum = one_persion_msg.get_text()
                                if (msgnum != None):
                                    if (int(msgnum) > 0 ):
                                        one_persion_msg.click()
                                        ret = self.get_new_message()
                                        if (ret != None):
                                            self.send_new_message(ret)
                                        self.dev.key("BACK")
                                    else:
                                        print("no new message,find next")
                                else:
                                    print("get msgnum failed")
                        else:
                                print("one_persion_msg no exists")
            #poco("android:id/content").offspring("消息，选中状态").offspring("com.taobao.idlefish:id/msg_tag_debug_text_id").click()
        except:
            print("oooo")
            traceback.print_exc()
            print("fail")    

# ret = get_new_message()
# print("result :" + ret)
# def pocoFind(self,name, times):
#     if times == 0:
#         return 1
#     if name == "home":
#         pos = poco("android:id/content").offspring("闲鱼，未选中状态").offspring("com.taobao.idlefish:id/tab_icon") 
#         if pos.exists():
#             pos.click()
#             print("找到闲鱼")
#             return 0
#         else: 
#             print("没有找到")
#             pos = poco("android:id/content").offspring("闲鱼，选中状态").offspring("com.taobao.idlefish:id/tab_icon") 
#             if pos.exists():
#                 pos.click()
#                 print("找到闲鱼")
#                 return 0
#             else: 
#                 print("没有找到")
#                 keyevent("BACK")
#                 if pocoFind("home", times-1) == 0:
#                     return 0
#                 else:
#                     return 1
#     else:
#         return 1                 
# def runApp(appName):
#     start_app(appName)
#     sleep(2)
    
# def goHome():
#     runApp("com.taobao.idlefish")
#     return pocoFind("home", 5)
#     #while i < 5 :
#     #    return 0
#     #findPicArea()

# while(1):
#     sleep(10)
#     goHome()
#     try:
#         messagenum = 0
#         message_node_un = poco("android:id/content").offspring("消息，未选中状态")
#         if message_node_un.exists():
#             message_node_un.offspring("com.taobao.idlefish:id/tab_icon").click()
#         else:
#             message_node = poco("android:id/content").offspring("消息，选中状态")
#             if message_node.exists():
#                 messagenum_node = message_node.offspring("com.taobao.idlefish:id/msg_tag_debug_text_id")
#                 if messagenum_node.exists():
#                     messagenum = messagenum_node.get_text()
#         print("find message num :", messagenum)
#         #有时可能找不到messagenum_node，所以无论如何也要尝试在fnml_list中找下
#         if int(messagenum) >= 0:
#             messagelist_node = poco("android:id/content").offspring("com.taobao.idlefish:id/id_pager").child("android.widget.FrameLayout").offspring("com.taobao.idlefish:id/fnml_list")
#             if messagelist_node.exists():
#                 for msg_node in messagelist_node.child("android.widget.RelativeLayout"):
#                    #msg_node.offspring("com.taobao.idlefish:id/vmmici_item_logo").click()
#                    one_persion_msg = msg_node.offspring("com.taobao.idlefish:id/msg_tag_debug_text_id")
#                    if one_persion_msg.exists():
#                         msgnum = one_persion_msg.get_text()
#                         if (msgnum != None):
#                             if (int(msgnum) > 0 ):
#                                 one_persion_msg.click()
#                                 ret = get_new_message()
#                                 if (ret != None):
#                                     send_new_message(ret)

#                                     keyevent("BACK")
#                             else:
#                                 print("no new message,find next")
#                         else:
#                             print("get msgnum failed")
#                    else:
#                         print("one_persion_msg no exists")
#         #poco("android:id/content").offspring("消息，选中状态").offspring("com.taobao.idlefish:id/msg_tag_debug_text_id").click()

#     except:
#         print("oooo")
#         traceback.print_exc()
#         print("fail")





