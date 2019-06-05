# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@ouds.us
# File Name: ouds/init.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

from django.template import loader, Context
from django.http import HttpResponse

def home(request, template_name = 'home.ouds'):

    # 玩家默认语言
    language = request.META["HTTP_ACCEPT_LANGUAGE"].lower()
    if 'zh-cn' in language:
        language = 'zh-cn'
    elif 'zh-tw' in language:
        language = 'zh-tw'
    else:
        language = language[:2]
    
    request.session['django_language'] = language

    c = Context(
            {'language': request.session['django_language'],},
           )
    t = loader.get_template(template_name)

    return HttpResponse(t.render(c))
