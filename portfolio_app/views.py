from django.shortcuts import render,get_object_or_404
from .models import Exhibition

def home(request):
    exhibitions = Exhibition.objects.all()
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
