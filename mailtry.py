#! /usr/bin/env python

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib



def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))



from_addr = "yuyiwei114@126.com"
password = "SSS3052301"
smtp_server = "smtp.126.com"
to_addr = "465360040@qq.com"

def fasong(gaojingmsg):
	msg = MIMEText (gaojingmsg,"plain","utf-8")
	msg["From"] = _format_addr(from_addr)
	msg["To"] = _format_addr(to_addr)
	msg['Subject'] = Header("gaojing").encode()
	server = smtplib.SMTP(smtp_server,25)
	server.set_debuglevel(4)
	server.login(from_addr,password)
	server.sendmail(from_addr,[to_addr],msg.as_string())
	server.quit()
