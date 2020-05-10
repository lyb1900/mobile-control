
# smtplib 用于邮件的发信动作
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def mail_send(message):
    from_addr = '18913913607@189.cn'
    password = 'Lin49800'
    to_addr = 'lyb.19@qq.com'
    smtp_server = 'smtp.189.cn'
    # 开启发信服务，这里使用的是加密传输
    mail_server = smtplib.SMTP_SSL()    
    
    mail_server.connect(smtp_server,465)
    # 登录发信邮箱
    mail_server.login(from_addr, password)
    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(message,'plain','utf-8')
    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('我的机器人助理消息')
    # 发送邮件
    mail_server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    mail_server.quit()
