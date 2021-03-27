#!/usr/bin/env python
# coding=utf-8
import requests
import threading
from report.report import save

global target
pocname = "bakfile"
headers = {'Content-Type': 'application/x-www-form-urlencoded','User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

def verify(arg, **kwargs):
	file_fuzz_dic = "./dict/weakfile/file.txt"
	with open(file_fuzz_dic,"rt") as file:
		for i in range(50):
			for f in file.readlines():
				t = threading.Thread(target=bak,args=(arg,f.strip()))
				t.start()
	#print(target)

def bak(domain,file):
	try:
		r = requests.get(url=domain+file,headers=headers)
		if r.status_code == 200 and "Content-Type" in r.headers and "application" in r.headers["Content-Type"]:
			#global target
			target = domain + file
			save(domain,pocname,target)
			print({"url": domain, "poc-name": pocname, "exploit": target})
			#print(target)
	except Exception as e:
		pass