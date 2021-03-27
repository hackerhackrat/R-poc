import os
import time

def save(url,pocname,exp):
	with open("report/report.html","at") as f:
		f.writelines("目标:" + "<a href=" + '"' + url.strip() + '">' + url.strip() + "</a>" + "  " + "POC名称:" + pocname.strip() + "  " + "Exp:" + exp.strip() + '<br />')
		f.writelines("------------------------------------------------------------------------------------------------------------" + '<br />')
