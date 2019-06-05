# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/utils/brn.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: batch rename.
#===============================================================================

import os, shutil

dir = 'E:/conceptuous/con-chili/templates/base'
i = 0

for file in os.listdir(dir):
    print file.name
    old_file = dir+'/' + file
    new_file = dir+'/' + file.replace('ouds', 'chili')
    i += 1
    print i, old_file, '----------->', new_file
    shutil.move(old_file, new_file)
    

    
    