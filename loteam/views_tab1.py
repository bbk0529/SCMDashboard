#view_ajax.py
from .models import Ymon, YCP4
from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
from django.core.serializers import serialize
from django_pandas.io import read_frame
import json

import time
starttime = time.time()

def tab1(request) :
    if request.user.is_authenticated:
        print("login")
        ymon=Ymon.objects.all()
        print("data read")
        print(starttime-time.time())


        return render(
            request, 'blog/tab1.html',{
                'ymon' : ymon
        })
    else:
        return redirect('login')

def tab2(request) :
    ymon=read_frame(Ymon.objects.filter(Description__contains='dgsl')).to_json()
    print(ymon)
    return HttpResponse(json.dumps(ymon), content_type="application/json")
    # return render(
    #     request, 'blog/table_tab2.html',{
    #         'ymon' : ymon
    # })
