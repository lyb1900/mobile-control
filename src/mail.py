
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class Mail():
    from_addr = ''
    password = ''
    to_addr = ''
    smtp_server = ''
    @classmethod
    def mail_init(cls,paras):
        cls.from_addr = paras['mail']['from_addr']
        cls.password = paras['mail']['password']
        cls.to_addr = paras['mail']['to_addr']
        cls.smtp_server = paras['mail']['smtp_server']
    @classmethod
    def mail_send(cls, message):

        # 开启发信服务，这里使用的是加密传输
        mail_server = smtplib.SMTP_SSL()    
        
        mail_server.connect(cls.smtp_server,465)
        # 登录发信邮箱
        mail_server.login(cls.from_addr, cls.password)
        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        msg = MIMEText(message,'plain','utf-8')
        # 邮件头信息
        msg['From'] = Header(cls.from_addr)
        msg['To'] = Header(cls.to_addr)
        msg['Subject'] = Header('我的机器人助理消息')
        # 发送邮件
        mail_server.sendmail(cls.from_addr, cls.to_addr, msg.as_string())
        # 关闭服务器
        mail_server.quit()
