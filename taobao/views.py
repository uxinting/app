#-*- coding: utf-8 -*-
'''
Created on 2013-4-16

@author: xinting
'''
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
import top.api as topapi
from taobao import settings
import top
import time
import json
from django.http import HttpResponse
import tb

def sell(request):
    try:
        print request.user.get_profile().sessionKey
    except:
        return render_to_response('auth/login.html', {}, context_instance=RequestContext(request))
    
    title = u'我的销售'
    try:
        sessionKey = request.user.get_profile().sessionKey
        
        res = request.session.get('res', None)
        if res is None:
            trade = tb.Trade()
            res = trade.getRes(settings.APPKEY, settings.APPSECRET, settings.SANDBOX_URL, sessionKey, options={'start_created': '2013-04-01 00:00:00'})
            request.session['res'] = res
        
        sell = res.get('trades').get('trade')[0].items()
        orders = res.get('trades').get('trade')[0].get('orders').items()
    except Exception, e:
        return render_to_response('error.html', {'from': 'sell', 'error': repr(e)})
    return render_to_response('sell/sell.html', locals(), context_instance=RequestContext(request))
    
def ajax(request):
    try:
        type = request.GET['type']
        res = request.session['res']
        
        if type == 'sell':
            return HttpResponse(tb.Trade(res).getSellJson())
        
        if type == 'turnover':
            return HttpResponse(tb.Trade(res).getTurnoverJson())
    except Exception, e:
        pass
    
    return HttpResponse('error')