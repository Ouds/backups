# -*- coding: UTF-8 -*-

import sys, urllib, time
from pinyin import PinYinDomain

def filter_domains(domain_file):
    domains = open(domain_file)
    a = file('a.txt', 'a')
    b = file('b.txt', 'a')
    try:
        s = 0
        for domain in domains:
            s += 1

            domain = domain.strip()
            domain_list = domain.split('.')
            domain_prefix = domain_list[0]

            try:
                int(domain_prefix)
                is_number = True
            except:
                is_number = False
            
            pyd = PinYinDomain()

            if len(domain_prefix) <= 3:
                if not is_registered(domain):
                    a.write(domain + '\n')
            elif  len(domain_prefix) <= 4 and len(domain_list) == 2 and domain_list[1] in ['com', 'cn'] and '-' not in domain_prefix \
              and '0' not in domain_prefix and '1' not in domain_prefix and '2' not in domain_prefix and '3' not in domain_prefix and '4' not in domain_prefix \
              and '5' not in domain_prefix and '6' not in domain_prefix and '7' not in domain_prefix and '8' not in domain_prefix and '9' not in domain_prefix:
                if not is_registered(domain):
                    a.write(domain + '\n')
            elif is_number and len(domain_prefix) <= 6 and len(domain_list) == 2 and domain_list[1] in ['com', 'cn']:
                if not is_registered(domain):
                    a.write(domain + '\n')
            elif len(domain_prefix) <= 7 and len(domain_list) == 2 and domain_list[1] in ['com', 'cn'] and ('-' not in domain_prefix \
              and '0' not in domain_prefix and '1' not in domain_prefix and '2' not in domain_prefix and '3' not in domain_prefix and '4' not in domain_prefix \
              and '5' not in domain_prefix and '6' not in domain_prefix and '7' not in domain_prefix and '8' not in domain_prefix and '9' not in domain_prefix) \
              or (len(domain_list) == 3 and len(domain_prefix) <= 4 and 'com' == domain_list[1] and 'cn' == domain_list[2]):
                if pyd.get_pinyin_domain(domain):
                    if not is_registered(domain):
                        b.write(domain + '\n')
            else:
                print s, domain

    finally:
        domains.close()
        b.close()
        a.close()

def is_registered(domain):
    req = urllib.urlopen('http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=' + domain)
    '''
        210 : Domain name is available     表示域名可以注册
        211 : Domain name is not available 表示域名已经注册
        212 : Domain name is invalid       表示查询的域名无效
        213 : Time out 查询超时
    '''
    result = req.read().decode()
    is_registered = '211' in result
    print '\n', result, domain, is_registered
    time.sleep(2)
    return is_registered

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Input file name, please!'
    else:
        domain_file = sys.argv[1]
        filter_domains(domain_file)
