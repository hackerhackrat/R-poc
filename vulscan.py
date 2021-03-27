#!/usr/bin/env python
# coding=utf-8
import requests
import os
import time
import sys
#from queue import Queue
from lib.data import VERSION, PATHS_POCS, POCS, WORKER
from lib.loader import load_string_to_module
from lib.threads import *
from lib.requests import session_request,patch_session

url=[]
def attack(domain_file):
    version = "v1.0"
    usage(version)
    url.append(domain_file.strip())
    config = {
        "url": url,
        "poc": [],
        "thread_num": 200,
        "requsts":{
            "timeout": 10,
            "headers":{
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        }
    }
    init(config)
    start(config)
    end()

def main(domain_file):
	version = "v1.0"
	usage(version)
	with open(domain_file,"rt") as f:
			for domain in f:
				url.append(domain.strip())
	config = {
        "url": url,
        "poc": [],
        "thread_num": 20000,
        "requsts":{
        	"timeout": 10,
        	"headers":{
        		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
                'Content-Type': 'application/x-www-form-urlencoded'
        	}
        }
    }
	init(config)
	start(config)
	end()


def init(config: dict):
    #print("[*] target:{}".format(config["url"]))
    patch_session()
    # 加载poc，首先遍历出路径

    _pocs = []
    for root, dirs, files in os.walk(PATHS_POCS):
        files = filter(lambda x: not x.startswith("__") and x.endswith(".py") and x not in config.get("poc", []),
                       files)  # 过滤掉__init__.py文件以及指定poc文件
        _pocs.extend(map(lambda x: os.path.join(root, x), files))

    # 根据路径加载PoC
    for poc in _pocs:
        with open(poc, 'r') as f:
            model = load_string_to_module(f.read())
            POCS.append(model)
def end():
    print("[*] shutting down at {0}".format(time.strftime("%X")))
'''
def start(config: dict):
    url_list = config.get("url", [])
    # 循环url_list与pocs，逐一对应执行。
    for i in url_list:
        for poc in POCS:
            try:
                ret = poc.verify(i)
            except Exception as e:
                ret = None
                print(e)
            if ret:
                print(ret)'''

def worker():
    if not WORKER.empty():
        arg, poc = WORKER.get()
        try:
            ret = poc.verify(arg)
        except Exception as e:
            ret = None
            print(e)
        if ret:
            print(ret)


def start(config: dict):
    url_list = config.get("url", [])

    # 任务生成
    for arg in url_list:
        for poc in POCS:
            WORKER.put((arg, poc))

    # 执行
    run_threads(config.get("thread_num", 200), worker)

def usage(version):
	logo='''
 _____            _____   _____   ______
|  _  \          |  _  \ /  _  \ /  ___|
| |_| |          | |_| | | | | | | |
|  _  /  ——————— |  ___/ | | | | | |
| | \ \          | |     | |_| | | |___
|_|  \_\         |_|     \_____/ \_____| {}
	'''.format(version)
	print(logo)
	print("author:hackerhack@qq.com")

if __name__ == '__main__':
    '''
	domain_file = "target/target.txt"
	main(domain_file)
    '''
    domain_file = sys.argv[1]
    if ".txt" in domain_file:
        domain_file = "target/" + domain_file
        main(domain_file)
    else:
        attack(domain_file)