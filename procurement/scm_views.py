from django.shortcuts import render
from .models import Assay

# Create your views here.
As=Assay.objects.all()
def main(request) :
    print("==========================main called")

    As=Assay.objects.all()

    if request.method=='GET':
        print("request.method = GET")
        try :
            SA_No=request.GET['SA_No'].strip()
            Ass=Assay.objects.get(SA_No=SA_No)

        except Exception as e:
            return render(
                request, 'procurement/view.html',{
                'assayList' : As
                })


        return render(
            request, 'procurement/view.html',{
                'Assay' : Ass,
                'assayList' : As
        })


def assayQuery(request) :
    if request.method=='GET':
        print("request.method = GET ///assay Query")
        SA_No=request.GET['SA_No'].strip()
        Ass=Assay.objects.get(SA_No=SA_No)
        print(SA_No)

    return render(
        request, 'procurement/view_tab1.html',{
            'Assay' : Ass,
            'assayList' : As
    })
