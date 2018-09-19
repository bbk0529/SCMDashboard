#view_ajax.py
from .models import Ymon, YCP4
from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
from django.core.serializers import serialize
from django_pandas.io import read_frame
import json

import time
starttime = time.time()

def tab3(request) :
    df=YCP4.objects.filter(Status__lt=0)
    print(df)
    return render(
            request, 'blog/tab3.html',{
                'df' : df
    })
