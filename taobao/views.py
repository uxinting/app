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
from django.http.response import HttpResponse

def sell(request):
    if request.user is None:
        return render_to_response('auth/login.html', {}, context_instance=RequestContext(request))
        
    try:
        sessionKey = request.user.get_profile().sessionKey
        
        req = topapi.TradesSoldGetRequest(settings.SANDBOX_URL)
        req.set_app_info(top.appinfo(settings.APPKEY, settings.APPSECRET))
        
        req.fields = 'total_fee, buyer_nick, pay_time, end_time'
        t = list(time.gmtime())
        t[1] = t[1] - 1
        req.start_created = time.strftime('%Y-%m-%d %H:%M:%S', tuple(t))
        
        res = req.getResponse(sessionKey).get('trades_sold_get_response', '')
        total_results = res.get('total_results', '0')
        trade = res.get('trades', None).get('trade', None)
        request.session['trade'] = trade
        
        sell = {}
        for item in trade:
            if item.get('pay_time', None) is None:
                continue
            key = item['pay_time'][:10]
            
            try:
                sell[key] = sell[key] + 1
            except:
                sell[key] = 1
                
        sell = sell.items()
            
    except Exception, e:
        return render_to_response('error.html', {'from': 'sell', 'error': repr(e)})
    return render_to_response('sell.html', locals(), context_instance=RequestContext(request))
    
def ajax(request):
    try:
        type = request.GET['type']
        trade = request.session['trade']
        print type, trade
    except Exception, e:
        return render_to_response('error.html', {'from': 'sell', 'error': repr(e)})
    
    return HttpResponse('ok')