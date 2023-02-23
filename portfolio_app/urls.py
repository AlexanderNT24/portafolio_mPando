from django.urls import path
#importamos la vista
from .views import exhibition_detail

app_name='exhibition'

#cuando /posts/ es la ruta inicial
urlpatterns = [
    path('<int:exhibition_id>',exhibition_detail,name='exhibition_detail'),
]
