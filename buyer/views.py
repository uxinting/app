#-*- coding: utf-8 -*-
'''
Created on 2013-4-26

@author: xinting
'''
from django.shortcuts import render_to_response
from tb import Buyer
from taobao import settings

def buyer(request):
    title = u'我的买家'
    
    sessionKey = request.user.get_profile().sessionKey
    if request.session.get('trade', None) is None:
        buyer = Buyer(request.session)
        buyers = buyer.getBuyers(settings.APPKEY, settings.APPSECRET, settings.SANDBOX_URL, sessionKey, options={'start_created': '2013-04-01 00:00:00'})
        request.session['trade'] = buyer.getTrade()
        request.session['buyer'] = buyers
    return render_to_response('buyer/buyer-buyer.html', locals())

def ajax(request):
    try:
        type = request.GET['type']
        trade = request.session['trade']
    except:
        pass