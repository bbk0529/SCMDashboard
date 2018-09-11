import pandas as pd

#filename='F-KR-YMON_180813.XLSX'
errorfile=open('errorfile.txt','a')
filename="Q:\\KRGrp007\\★NSC Meeting\\현황판\\YCP4.XLSX"
sheet_name='ycp4'
df=pd.read_excel(filename, header=0)
#df=pd.read_excel(filename, sheet_name=sheet_name, header=1)
df=df.iloc[:,[6,7,4,5,18,23,24,26]]
df.columns=['Material', 'Description', 'Con3M','Con12M','Stock','DelayedPO','Incoming','Order']
df['Status']= df['Stock'] + df['Order'] + df['Incoming'] + df['DelayedPO']

#df=df.set_index('Pn')

from loteam.models import YCP4

for i,v in df.iterrows():
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
            }
        )



    except Exception as ex :
        print(ex, v)
        errorfile.write(ex,v)
        continue



errorfile.close()
