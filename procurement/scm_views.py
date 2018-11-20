from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Assay, ChangeLog
import datetime
import decimal
from .scm_views_updateQuery import *
import xlwt
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import DocumentForm

# Create your views here.
# As=Assay.objects.order_by('SA_No')[:20]
As=Assay.objects.all()

#
# ############################################
# def setting(request):
#     ipAddress=get_client_ip(request)
#     if request.user.username=='buyer':
#         return render(
#             request, 'procurement/setting.html',{
#             'assayList' : As,
#             'ipAddress' : ipAddress
#             }
#         )
#     else:
#         return redirect('/')


#######################################
# MAIN default                        #
#######################################
def approvalPlan(request):
    ipAddress=get_client_ip(request)
    if request.user.username=='buyer':
        return render(
            request, 'procurement/approvalPlan.html',{
            'assayList' : As,
            'ipAddress' : ipAddress
            }
        )
    else:
        return redirect('/')
####################################################
def listAssay(request) :
    ipAddress=get_client_ip(request)
    if request.user.is_authenticated:
        return render(
            request, 'procurement/assayList.html',{
            'assayList' : As,
            'ipAddress' : ipAddress
        })
    else:
        return redirect('login')
def assayQuery(request) :
    if request.method=='GET':
        print("request.method = GET ///assay Query")
        SA_No=request.GET['SA_No'].strip()
        Ass=Assay.objects.get(SA_No=SA_No)
        print(SA_No)

    return render(
        request, 'procurement/assayListDetail.html',{
            'Assay' : Ass,
            'assayList' : As
    })
def approvalPlanQuery(request):
    if request.method == 'GET':
        SA_No=request.GET['SA_No'].strip()
        print("READ ASSAY___",SA_No)
        Ass=Assay.objects.get(SA_No=SA_No)

    return render(
        request,
        'procurement/approvalPlanBody.html',{
            'Assay' : Ass,
            'assayList' : As
        }
    )
def approvalPlanCreate(request):
    return render(
        request,
        'procurement/approvalPlanBody.html',{
        }
    )
#########################################################
def changeLog(request):
    ipAddress=get_client_ip(request)
    if request.user.username=='buyer':
        changeLog=ChangeLog.objects.all()
        return render(
            request, 'procurement/changeLog.html',{
            'changeLog' : changeLog,
            'ipAddress' : ipAddress
        })
    else:
        return redirect('/')
def export_data_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('data')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        'SA_No',
        'Date',
        'Number_of_suppliers',
        'Type',
        'Details_1',
        'Details_2',
        'Description',
        'Category',
        'Updated_date',
        'Supplier1',
        'Supplier1_Fabricating_Goods',
        'Supplier1_Modification_of_free_offerd_item',
        'Supplier1_Qty',
        'Supplier1_Final_Unit_Price',
        'Supplier2',
        'Supplier2_Fabricating_Goods',
        'Supplier2_Modification_of_free_offerd_item',
        'Supplier2_Qty',
        'Supplier2_Final_Unit_Price',
        'Supplier3',
        'Supplier3_Fabricating_Goods',
        'Supplier3_Modification_of_free_offerd_item',
        'Supplier3_Qty',
        'Supplier3_Final_Unit_Price',
        'Supplier4',
        'Supplier4_Fabricating_Goods',
        'Supplier4_Modification_of_free_offerd_item',
        'Supplier4_Qty',
        'Supplier4_Final_Unit_Price',
        'Supplier5',
        'Supplier5_Fabricating_Goods',
        'Supplier5_Modification_of_free_offerd_item',
        'Supplier5_Qty',
        'Supplier5_Final_Unit_Price',
        'Supplier6',
        'Supplier6_Fabricating_Goods',
        'Supplier6_Modification_of_free_offerd_item',
        'Supplier6_Qty',
        'Supplier6_Final_Unit_Price',
        'Supplier7',
        'Supplier7_Fabricating_Goods',
        'Supplier7_Modification_of_free_offerd_item',
        'Supplier7_Qty',
        'Supplier7_Final_Unit_Price',
        'Supplier8',
        'Supplier8_Fabricating_Goods',
        'Supplier8_Modification_of_free_offerd_item',
        'Supplier8_Qty',
        'Supplier8_Final_Unit_Price',
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Assay.objects.all().values_list(
        'SA_No',
        'Date',
        'Number_of_suppliers',
        'Type',
        'Details_1',
        'Details_2',
        'Description',
        'Category',
        'Updated_date',
        'Supplier1',
        'Supplier1_Fabricating_Goods',
        'Supplier1_Modification_of_free_offerd_item',
        'Supplier1_Qty',
        'Supplier1_Final_Unit_Price',
        'Supplier2',
        'Supplier2_Fabricating_Goods',
        'Supplier2_Modification_of_free_offerd_item',
        'Supplier2_Qty',
        'Supplier2_Final_Unit_Price',
        'Supplier3',
        'Supplier3_Fabricating_Goods',
        'Supplier3_Modification_of_free_offerd_item',
        'Supplier3_Qty',
        'Supplier3_Final_Unit_Price',
        'Supplier4',
        'Supplier4_Fabricating_Goods',
        'Supplier4_Modification_of_free_offerd_item',
        'Supplier4_Qty',
        'Supplier4_Final_Unit_Price',
        'Supplier5',
        'Supplier5_Fabricating_Goods',
        'Supplier5_Modification_of_free_offerd_item',
        'Supplier5_Qty',
        'Supplier5_Final_Unit_Price',
        'Supplier6',
        'Supplier6_Fabricating_Goods',
        'Supplier6_Modification_of_free_offerd_item',
        'Supplier6_Qty',
        'Supplier6_Final_Unit_Price',
        'Supplier7',
        'Supplier7_Fabricating_Goods',
        'Supplier7_Modification_of_free_offerd_item',
        'Supplier7_Qty',
        'Supplier7_Final_Unit_Price',
        'Supplier8',
        'Supplier8_Fabricating_Goods',
        'Supplier8_Modification_of_free_offerd_item',
        'Supplier8_Qty',
        'Supplier8_Final_Unit_Price',
    )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
