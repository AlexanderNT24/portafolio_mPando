from django.shortcuts import render,get_object_or_404
from .models import Post

def render_posts(request):
    posts = Post.objects.order_by('-start_date')
    return render(request, 'posts.html', {'posts': posts})


def post_detail(request,post_id):
    #Funcion de django para obtener un valor o retornar 404
    post=get_object_or_404(Post,pk=post_id)
    return render(request, 'post_detail.html',{'post':post})    