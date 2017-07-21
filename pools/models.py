# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length = 30,  primary_key=True)
    password = models.CharField(max_length = 15)