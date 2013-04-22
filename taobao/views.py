#-*- coding: utf-8 -*-
'''
Created on 2013-4-16

@author: xinting
'''
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext

def sell(request):
    return render_to_response('sell.html', locals(), context_instance=RequestContext(request))
    
