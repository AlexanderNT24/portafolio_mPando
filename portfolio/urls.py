from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import settings

from portfolio_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('biography/', views.biography,name='biography'),
    #traigo todo el contenido de blog_app/url
    path('blog/', include('blog_app.urls')),
    path('exhibition/', include('portfolio_app.urls'))
]

handler404 = views.error_404
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

