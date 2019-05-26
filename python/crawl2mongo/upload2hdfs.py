#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# created by: zhangzhongyu
'''
上传josn文件到hadoop hdfs
'''

import time
import datetime
from datadig import hdfs

while True:
    fs = hdfs.HdfsClient(hosts='192.168.2.54:50070', user_name='bigdata')

    today = datetime.datetime.now()
    yesterday = (today + datetime.timedelta(days=-1)).strftime('%Y%m%d')

    prePath = '/user/bigdata/'
    localPrePath = '/home/bigdata/jsonfiles/'
    if not fs.exists(prePath+'jobs/'+yesterday+'.jl'):
        fs.copy_from_local(localPrePath+'jobs/'+yesterday+'.jl', prePath+'jobs/'+yesterday+'.jl')

    if not fs.exists(prePath+'companies/'+yesterday+'.jl'):
        fs.copy_from_local(localPrePath+'companies/'+yesterday+'.jl', prePath+'companies/'+yesterday+'.jl')

    time.sleep(86400)

