# -*- coding: UTF-8 -*-

import urllib.request, urllib.parse, urllib.error
import sys

def get_pagerank(url):
    hsh = check_hash(hash_url(url))
    #64.233.189.161
    #66.249.89.162
    #66.102.9.99
    gurl = 'http://www.google.com/search?client=navclient-auto&features=Rank:&q=info:%s&ch=%s' % (urllib.parse.quote(url), hsh)
    try:
        f = urllib.request.urlopen(gurl)
        rank = f.read().strip()[9:]
    except Exception:
        rank = '' #'N/A'
    if rank == '':
        rank = '0'
    return rank


def  int_str(string, integer, factor):
    for i in range(len(string)) :
        integer *= factor
        integer &= 0xFFFFFFFF
        integer += ord(string[i])
    return integer


def hash_url(string):
    c1 = int_str(string, 0x1505, 0x21)
    c2 = int_str(string, 0, 0x1003F)

    c1 >>= 2
    c1 = ((c1 >> 4) & 0x3FFFFC0) | (c1 & 0x3F)
    c1 = ((c1 >> 4) & 0x3FFC00) | (c1 & 0x3FF)
    c1 = ((c1 >> 4) & 0x3C000) | (c1 & 0x3FFF)

    t1 = (c1 & 0x3C0) << 4
    t1 |= c1 & 0x3C
    t1 = (t1 << 2) | (c2 & 0xF0F)

    t2 = (c1 & 0xFFFFC000) << 4
    t2 |= c1 & 0x3C00
    t2 = (t2 << 0xA) | (c2 & 0xF0F0000)

    return (t1 | t2)


def check_hash(hash_int):
    hash_str = '%u' % (hash_int)
    flag = 0
    check_byte = 0

    i = len(hash_str) - 1
    while i >= 0:
        byte = int(hash_str[i])
        if 1 == (flag % 2):
            byte *= 2;
            byte = byte / 10 + byte % 10
        check_byte += byte
        flag += 1
        i -= 1

    check_byte %= 10
    if 0 != check_byte:
        check_byte = 10 - check_byte
        if 1 == flag % 2:
            if 1 == check_byte % 2:
                check_byte += 9
            check_byte >>= 1

    return '7' + str(check_byte) + hash_str



if __name__ == '__main__':
    if len(sys.argv) != 2:
        url = 'http://www.nodesites.org'
    else:
        url = sys.argv[1]

    print(get_pagerank(url))