
from django import forms
from .models import Tenant, Property
import datetime



class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'location', 'features', 'flats_1bhk', 'flats_2bhk', 'flats_3bhk', 'flats_4bhk','cost_1bhk'
                  ,'cost_2bhk','cost_3bhk','cost_4bhk']


class TenantForm(forms.ModelForm):
    agreement_end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), 
        initial=datetime.date.today
    )
    monthly_rent_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), 
        initial=datetime.date.today
    )

    class Meta:
        model = Tenant
        fields = ['name', 'address', 'property', 'unit_type', 'agreement_end_date', 'monthly_rent_date' ,'document']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'property': forms.Select(attrs={'class': 'form-control'}),
            'unit_type': forms.Select(attrs={'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class': 'form-control'}),

            
        }

#class SearchForm(forms.Form):
#    unit_type = forms.CharField(required=False)
#    property_name = forms.CharField(required=False)