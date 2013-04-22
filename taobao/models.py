#-*- coding: utf-8 -*-
'''
Created on 2013-4-21

@author: xinting
'''
from django.db import models

class TaobaoUser(models.Model):
    user_id = models.IntegerField()
    uid = models.CharField(max_length=32)
    nick = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.nick