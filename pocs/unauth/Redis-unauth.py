#!/usr/bin/env python
# coding=utf-8
import redis
from report.report import save

pocname = "Redis-unauth"

def verify(arg, **kwargs):
    port = 6379
    host = arg.replace("http://","")
    host = arg.replace("https://","")
    host = host.split(":")[0]
    a = check_redis(host,port)
    try:
        if a:
            save(arg,pocname,str(port))
            #print(ip)
            return {"url": host, "poc-name":pocname, "exploit": str(port)}
    except Exception as e:
        pass

def check_redis(host,port):
    try:
        r = redis.Redis(host=host, port=port, socket_timeout=7)
        r.set('name', 'test')
        if len(r.get('name')) > 0:
            return True
        else:
            pass
    except Exception as e:
        pass