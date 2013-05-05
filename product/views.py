#-*- coding: utf-8 -*-
'''
Created on 2013-4-27

@author: Administrator
'''
from django.shortcuts import render_to_response
from taobao import settings
from django.http import HttpResponse
import tb
from django.views.decorators.csrf import csrf_exempt

def product(request):
    title = u'我的宝贝'
    try:
        sessionKey = request.user.get_profile().sessionKey
    except:
        error = u"您还没有登录.."
    return render_to_response('product/product.html', locals())

@csrf_exempt
def ajax(request):
    options = {}
    
    if request.method == 'POST':
        data = request.POST
    else:
        data = request.GET
        
    if request.session.get('product'+data.get('id', '0'), False) is False:
        try:
            sessionKey = request.user.get_profile().sessionKey
        except:
            error = 'error: ' + u'获取授权密钥失败'
        
        options['appkey'] = settings.APPKEY
        options['appsecret'] = settings.APPSECRET
        options['sessionKey'] = sessionKey
        options['url'] = settings.SANDBOX_URL
          
    try:
        type = data['type']
        
        if type == 'product':
            id = data.get('id', 0)
            options['parent_cid'] = id
            return HttpResponse(tb.Products(request.session, options).getProductJson())
    except Exception, e:
        error = 'error: ' + repr(e)
        return HttpResponse(error)