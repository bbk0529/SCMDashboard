import pandas as pd
df=pd.read_excel('product family.xlsx')
#df=pd.read_excel('product family.xlsx',dtype={'SGF code':str})
from loteam.models import ProductFamily

for i,v in df.iterrows():
    try :
        ProductFamily.objects.create(
            Product= v['Product'],
            SGFCode= v['SGF code'],
            Focus= v['Focus'],
            Pn=v['Pn']
        )
    except Exception as ex :
        print(ex)
        print(ex, v)
        continue
