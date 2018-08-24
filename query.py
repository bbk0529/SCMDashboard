# query set to Dataframe    
from django_pandas.io import read_frame
from blog.models import Ymon
qs=Ymon.objects.all()
DF=read_frame(qs) #df dataframe from query set
BoxPlotLT=DF[['Category','LT']].groupby('Category').describe()
BoxPlotLT['LT'][['min','25%','50%','75%','max']]


DF.sort_values(by='Delta', ascending = True)[['Material','Open quantity','Requested deliv.date', 'Act.conf.date', 'Delta']]


BoxPlotLT=DF[['Category','LT']].groupby('Category').describe()
BoxPlotLT['LT'][['min','25%','50%','75%','max']]

confirmed=DF[DF.Delta>-200]
confirmedDF=DF[DF.Delta>-200].groupby('Division').describe()

unconfirmed=DF[DF.Delta<-200]
unconfirmedDF=DF[DF.Delta<-200].groupby('Division').describe()

confirmedDF=DF[DF.Delta>-200][['Division', 'MRP Type','Open quantity','Pos. created on', 'Act.conf.date','Requested deliv.date','Delta', 'LT']].groupby('Division').describe()




#query1

df1=DF[['Material','Order Quantity','Open quantity']].groupby('Material').sum().sort_values(by='Open quantity', ascending=False)
df2=DF[['Material','Description']] #material info table
df2=df2.drop_duplicates(subset='Material') #remove duplicats
result=df1.merge(df2, on='Material').sort_values(by='Open quantity',ascending=False) #Worked as vlookup in excel
result=result[['Material', 'Description', 'Order Quantity', 'Open quantity' ]]



#QUERY2
df3=DF[DF['Act.conf.date']<datetime.date(2018,12,31)][['Material','Open quantity','Requested deliv.date', 'Act.conf.date']]
df3['delta']=df3['Requested deliv.date']-df3['Act.conf.date']
df3['delta']= df3.delta.apply(lambda x : x.days)
df3.sort_values(by='delta', ascending = True)


#DF['Act.conf.date'].apply(lambda x : type(x))
result2=df3.merge(df2, on='Material').sort_values(by='Open quantity',ascending=False) #Worked as vlookup in excel
result2=result2[['Material', 'Description', 'Open quantity', 'Requested deliv.date', 'Act.conf.date','delta']]
result2.groupby('Material').count().sort_values(by='Open quantity', ascending=False)
result2.groupby('Material').sum().sort_values(by='Open quantity', ascending=False)
result2.groupby('Material').sum()


#QUERY3
DF.sort_values(by=['Material','Act.conf.date'])[['Material','Act.conf.date', 'Open quantity']]


#QUERY4
subdf1=confirmedDF[['LT','Open quantity']].sort_values(by=('LT','mean'), ascending=False)
test=subdf1['LT']['mean']


# from blog.models import leadtime

# for i in test.iteritems() : 
    # try :
        # leadtime.objects.create
        # print(i[0], i[1])


    
# for i,v in DF.iterrows(): 
    # try : 
        # Ymon.objects.create(
            # U=v['U'], 
            # Sold_To_Party=v['Sold-To Party'],
            # Name_1=v['Name 1'],
            # Sales_Document=str(v['Sales Document']),
            # Item=str(v['Item (SD)']),
            # Purchase_order_no=str(v['Purchase order no.']),
            # Material=v['Material'],
            # MRP_Type=v['MRP Type'],
            # Description=v['Description'],
            # Ident_code_1=v['Ident-code 1'],
            # Ident_code_2=v['Ident-code 2'],
            # Order_Quantity=v['Order Quantity'],
            # Open_quantity=v['Open quantity'],
            # Pos_created_on=v['Pos. created on'],
            # Actconf_date=v['Act.conf.date'],
            # Requested_deliv_date=v['Requested deliv.date']
        # )
    # except Exception as ex : 
        # print(ex, v[['Sales Document','Item (SD)']])
        # continue

        
        
        
        
items=[]
for i,v in BoxPlotLT.iterrows():
    item={i:(v.values)}
    print()
    items.append(item)