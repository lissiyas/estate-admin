from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PropertyForm,TenantForm
from .models import Property, Tenant


def list_properties(request):
    properties = Property.objects.all()
    return render(request, 'estate_admin/list_properties.html', {'properties': properties})



def list_tenants(request):
    tenants = Tenant.objects.all()
    return render(request, 'estate_admin/list_tenants.html', {'tenants': tenants})

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_properties')  # redirect to the property listing page
    else:
        form = PropertyForm()
    return render(request, 'estate_admin/add_property.html', {'form': form})

def add_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tenants')  # redirect to the tenant listing page
    else:
        form = TenantForm()
    return render(request, 'estate_admin/add_tenant.html', {'form': form})






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
