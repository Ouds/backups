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
    def __init__(self, data_path = u"./mandarin.dat"):
        self.dict = {}
        for line in open(data_path):
            k, v = line.split('\t')
            self.dict[k] = v
        self.splitter = ''
    
    def get_pinyin(self, chars = u"你好吗"):
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                result.append(self.dict[key].split(" ")[0].strip()[:-1].lower())
            except:
                result.append(char)
        
        return self.splitter.join(result)
    
    def get_initials(self, char=u'你'):
        try:
            return self.dict["%X" % ord(char)].split(" ")[0][0]
        except:
            return char

class PinYinDomain():
    def __init__(self, data_path = u"./mandarin.dat"):
        self.list = []
        
        for line in open(data_path):
            values = line.split('\t')[1].split(" ")
            
            for value in values:
                if "\n" in value:
                    yinjie = value[:-2]
                else:
                    yinjie = value[:-1]
                
                if yinjie not in self.list:
                    self.list.append(yinjie)

    def get_pinyin_domain(self, domain = u"nihaoma.com"):        
        if domain[-2:].upper() == u"CN":
            domainLen = len(domain[:-3])
        else:
            domainLen = len(domain[:-4])
         
        if domainLen > 4:
            if domain[:domainLen].upper() in self.list:
                print domain
                return
            elif domain[0:1].upper() in self.list:
                if domain[1:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[1:2].upper() and domain[2:domainLen].upper() in self.list:
                    print domain
                    return            
                elif domain[1:3].upper() and domain[3:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[1:4].upper() and domain[4:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[1:5].upper() and domain[5:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[1:6].upper() and domain[6:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[1:7].upper() and domain[7:domainLen].upper() in self.list:
                    print domain
                    return
                
            elif domain[0:2].upper() in self.list:
                if domain[2:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[2:3].upper() and domain[3:domainLen].upper() in self.list:
                    print domain
                    return            
                elif domain[2:4].upper() and domain[4:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[2:5].upper() and domain[5:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[2:6].upper() and domain[6:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[2:7].upper() and domain[7:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[2:8].upper() and domain[8:domainLen].upper() in self.list:
                    print domain
                    return

            elif domain[0:3].upper() in self.list:
                if domain[3:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[3:4].upper() and domain[4:domainLen].upper() in self.list:
                    print domain
                    return            
                elif domain[3:5].upper() and domain[5:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[3:6].upper() and domain[6:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[3:7].upper() and domain[7:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[3:8].upper() and domain[8:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[3:9].upper() and domain[9:domainLen].upper() in self.list:
                    print domain
                    return

            elif domain[0:4].upper() in self.list:
                if domain[4:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[4:5].upper() and domain[5:domainLen].upper() in self.list:
                    print domain
                    return            
                elif domain[4:6].upper() and domain[6:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[4:7].upper() and domain[7:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[4:8].upper() and domain[8:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[4:9].upper() and domain[9:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[4:10].upper() and domain[10:domainLen].upper() in self.list:
                    print domain
                    return

            elif domain[0:5].upper() in self.list:
                if domain[5:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[5:6].upper() and domain[6:domainLen].upper() in self.list:
                    print domain
                    return            
                elif domain[5:7].upper() and domain[7:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[5:8].upper() and domain[8:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[5:9].upper() and domain[9:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[5:10].upper() and domain[10:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[5:11].upper() and domain[11:domainLen].upper() in self.list:
                    print domain
                    return

            elif domain[0:6].upper() in self.list:
                if domain[6:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[6:7].upper() and domain[7:domainLen].upper() in self.list:
                    print domain
                    return            
                elif domain[6:8].upper() and domain[8:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[6:9].upper() and domain[9:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[6:10].upper() and domain[10:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[6:11].upper() and domain[11:domainLen].upper() in self.list:
                    print domain
                    return
                elif domain[6:12].upper() and domain[12:domainLen].upper() in self.list:
                    print domain
                    return

        else:
            print domain
            return



