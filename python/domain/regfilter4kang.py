# -*- coding: UTF-8 -*-

import sys
from pinyin import PinYin3Domain

def filter_domains(domain_file, csv_file):
    with open(domain_file) as domains:
        s = 0
        for domain in domains:
            s += 1
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
            
            pyd = PinYin3Domain()

            if 'kang' in domain_prefix and domain_prefix_len <= 12 and domain_list_len == 2 and domain_suffix in ['com', 'cn']:
                if pyd.get_pinyin_domain(domain):
                    write_csv(domain, csv_file)

            else:
                if s%1000 == 0:
                    print(s, domain)

import csv
def write_csv(domain, csv_file):
    with open(csv_file, 'a', newline='') as data_csv:
        # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
        csvWriter = csv.writer(data_csv, dialect = ("excel"))
        # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
        csvWriter.writerow([domain])
        print(domain, "write in csv")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Input file name, please!')
    else:
        domain_file = sys.argv[1]
        csv_file = sys.argv[2]
        filter_domains(domain_file, csv_file)
