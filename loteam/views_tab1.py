#view_ajax.py
from .models import Ymon, YCP4
from django.shortcuts import render
def tab1(request) :
    ymon=Ymon.objects.all()
    #print(ymon)
    return render(
        request, 'blog/tab1.html',{
            'ymon' : ymon
    })
