#-*- coding: utf-8 -*-
'''
Created on 2013-4-26

@author: xinting
'''
from django.conf.urls import patterns, include, url
urlpatterns = patterns('buyer.views',
                       url('^$', 'buyer'),
                       url('^ajax', 'ajax'),
                       )