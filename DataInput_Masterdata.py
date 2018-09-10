import pandas as pd
df=pd.read_excel('Master_Data.xlsx')

#Column name changed for convenince
df.columns=[
    'Material', 'Description', 'TypeDescription', 'Segmentation',
    'Hierarchy', 'Division', 'PhaseoutDate',
    'MatStat', 'Flag', 'Type',
    'MRPController', 'SpecialProcurementType',
    'SupplyPlant', 'SS0015', 'Outlier0015',
    'SS0360', 'Outier0360', 'SS0208',
    'Outier0208', 'SS0209', 'Outlier0209',
    'SS0330', 'Outlier0330', 'SS0480',
    'Outlier0480', 'SS0481', 'Outlier0481',
    'Con0015', 'Con0208', 'Con0209', 'Con0330','Con0360', 'Con0480','Con0481', 'Vendor'
    ]

#Extract datas for 0360 f-kr
df=df[df['Con0360'].notnull()][[
        'Material', 'Description', 'TypeDescription', 'Segmentation',
        'Hierarchy', 'Type','SupplyPlant',
        'SS0015', 'Outlier0015', 'SS0360', 'Outier0360',
        'Con0015', 'Con0360', 'Vendor'
    ]]


#Pretreatment for wrong value
df.loc[df.Segmentation=='#','Segmentation'] = None
df.loc[df.Vendor=='#','Vendor'] = None
df.loc[df.TypeDescription=='#','TypeDescription'] = None
df.loc[df.Hierarchy=='#','Hierarchy'] = None
df=df.fillna(0)
##################################################################

#EXAMPLE for QUERY1
df.loc[df['Hierarchy'].str.contains('101002020218'),:][['Con0015', 'Con0360']]



from loteam.models import Masterdata, ProductFamily
"""
objs = [
    Masterdata(
        Material= v['Material'],
        Description= v['Description'],
        TypeDescription=v['TypeDescription'],
        Segmentation=v['Segmentation'],
        Hierarchy=v['Hierarchy'],
        Type=v['Type'],
        SupplyPlant=v['SupplyPlant'],
        SS0015=v['SS0015'],
        Outlier0015=v['Outlier0015'],
        SS0360=v['SS0360'],
        Outier0360=v['Outier0360'],
        Con0015=v['Con0015'],
        Con0360=v['Con0360'],
        Vendor=v['Vendor']
    )
    for i, v in df.iterrows()
]
msg = Masterdata.objects.bulk_create(objs)

from itertools import islice
batch_size = 100
while True:
    batch = list(islice(objs, batch_size))
    if not batch:
        break
    Masterdata.objects.bulk_create(batch)

"""
for i,v in df.iterrows():
    try :
        Masterdata.objects.create(
            Material= v['Material'],
            Description= v['Description'],
            TypeDescription=v['TypeDescription'],
            Segmentation=v['Segmentation'],
            Hierarchy=v['Hierarchy'],
            Type=v['Type'],
            SupplyPlant=v['SupplyPlant'],
            SS0015=v['SS0015'],
            Outlier0015=v['Outlier0015'],
            SS0360=v['SS0360'],
            Outier0360=v['Outier0360'],
            Con0015=v['Con0015'],
            Con0360=v['Con0360'],
            Vendor=v['Vendor']        
        )
    except Exception as ex :
        print(ex)
        print(ex, v[['Material']])
        continue


for i,v in df.iterrows():
    try :
        print(v['Material'])

    except Exception as ex :
        print(ex, v[['Material']])
        continue




for i in df.columns :
    for j in df[i] :
        if(j=='#') : print(i, j)
