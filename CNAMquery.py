#! /usr/bin/env python

import dns.resolver

domain  = raw_input (" please input your domain : ")

CNAME =	dns.resolver.query(domain,"CNAME")

for i in CNAME.response.answer :
	for j in i.items:
		print j.to_text()
