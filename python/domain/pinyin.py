# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds.cg@gmail.com
# Project: Game
# File Name: ouds/common/pinyin.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: handler pinyin.
#===============================================================================

class PinYin():
    def __init__(self, data_path = "./mandarin.dat"):
        self.dict = {}
        pyd = open(data_path)
        for line in pyd:
            k, v = line.split('\t')
            self.dict[k] = v
        
        self.splitter = ''
    
    def get_pinyin(self, chars = "你好吗"):
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                result.append(self.dict[key].split(" ")[0].strip()[:-1].lower())
            except:
                result.append(char)
        
        return self.splitter.join(result)
    
    def get_initials(self, char='你'):
        try:
            return self.dict["%X" % ord(char)].split(" ")[0][0]
        except:
            return char


class PinYin2Domain():
    def __init__(self, data_path = "./mandarin.dat"):
        self.list = []
        pyd = open(data_path)
        for line in pyd:
            values = line.split('\t')[1].split(" ")
            
            for value in values:
                if "\n" in value:
                    yinjie = value[:-2]
                else:
                    yinjie = value[:-1]
                
                if yinjie not in self.list:
                    self.list.append(yinjie)

    def get_pinyin_domain(self, domain = "nihaoma.com"):
        if domain[-2:].upper() == "CN" or domain[-3:].upper() == "COM":
            if domain[-2:].upper() == "CN":
                domainLen = len(domain[:-3])
            else:
                domainLen = len(domain[:-4])
        else:
            return False
         
        if domain[:domainLen].upper() in self.list:
            print(domain, '+')
            return True
        elif (domain[:1].upper() in self.list) and (domain[1:domainLen].upper() in self.list):
            print(domain, '1+')
            return True
        elif (domain[:2].upper() in self.list) and (domain[2:domainLen].upper() in self.list):
            print(domain, '2+')
            return True
        elif (domain[:3].upper() in self.list) and (domain[3:domainLen].upper() in self.list):
            print(domain, '3+')
            return True
        elif (domain[:4].upper() in self.list) and (domain[4:domainLen].upper() in self.list):
            print(domain, '4+')
            return True
        elif (domain[:5].upper() in self.list) and (domain[5:domainLen].upper() in self.list):
            print(domain, '5+')
            return True
        elif (domain[:6].upper() in self.list) and (domain[6:domainLen].upper() in self.list):
            print(domain, '6+')
            return True


