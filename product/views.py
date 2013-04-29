#-*- coding: utf-8 -*-
'''
Created on 2013-4-27

@author: Administrator
'''
from django.shortcuts import render_to_response
from taobao import settings
from django.http import HttpResponse
import tb

def product(request):
    title = u'我的宝贝'
    try:
        sessionKey = request.user.get_profile().sessionKey
    except:
        error = u"您还没有登录.."
    return render_to_response('product/product.html', locals())

def ajax(request):
    options = {}
    if request.session.get('product', False) is False:
        try:
            sessionKey = request.user.get_profile().sessionKey
        except:
            error = 'error: ' + u'获取授权密钥失败'
        
        options['appkey'] = settings.APPKEY
        options['appsecret'] = settings.APPSECRET
        options['sessionKey'] = sessionKey
        options['url'] = settings.SANDBOX_URL
    try:
        type = request.GET['type']
        
        if type == 'product':
            return HttpResponse(tb.Products(request.session, options).getProductJson())
    except Exception, e:
        error = 'error: ' + repr(e)
        return HttpResponse(error)