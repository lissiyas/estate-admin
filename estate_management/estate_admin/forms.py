
from django import forms
from .models import Tenant, Property



class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'address', 'location', 'features', 'flats_1bhk', 'flats_2bhk', 'flats_3bhk', 'flats_4bhk']

class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'address','property','unit_type','agreement_end_date','monthly_rent_date']

    def __init__(self, *args, **kwargs):
        super(TenantForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control' 
