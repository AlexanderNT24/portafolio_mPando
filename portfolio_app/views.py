from django.shortcuts import render,get_object_or_404
from .models import Exhibition,Biography_Content

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
    biography_contents = Biography_Content.objects.all().order_by('biography__title')
    
    grouped_contents = {}
    
    for content in biography_contents:
        title = content.biography.title
        if title not in grouped_contents:
            grouped_contents[title] = {'title': title, 'contents': []}
        grouped_contents[title]['contents'].append(content)

    context = {'grouped_biography_contents': grouped_contents.values()}
    return render(request, 'biography.html', context)


def error_404(request, exception):
    return render(request, '404.html', {})
