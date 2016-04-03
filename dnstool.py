#! /usr/bin/env python

import dns.resolver
import os
import requests
import time
import mailtry

iplist = []
headers = {'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:32.0) Gecko/20100101 Firefox/32.0'}
appdomain = "zucheqhd.com"
def get_iplist(domain):
	A = dns.resolver.query(domain,"A")
	for i in A.response.answer:
		for j in i.items:
			iplist.append(j.address)
	return True

def checkip(ip):
	checkurl = "http://"+ip+":8080"
	r = requests.get(checkurl,headers)
	if r.status_code == 200:
		gaojingmsg =  ip+" [ok]"+"      "+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		f = open("log.txt","a+")
                f.write(gaojingmsg)
                f.close()
	else:
		gaojingmsg = ip+" [Error]"+"      "+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		f = open("log.txt","a+")
		f.write(gaojingmsg)
		f.close()
		mailtry.fasong(gaojingmsg)
		
		mailtry.fasong(gaojingmsg)

		
	

get_iplist(appdomain)
for ip in  iplist:
	checkip(ip)

