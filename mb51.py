#MB51Parser('MB51test.txt')

"""

from mb51 import *
from loteam.models import Consumption
errorfile=open('errorfilemb51.txt','a')

list=[
    'Dashboard_MB51_1-300',
    'Dashboard_MB51_301-600',
    'Dashboard_MB51_601-900',
    'Dashboard_MB51_901-',
]

list=['MB51test.txt']

for i in list :
    print(i)
    total=MB51Parser(i)
    for v in total:     
        try :
            Consumption.objects.create(
                Pn=v[0],
                Date=v[1],
                Qty=v[2]
            )
        except Exception as ex :
            errorfile.write(ex,v)
            print(ex, v)
            continue
"""

import pandas as pd
import numpy as np
import datetime
import time

filename="TESTMB51.txt"
#filename="Clearing_DGSL_MB51_180615"

def MB51Parser(filename) :
    total=[]
    partnum=None
    errorfile=open(filename + "error.txt","a")
    with open(filename,"r", encoding="ISO-8859-1") as file:
        for i in range(3) : #skip the header
            line=file.readline()

        for line in file:


            flag=line[70:].count(" ")
            if(line.count("|")==2) : # start part
                splitLine = line.replace("|","").split()
                if flag==65 : #partnum line
                    if partnum!=None :
                        partnum=splitLine[0]

                    partnum=splitLine[0]
                    print("Partno : ",partnum)
                else : #if document line
                    try :
                        y = int(line[line.find("/")-4:line.find("/")])
                        m = int(line[line.find("/")+1:line.find("/")+3])
                        d = int(line[line.find("/")+4:line.find("/")+6])

                        qty=splitLine[splitLine.index('PC')-1]
                        if(qty.find("-")>0) :
                            qty=-int(float(qty.replace("-","").replace(",","")))
                        else :
                            qty=int(float(qty))

                        item =[partnum, datetime.date(y,m,d),-qty]
                        total.append(item)

                    except :
                        error=filename + line + "\n"
                        print(error)
                        errorfile.write(error)
                        continue
    file.close()
    return total
