#-*- coding: utf-8 -*-
'''
Created on 2013-4-27

@author: Administrator
'''
from django.conf.urls import patterns, include, url
urlpatterns = patterns('about.views',
                       url(r'^$', 'about'),
                       url(r'^ajax', 'ajax'),
                       )