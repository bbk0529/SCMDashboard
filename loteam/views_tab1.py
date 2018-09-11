#view_ajax.py
from .models import Ymon, YCP4
from django.shortcuts import render
from django.shortcuts import redirect

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
