#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# created by: zhangzhongyu
'''
不同的爬虫执行间隔不同
'''

import threading
import time
import os

def testp(cmds, sleep_time):
    while True:
        ctime = time.strftime('%Y-%m-%d %H:%M:%S  ',time.localtime(time.time()))

        if type(cmds) == list:
            for cmd in cmds:
                os.system(cmd)
                print(ctime+cmd)
        else:
            os.system(cmds)
            print(ctime+cmds)
        
        time.sleep(sleep_time)

def testt(sleep_time):
    while True:
        print(sleep_time)
        time.sleep(sleep_time)

if __name__ == "__main__":
    p1 = threading.Thread(target=testp, args=(['ipconfig','ping'], 2.5))
    p1.start()

    p2 = threading.Thread(target=testp, args=('dir', 5.5))
    p2.start()

    p3 = threading.Thread(target=testt, args=(2.5, ))
    p3.start()

    