# -*- coding: UTF-8 -*-

import sys
import time

import pr

def filter_domains(file, value):
    domains = open(file)
    try:
        for domain in domains:
            domain = domain.strip('\n')
            domain_list = domain.split('.')
            domain_prefix = domain_list[0]
            url = 'http://www.' + domain

            if (len(domain_list) == 2 and len(domain_prefix) <= 12) or (len(domain_list) == 3 and len(domain_prefix) <= 9):
                prv = pr.get_pagerank(url)
                if int(prv) >= value or 'kang' in domain_prefix or (len(domain_prefix) <= 3 and len(domain_list) == 2) or (len(domain_prefix) == 4 and len(domain_list) == 2 and 'com' == domain_list[1]):
                    print(domain, prv)
                time.sleep(3)
    finally:
        domains.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Input file name, please!')
    else:
        file = sys.argv[1]
        value = int(sys.argv[2])
        print('pr >= %s in %s :' %(value, file)) 
        filter_domains(file, value)




