# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.shortcuts import render

# Create your views here.
def index(requests):
    text = {'name' : 'ram','password' : 'sita','datetime' :'' }
    return render(requests,'pools/index.html',context=text)