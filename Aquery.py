#! /usr/bin/env python

import dns.resolver


domain = raw_input("please input your domin what you wanna query ! : ")

A = dns.resolver.query(domain,"A")

for i in A.response.answer:
	for j in i.items :
		print j.to_text()


