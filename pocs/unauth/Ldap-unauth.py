#!/usr/bin/env python
# coding=utf-8
import ldap3
from ldap3 import Connection
from report.report import save

pocname = "Ldap-unauth"

def verify(arg, **kwargs):
    #port = 27017
    host = arg.replace("http://","")
    host = arg.replace("https://","")
    ip = host.split(":")[0]
    a = check_ldap(ip)
    try:
        if a:
            save(arg,pocname,"389")
            return {"url": host, "poc-name":pocname, "exploit": "389"}
    except Exception as e:
        pass

def check_ldap(ip):
    try:
        server = ldap3.Server(ip, get_info=ldap3.ALL, connect_timeout=30)
        conn = ldap3.Connection(server, auto_bind=True)
        if len(server.info.naming_contexts) > 0:
            return True
    except Exception as e:
        pass