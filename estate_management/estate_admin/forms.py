
from django import forms
from .models import Tenant, Property



class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'location', 'features', 'flats_1bhk', 'flats_2bhk', 'flats_3bhk', 'flats_4bhk']

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'address']
