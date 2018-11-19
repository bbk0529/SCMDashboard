# imported by scm_views.py
from django.views.decorators.csrf import csrf_exempt
from .models import Assay, ChangeLog
from django.shortcuts import render
import datetime


As=Assay.objects.order_by('SA_No')
@csrf_exempt
def updateQuery(request):


    if request.method == 'POST':
        username = request.user.username
        assay=Assay(request.POST)
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
        Supplier7=request.POST.get('Supplier7')
        Supplier7_Qty=request.POST.get('Supplier7_Qty')
        Supplier7_Final_Unit_Price=request.POST.get('Supplier7_Final_Unit_Price')
        Supplier7_Fabricating_Goods=request.POST.get('Supplier7_Fabricating_Goods')
        Supplier7_Modification_of_free_offerd_item=request.POST.get('Supplier7_Modification_of_free_offerd_item')
        Supplier8=request.POST.get('Supplier8')
        Supplier8_Qty=request.POST.get('Supplier8_Qty')
        Supplier8_Final_Unit_Price=request.POST.get('Supplier8_Final_Unit_Price')
        Supplier8_Fabricating_Goods=request.POST.get('Supplier8_Fabricating_Goods')
        Supplier8_Modification_of_free_offerd_item=request.POST.get('Supplier8_Modification_of_free_offerd_item')
        print(request.POST)
        try :
            Ass=Assay.objects.get(SA_No=SA_No)
            if Ass.Type!=Type:
                print("type log"*100)
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Type",
                    Before=Ass.Type,
                    After=Type,
                )

            if Ass.Date!=Date:
                print("Date log")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Date",
                    Before=Ass.Date,
                    After=Date,
                )

            if Ass.Description!=Description:
                print("Description log")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Description",
                    Before=Ass.Description,
                    After=Description,
                )

            if Ass.Number_of_suppliers!=Number_of_suppliers:
                print("Number_of_supplierslog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Number_of_suppliers",
                    Before=Ass.Number_of_suppliers,
                    After=Number_of_suppliers,
                )
            if Ass.Details_1!=Details_1:
                print("Number_of_supplierslog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Details_1",
                    Before=Ass.Details_1,
                    After=Details_1,

                )
            if Ass.Details_2!=Details_2:
                print("Number_of_supplierslog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Details_2",
                    Before=Ass.Details_2,
                    After=Details_2,
                )


            if Ass.Supplier1!=Supplier1 :
                print("Supplier1log")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier1",
                    Before=Ass.Supplier1,
                    After=Supplier1,
                )

            if Ass.Supplier1_Qty!=Supplier1_Qty :
                print("Supplier1_Qtylog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier1_Qty",
                    Before=Ass.Supplier1_Qty,
                    After=Supplier1_Qty,
                )

            if Ass.Supplier1_Final_Unit_Price!=Supplier1_Final_Unit_Price :
                print("Supplier1_Final_Unit_Price_log")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier1_Final_Unit_Price",
                    Before=Ass.Supplier1_Final_Unit_Price,
                    After=Supplier1_Final_Unit_Price,
                )

            if Ass.Supplier1_Fabricating_Goods!=Supplier1_Fabricating_Goods :
                print("Supplier1_Fabricating_Goodslog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier1_Fabricating_Goods",
                    Before=Ass.Supplier1_Fabricating_Goods,
                    After=Supplier1_Fabricating_Goods,
                )

            if Ass.Supplier1_Modification_of_free_offerd_item!=Supplier1_Modification_of_free_offerd_item :
                print("Supplier1_Modification_of_free_offerd_itemlog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier1_Modification_of_free_offerd_item",
                    Before=Ass.Supplier1_Modification_of_free_offerd_item,
                    After=Supplier1_Modification_of_free_offerd_item,
                )

            if Ass.Supplier2!=Supplier2 :
                print("Supplier2log")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier2",
                    Before=Ass.Supplier2,
                    After=Supplier2,
                )

            if Ass.Supplier2_Qty!=Supplier2_Qty :
                print("Supplier2_Qtylog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier2_Qty",
                    Before=Ass.Supplier2_Qty,
                    After=Supplier2_Qty,
                )

            if Ass.Supplier2_Final_Unit_Price!=Supplier2_Final_Unit_Price :
                print("Supplier2_Final_Unit_Pricelog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier2_Final_Unit_Price",
                    Before=Ass.Supplier2_Final_Unit_Price,
                    After=Supplier2_Final_Unit_Price,
                )

            if Ass.Supplier2_Fabricating_Goods!=Supplier2_Fabricating_Goods :
                print("Supplier2_Fabricating_Goodslog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier2_Fabricating_Goods",
                    Before=Ass.Supplier2_Fabricating_Goods,
                    After=Supplier2_Fabricating_Goods,
                )

            if Ass.Supplier2_Modification_of_free_offerd_item!=Supplier2_Modification_of_free_offerd_item :
                print("Supplier2_Modification_of_free_offerd_itemlog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier2_Modification_of_free_offerd_item",
                    Before=Ass.Supplier2_Modification_of_free_offerd_item,
                    After=Supplier2_Modification_of_free_offerd_item,
                )

            if Ass.Supplier3!=Supplier3 :
                print("Supplier3log")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier3",
                    Before=Ass.Supplier3,
                    After=Supplier3,
                )

            if Ass.Supplier3_Qty!=Supplier3_Qty :
                print("Supplier3_Qtylog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier3_Qty",
                    Before=Ass.Supplier3_Qty,
                    After=Supplier3_Qty,
                )

            if Ass.Supplier3_Final_Unit_Price!=Supplier3_Final_Unit_Price :
                print("Supplier3_Final_Unit_Pricelog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier3_Final_Unit_Price",
                    Before=Ass.Supplier3_Final_Unit_Price,
                    After=Supplier3_Final_Unit_Price,
                )

            if Ass.Supplier3_Fabricating_Goods!=Supplier3_Fabricating_Goods :
                print("Supplier3_Fabricating_Goodslog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier3_Fabricating_Goods",
                    Before=Ass.Supplier3_Fabricating_Goods,
                    After=Supplier3_Fabricating_Goods,
                )

            if Ass.Supplier3_Modification_of_free_offerd_item!=Supplier3_Modification_of_free_offerd_item :
                print("Supplier3_Modification_of_free_offerd_itemlog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier3_Modification_of_free_offerd_item",
                    Before=Ass.Supplier3_Modification_of_free_offerd_item,
                    After=Supplier3_Modification_of_free_offerd_item,
                )


            if Ass.Supplier4!=Supplier4 :
                print("Supplier4log")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier4",
                    Before=Ass.Supplier4,
                    After=Supplier4,
                )

            if Ass.Supplier4_Qty!=Supplier4_Qty :
                print("Supplier4_Qtylog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier4_Qty",
                    Before=Ass.Supplier4_Qty,
                    After=Supplier4_Qty,
                )

            if Ass.Supplier4_Final_Unit_Price!=Supplier4_Final_Unit_Price :
                print("Supplier4_Final_Unit_Pricelog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier4_Final_Unit_Price",
                    Before=Ass.Supplier4_Final_Unit_Price,
                    After=Supplier4_Final_Unit_Price,
                )

            if Ass.Supplier4_Fabricating_Goods!=Supplier4_Fabricating_Goods :
                print("Supplier4_Fabricating_Goodslog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier4_Fabricating_Goods",
                    Before=Ass.Supplier4_Fabricating_Goods,
                    After=Supplier4_Fabricating_Goods,
                )

            if Ass.Supplier4_Modification_of_free_offerd_item!=Supplier4_Modification_of_free_offerd_item :
                print("Supplier4_Modification_of_free_offerd_itemlog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier4_Modification_of_free_offerd_item",
                    Before=Ass.Supplier4_Modification_of_free_offerd_item,
                    After=Supplier4_Modification_of_free_offerd_item,
                )
            print(Ass.Supplier5, Supplier5)
            if Ass.Supplier5!=Supplier5 :
                print("Supplier5log")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier5",
                    Before=Ass.Supplier5,
                    After=Supplier5,
                )

            if Ass.Supplier5_Qty!=Supplier5_Qty :
                print("Supplier5_Qtylog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier5_Qty",
                    Before=Ass.Supplier5_Qty,
                    After=Supplier5_Qty,
                )

            if Ass.Supplier5_Final_Unit_Price!=Supplier5_Final_Unit_Price :
                print("Supplier5_Final_Unit_Pricelog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier5_Final_Unit_Price",
                    Before=Ass.Supplier5_Final_Unit_Price,
                    After=Supplier5_Final_Unit_Price,
                )

            if Ass.Supplier5_Fabricating_Goods!=Supplier5_Fabricating_Goods :
                print("Supplier5_Fabricating_Goodslog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier5_Fabricating_Goods",
                    Before=Ass.Supplier5_Fabricating_Goods,
                    After=Supplier5_Fabricating_Goods,
                )

            if Ass.Supplier5_Modification_of_free_offerd_item!=Supplier5_Modification_of_free_offerd_item :
                print("Supplier5_Modification_of_free_offerd_itemlog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier5_Modification_of_free_offerd_item",
                    Before=Ass.Supplier5_Modification_of_free_offerd_item,
                    After=Supplier5_Modification_of_free_offerd_item,
                )

            if Ass.Supplier6!=Supplier6 :
                print("Supplier6log")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier6",
                    Before=Ass.Supplier6,
                    After=Supplier6,
                )

            if Ass.Supplier6_Qty!=Supplier6_Qty :
                print("Supplier6_Qtylog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier6_Qty",
                    Before=Ass.Supplier6_Qty,
                    After=Supplier6_Qty,
                )

            if Ass.Supplier6_Final_Unit_Price!=Supplier6_Final_Unit_Price :
                print("Supplier6_Final_Unit_Pricelog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier6_Final_Unit_Price",
                    Before=Ass.Supplier6_Final_Unit_Price,
                    After=Supplier6_Final_Unit_Price,
                )

            if Ass.Supplier6_Fabricating_Goods!=Supplier6_Fabricating_Goods :
                print("Supplier6_Fabricating_Goodslog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier6_Fabricating_Goods",
                    Before=Ass.Supplier6_Fabricating_Goods,
                    After=Supplier6_Fabricating_Goods,
                )

            if Ass.Supplier6_Modification_of_free_offerd_item!=Supplier6_Modification_of_free_offerd_item :
                print("Supplier6_Modification_of_free_offerd_itemlog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier6_Modification_of_free_offerd_item",
                    Before=Ass.Supplier6_Modification_of_free_offerd_item,
                    After=Supplier6_Modification_of_free_offerd_item,
                )

            if Ass.Supplier7!=Supplier7 :
                print("Supplier7log")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier7",
                    Before=Ass.Supplier7,
                    After=Supplier7,
                )

            if Ass.Supplier7_Qty!=Supplier7_Qty :
                print("Supplier7_Qtylog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier7_Qty",
                    Before=Ass.Supplier7_Qty,
                    After=Supplier7_Qty,
                )

            if Ass.Supplier7_Final_Unit_Price!=Supplier7_Final_Unit_Price :
                print("Supplier7_Final_Unit_Pricelog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier7_Final_Unit_Price",
                    Before=Ass.Supplier7_Final_Unit_Price,
                    After=Supplier7_Final_Unit_Price,
                )

            if Ass.Supplier7_Fabricating_Goods!=Supplier7_Fabricating_Goods :
                print("Supplier7_Fabricating_Goodslog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier7_Fabricating_Goods",
                    Before=Ass.Supplier7_Fabricating_Goods,
                    After=Supplier7_Fabricating_Goods,
                )

            if Ass.Supplier7_Modification_of_free_offerd_item!=Supplier7_Modification_of_free_offerd_item :
                print("Supplier7_Modification_of_free_offerd_itemlog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier7_Modification_of_free_offerd_item",
                    Before=Ass.Supplier7_Modification_of_free_offerd_item,
                    After=Supplier7_Modification_of_free_offerd_item,
                )
            if Ass.Supplier8!=Supplier8 :
                print("Supplier8log")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier8",
                    Before=Ass.Supplier8,
                    After=Supplier8,
                )

            if Ass.Supplier8_Qty!=Supplier8_Qty :
                print("Supplier8_Qtylog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier8_Qty",
                    Before=Ass.Supplier8_Qty,
                    After=Supplier8_Qty,
                )

            if Ass.Supplier8_Final_Unit_Price!=Supplier8_Final_Unit_Price :
                print("Supplier8_Final_Unit_Pricelog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier8_Final_Unit_Price",
                    Before=Ass.Supplier8_Final_Unit_Price,
                    After=Supplier8_Final_Unit_Price,
                )

            if Ass.Supplier8_Fabricating_Goods!=Supplier8_Fabricating_Goods :
                print("Supplier8_Fabricating_Goodslog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier8_Fabricating_Goods",
                    Before=Ass.Supplier8_Fabricating_Goods,
                    After=Supplier8_Fabricating_Goods,
                )

            if Ass.Supplier8_Modification_of_free_offerd_item!=Supplier8_Modification_of_free_offerd_item :
                print("Supplier8_Modification_of_free_offerd_itemlog")
                ChangeLog.objects.create(
                    SA_No=int(SA_No),
                    DateTime=datetime.datetime.now(),
                    User=username,
                    Field="Supplier8_Modification_of_free_offerd_item",
                    Before=Ass.Supplier8_Modification_of_free_offerd_item,
                    After=Supplier8_Modification_of_free_offerd_item,
                )



        except Exception as e:
            print(e, "New creation")


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
                    'Updated_date' : datetime.datetime.now(),
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
