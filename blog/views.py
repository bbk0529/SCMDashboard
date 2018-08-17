from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/index.html',{})
    #return render(request, 'blog/post_list.html',{})