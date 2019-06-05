# -*- coding: UTF-8 -*-

import sys, urllib.request, urllib.parse, urllib.error, time
from pinyin import PinYin2Domain

def filter_domains(domain_file, csv_file):
    '''
    使用with语法替代try/finally
    try:
        domains = open(domain_file)
        a = open('a.txt', 'a')
        b = open('b.txt', 'a')
    '''
    with open(domain_file) as domains:
        df_txt = 'filtered.txt'
        line = 0
        for domain in domains:
            line += 1
            domain = domain.strip()
            
            domain_list = domain.split('.')
            domain_prefix = domain_list[0]
            domain_suffix = domain_list[1]
            
            domain_list_len = len(domain_list)
            domain_prefix_len = len(domain_prefix)

            try:
                int(domain_prefix)
                is_number = True
            except:
                is_number = False
            
            pyd = PinYin2Domain()

            if domain_prefix_len <= 3 and domain_suffix in ['com', 'cn']: #, 'org', 'net'
                write_csv(domain, csv_file)
                if not is_registered(domain):
                    write_txt(domain, df_txt)
            elif domain_prefix_len <= 4 and domain_list_len == 2 and domain_suffix in ['com', 'cn'] and '-' not in domain_prefix \
              and '0' not in domain_prefix and '1' not in domain_prefix and '2' not in domain_prefix and '3' not in domain_prefix and '4' not in domain_prefix \
              and '5' not in domain_prefix and '6' not in domain_prefix and '7' not in domain_prefix and '8' not in domain_prefix and '9' not in domain_prefix:
                write_csv(domain, csv_file)
                if not is_registered(domain):
                    write_txt(domain, df_txt)
            elif is_number and domain_prefix_len <= 5 and domain_list_len == 2 and domain_suffix in ['com', 'cn']:
                write_csv(domain, csv_file)
                if not is_registered(domain):
                    write_txt(domain, df_txt)
            #elif is_number and domain_prefix_len == 6 and domain_list_len == 2 and domain_suffix in ['com', 'cn'] \
            #  and '0' not in domain_prefix and '4' not in domain_prefix:
            #    write_csv(domain, csv_file)
            #    if not is_registered(domain):
            #        write_txt(domain, df_txt)
            elif domain_prefix_len <= 12 and domain_list_len == 2 and domain_suffix in ['com', 'cn']:
                '''
                ('-' not in domain_prefix and '0' not in domain_prefix and '1' not in domain_prefix \ 
                and '2' not in domain_prefix and '3' not in domain_prefix and '4' not in domain_prefix \ 
                and '5' not in domain_prefix and '6' not in domain_prefix and '7' not in domain_prefix \ 
                and '8' not in domain_prefix and '9' not in domain_prefix) \ 
                or (domain_list_len == 3 and domain_prefix_len <= 4 and 'com' == domain_suffix and 'cn' == domain_list[2])
                '''
                if pyd.get_pinyin_domain(domain):
                    write_csv(domain, csv_file)
                    if not is_registered(domain):
                        write_txt(domain, df_txt)
            else:
                print(line, domain)
            
    '''
    使用with语法替代try/finally
    finally:
        domains.close()
        b.close()
        a.close()
    '''

def write_txt(domain, txt_file):
    with open(txt_file, 'a', newline='\r\n') as data_txt:
        data_txt.write(domain + '\n')
        print(domain, "write in txt")

import csv
def write_csv(domain, csv_file):
    with open(csv_file, 'a', newline='') as data_csv:
        # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
        csvWriter = csv.writer(data_csv, dialect = ("excel"))
        # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
        csvWriter.writerow([domain])
        print(domain, "write in csv")

def is_registered(domain):
    req = urllib.request.urlopen('http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=' + domain)
    '''
        210 : Domain name is available     表示域名可以注册
        211 : Domain name is not available 表示域名已经注册
        212 : Domain name is invalid       表示查询的域名无效
        213 : Timeout 查询超时
        214 : Unknown error 未知错误
    '''
    result = req.read().decode()
    is_registered = '211' in result
    print('\n', result, domain, is_registered)
    time.sleep(2)
    return is_registered

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Input file name, please!')
    else:
        domain_file = sys.argv[1]
        csv_file = sys.argv[2]
        filter_domains(domain_file, csv_file)
