# -*- coding: UTF-8 -*-

import csv
def write_csv(domain, csv_file):
    with open(csv_file, 'a', newline='') as data_csv:
        # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
        csvWriter = csv.writer(data_csv, dialect = ("excel"))
        # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
        csvWriter.writerow([domain])

write_csv("budshome.com", "filtered.csv")
write_csv("gaiding.com", "filtered.csv")
write_csv("yashayan.com", "filtered.csv")