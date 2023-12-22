from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),  # Updated to 'login_view'
    path('properties/', views.list_properties, name='list_properties'),
    path('add-properties/', views.add_or_update_property, name='add_property'),
    path('property/update/<int:property_id>/', views.add_or_update_property, name='update_property'),
    path('tenant/add/', views.add_or_update_tenant, name='add_tenant'),
    path('tenant/update/<int:tenant_id>/', views.add_or_update_tenant, name='update_tenant'),
    path('list-tenant/', views.list_tenants, name='list_tenants'),
    path('logout/', views.logout_view, name='logout'),
    path('properties/<int:property_id>/tenants/', views.property_tenants, name='property-tenants'),
    path('properties/<int:property_id>/delete/', views.delete_property, name='delete_property'),
    path('tenants/<int:tenant_id>/delete/', views.delete_tenant, name='delete_tenant'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)