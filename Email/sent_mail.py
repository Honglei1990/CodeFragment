# -*- coding:utf-8 -*-
import email.mime.multipart
import email.mime.text
import smtplib

from_address = 'weiliwang880@163.com'
password = 'fucktheworld1'
to_address = 'weiliwang880@163.com'

msg = email.mime.multipart.MIMEMultipart()
msg['From'] = 'weiliwang880@163.com'
msg['To'] = '15011533375@qq.com'
msg['Subject'] = 'test email!'

content = '''''
    Hello, there!
        This is test text.
        qq:408445670
'''

txt = email.mime.text.MIMEText(content)
msg.attach(txt)

server = smtplib
server = smtplib.SMTP()
server.connect('smtp.163.com', '25')
server.set_debuglevel(1)
server.login(from_address,password)
server.sendmail(from_address, to_address, str(msg))
server.quit()