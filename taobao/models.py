#-*- coding: utf-8 -*-
'''
Created on 2013-4-21

@author: xinting
'''
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    
    sessionKey = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.user.username, self.sessionKey