class PinYin3Domain():
    def __init__(self, data_path = "./mandarin.dat"):
        self.list = []
        pyd = open(data_path)
        for line in pyd:
            values = line.split('\t')[1].split(" ")
            
            for value in values:
                if "\n" in value:
                    yinjie = value[:-2]
                else:
                    yinjie = value[:-1]
                
                if yinjie not in self.list:
                    self.list.append(yinjie)

    def get_pinyin_domain(self, domain = "nihaoma.com"):
        if domain[-2:].upper() == "CN" or domain[-3:].upper() == "COM":
            if domain[-2:].upper() == "CN":
                domainLen = len(domain[:-3])
            else:
                domainLen = len(domain[:-4])
        else:
            return False
         
        if domain[:domainLen].upper() in self.list:
            print(domain, '+')
            return True
        elif domain[:1].upper() in self.list:
            if domain[1:domainLen].upper() in self.list:
                print(domain, '1+')
                return True
            elif (domain[1:2].upper() in self.list) and (domain[2:domainLen].upper() in self.list):
                print(domain, '1+1+')
                return True
            elif (domain[1:3].upper() in self.list) and (domain[3:domainLen].upper() in self.list):
                print(domain, '1+2+')
                return True
            elif (domain[1:4].upper() in self.list) and (domain[4:domainLen].upper() in self.list):
                print(domain, '1+3+')
                return True
            elif (domain[1:5].upper() in self.list) and (domain[5:domainLen].upper() in self.list):
                print(domain, '1+4+')
                return
            elif (domain[1:6].upper() in self.list) and (domain[6:domainLen].upper() in self.list):
                print(domain, '1+5+')
                return True
            elif (domain[1:7].upper() in self.list) and (domain[7:domainLen].upper() in self.list):
                print(domain, '1+6+')
                return True
            
        elif domain[:2].upper() in self.list:
            if domain[2:domainLen].upper() in self.list:
                print(domain, '2+')
                return True
            elif (domain[2:3].upper() in self.list) and (domain[3:domainLen].upper() in self.list):
                print(domain, '2+1+')
                return True
            elif (domain[2:4].upper() in self.list) and (domain[4:domainLen].upper() in self.list):
                print(domain, '2+2+')
                return True
            elif (domain[2:5].upper() in self.list) and (domain[5:domainLen].upper() in self.list):
                print(domain, '2+3+')
                return True
            elif (domain[2:6].upper() in self.list) and (domain[6:domainLen].upper() in self.list):
                print(domain, '2+4+')
                return True
            elif (domain[2:7].upper() in self.list) and (domain[7:domainLen].upper() in self.list):
                print(domain, '2+5+')
                return True
            elif (domain[2:8].upper() in self.list) and (domain[8:domainLen].upper() in self.list):
                print(domain, '2+6+')
                return True

        elif domain[:3].upper() in self.list:
            if domain[3:domainLen].upper() in self.list:
                print(domain, '3+')
                return True
            elif (domain[3:4].upper() in self.list) and (domain[4:domainLen].upper() in self.list):
                print(domain, '3+1+')
                return True
            elif (domain[3:5].upper() in self.list) and (domain[5:domainLen].upper() in self.list):
                print(domain, '3+2+')
                return True
            elif (domain[3:6].upper() in self.list) and (domain[6:domainLen].upper() in self.list):
                print(domain, '3+3+')
                return True
            elif (domain[3:7].upper() in self.list) and (domain[7:domainLen].upper() in self.list):
                print(domain, '3+4+')
                return True
            elif (domain[3:8].upper() in self.list) and (domain[8:domainLen].upper() in self.list):
                print(domain, '3+5+')
                return True
            elif (domain[3:9].upper() in self.list) and (domain[9:domainLen].upper() in self.list):
                print(domain, '3+6+')
                return True

        elif domain[:4].upper() in self.list:
            if domain[4:domainLen].upper() in self.list:
                print(domain, '4+')
                return True
            elif (domain[4:5].upper() in self.list) and (domain[5:domainLen].upper() in self.list):
                print(domain, '4+1+')
                return True
            elif (domain[4:6].upper() in self.list) and (domain[6:domainLen].upper() in self.list):
                print(domain, '4+2+')
                return True
            elif (domain[4:7].upper() in self.list) and (domain[7:domainLen].upper() in self.list):
                print(domain, '4+3+')
                return True
            elif (domain[4:8].upper() in self.list) and (domain[8:domainLen].upper() in self.list):
                print(domain, '4+4+')
                return True
            elif (domain[4:9].upper() in self.list) and (domain[9:domainLen].upper() in self.list):
                print(domain, '4+5+')
                return True
            elif (domain[4:10].upper() in self.list) and (domain[10:domainLen].upper() in self.list):
                print(domain, '4+6+')
                return True

        elif domain[:5].upper() in self.list:
            if domain[5:domainLen].upper() in self.list:
                print(domain, '5+')
                return True
            elif (domain[5:6].upper() in self.list) and (domain[6:domainLen].upper() in self.list):
                print(domain, '5+1+')
                return True
            elif (domain[5:7].upper() in self.list) and (domain[7:domainLen].upper() in self.list):
                print(domain, '5+2+')
                return True
            elif (domain[5:8].upper() in self.list) and (domain[8:domainLen].upper() in self.list):
                print(domain, '5+3+')
                return True
            elif (domain[5:9].upper() in self.list) and (domain[9:domainLen].upper() in self.list):
                print(domain, '5+4+')
                return True
            elif (domain[5:10].upper() in self.list) and (domain[10:domainLen].upper() in self.list):
                print(domain, '5+5+')
                return True
            elif (domain[5:11].upper() in self.list) and (domain[11:domainLen].upper() in self.list):
                print(domain, '5+6+')
                return True

        elif domain[:6].upper() in self.list:
            if domain[6:domainLen].upper() in self.list:
                print(domain, '6+')
                return True
            elif (domain[6:7].upper() in self.list) and (domain[7:domainLen].upper() in self.list):
                print(domain, '6+1+')
                return True
            elif (domain[6:8].upper() in self.list) and (domain[8:domainLen].upper() in self.list):
                print(domain, '6+2+')
                return True
            elif (domain[6:9].upper() in self.list) and (domain[9:domainLen].upper() in self.list):
                print(domain, '6+3+')
                return True
            elif (domain[6:10].upper() in self.list) and (domain[10:domainLen].upper() in self.list):
                print(domain, '6+4+')
                return True
            elif (domain[6:11].upper() in self.list) and (domain[11:domainLen].upper() in self.list):
                print(domain, '6+5+')
                return True
            elif (domain[6:12].upper() in self.list) and (domain[12:domainLen].upper() in self.list):
                print(domain, '6+6+')
                return True
