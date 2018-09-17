from loteam.models import YCP4
from django_pandas.io import read_frame
data=YCP4.objects.values_list('Material')
df=read_frame(data)
df.to_clipboard()

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
                'Mrp': v['MRP Type'],
            }
        )



    except Exception as ex :
        print(ex, v)
        errorfile.write(ex,v)
        continue
