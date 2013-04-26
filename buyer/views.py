#-*- coding: utf-8 -*-
'''
Created on 2013-4-26

@author: xinting
'''
from django.shortcuts import render_to_response
from taobao import settings
from django.http.response import HttpResponse
import tb

def buyer(request):
    title = u'我的买家'
    try:
        sessionKey = request.user.get_profile().sessionKey
    except:
        error = u"您还没有登录.."
    return render_to_response('buyer/buyer.html', locals())

def ajax(request):
    if request.session.get('hasData', False) is False:
        try:
            sessionKey = request.user.get_profile().sessionKey
        except:
            error = 'error: ' + u'获取授权密钥失败'
        
        options = {}
        options['appkey'] = settings.APPKEY
        options['appsecret'] = settings.APPSECRET
        options['sessionKey'] = sessionKey
        options['url'] = settings.SANDBOX_URL
        
    try:
        type = request.GET['type']
        
        if type == 'buyer':
            return HttpResponse(tb.Buyers(session=request.session, options=options).getBuyerJson())
    except Exception, e:
        error = 'error:' + repr(e)
    return HttpResponse(error)