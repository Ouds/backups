# -*- coding: UTF-8 -*-

def write_txt(domain, txt_file):
    with open(txt_file, 'a', newline='\r\n') as data_txt:
        data_txt.write(domain+'\n')

a, b, s = 'a.txt', 'b.txt', 0
write_txt(str(s+1), a)
write_txt(str(s+2), b)
write_txt(str(s+3), a)
write_txt(str(s+4), b)