def export_log_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="changeLog.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('changeLog')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
            'SA_No',
            'DateTime',
            'User',
            'Field',
            'Before',
            'After',
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = ChangeLog.objects.all().values_list(
            'SA_No',
            'DateTime',
            'User',
            'Field',
            'Before',
            'After',

    )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip




import pandas as pd
def setting(request):
    print('simple load')
    if request.method == 'POST' and request.FILES['myfile']:
        print('post received')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        uploaded_file_url = fs.url(filename)
        return render(request, 'procurement/setting.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'procurement/setting.html')

def import_data_xls(request):
    print("kkkkkkkkkkkkkkkkkkk")
    uploaded_file_url=request.GET['uploaded_file_url'].strip()
    print(uploaded_file_url)


    df=pd.read_excel('/dev/django' + uploaded_file_url)
    print(df)
    df=df.fillna('')
    Assay.objects.all().delete()
    df.columns=[
        'SA_No',
        'Date',
        'Number_of_suppliers',
        'Type',
        'Supplier1_Fabricating_Goods',
        'Supplier1_Modification_of_free_offerd_item',
        'Supplier1_Qty','Supplier1_Final_Unit_Price',
        'Supplier1',
        'Supplier2_Fabricating_Goods','Supplier2_Modification_of_free_offerd_item','Supplier2_Qty','Supplier2_Final_Unit_Price','Supplier2',
        'Supplier3_Fabricating_Goods','Supplier3_Modification_of_free_offerd_item','Supplier3_Qty','Supplier3_Final_Unit_Price','Supplier3',
        'Supplier4_Fabricating_Goods','Supplier4_Modification_of_free_offerd_item','Supplier4_Qty','Supplier4_Final_Unit_Price','Supplier4',
        'Supplier5_Fabricating_Goods','Supplier5_Modification_of_free_offerd_item','Supplier5_Qty','Supplier5_Final_Unit_Price','Supplier5',
        'Supplier6_Fabricating_Goods','Supplier6_Modification_of_free_offerd_item','Supplier6_Qty','Supplier6_Final_Unit_Price','Supplier6',
        'Details_1',
        'Details_2',
        'Description',
        'Category',
        'Updated_date',
    ]
    for i,v in df.iterrows() :
        print(i)
        Assay.objects.update_or_create(
                    SA_No=v['SA_No']                        ,
                    defaults={
                        'SA_No':v['SA_No'],
                        'Date':v['Date'],
                        'Number_of_suppliers':v['Number_of_suppliers'],
                        'Type':v['Type'],
                        'Details_1':v['Details_1'],
                        'Details_2':v['Details_2'],
                        'Description':v['Description'],
                        'Category':v['Category'],
                        'Updated_date':v['Updated_date'],

                        'Supplier1':v['Supplier1'],
                        'Supplier1_Fabricating_Goods':v['Supplier1_Fabricating_Goods'],
                        'Supplier1_Modification_of_free_offerd_item':v['Supplier1_Modification_of_free_offerd_item'],
                        'Supplier1_Qty':v['Supplier1_Qty'],
                        'Supplier1_Final_Unit_Price': v['Supplier1_Final_Unit_Price'],

                        'Supplier2':v['Supplier2'],
                        'Supplier2_Fabricating_Goods':v['Supplier2_Fabricating_Goods'],
                        'Supplier2_Modification_of_free_offerd_item':v['Supplier2_Modification_of_free_offerd_item'],
                        'Supplier2_Qty':v['Supplier2_Qty'],
                        'Supplier2_Final_Unit_Price': v['Supplier2_Final_Unit_Price'],

                        'Supplier3':v['Supplier3'],
                        'Supplier3_Fabricating_Goods':v['Supplier3_Fabricating_Goods'],
                        'Supplier3_Modification_of_free_offerd_item':v['Supplier3_Modification_of_free_offerd_item'],
                        'Supplier3_Qty':v['Supplier3_Qty'],
                        'Supplier3_Final_Unit_Price': v['Supplier3_Final_Unit_Price'],

                        'Supplier4':v['Supplier4'],
                        'Supplier4_Fabricating_Goods':v['Supplier4_Fabricating_Goods'],
                        'Supplier4_Modification_of_free_offerd_item':v['Supplier4_Modification_of_free_offerd_item'],
                        'Supplier4_Qty':v['Supplier4_Qty'],
                        'Supplier4_Final_Unit_Price': v['Supplier4_Final_Unit_Price'],

                        'Supplier5':v['Supplier5'],
                        'Supplier5_Fabricating_Goods':v['Supplier5_Fabricating_Goods'],
                        'Supplier5_Modification_of_free_offerd_item':v['Supplier5_Modification_of_free_offerd_item'],
                        'Supplier5_Qty':v['Supplier5_Qty'],
                        'Supplier5_Final_Unit_Price': v['Supplier5_Final_Unit_Price'],

                        'Supplier6':v['Supplier6'],
                        'Supplier6_Fabricating_Goods':v['Supplier6_Fabricating_Goods'],
                        'Supplier6_Modification_of_free_offerd_item':v['Supplier6_Modification_of_free_offerd_item'],
                        'Supplier6_Qty':v['Supplier6_Qty'],
                        'Supplier6_Final_Unit_Price': v['Supplier6_Final_Unit_Price'],
                    }
        )
    return HttpResponse('')
