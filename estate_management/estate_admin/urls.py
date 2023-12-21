from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),  # Updated to 'login_view'
    path('properties/', views.list_properties, name='list_properties'),
    path('add-properties/', views.add_property, name='add_property'),
     path('add-tenant/', views.add_tenant, name='add_tenant'),
     path('list-tenant/', views.list_tenants, name='list_tenants'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)