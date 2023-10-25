from django.shortcuts import render,get_object_or_404,redirect
from .models import Exhibition
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import ExhibitionForm

def home(request):
    exhibitions = Exhibition.objects.filter(hidden=False).order_by('-date')
    context = {'exhibitions': exhibitions}
    return render(request, 'home.html', context)

def exhibition_detail(request,exhibition_id):
    exhibition = get_object_or_404(Exhibition, pk=exhibition_id)
    context = {'exhibition': exhibition}
    return render(request, 'exhibition_detail.html', context)    

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def biography(request):
    return render(request,'biography.html')

def error_404(request, exception):
    return render(request, '404.html', {})

def administrator_login(request):
    return render(request, './crud/login.html')

def administrator(request):
    exhibitions = Exhibition.objects.filter(hidden=False).order_by('-date')
    context = {'exhibitions': exhibitions}
    return render(request, './crud/administrator.html', context)

def administrator_detail(request,exhibition_id):
    exhibition = get_object_or_404(Exhibition, pk=exhibition_id)
    context = {'exhibition': exhibition}
    return render(request, './crud/administrator_detail.html', context)
  
def create_exhibition(request):
    if request.method == 'POST':
        form = ExhibitionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('exhibition_list')  # Redirige a la lista de exhibiciones
    else:
        form = ExhibitionForm()
    return render(request, 'create_exhibition.html', {'form': form})


def update_exhibition(request, exhibition_id):
    exhibition = get_object_or_404(Exhibition, pk=exhibition_id)
    
    if request.method == 'POST':
        form = ExhibitionForm(request.POST, request.FILES, instance=exhibition)
        if form.is_valid():
            form.save()
            return redirect('exhibition_list')  # Redirige a la lista de exhibiciones
    else:
        form = ExhibitionForm(instance=exhibition)
    
    return render(request, 'update_exhibition.html', {'form': form, 'exhibition': exhibition})

def delete_exhibition(request, exhibition_id):
    exhibition = get_object_or_404(Exhibition, pk=exhibition_id)
    
    if request.method == 'POST':
        exhibition.delete()
        return redirect('exhibition_list')  # Redirige a la lista de exhibiciones
    
    return render(request, 'delete_exhibition.html', {'exhibition': exhibition})
