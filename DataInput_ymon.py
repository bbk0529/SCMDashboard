###################################################
#   DATA INPUT                                    #
###################################################
import pandas as pd
import datetime
from django_pandas.io import read_frame
from loteam.models import Ymon, Clearing, YCP4

columns=['U','Sold-To Party','Name 1','Sales Document','Item (SD)','Purchase order no.','Material','MRP Type','Description','Ident-code 1','Ident-code 2','Order Quantity','Open quantity','Pos. created on','Act.conf.date','Requested deliv.date', 'No.Tickets', 'Shipping Conditions']
filename="Q:\\KRGrp007\\★NSC Meeting\\현황판\\YMON.XLSX"

DF=pd.read_excel(filename)
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

for i,v in DF.iterrows():
    #print(i)
    #print(v)
    #ycp4=YCP4.objects.filter(Material=v['Material']),
    #print(ycp4[0].values())
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
        Ymonerrorfile.write(str(ex))
        Ymonerrorfile.write(str(v[['Sales Document','Item (SD)', 'Material']]))

        continue




Ymonerrorfile.close()



for i,v in DF.iterrows():
    try :
        Ymon.objects.create(
            U=v['U'],
            Category=v['Category'],
            Sold_To_Party=v['Sold-To Party'],
            Name_1=v['Name 1'],
            Sales_Document=str(v['Sales Document']),
            Item=v['Item (SD)'],
            Purchase_order_no=str(v['Purchase order no.']),
            ycp4=YCP4.objects.get(Material=v['Material']),
            MRP_Type=v['MRP Type'],
            Description=v['Description'],
            Ident_code_1=v['Ident-code 1'],
            Ident_code_2=v['Ident-code 2'],
            Order_Quantity=v['Order Quantity'],
            Open_quantity=v['Open quantity'],
            Pos_created_on=v['Pos. created on'],
            Actconf_date=v['Act.conf.date'],
            Requested_deliv_date=v['Requested deliv.date'],
            Delta=v['Delta'],
            LT=v['LT'],
            Remark=v['Remark'],
            Topticket=v['No.Tickets'],
            Shippingcondition=v['Shipping Conditions']
        )
    except Exception as ex :
        print(ex, v[['Sales Document','Item (SD)']])
        continue


########################
#Consumption
########################


import pandas as pd
df=pd.read_excel('Dashboard Modeling.xlsx', sheet_name='data')

df['Date']=df['Date'].apply(lambda x: x.to_pydatetime().date()) #timestamp type to datetime.date
df['year']=df['Date'].apply(lambda x: x.year)
df['month']=df['Date'].apply(lambda x: x.month)
df['week']=df['Date'].apply(lambda x: x.isocalendar()[1])
df.groupby(['PN','year','month']).sum()['Qty'].loc[3013354,:,:].to_dict()
df.groupby(['PN','year','week']).sum()['Qty'].loc[3013354,:,:].to_dict()


for i,v in df.iterrows():
    try :
        Consumption.objects.create(
            Pn=v['PN'],
            Date=v['Date'],
            Qty=v['Qty']
        )
    except Exception as ex :
        print(ex, v)
        continue
