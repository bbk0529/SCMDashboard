from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductFamily
from .models import Masterdata
from .models import YCP4
import json

def productFamily(request) :
    if request.method=='GET':
        product=request.GET['product'].strip()
        print(product)
        #SGFCode = ProductFamily.objects.filter(Product__contains=product).values()
        SGFCode = str(ProductFamily.objects.filter(Product__contains=product).values()[0]['SGFCode']).replace(".0","")
        partnumbers=Masterdata.objects.filter(Hierarchy__contains=SGFCode).values('Material')
        partlist=[]
        for i in partnumbers :
            #print(i['Material'])
            partlist.append(i['Material'])

        TableData=Masterdata.objects.filter(Material__in=partlist)
        ycp4data=YCP4.objects.filter(Pn__in=partlist)
        print(TableData)
        print(ycp4data)

    else :
        print("not given any product")

    return render (
        request, 'blog/table.html',{
            'TableData' : TableData,
    })
