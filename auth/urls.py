#-*- coding: utf-8 -*-
'''
Created on 2013-4-22

@author: xinting
'''
from django.conf.urls import patterns, include, url
urlpatterns = patterns('auth.views',
                       url('^$', 'auth'),
                       url('^login/', 'login'),
                       url('^password/', 'password'),
                       )