from django.db import models
import datetime

class Property(models.Model):
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.TextField(default='tvm')
    features = models.TextField(default='superb')
    flats_1bhk = models.PositiveIntegerField(default=0)
    flats_2bhk = models.PositiveIntegerField(default=0)
    flats_3bhk = models.PositiveIntegerField(default=0)
    flats_4bhk = models.PositiveIntegerField(default=0)
    cost_1bhk = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    cost_2bhk = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    cost_3bhk = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    cost_4bhk = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

    def get_cost_for_flat_type(self, flat_type):
        """
        Returns the cost for the given flat type.
        """
        return getattr(self, f'cost_{flat_type.lower()}', 0.0)

    def allocate_flat(self, flat_type):
        """
        Decrease the count of flats of the specified type.
        Make sure to check availability before calling this method.
        """
        flat_count_attr = f'flats_{flat_type.lower()}'
        if hasattr(self, flat_count_attr):
            current_count = getattr(self, flat_count_attr)
            if current_count > 0:
                setattr(self, flat_count_attr, current_count - 1)
                self.save()
                return True  # Successfully allocated
        return False  # Allocation failed due to unavailability

class UnitType(models.TextChoices):
    ONE_BHK = '1BHK', '1BHK'
    TWO_BHK = '2BHK', '2BHK'
    THREE_BHK = '3BHK', '3BHK'
    FOUR_BHK = '4BHK', '4BHK'

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    property = models.ForeignKey('Property', on_delete=models.SET_NULL, null=True, blank=True)
    unit_type = models.CharField(max_length=5, choices=UnitType.choices, default=UnitType.ONE_BHK)
    agreement_end_date = models.DateField(default=datetime.date.today)
    monthly_rent_date = models.DateField(default=datetime.date.today)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.name} - {self.property.name if self.property else 'No Property'} - {self.unit_type}"

    def save(self, *args, **kwargs):
        if self.property and self.unit_type:
            self.rent_cost = self.property.get_cost_for_flat_type(self.unit_type)
        super(Tenant, self).save(*args, **kwargs)
    #document = models.FileField(upload_to='tenant_documents/', null=True, blank=True)  # Updated upload path

   

