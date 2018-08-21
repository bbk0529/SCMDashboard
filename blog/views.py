from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect


   
def index(request):
    
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html',{'test' : "BKPARK"})
    #return render(request, 'blog/post_list.html',{'posts' : posts})
 
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
    
    
