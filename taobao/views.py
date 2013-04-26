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
        
        trade = request.session.get('trade', None)
        if trade is None:
            res = tb.Trade().getRes(settings.APPKEY, settings.APPSECRET, settings.SANDBOX_URL, sessionKey, options={'start_created': '2013-04-01 00:00:00'})
            trade = res.get('trades').get('trade')
            total_results = res.get('total_results', 0)
            request.session['total_results'] = total_results
            request.session['trade'] = trade
        
        sell = trade[0].items()
        orders = trade[0].get('orders').get('order')[0].items()
    except Exception, e:
        return render_to_response('error.html', {'from': 'sell', 'error': repr(e)})
    return render_to_response('sell/sell.html', locals(), context_instance=RequestContext(request))
    
def ajax(request):
    try:
        type = request.GET['type']
        trade = request.session['trade']
        
        if type == 'sell':
            return HttpResponse(tb.Trade().getSellJson(trade=trade))
        
        if type == 'turnover':
            return HttpResponse(tb.Trade().getTurnoverJson(trade=trade))
    except Exception, e:
        pass
    
    return HttpResponse('error')