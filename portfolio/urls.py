from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings

from portfolio_app import views

urlpatterns = [
    path('admin/', views.administrator, name='administrator'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('biography/', views.biography, name='biography'),
    path('blog/', include('blog_app.urls')),
    path('exhibition/', include('portfolio_app.urls')),
    path('administrator_login/', views.administrator_login, name='administrator_login'),
    path('administrator/', views.administrator, name='administrator'),
    path('administrator_detail/<int:exhibition_id>', views.administrator_detail, name='administrator_detail'),
    path('administrator_create/', views.create_exhibition, name='administrator_create'),

    path('administrator_update/<int:exhibition_id>/', views.update_exhibition, name='administrator_update'),
    path('administrator_delete/<int:exhibition_id>/', views.delete_exhibition, name='administrator_delete'),

]


handler404 = views.error_404
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
