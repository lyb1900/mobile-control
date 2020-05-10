import sqlite3
import unittest
import traceback
import time
import re
class Xydb():
    
    def __init__(self, file):
        self.file = file
        #数据库初始化
        #创建一个连接对象，连接到本地数据库
        self.conn=sqlite3.connect(file)
        self.conn.execute("""create table if not exists xy_info (
        id integer PRIMARY KEY AUTOINCREMENT, 
        name text, 
        price integer, 
        star integer, 
        des text UNIQUE, 
        pic blob, 
        url text, 
        update_date DATE, 
        insert_date DATE, 
        nophone BOOL, 
        see BOOL, 
        leavemessage BOOLEAN)""")


    def find_same_desc(self,desc):
        cursor = self.conn.cursor()
        cursor.execute("select * from xy_info where des='{}'".format(desc))
        result = cursor.fetchall()
        if len(result) == 0:
            print("no find")
            cursor.close()
            return 1
        else:
            return 0

    def find_and_get_url(self,desc):
        cursor = self.conn.cursor()
        cursor.execute("select url,nophone from xy_info where des='{}'".format(desc))
        result = cursor.fetchall()
        if len(result) == 0:
            print("no find")
            url = ""
        else:
            print("find url" + result[0][0])
            if (result[0][1] == 1):
                url = ""
            else:
                url = result[0][0]
                if url == None:
                    url = ""
        cursor.close()  
        return url

    def find_and_get_leavemessage(self,desc):
        cursor = self.conn.cursor()
        cursor.execute("select leavemessage from xy_info where des='{}'".format(desc))
        result = cursor.fetchall()
        if len(result) == 0:
            print("no find")
            return False
        else:
            leavemessage = result[0][0]
            if leavemessage == None:
                return False
            else:
                return True
        cursor.close()  
        return False

    def update(self,price,star,des,url,leavemessage):
        try:
            nowdate = time.strftime("%Y-%m-%d", time.localtime())
            sql = '''UPDATE xy_info SET price = ?,star = ? ,update_date = ?, url = ?, leavemessage = ? WHERE des = ?'''    
            cur = self.conn.cursor()    
            cur.execute(sql, (price,star,nowdate,url,leavemessage,des))
            self.conn.commit()
            print("update" + des + "success")
        except:
            traceback.print_exc()
            print("fail")

    def upgrade_update_des(self,des,newdes):
        try:
            sql = '''UPDATE xy_info SET des = ? WHERE des = ?'''    
            cur = self.conn.cursor()    
            cur.execute(sql, (newdes,des))
            self.conn.commit()
            print("update" + des + "success")
        except:
            traceback.print_exc()
            print("fail")

    def upgrade_delete_other(self,des,newdes):
        try:
            sql = '''UPDATE xy_info SET des = ? WHERE des = ?'''    
            cur = self.conn.cursor()    
            cur.execute(sql, (newdes,des))
            self.conn.commit()
            print("update" + des + "success")
        except:
            traceback.print_exc()
            print("fail")

    def replace(self,name,price,star,des,url):
        try:
            nowdate = time.strftime("%Y-%m-%d", time.localtime())
            dbstr = 'replace into xy_info (name,price,star,des,url,update_date) values ("{}","{}","{}","{}","{}","{}")'.format(name,price,star,des,url,nowdate)
            print(dbstr)
            self.conn.execute(dbstr)
            self.conn.commit()
        except:
            traceback.print_exc()
            print("fail")

    def insert(self,name,price,star,des,url,leavemessage):
        if self.find_same_desc(des) != 0:
            # 插入一条数据
            #dbstr = "insert into xy_info (name,price,des) values (" + goods+ "," + str(price) + "," + nodestr + ")"
            nowdate = time.strftime("%Y-%m-%d", time.localtime())
            dbstr = 'insert into xy_info (name,price,star,des,url,insert_date,leavemessage) values ("{}","{}","{}","{}","{}","{}","{}")'.format(name,str(price),star,des,url,nowdate,leavemessage)
            #print(dbstr)
            self.conn.execute(dbstr)
            self.conn.commit()
            print("insert" + des + "success")
        else:
            print("has the same")
            self.update(str(price),star,des,url,leavemessage)
    def find(self,condition):
        cursor = self.conn.cursor()
        cursor.execute(condition)
        result = cursor.fetchall()
        cursor.close()  
        return result

    def goodsname_relation(self,goodsname):
        if goodsname == "荣耀v10":
            return ["荣耀","v10"]
        elif goodsname == "坚果u1":
            return ["坚果","u1","yq601","yq603","yq605","yq607"]
        elif goodsname == "海信m30":
            return ["m30","海信"]
        elif goodsname == "荣耀7":
            return ["荣耀7","honor7"]      
        elif goodsname == "lephonet7a":
            return ["lephonet7a","百立丰t7a"]        
        else:
            return None

    def match_gooodsname(self,des,goodsname):
        namearray = self.goodsname_relation(goodsname)
        if namearray:
            for name in namearray:
                if des.find(name) != -1:
                    return True
        return False

    def upgrade(self):
        cursor = self.conn.cursor()
        cursor.execute("select des from xy_info")
        result = cursor.fetchall()
        print("=====upgrade each ======")
        for row in result:
            print("get result")
            print(row[0]) 
            match = re.search(r"(.*\n)(￥\n)(\d+)", row[0])
            if match:
                newdes = match.groups(0)[0]
                self.upgrade_update_des(row[0],newdes)

    def upgrade1(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("select id,name,des from xy_info")
            result = cursor.fetchall()
            for row in result:
                print("get result")
                print(row[2]) 
                if self.match_gooodsname(row[2],row[1]) == False:
                    cursor.execute("delete from xy_info where id = " + str(row[0]))
            self.conn.commit()
        except:
            traceback.print_exc()
            print("fail")
        
        # print("=====upgrade each ======")
        # for row in result:
        #     print("get result")
        #     print(row[0]) 
        #     match = re.search(r"(.*\n)(￥\n)(\d+)", row[0])
        #     if match:
        #         newdes = match.groups(0)[0]
        #         self.upgrade_update_des(row[0],newdes)
class XydbTest(unittest.TestCase):
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
        db = Xydb("e:\\dbtest.db")
        db.insert("test",88,1,"这是测试用的","http://www.baidu.com",0)

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

