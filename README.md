# R-poc

一款用于快速验证漏洞的简易框架

基于Airpoc，对其进行了微小改动

原项目文章：https://paper.seebug.org/913/

支持单/多目标

暴力执行pocs目录下的所有poc对目标进行测试

# usage：

vulscan.py http://www.xxx.com

vulscan.py target.txt(目标文件放置于target目录下)

有关文章：https://www.freebuf.com/sectool/267793.html

![](https://github.com/hackerhackrat/R-poc/blob/main/img/R-poc1.png)

# 如何编写poc？

以下为ueditor.net漏洞的poc

`#!/usr/bin/env python
#coding=utf-8
import requests
from report.report import save
pocname = "ueditor-net"
headers = {'Content-Type': 'application/x-www-form-urlencoded','User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
def verify(arg, **kwargs):
	exploit = "/ueditor/net/controller.ashx?action=catchimage"
	try:
		r = requests.get(url=arg+exploit,headers=headers)
		if '参数错误：没有指定抓取源' in r.text:
			save(arg,pocname,exploit)
			return {"url": arg, "poc-name":pocname, "exploit": exploit}
	except Exception as e:
		pass`

poc都要引用report目录下的report文件的save函数

需要提供三个参数:arg,pocname,exploit

# 更新

2021.4.17 update requirements.txt;

update poc:eyou-rce-2021,Druid-unauth,Spring-unauth，Resin

2021.4.18 update NginxCVE-2017-7529,shiro_key

NginxCVE-2017-7529和shiro_key进行自动判断，减少误报率

shiro检测效果如图所示

![https://github.com/hackerhackrat/R-poc/blob/main/img/shiro.jpg]()

感谢各位师傅的支持，鄙人QQ:3382340265