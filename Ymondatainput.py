###################################################
#   DATA INPUT                                    #
###################################################
import pandas as pd
import datetime
from blog.models import Ymon

columns=['U','Sold-To Party','Name 1','Sales Document','Item (SD)','Purchase order no.','Material','MRP Type','Description','Ident-code 1','Ident-code 2','Order Quantity','Open quantity','Pos. created on','Act.conf.date','Requested deliv.date']
DF=pd.read_excel('F-KR-YMON_180813.XLSX', converters={'Material':int})
partnr=pd.read_excel('F-KR-YMON_180813.XLSX', sheet_name='partnr', converters={'Material':int})
partnr.columns=['Material','Type','Category','Description']

#PRETREATMENT 
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


#Adding additional columns , induced by others
DF['Delta']=DF['Act.conf.date']-DF['Requested deliv.date']
DF['Delta']= DF.Delta.apply(lambda x : x.days)

DF['LT']=DF['Act.conf.date']-DF['Pos. created on']
DF['LT']= DF.LT.apply(lambda x : x.days)

DF=DF.merge(partnr[['Material','Category']], on='Material')
    
for i,v in DF.iterrows(): 
    try : 
        Ymon.objects.create(
            U=v['U'], 
            Category=v['Category'],
            Sold_To_Party=v['Sold-To Party'],
            Name_1=v['Name 1'],
            Sales_Document=str(v['Sales Document']),
            Item=str(v['Item (SD)']),
            Purchase_order_no=str(v['Purchase order no.']),
            Material=v['Material'],
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
            LT=v['LT']
        )
    except Exception as ex : 
        print(ex, v[['Sales Document','Item (SD)']])
        continue












