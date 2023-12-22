from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PropertyForm , TenantForm
from .models import Property, Tenant, UnitType

from django.contrib.auth.decorators import login_required

@login_required
def list_properties(request):
    properties = Property.objects.all()
    return render(request, 'estate_admin/list_properties.html', {'properties': properties})



#----------------------------property addition /updatation-----------------
@login_required
def add_or_update_property(request, property_id=None):
    if property_id:
        property_obj = get_object_or_404(Property, pk=property_id)
        form = PropertyForm(request.POST or None, instance=property_obj)
    else:
        form = PropertyForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list_properties')  # Redirect to the property listing page
    
    context = {
        'form': form,
        'property': property_obj if property_id else None
    }
    return render(request, 'estate_admin/add_or_edit_property.html', context)


@login_required
def delete_property(request , property_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':

        property_obj.delete()
        return redirect('list_properties')
    context = {'property': property_obj}
    return render(request, 'estate_admin/confirm_delete_property.html', context)

#-------------------------------------------------------------------------------tenants view--------------------------

@login_required
def list_tenants(request):
    tenants = Tenant.objects.all()
    tenants_by_unit_type = {}
    for unit_type in UnitType:
        tenants_by_unit_type[unit_type.label] = Tenant.objects.filter(unit_type=unit_type.value)
    context = {
        'tenants': tenants,
    }
    return render(request, 'estate_admin/list_tenants.html', context)
    



#--tenants addition /updatation


def add_or_update_tenant(request, tenant_id=None):
    if tenant_id:
        tenant = get_object_or_404(Tenant, pk=tenant_id)
        form = TenantForm(request.POST or None, instance=tenant)
    else:
        tenant = None
        form = TenantForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list_tenants')  # Redirect to the tenant listing page

    return render(request, 'estate_admin/add_or_edit_tenant.html', {
        'form': form,
        'tenant': tenant
    })


@login_required
def delete_tenant(request , tenant_id):
    tenant_obj = get_object_or_404(Tenant, pk=tenant_id)
    if request.method == 'POST':

        tenant_obj.delete()
        return redirect('list_tenants')
    context = {'tenant': tenant_obj}
    return render(request, 'estate_admin/confirm_delete_tenant.html', context)



def home(request):
    return render(request, 'estate_admin/index.html')

def login_view(request):  # Renamed to avoid conflict with 'login' from django.contrib.auth
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login here
            return redirect('home')  # Redirect to admin dashboard or a different page as required
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'estate_admin/index.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def property_tenants(request, property_id):
    # Get the property object
    property_obj = get_object_or_404(Property, pk=property_id)

    # Get tenants for this property
    tenants = Tenant.objects.filter(property=property_obj)

    context = {
        'property': property_obj,
        'tenants': tenants,
    }
    return render(request, 'estate_admin/property_tenants.html', context)
