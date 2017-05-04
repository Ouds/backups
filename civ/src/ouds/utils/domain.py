# -*- coding: UTF-8 -*-

from pinyin import PinYinDomain

pyd = PinYinDomain()

for line in open(u"./domain.txt"):
    pyd.get_pinyin_domain(unicode(line).strip())



