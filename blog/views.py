from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from tablib import Dataset
from django.http import HttpResponse
from .resources import YmonResource
from .resources import PersonResource
from django.db.models import Avg, Count, Min, Sum, Max
from .models import Ymon

def index(request):
    
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    YmonSum=Ymon.objects.all().aggregate(Sum('Open_quantity'))['Open_quantity__sum']
    YmonAvg=Ymon.objects.all().aggregate(Avg('Open_quantity'))['Open_quantity__avg']
    YmonMax=Ymon.objects.all().aggregate(Max('Open_quantity'))['Open_quantity__max']
    YmonCount=Ymon.objects.all().aggregate(Count('Open_quantity'))['Open_quantity__count']
    
    print("YMON SUM",  YmonSum, YmonAvg, YmonMax, YmonCount)
    
    return render(
        request, 'blog/index.html',{
            'YmonSum':YmonSum, 
            'YmonAvg' : YmonAvg,
            'YmonMax' : YmonMax,
            'YmonCount' : YmonCount
    })
    
 
def ui_buttons(request):
    return render(request, 'blog/ui-buttons.html',{'test' : 10293845})
    
@csrf_protect
def test(request):
    print("test, json called")
    #posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = list(Post.objects.all())
    #entry_list = list(Entry.objects.all())
    #return  JsonResponse({'foo': 'bar'})
    # data = {
        # 'name': 'Vitor',
        # 'location': 'Finland',
        # 'is_active': True,
        # 'count': 28
    # }
    #return JsonResponse(data)
    data = list(Post.objects.values())
    for i in  Post.objects.values(): print(i['title'])
    return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})
    
    

def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="persons.json"'
    return response
    
    
def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'blog/simple_upload.html')