import unittest
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import *
import time
import re
import random
                      
import traceback

class XyXy():
    dev_index = 0
  
    def __init__(self, dev,db,find_url = False):
        self.dev = dev
        self.db = db
        self.find_url = find_url
        pass

    def __str__(self):  # 其实一般可能都是这样简单用一下的
        pass

    def pocoFind(self, name, times):
        if times == 0:
            return 1
        if name == "home":
            pos = self.dev.poco("android:id/content").offspring("闲鱼，未选中状态").offspring("com.taobao.idlefish:id/tab_icon") 
            if pos.exists():
                pos.click()
                time.sleep(1)
                print("找到闲鱼")
                return 0
            else: 
                print("没有找到")
                pos = self.dev.poco("android:id/content").offspring("闲鱼，选中状态").offspring("com.taobao.idlefish:id/tab_icon") 
                if pos.exists():
                    pos.click()
                    time.sleep(1)
                    print("找到闲鱼")
                    return 0
                else: 
                    print("没有找到")
                    self.dev.key("BACK")
                    if self.pocoFind("home", times-1) == 0:
                        return 0
                    else:
                        return 1
        else:
            return 1        
                    
    def goHome(self):
        if self.dev.isApp("com.taobao.idlefish") == False:
            self.dev.runApp("com.taobao.idlefish")
            time.sleep(6)
            #self.dev.updatepoco()
        self.detection()
        return self.pocoFind("home", 5)
        #while i < 5 :
        #    return 0
        #findPicArea()


    def action_message(self):
        node = self.dev.poco(text="留言")
        if node.exists():
            node.click()
            index = random.randint(0,7)
            message = ["我也便宜出手机",
            "同出，楼主优先",
            "怎么没人看我的闲置手机呢",
            "我也有手机，便宜出售",
            "急出，我的手机更便宜些呢",
            "看我的手机，我的更便宜些呢",
            "这手机我也便宜出，楼主优先",
            "我的手机也便宜出，楼主优先"]
            self.dev.text(message[index])
            sendnode = self.dev.poco("com.taobao.idlefish:id/send_button")
            if sendnode.exists():
                sendnode.click()
    def brushup(self):
        if self.goHome() != 0:
            return 
        self.clickMy()
        node = self.dev.poco(textMatches="我发布的.*")
        if node.exists():
            node.click()
            for i in range(8):
                for node in self.dev.poco(textMatches=".*留言.*").parent().offspring():
                    for brushup in node.child("android.widget.FrameLayout").offspring("擦亮"):
                        brushup.click()
                        self.dev.devswipe([-0.0071, -0.3877])
                self.dev.devswipe([-0.0071, -0.3877])            
    def collectciycle1(self,goods,goodsname,toleavemessage):
        poslist = [[0.24,0.35],[0.75,0.35],[0.24,0.74],[0.75,0.74]]
        for i in range(80):
            for pos in poslist:
                self.dev.poco.click(pos)
                time.sleep(2)
                star = 0
                
                element=self.dev.poco(textMatches=".*现价\d+.*")
                if element.exists():
                    pricestr = element.get_text()
                else:
                    pricestr = ""
                if pricestr:
                    match = re.search(r"现价(\d+)", pricestr)
                    if match:
                        price = match.groups(0)[0]
                items = element.sibling()
                
                if items.exists():
                    for item in items:
                        print(item.get_text())
                    desc = items[0].get_text()            
                    equitprice = self.goods_equitable_price(goodsname)
                    getdetail = 0 
                    urlstr =""
                    print("price :" + price + "  " + str(equitprice))
                    if int(price) <= equitprice:
                        print("adbadf")
                        urlstr = self.db.find_and_get_url(desc)
                        if urlstr == "":
                            getdetail = 1
                    if toleavemessage:
                        toleavemessage = self.db.find_and_get_leavemessage(desc)
                        if toleavemessage == False:
                            self.action_message()
                            toleavemessage = True

                    print(getdetail)       
                    if (getdetail == 1):   
                        pos = self.dev.poco(text="更多")
                        if pos.exists():
                            pos.click()
                            time.sleep(1)
                        else: 
                            self.dev.key("BACK")
                            continue
                        try:        
                            pos = self.dev.poco("android.widget.FrameLayout").offspring("com.taobao.idlefish:id/share_main_content_root").offspring("com.taobao.idlefish:id/share_native_targets_view").child("android.widget.LinearLayout")[1].child("com.taobao.idlefish:id/target_item_image")
                        except:
                            traceback.print_exc()
                        if pos.exists():
                            pos.click()
                            time.sleep(1)
                        else: 
                            self.dev.key("BACK")
                            continue
                        clip = self.dev.shell("am broadcast -a clipper.get")
                        url = re.search('data="(.*)"', clip)    
                        if url:
                            #print(url)
                            print(url.groups(0)[0])
                            urlstr = url.groups(0)[0]
                        else:
                            print("no url match")
                            urlstr = ''
                        self.dev.key("BACK")                
                    self.db.insert(goodsname,str(price),star, desc,urlstr,toleavemessage)
                else:
                    print("no get text")
                    self.dev.poco.swipe([-0.0977, -0.8247])
                    i = i + 1



    def collectciycle(self,goods,goodsname,toleavemessage):
        for i in range(80):
            # poco = AndroidUiautomationPoco()
            # 闲鱼6.6.70之后的版本无法实时刷新，需要关闭再刷新
            # 为了保证poco树能实时刷新，关闭pocoservcie，关闭后会被自动拉起
            # dev.shell("am force-stop com.netease.open.pocoservice")
            # sleep(4)
            #poco = AndroidUiautomationPoco()

            element=self.dev.poco(text=goods).parent().offspring()
            if element.exists():
                j = 0
                for name in element:
                    nodestr = name.get_text()
                    if nodestr:

                        if nodestr.lower().find("￥".lower())!=-1:
                            j = j + 1
                            if self.db.match_gooodsname(nodestr,goodsname) == False:
                                if j == 4:
                                    time.sleep(2)
                                    name.swipe([-0.0977, -0.8247])
                                    break
                                else:
                                    continue
                            #print(nodestr)
                            print("==========")
                            match = re.search(r"(.*\n)(￥\n)(\d+)", nodestr)
                            if match:
                                desc = match.groups(0)[0]
                                price = match.groups(0)[2]
                                print(match.groups(0)[2])
                            else:
                                price = 0
                                print("no match")

                            match = re.search(r"\n(\d+)人想要", nodestr)
                            if match:
                                star = match.groups(0)[0]
                                print(match.groups(0)[0])
                            else:
                                star = 0
                                print("no match")

                            equitprice = self.goods_equitable_price(goodsname)
                            getdetail = 0 
                            urlstr =""
                            print("price :" + price + "  " + str(equitprice))
                            if self.find_url == True and int(price) <= equitprice:
                                urlstr = self.db.find_and_get_url(desc)
                                if urlstr == "":
                                    getdetail = 1
                            if toleavemessage:
                                toleavemessage = self.db.find_and_get_leavemessage(desc)
                                if toleavemessage == False:
                                    name.click()
                                    time.sleep(2)
                                    self.action_message()
                                    self.dev.key("BACK")
                                    toleavemessage = True

                            print(getdetail)       
                            if (getdetail == 1):   
                                name.click()
                                time.sleep(2)
                                pos = self.dev.poco(text="更多")
                                if pos.exists():
                                    pos.click()
                                else: 
                                    if j == 4:
                                        time.sleep(2)
                                        name.swipe([-0.0977, -0.8247])
                                        break
                                    else:
                                        continue
                                try:        
                                    pos = self.dev.poco("android.widget.FrameLayout").offspring("com.taobao.idlefish:id/share_main_content_root").offspring("com.taobao.idlefish:id/share_native_targets_view").child("android.widget.LinearLayout")[1].child("com.taobao.idlefish:id/target_item_image")
                                except:
                                    traceback.print_exc()
                                if pos.exists():
                                    pos.click()
                                    time.sleep(1)
                                else: 
                                    if j == 4:
                                        time.sleep(2)
                                        name.swipe([-0.0977, -0.8247])
                                        break
                                    else:
                                        continue
                                clip = self.dev.shell("am broadcast -a clipper.get")
                                url = re.search('data="(.*)"', clip)    
                                if url:
                                    #print(url)
                                    print(url.groups(0)[0])
                                    urlstr = url.groups(0)[0]
                                else:
                                    print("no url match")
                                    urlstr = ''
                                self.dev.key("BACK")
                                    
                            self.db.insert(goodsname,str(price),star, desc,urlstr,toleavemessage)
                            
                            if j >= 4:
                                time.sleep(2)
                                name.swipe([-0.0977, -0.8247])
                                break
                    else:
                        print("no get text")

            else:
                print("===no find===")
        #swipe([-0.0977, -0.8247])


    def collectgoods(self,goods, goodsname,lowprice, highprice,toleavemessage,justsearch = False):
        if self.goHome() != 0:
            print("没有找到家")
            return
        self.dev.poco("com.taobao.idlefish:id/tx_id").click()
        self.dev.text(goods)
        self.dev.poco("com.taobao.idlefish:id/search_button").click()
        
        if toleavemessage == True:
            price = highprice
        else:
            price = lowprice

        if justsearch == False:
            node = self.dev.poco(text="筛选")
            if node.exists():
                node.click()
            try:
                self.dev.touch(Template(r"tpl1586269931551.png", record_pos=(-0.1, 0.045), resolution=self.dev.resolution))
                self.dev.text(str(price[0]))
                time.sleep(1)
                self.dev.touch(Template(r"tpl1586269945392.png", record_pos=(0.307, 0.051), resolution=self.dev.resolution))
                self.dev.text(str(price[1]))
                node = self.dev.poco(text="确定")
                if node.exists():
                    node.click()
                else:
                    print("no find submit node")
                    return
            except:
                print("no find pic")
                return

        self.collectciycle(goods, goodsname, toleavemessage)

    def collect_relategoods(self, goods, toleavemessage):
        if goods == "v10":
            lowprice = [300,550]
            highprice = [650,1200]
            self.collectgoods("荣耀v10", "荣耀v10", lowprice,highprice,toleavemessage)
            self.collectgoods("honor v10","荣耀v10", lowprice,highprice,toleavemessage)
        elif goods == "u1":
            lowprice = [30,80]
            highprice = [150,250]
            self.collectgoods("坚果u1","坚果u1", lowprice,highprice,toleavemessage)
            self.collectgoods("yq601","坚果u1", lowprice,highprice,toleavemessage)
            self.collectgoods("yq603","坚果u1", lowprice,highprice,toleavemessage)
            self.collectgoods("yq605","坚果u1",lowprice,highprice,toleavemessage)
            self.collectgoods("yq607","坚果u1",lowprice,highprice,toleavemessage)
        elif goods == "m30":
            lowprice = [5,65]
            highprice = [100,250]
            self.collectgoods("海信m30","海信m30",lowprice,highprice,toleavemessage)    
        elif goods == "honor7":
            lowprice = [60,260]
            highprice = [300,400]
            self.collectgoods("荣耀7","荣耀7", lowprice,highprice,toleavemessage)
        elif goods == "lephonet7a":
            lowprice = [30,100]
            highprice = [100,200]
            self.collectgoods("百立丰t7a","lephonet7a", lowprice,highprice,toleavemessage,True)    
        else:
            print("error")

    def user_find_assign(self,user_assign_text):
        str =user_assign_text.get() #获取文本框内容
        if str:
            print(str)
            if self.goHome() != 0:
                print("没有找到家")
                return
            self.dev.poco("com.taobao.idlefish:id/tx_id").click()
            self.dev.text(str)
            self.dev.poco("com.taobao.idlefish:id/search_button").click()

    def goods_equitable_price(self, goodsname):
        if goodsname == "荣耀v10":
            return 450
        elif goodsname == "坚果u1":
            return 75
        elif goodsname == "海信m30":
            return 45
        elif goodsname == "荣耀7":
            return 140
        else:
            return 0

    def goods_message_price(self, goodsname):
        if goodsname == "荣耀v10":
            return 999999
        elif goodsname == "坚果u1":
            return 150
        elif goodsname == "海信m30":
            return 45
        else:
            return 999999

    def clickMy(self):
        #pos = self.dev.poco("android:id/content").offspring("我的，未选中状态").offspring("com.taobao.idlefish:id/tab_icon")
        pos = self.dev.poco(textMatches="我的")
        if pos.exists():
            print("找到我的")
            pos.click()
        else: 
            print("没有找到我的")

    def clickXianyu(self):
        pos = self.dev.poco("android:id/content").offspring("闲鱼，未选中状态").offspring("com.taobao.idlefish:id/tab_icon").click()
        if pos.exists():
            print("找到闲鱼")
            pos.click()
        else: 
            print("没有找到")

    def clickPersion(self):
        pos = self.dev.poco(text="个人主页").click()
        if pos.exists():
            print("找到个人主页")
            pos.click()
        else: 
            print("没有找到")

    def qianDao(self):
        if self.goHome() != 0:
            print("没有找到家")
            return
        self.clickMy()
        self.dev.poco(text="闲鱼币").click()
        self.dev.touch(Template(r"tpl1585401111451.png", record_pos=(0.008, -0.625), resolution=self.dev.resolution))
        self.dev.poco("100闲鱼币夺宝").click()

    def guanQian(self):
        if self.goHome() != 0:
            print("没有找到家")
            return
        self.clickMy()

        node = self.dev.poco(text="边逛边赚钱")
        if node.exists():
           node.click()    
           time.sleep(1)
        else:
            self.dev.touch(Template(r"tpl1588682705601.png", record_pos=(0.358, -0.428), resolution=self.dev.resolution))
            print("没有找到赚钱")
            return    
        for i in range(160):
            node = self.dev.poco(name="¥")    
            if node.exists():
                node.click()
                time.sleep(1)
                node.swipe([-0.0977, -0.8247])
                time.sleep(1)
                back = self.dev.poco(text="返回")
                if back.exists():
                    back.click()
                else:
                    #可能是宝箱弹出了等会
                    time.sleep(5)
                    back = self.dev.poco(text="返回")
                    if back.exists():
                        back.click()
                    else:
                        self.dev.key("BACK")
                        #结束寻宝
                        return
           
            self.dev.movePageUp()    
            
    def detection(self):
        if self.dev.isApp("com.taobao.idlefish") == False:
            return
        sleeptime = random.randint(1,5)
        sleep(sleeptime)
        node = self.dev.poco(text="暂不升级")
        if node.exists():
            node.click()
        water = self.dev.poco("休息会呗，坐下来喝口水，")
        if water.exists():
            swipenode = self.dev.poco("nc_1_n1t")
            if swipenode.exists():
                swipenode.swipe([0.7519, 0.0028])
                #swipenode.swipe([0.8172, -0.0302])
        sleeptime = random.randint(1,5)
        sleep(sleeptime) 

    def findCheap(self):
        if self.goHome() != 0:
            print("没有找到家")
            return
        self.dev.poco("com.taobao.idlefish:id/tx_id").click()
        self.dev.text("海信m30")
        self.dev.poco("com.taobao.idlefish:id/search_button").click()

        for i in range(3):
            element=self.dev.poco(text="海信m30").parent().offspring()
            if element.exists():
                j = 0
                for name in element:
                    str = name.get_text()
                    if str:
        #                 if str.lower().find("海信m30".lower()) != -1:     
        #                     print(str) 
        #                     print(name)
        #                     print("ooooooooooo")
                        if str.lower().find("￥".lower())!=-1:
                            j = j + 1
                            name.click()
                            sleep(2)
                            keyevent("BACK")


                            if j == 4:
                                sleep(2)
                                name.swipe([-0.0977, -0.8247])
                                break
            else:
                print("===no find===")
            i = i + 1



    def changePrice(self,price):
        pass
    # def changePrice(price):
    #     time.sleep(1)
    #     for i in range(10):
    #         click(907,1625)

    #     pricerand = random.randint(0,9)
    #     price = price + pricerand
    #     print("rand price" + price)
    #     i = 0
    #     for i in range(3):
    #         if i == 0:
    #             newprice = int(price/100)
    #             if (newprice == 0):
    #                 continue
    #         elif i == 1 :
    #             newprice = int(price/10%10)
    #         else :
    #             newprice = int(price %10)
                
    #         time.sleep(1)
    #         print("new price " + price +" " + newprice)
    #         if newprice == 0:
    #             clickDelay1s(417, 2045)
    #         elif newprice == 1:
    #             clickDelay1s(130,1533)
    #         elif newprice == 2:
    #             clickDelay1s(388,1509)
    #         elif newprice == 3:
    #             clickDelay1s(675,1521)
    #         elif newprice == 4:
    #             clickDelay1s(147,1693)
    #         elif newprice == 5:
    #             clickDelay1s(427,1710)
    #         elif newprice == 6:
    #             clickDelay1s(699,1703)
    #         elif newprice == 7:
    #             clickDelay1s(172,1871)
    #         elif newprice == 8:
    #             clickDelay1s(427,1878)
    #         elif newprice == 9:  
    #             clickDelay1s(664,1896)
    #         else:
    #             print("error price")

    #     print("confirm")
    #     #确定
    #     (x,y) = rToA(0.9,0.9)
    #     clickDelay1s(x,y)
    #     #确定发布有两种界面风格，需要判断处理
    #     if  0 == findAndClickPic( "publish.bmp"):
    #         print("a")
    #     else:
    #         print("confirm")
    #         (x,y) = rToA(0.5,0.95)
    #         clickDelay2s(x,y)
    #     #返回
    #     clickBack2S()
    #     clickBack2S()
    #     clickBack2S()
    #     clickBack2S()
    #     return 0
        


class XyXyTest(unittest.TestCase):
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
        pass

    def test_sub(self):
        pass

# def main():
#     db = Xydb("e:\\xy1.db")
#     db.upgrade1()

# main()
if __name__ == '__main__':
    unittest.main()


