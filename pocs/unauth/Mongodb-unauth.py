#!/usr/bin/env python
# coding=utf-8
from pymongo import MongoClient
from report.report import save

pocname = "Mongodb-unauth"

def verify(arg, **kwargs):
    port = 27017
    host = arg.replace("http://","")
    host = arg.replace("https://","")
    host = host.split(":")[0]
    a = check_mongodb(host,port)
    try:
        if a:
            save(arg,pocname,str(port))
            return {"url": host, "poc-name":pocname, "exploit": str(port)}
    except Exception as e:
        pass

def check_mongodb(host,port):
    try:
        conn = MongoClient(host, port, socketTimeoutMS=5000)
        dbs = conn.database_names()
        if len(dbs) > 0:
            conn.close()
            return True
            #print('[ok] -> {}:{}   {}'.format(host, port, chidlrens))
    except Exception as e:
        conn.close()
        pass