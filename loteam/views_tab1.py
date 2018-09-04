#view_ajax.py
from .models import Ymon, YCP4
from django.shortcuts import render
from django.shortcuts import redirect
def tab1(request) :
    if request.user.is_authenticated:
        ymon=Ymon.objects.all()
        #print(ymon)
        return render(
            request, 'blog/tab1.html',{
                'ymon' : ymon
        })
    else:
        return redirect('login')
