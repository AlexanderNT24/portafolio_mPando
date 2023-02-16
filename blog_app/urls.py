from django.urls import path
#importamos la vista
from .views import render_posts,post_detail

app_name='blog'

#cuando /posts/ es la ruta inicial
urlpatterns = [
    path('', render_posts,name='posts'),
    path('<int:post_id>',post_detail,name='post_detail'),
]
