#-*- coding: utf-8 -*-
'''
Created on 2013-4-27

@author: Administrator
'''
from django.conf.urls import patterns, include, url
urlpatterns = patterns('product.views',
                       url(r'^$', 'product'),
                       url(r'^ajax', 'ajax'),
                       )