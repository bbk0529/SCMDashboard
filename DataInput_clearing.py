import pandas as pd
import datetime
from loteam.models import Ymon,YCP4, Clearing

filename="Q:\\KRGrp007\\★NSC Meeting\\현황판\\clearing.XLSX"
df=pd.read_excel(filename)



for i,v in df.iterrows():
    try :
        Clearing.objects.create(
            Material = v
        )
    except Exception as ex :
        print(ex, v)
        continue





DF.join(df.iloc[:,4])
D.Grouping.describe()
A.join(df.iloc[:,4]).iloc[:,-2:].groupby('Grouping').count()
