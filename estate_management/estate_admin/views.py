from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PropertyForm , TenantForm , SearchForm
from .models import Property, Tenant
from django.db.models import Q

from django.contrib.auth.decorators import login_required

@login_required
def list_properties(request):
    properties = Property.objects.all()
    return render(request, 'estate_admin/list_properties.html', {'properties': properties})



#----------------------------property addition /updatation-----------------
@login_required
def add_or_update_property(request, property_id=None):
    is_update = property_id is not None
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
        'property': property_obj if property_id else None,
        'is_update':is_update
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
    search_query = request.GET.get('search_query', '').strip()

    tenants = Tenant.objects.all()
    if search_query:
        # Check if the query matches unit types or property names
        tenants = tenants.filter(
            Q(unit_type__icontains=search_query) |
            Q(property__features__icontains=search_query)
        )

    context = {
        'tenants': tenants
    }
    return render(request, 'estate_admin/list_tenants.html', context)
    



#--tenants addition /updatation


def add_or_update_tenant(request, tenant_id=None):
    is_update = tenant_id is not None
    if tenant_id:
        tenant = get_object_or_404(Tenant, pk=tenant_id)
        form = TenantForm(request.POST or None, instance=tenant)
    else:
        tenant = None
        form = TenantForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list_tenants')  # Redirect to the tenant listing page
    
    context ={
        'form': form,
        'tenant': tenant,
        'is_update':is_update
    }


    return render(request, 'estate_admin/add_or_edit_tenant.html', context)


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

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Retrieve the username based on the email
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'estate_admin/index.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('list_properties')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'estate_admin/index.html')


def logout_view(request):
    logout(request)
    return redirect('login')


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
