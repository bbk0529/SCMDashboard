from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from tablib import Dataset
from django.http import HttpResponse
from .resources import YmonResource
from django.db.models import Avg, Count, Min, Sum, Max
from .models import Ymon
from django_pandas.io import read_frame
import pandas as pd
import datetime

qs=Ymon.objects.all()
DF=read_frame(qs) #df dataframe from query set

def index(request):
    
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    YmonSum=Ymon.objects.all().aggregate(Sum('Open_quantity'))['Open_quantity__sum']
    YmonAvg=Ymon.objects.all().aggregate(Avg('Open_quantity'))['Open_quantity__avg']
    YmonMax=Ymon.objects.all().aggregate(Max('Open_quantity'))['Open_quantity__max']
    YmonCount=Ymon.objects.all().aggregate(Count('Open_quantity'))['Open_quantity__count']
    
    print("YMON SUM",  YmonSum, YmonAvg, YmonMax, YmonCount)
    TableData=Ymon.objects.values('Category','Material', 'Description','LT').filter(LT__lte=300).order_by('-LT')
    #TableData=DF[['Category','Material','Description','LT']]
    return render(
        request, 'blog/index.html',{
            'YmonSum':YmonSum, 
            'YmonAvg' : YmonAvg,
            'YmonMax' : YmonMax,
            'YmonCount' : YmonCount,
            'TableData' : TableData
    })
    
 
def ui_buttons(request):
    return render(request, 'blog/ui-buttons.html',{'test' : 10293845})
    
@csrf_protect
def test(request): #called by dashboard.js (traffic)
    print("test, json called")
    #posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = list(Post.objects.all())
    #entry_list = list(Entry.objects.all())
    #return  JsonResponse({'foo': 'bar'})
    # data = {
        # 'name': 'Vitor',
        # 'location': 'Finland',
        # 'is_active': True,
        # 'count': 28
    # }
    #return JsonResponse(data)
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
    
def barchart(request):
    BarPlot=DF[DF.LT<365][['Category','LT']].groupby('Category').mean()
    BarPlot=BarPlot.sort_values(by='LT',ascending=False)
    items=BarPlot.to_dict()['LT']
    print("barchart @ server side, called")
    return JsonResponse(items)

def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="persons.json"'
    return response
    
    
def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'blog/simple_upload.html')