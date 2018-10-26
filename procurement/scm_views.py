from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Assay
import decimal

# Create your views here.
As=Assay.objects.all()[:10]
def main(request) :
    print("==========================main called")
    #As=Assay.objects.filter(close=decimal.Decimal('NaN'))


    try :
        SA_No=request.GET['SA_No'].strip()
        Ass=Assay.objects.get(SA_No=SA_No)
        return render(
            request, 'procurement/view.html',{
                'Assay' : Ass,
                'assayList' : As
        })


    except Exception as e:
        return render(
            request, 'procurement/view.html',{
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


def updateQuery(request):
    if request.method == 'POST':
        assay=Assay(request.POST)
        print("READ ASSAY",assay)



        SA_No=request.POST.get('SA_No')
        Type=request.POST.get('Type')
        Date=request.POST.get('Date')
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
        request, 'procurement/view.html',{
            'Assay' : Ass,
            'assayList' : As
    })
    # return HttpResponse(request.POST) # methods must return HttpResponse



def deleteQuery(request):
    return
