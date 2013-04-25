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

def sell(request):
    try:
        print request.user.get_profile().sessionKey
    except:
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
        turnover = {}
        for item in trade:
            if item.get('pay_time', None) is None:
                continue
            key = item['pay_time'][:10]
            
            try:
                sell[key] = sell[key] + 1
                turnover[key] = turnover[key] + float(item['total_fee'])
            except:
                sell[key] = 1
                turnover[key] = float(item['total_fee'])
                
        sell = sell.items()
        turnover = turnover.items()
            
    except Exception, e:
        return render_to_response('error.html', {'from': 'sell', 'error': repr(e)})
    return render_to_response('sell/sell.html', locals(), context_instance=RequestContext(request))
    
def ajax(request):
    try:
        type = request.GET['type']
        trade = request.session['trade']
        
        turnover = {}
        for item in trade:
            if item.get('pay_time', None) is None:
                continue

            key = item['pay_time'][:10]
            
            try:
                turnover[key] = turnover[key] + float(item['total_fee'])
            except:
                turnover[key] = float(item['total_fee'])
            
        turnover = turnover.items()
            
        return HttpResponse(json.dumps(turnover))
    except Exception, e:
        print e
        pass
    
    return HttpResponse('error')