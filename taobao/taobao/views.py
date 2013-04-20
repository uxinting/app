#-*- coding: utf-8 -*-
'''
Created on 2013-4-16

@author: xinting
'''
from django.shortcuts import render_to_response
import top.api
from taobao import settings

def welcome(request):
    top.setDefaultAppInfo(settings.APPKEY, settings.APPSECRET)
    
    #req = top.api.UserGetRequest(settings.SANDBOX_URL)
    #req = top.api.UserBuyerGetRequest(settings.SANDBOX_URL)
    req = top.api.ItemcatsGetRequest(settings.SANDBOX_URL)
    req.fields = 'cid, name, parent_cid'
    req.parent_cid = 0
    try:
        info = req.getResponse(settings.C_1_SESSION_KEY).get('itemcats_get_response', '').get('item_cats', '').get('item_cat', '')
    except Exception, e:
        info = e
    return render_to_response('welcome.html', {'info': info})