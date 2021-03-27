#!/usr/bin/env python
# coding=utf-8
import requests
from kazoo.client import KazooClient
from report.report import save

pocname = "ZooKeeper-unauth"

def verify(arg, **kwargs):
    port = 2181
    host = arg.replace("http://","")
    host = arg.replace("https://","")
    host = host.split(":")[0]
    a = check_zookeeper(host,port)
    try:
        if a:
            save(arg,pocname,str(port))
            return {"url": host, "poc-name":pocname, "exploit": str(port)}
    except Exception as e:
        pass

def check_zookeeper(host,port):
    try:
        zk = KazooClient(hosts='{}:{}'.format(host, port))
        zk.start()
        chidlrens = zk.get_children('/')
        if len(chidlrens) > 0:
            zk.stop()
            return True
            #print('[ok] -> {}:{}   {}'.format(host, port, chidlrens))
    except Exception as e:
        zk.stop()
        pass