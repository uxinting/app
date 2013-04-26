#-*- coding: utf-8 -*-
'''
Created on 2013-4-22

@author: xinting
'''
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from taobao import settings
from hashlib import md5
import base64
from taobao.models import UserProfile
import urlparse
from django.template.context import RequestContext
from django.contrib import auth as pyauth

def auth(request):
    try:
        top_appkey = request.GET.get('top_appkey', 'none')
        top_session = request.GET.get('top_session', 'none')
        top_parameters_base64 = request.GET.get('top_parameters', 'none')
        top_parameters = base64.decodestring(top_parameters_base64)
        top_sign = request.GET.get('top_sign', 'none')
        
        request.session['top_parameters'] = top_parameters
        request.session['top_session'] = top_session
        #验证
        if top_sign != base64.b64encode(md5(top_appkey + top_parameters_base64 + top_session + settings.APPSECRET).digest()):
            return render_to_response('error.html', {'error': '签名未通过, 授权失败'}) 
    except Exception, e:
        return render_to_response('error.html', {'from': 'auth', 'error': repr(e)})
    return render_to_response('auth/password.html', {}, context_instance=RequestContext(request))

def password(request):
    try:
        top_parameters = urlparse.parse_qs(urlparse.urlparse('?' + request.session['top_parameters']).query)
        top_session = request.session['top_session']
        
        #添加用户
        nick = top_parameters['visitor_nick'][0]
        pw = request.POST['password']
        #直接登录
        User.objects.create_user(username=nick, password=pw).save()
        user = pyauth.authenticate(username=nick, password=pw)
        
        #保存sessionKeyl
        UserProfile.objects.create(user=user, sessionKey=top_session).save()
        if user is not None and user.is_active:
            pyauth.login(request, user)
    except Exception, e:
        return render_to_response('error.html', {'from': 'password', 'error': repr(e)})
    return HttpResponseRedirect('/')

def login(request):
    try:
        nick = request.POST['username']
        password = request.POST['password']
        
        try:
            User.objects.get(username=nick)
        except:
            return HttpResponseRedirect(settings.SANDBOX_AUTH)

        user = pyauth.authenticate(username=nick, password=password)
        if user is not None and user.is_active:
            pyauth.login(request, user)
    except Exception, e:
        return render_to_response('error.html', {'from': 'login', 'error': repr(e)})
    return HttpResponseRedirect('/')

def logout(request):
    try:
        pyauth.logout(request)
    except Exception, e:
        return render_to_response('error.html', {'error': repr(e)})       
    return HttpResponseRedirect('/')