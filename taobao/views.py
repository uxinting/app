#-*- coding: utf-8 -*-
'''
Created on 2013-4-16

@author: xinting
'''
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from taobao import settings
from django.http import HttpResponse
import tb

def sell(request):
    title = u'我的销售'
    try:
        sessionKey = request.user.get_profile().sessionKey
    except:
        error = u'您还没有登录..'

    return render_to_response('sell/sell.html', locals(), context_instance=RequestContext(request))
    
def ajax(request):
    if request.session.get('hasData', False) is False:
        try:
            sessionKey = request.user.get_profile().sessionKey
        except:
            return HttpResponse(u'error: 获取授权密钥失败')
        
        options = {}
        options['appkey'] = settings.APPKEY
        options['appsecret'] = settings.APPSECRET
        options['sessionKey'] = sessionKey
        options['url'] = settings.SANDBOX_URL
    
    try:
        type = request.GET['type']
        if type == 'sell':
            return HttpResponse(tb.Trades(session=request.session, options=options).getSellJson())
        
        if type == 'turnover':
            return HttpResponse(tb.Trades(session=request.session, options=options).getTurnoverJson())
    except Exception, e:
        pass
    
    return HttpResponse(u'error: 获取数据失败')