#views_form
from .forms import NameForm
def get_name(request):    
    
    if request.method == 'POST':    
        form = NameForm(request.POST)            
    
        if form.is_valid():    
            return render(request,'nameshow.html', {
            'name' : form.cleaned_data['name'],
            'email' : form.cleaned_data['email']
            })
        
    else:            
        form = NameForm()
        
    return render(request, 'name.html', {'form': form})
