#!/usr/bin/env python
# coding=utf-8
from report.report import save
import dns.resolver
import dns.zone
import sys

pocname = "dns"
def verify(arg, **kwargs):
    try:
        dnsResolver = dns.resolver.Resolver()
        dnsResolver.timeout = 10
        host = arg.replace("http://","")
        host = arg.replace("https://","")
        domain = host.split(":")[0]
        ns = dnsResolver.query(domain, 'NS')                
        isVul = False
        if ns:                                              
            for domain_dns in ns:                           
                xfr = dns.query.xfr(str(domain_dns), domain, timeout=10, lifetime=10)
                if dns.zone.from_xfr(xfr):
                    isVul = True
                    #print('[+] dig @{} {} axfr'.format(domain_dns, domain))
                    save(domain,pocname,domain_dns)
                    return {"url": domain, "poc-name":pocname, "exploit": domain_dns}
            if not isVul:
                pass
        else:
            pass
    except Exception as e:
        pass