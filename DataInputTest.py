# import pandas as pd
# import datetime
# from loteam.models import Ymon,YCP4
#
# Ymon.objects.all().delete()
# YCP4.objects.all().delete()
#
#
# filename="Q:\\KRGrp007\\★NSC Meeting\\현황판\\YCP4.XLSX"
# sheet_name='ycp4'
# df=pd.read_excel(filename, header=1)
#
# df=df.iloc[:,[6,7,4,5,18,24,26]]
# df.columns=['Material', 'Description', 'Con3M','Con12M','Stock','Incoming','Order']
#
#
# from loteam.models import YCP4
#
#
# for i,v in df.iterrows():
#     try :
#         YCP4.objects.create(
#             Material = v['Material'],
#             Description=v['Description'],
#             Con3M=v['Con3M'],
#             Con12M=v['Con12M'],
#             Stock=v['Stock'],
#             Incoming=v['Incoming'],
#             Order=v['Order'],
#         )
#     except Exception as ex :
#         print(ex)
#         print(ex, v)
#         continue
#
#
#
#
#
# columns=['U','Sold-To Party','Name 1','Sales Document','Item (SD)','Purchase order no.','Material','MRP Type','Description','Ident-code 1','Ident-code 2','Order Quantity','Open quantity','Pos. created on','Act.conf.date','Requested deliv.date']
# filename="Q:\\KRGrp007\\★NSC Meeting\\현황판\\YMON.XLSX"
#
# DF=pd.read_excel(filename)
# #DF=pd.read_excel('F-KR-YMON_180813.XLSX', converters={'Material':int})
# partnr=pd.read_excel('F-KR-YMON_180813.XLSX', sheet_name='partnr', converters={'Material':int})
# partnr.columns=['Material','Type','Category','Description']
#
# #PRETREATMENT
# DF=DF[columns]
#
# DF['Act.conf.date']=DF['Act.conf.date'].apply(lambda x: x.to_pydatetime().date())
# DF['Pos. created on']=DF['Pos. created on'].apply(lambda x: x.to_pydatetime().date())
# DF['Requested deliv.date']=DF['Requested deliv.date'].apply(lambda x: x.to_pydatetime().date())
# DF.loc[DF['Act.conf.date'].isnull(),'Act.conf.date']=datetime.date(2099,12,31)
#
# #ones with purchase order no is null to be removed
# DF=DF.drop(DF[DF['Purchase order no.'].isnull()].index)
#
# #ones with "nicher" included in description to be removed
# idx=DF['Description'].apply(lambda x : x.find("NICHTER"))
# DF=DF.drop(idx[idx>0].index)
# DF=DF.drop(DF[DF['Material']>51200000].index)
# DF=DF.drop(DF[DF['Material'].between(11900000,12000000)].index)
#
#
# #Adding additional columns , induced by others
# DF['Delta']=DF['Act.conf.date']-DF['Requested deliv.date']
# DF['Delta']= DF.Delta.apply(lambda x : x.days)
#
# DF['LT']=DF['Act.conf.date']-DF['Pos. created on']
# DF['LT']= DF.LT.apply(lambda x : x.days)
#
# DF=DF.merge(partnr[['Material','Category']], on='Material')
#
# for i,v in DF.iterrows():
#     try :
#         Ymon.objects.create(
#             U=v['U'],
#             Category=v['Category'],
#             Sold_To_Party=v['Sold-To Party'],
#             Name_1=v['Name 1'],
#             Sales_Document=str(v['Sales Document']),
#             Item=v['Item (SD)'],
#             Purchase_order_no=str(v['Purchase order no.']),
#             ycp4=YCP4.objects.get(Material=v['Material']),
#             MRP_Type=v['MRP Type'],
#             Description=v['Description'],
#             Ident_code_1=v['Ident-code 1'],
#             Ident_code_2=v['Ident-code 2'],
#             Order_Quantity=v['Order Quantity'],
#             Open_quantity=v['Open quantity'],
#             Pos_created_on=v['Pos. created on'],
#             Actconf_date=v['Act.conf.date'],
#             Requested_deliv_date=v['Requested deliv.date'],
#             Delta=v['Delta'],
#             LT=v['LT']
#         )
#     except Exception as ex :
#         print(ex, v[['Sales Document','Item (SD)']])
#         continue
