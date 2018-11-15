from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Assay
from django.views.decorators.csrf import csrf_exempt

import decimal

# Create your views here.
# As=Assay.objects.order_by('SA_No')[:20]
As=Assay.objects.order_by('SA_No')
#######################################
# MAIN default                        #
#######################################
def approvalPlan(request):

    if request.user.is_authenticated:
        return render(
            request, 'procurement/approvalPlan.html',{
            'assayList' : As
            }
        )
    else:
        return redirect('login')

def listAssay(request) :
    return render(
        request, 'procurement/assayList.html',{
        'assayList' : As
    })


def assayQuery(request) :
    if request.method=='GET':
        print("request.method = GET ///assay Query")
        SA_No=request.GET['SA_No'].strip()
        Ass=Assay.objects.get(SA_No=SA_No)
        print(SA_No)

    return render(
        request, 'procurement/view_tab1.html',{
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

@csrf_exempt
def updateQuery(request):
    if request.method == 'POST':
        username = request.user.username
        print(username*100)
        assay=Assay(request.POST)
        print("READ ASSAY",assay)
        SA_No=request.POST.get('SA_No')
        Type=request.POST.get('Type')
        Date=request.POST.get('Date')
        Description=request.POST.get('Description')
        Number_of_suppliers=request.POST.get('Number_of_suppliers')
        Details_1=request.POST.get('Details_1')
        Details_2=request.POST.get('Details_2')
        Supplier1=request.POST.get("Supplier1")
        Supplier1_Qty=request.POST.get("Supplier1_Qty")
        Supplier1_Final_Unit_Price=request.POST.get("Supplier1_Final_Unit_Price")
        Supplier1_Fabricating_Goods=request.POST.get("Supplier1_Fabricating_Goods")
        Supplier1_Modification_of_free_offerd_item=request.POST.get('Supplier1_Modification_of_free_offerd_item')
        Supplier2=request.POST.get('Supplier2')
        Supplier2_Qty=request.POST.get('Supplier2_Qty')
        Supplier2_Final_Unit_Price=request.POST.get('Supplier2_Final_Unit_Price')
        Supplier2_Fabricating_Goods=request.POST.get('Supplier2_Fabricating_Goods')
        Supplier2_Modification_of_free_offerd_item=request.POST.get('Supplier2_Modification_of_free_offerd_item')
        Supplier3=request.POST.get('Supplier3')
        Supplier3_Qty=request.POST.get('Supplier3_Qty')
        Supplier3_Final_Unit_Price=request.POST.get('Supplier3_Final_Unit_Price')
        Supplier3_Fabricating_Goods=request.POST.get('Supplier3_Fabricating_Goods')
        Supplier3_Modification_of_free_offerd_item=request.POST.get('Supplier3_Modification_of_free_offerd_item')
        Supplier4=request.POST.get('Supplier4')
        Supplier4_Qty=request.POST.get('Supplier4_Qty')
        Supplier4_Final_Unit_Price=request.POST.get('Supplier4_Final_Unit_Price')
        Supplier4_Fabricating_Goods=request.POST.get('Supplier4_Fabricating_Goods')
        Supplier4_Modification_of_free_offerd_item=request.POST.get('Supplier4_Modification_of_free_offerd_item')
        Supplier5=request.POST.get('Supplier5')
        Supplier5_Qty=request.POST.get('Supplier5_Qty')
        Supplier5_Final_Unit_Price=request.POST.get('Supplier5_Final_Unit_Price')
        Supplier5_Fabricating_Goods=request.POST.get('Supplier5_Fabricating_Goods')
        Supplier5_Modification_of_free_offerd_item=request.POST.get('Supplier5_Modification_of_free_offerd_item')
        Supplier6=request.POST.get('Supplier6')
        Supplier6_Qty=request.POST.get('Supplier6_Qty')
        Supplier6_Final_Unit_Price=request.POST.get('Supplier6_Final_Unit_Price')
        Supplier6_Fabricating_Goods=request.POST.get('Supplier6_Fabricating_Goods')
        Supplier6_Modification_of_free_offerd_item=request.POST.get('Supplier6_Modification_of_free_offerd_item')

        try:
            Assay.objects.update_or_create(
                SA_No=SA_No,
                defaults={
                    'Type':Type,
                    'Date':Date,
                    'Number_of_suppliers':Number_of_suppliers,
                    'Details_1':Details_1,
                    'Details_2':Details_2,
                    'Description':Description,
                    'Supplier1'                                  :   Supplier1,
                    'Supplier1_Qty'                              :   Supplier1_Qty,
                    'Supplier1_Final_Unit_Price'                 :   Supplier1_Final_Unit_Price,
                    'Supplier1_Fabricating_Goods'                :   Supplier1_Fabricating_Goods,
                    'Supplier1_Modification_of_free_offerd_item' :   Supplier1_Modification_of_free_offerd_item,

                    'Supplier2'                                  :   Supplier2,
                    'Supplier2_Qty'                              :   Supplier2_Qty,
                    'Supplier2_Final_Unit_Price'                 :   Supplier2_Final_Unit_Price,
                    'Supplier2_Fabricating_Goods'                :   Supplier2_Fabricating_Goods,
                    'Supplier2_Modification_of_free_offerd_item' :   Supplier2_Modification_of_free_offerd_item,

                    'Supplier3'                                  :   Supplier3,
                    'Supplier3_Qty'                              :   Supplier3_Qty,
                    'Supplier3_Final_Unit_Price'                 :   Supplier3_Final_Unit_Price,
                    'Supplier3_Fabricating_Goods'                :   Supplier3_Fabricating_Goods,
                    'Supplier3_Modification_of_free_offerd_item' :   Supplier3_Modification_of_free_offerd_item,

                    'Supplier4'                                  :   Supplier4,
                    'Supplier4_Qty'                              :   Supplier4_Qty,
                    'Supplier4_Final_Unit_Price'                 :   Supplier4_Final_Unit_Price,
                    'Supplier4_Fabricating_Goods'                :   Supplier4_Fabricating_Goods,
                    'Supplier4_Modification_of_free_offerd_item' :   Supplier4_Modification_of_free_offerd_item,

                    'Supplier5'                                  :   Supplier5,
                    'Supplier5_Qty'                              :   Supplier5_Qty,
                    'Supplier5_Final_Unit_Price'                 :   Supplier5_Final_Unit_Price,
                    'Supplier5_Fabricating_Goods'                :   Supplier5_Fabricating_Goods,
                    'Supplier5_Modification_of_free_offerd_item' :   Supplier5_Modification_of_free_offerd_item,

                    'Supplier6'                                  :   Supplier6,
                    'Supplier6_Qty'                              :   Supplier6_Qty,
                    'Supplier6_Final_Unit_Price'                 :   Supplier6_Final_Unit_Price,
                    'Supplier6_Fabricating_Goods'                :   Supplier6_Fabricating_Goods,
                    'Supplier6_Modification_of_free_offerd_item' :   Supplier6_Modification_of_free_offerd_item,
                }
            )

        except Exception as ex :
            print(ex)
        Ass=Assay.objects.get(SA_No=SA_No)
    return render(
        # request, 'procurement/view.html',{
         request, 'procurement/approvalPlan.html',{
            'Assay' : Ass,
            'assayList' : As
    })
