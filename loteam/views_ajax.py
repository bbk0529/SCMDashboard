#views_ajax.py
import pandas as pd
import datetime
import json

from django_pandas.io import read_frame
from django.utils import timezone

from django.db.models import Avg, Count, Min, Sum, Max
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Post
from .models import Ymon
from .models import Consumption



 
def ui_buttons(request):
    return render(request, 'blog/ui-buttons.html',{'test' : 10293845})
    
    
    
def index(request):
    
    if request.user.is_authenticated:        
        
        posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        
        YmonSum=Ymon.objects.all().aggregate(Sum('Open_quantity'))['Open_quantity__sum']
        YmonAvg=Ymon.objects.all().aggregate(Avg('Open_quantity'))['Open_quantity__avg']
        YmonMax=Ymon.objects.all().aggregate(Max('Open_quantity'))['Open_quantity__max']
        YmonCount=Ymon.objects.all().aggregate(Count('Open_quantity'))['Open_quantity__count']
        
        print("YMON SUM",  YmonSum, YmonAvg, YmonMax, YmonCount)
        TableData=Ymon.objects.values('Category','Material', 'Description','LT').filter(LT__lte=300).order_by('-LT')
        # TableData=DF[['Category','Material','Description','LT']]
        print(TableData)
        return render(
            request, 'blog/index.html',{
                'YmonSum':YmonSum, 
                'YmonAvg' : YmonAvg,
                'YmonMax' : YmonMax,
                'YmonCount' : YmonCount,
                'TableData' : TableData
        })
    
    else:
        return redirect('login')


# qs=Ymon.objects.all()
# DF=read_frame(qs) #df dataframe from query set



def barchart(request):
    BarPlot=DF[DF.LT<365][['Category','LT']].groupby('Category').mean()
    BarPlot=BarPlot.sort_values(by='LT',ascending=False)
    items=BarPlot.to_dict()['LT']
    print("barchart @ server side, called")
    return JsonResponse(items)

def barchart2(request):
    try : #set up ID for search
        if request.method == 'GET':
            id = int(request.GET['id'])
    
    except : #default ID for showing at the initial view
        id = 1000500


    
    df=read_frame(Consumption.objects.filter(Pn=id))#SELECT * from Consumption WHERE pn=id   
    df['Date']=df['Date'].apply(lambda x : str(x))
    # df['year']=df['Date'].apply(lambda x: x.year)
    # df['month']=df['Date'].apply(lambda x: x.month)
    # df['week']=df['Date'].apply(lambda x: x.isocalendar()[1])       
    # df['rolling']=df[Qty].rolling(window=120, min_periods=1).mean()
    
    # BarPlot2=df.groupby(['Pn','year','week']).sum()['Qty'].loc[id,:,:].to_json()
    
    BarPlot2=df.groupby('Date').sum()['Qty'].sort_index()
    BarPlot2Mean=BarPlot2.rolling(window=30, min_periods=1).mean()
    BarPlot2=BarPlot2.to_json()    
    BarPlot2Mean=BarPlot2Mean.to_json()   
    data={'BarPlot2' : BarPlot2, 'BarPlot2Mean' : BarPlot2Mean}
    
    # return HttpResponse(data, content_type="application/json")
    return HttpResponse(json.dumps(data), content_type="application/json")
    
    

def test(request): #called by dashboard.js (traffic)
    print("test, json called")    
    posts = list(Post.objects.all())
    
    qs=Ymon.objects.all()
    DF=read_frame(qs) #df dataframe from query set    
    data1=DF[['Material','Open_quantity']].groupby('Material').sum()[:28].to_json()
    data2=DF[['Material','Open_quantity']].groupby('Material').sum()[:28].to_json()
    return JsonResponse(data1, safe=False)  # or JsonResponse({'data': data})
    
def boxplot(request):            
    
    BoxPlotLT=DF[DF.LT<365][['Category','LT']].groupby('Category').describe()
    BoxPlotLT=BoxPlotLT['LT'][['min','25%','50%','75%','max']].sort_values('50%', ascending=False)
    items={}
    z=0
    for i,v in BoxPlotLT.iterrows():
        items[i] = list(v.values)    
        z=z+1
        if(z>10) : break
    
    return JsonResponse(items)