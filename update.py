def ycp4Update() :
    print("_________ycp4Update loaded")
    import pandas as pd
    import time
    import datetime


    starttime=time.time()
    #filename='F-KR-YMON_180813.XLSX'
    errorfile=open('errorfile.txt','a')
    filename="Q:\\KRGrp007\\★NSC Meeting\\현황판\\YCP4.XLSX"
    print("________YCP4 excel file being loaded")
    df=pd.read_excel(filename, header=0)
    print("________YCP4 file loaded, to be put into the database")
    #df=pd.read_excel(filename, sheet_name=sheet_name, header=1)
    #df=df.loc[:,['Material',]]
    df=df.loc[:,[
        'Material','Material Description','Average consumption of 3 months',
        'Average consumption of 12 months','MRP Unrestr. stock',
        'Quantity delayed purch.orders','Quantity current purch.orders',
        'Total Reservierungen / Sales Orders', 'MRP Type']]
    df.columns=['Material', 'Description', 'Con3M','Con12M','Stock','DelayedPO','Incoming','Order', 'MRP Type']
    df['Status']= df['Stock'] + df['Order'] + df['Incoming'] + df['DelayedPO']

    #df=df.set_index('Pn')

    from loteam.models import YCP4
    i=0
    for i,v in df.iterrows():
        i=i+1
        if (i%100 == 0) : print(i,"inputted")
        try :
            YCP4.objects.update_or_create(
                Material = v['Material'],
                defaults={
                    'Description':v['Description'],
                    'Con3M':v['Con3M'],
                    'Con12M':v['Con12M'],
                    'Stock':v['Stock'],
                    'Incoming':v['Incoming'] + v['DelayedPO'],
                    'Order': v['Order'],
                    'Status': v['Status'],
                    'Mrp': v['MRP Type'],
                }
            )



        except Exception as ex :
            print(ex, v)
            errorfile.write((
                str(datetime.datetime.now()) +
                str(ex) +
                str(v['Material'])
                ))

            continue



    errorfile.close()


    print("completed")
    print(time.time()-starttime)
    print("completed")


def ymonUpdate() :
    ###################################################
    #   DATA INPUT                                    #
    ###################################################
    import pandas as pd
    import datetime
    from django_pandas.io import read_frame
    from loteam.models import Ymon, Clearing, YCP4
    print("ymonUpdate loaded")
    columns=['U','Sold-To Party','Name 1','Sales Document','Item (SD)','Purchase order no.','Material','MRP Type','Description','Ident-code 1','Ident-code 2','Order Quantity','Open quantity','Pos. created on','Act.conf.date','Requested deliv.date', 'No.Tickets', 'Shipping Conditions']
    filename="Q:\\KRGrp007\\★NSC Meeting\\현황판\\YMON.XLSX"
    print("ymonUpdate loaded, and ymon file to be read")
    DF=pd.read_excel(filename)
    print("ymonUpdate file read")
    #partnr=pd.read_excel('F-KR-YMON_180813.XLSX', sheet_name='partnr', converters={'Material':int})
    #partnr.columns=['Material','Type','Category','Description']

    ####################################################
    #PRETREATMENT
    ####################################################
    DF=DF[columns]

    DF['Act.conf.date']=DF['Act.conf.date'].apply(lambda x: x.to_pydatetime().date())
    DF['Pos. created on']=DF['Pos. created on'].apply(lambda x: x.to_pydatetime().date())
    DF['Requested deliv.date']=DF['Requested deliv.date'].apply(lambda x: x.to_pydatetime().date())
    DF.loc[DF['Act.conf.date'].isnull(),'Act.conf.date']=datetime.date(2099,12,31)

    #ones with purchase order no is null to be removed
    DF=DF.drop(DF[DF['Purchase order no.'].isnull()].index)

    #ones with "nicher" included in description to be removed
    idx=DF['Description'].apply(lambda x : x.find("NICHTER"))
    DF=DF.drop(idx[idx>0].index)
    DF=DF.drop(DF[DF['Material']>51200000].index)
    DF=DF.drop(DF[DF['Material'].between(11900000,12000000)].index)




    ####################################################
    #PRETREATMENT
    ####################################################

    #Adding additional columns , induced by others
    DF['Delta']=DF['Act.conf.date']-DF['Requested deliv.date']
    DF['Delta']= DF.Delta.apply(lambda x : x.days)

    DF['LT']=DF['Act.conf.date']-DF['Pos. created on']
    DF['LT']= DF.LT.apply(lambda x : x.days)
    #DF=DF.merge(partnr[['Material','Category']], on='Material')

    clearing=read_frame(Clearing.objects.all())
    DF.loc[DF['Material'].isin(clearing.Material),'Remark']='Clearing'
    DF.loc[:,'Remark']=DF.Remark.fillna("")
    writer=pd.ExcelWriter('masterforycp4.xlsx')
    pd.DataFrame(DF.Material.unique()).to_excel(writer, "Master")
    writer.save()



    Ymonerrorfile=open('ymonerrorfile.txt','a')
    i=0
    for i,v in DF.iterrows():
        #print(i)
        #print(v)
        #ycp4=YCP4.objects.filter(Material=v['Material']),
        #print(ycp4[0].values())

        i=i+1
        if (i%100 == 0) : print(i,"inputted")
        try:

            Ymon.objects.update_or_create(
                Sales_Document=str(v['Sales Document']),
                Item=v['Item (SD)'],
                defaults={
                    'ycp4': YCP4.objects.get(Material=v['Material']),
                    'U':v['U'],
                    'Sold_To_Party':v['Sold-To Party'],
                    'Name_1':v['Name 1'],
                    'Sales_Document':str(v['Sales Document']),
                    'Item':v['Item (SD)'],
                    'Purchase_order_no':str(v['Purchase order no.']),
                    'MRP_Type':v['MRP Type'],
                    'Description':v['Description'],
                    'Ident_code_1':v['Ident-code 1'],
                    'Ident_code_2':v['Ident-code 2'],
                    'Order_Quantity':v['Order Quantity'],
                    'Open_quantity':v['Open quantity'],
                    'Pos_created_on':v['Pos. created on'],
                    'Actconf_date':v['Act.conf.date'],
                    'Requested_deliv_date':v['Requested deliv.date'],
                    'Delta':v['Delta'],
                    'LT':v['LT'],
                    'Remark':v['Remark'],
                    'Topticket':v['No.Tickets'],
                    'Shippingcondition':v['Shipping Conditions']
                    }
                )

        except Exception as ex :
            print(ex, v[['Sales Document','Item (SD)']])
            Ymonerrorfile.write(str(datetime.datetime.now()))
            Ymonerrorfile.write(str(ex))
            Ymonerrorfile.write(str(v[['Sales Document','Item (SD)', 'Material']]))

            continue




    Ymonerrorfile.close()
