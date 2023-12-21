from django.db import models
import datetime

class Property(models.Model):
    #image = models.ImageField(default='default.jpg' , upload_to='profile_pics')
    name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.TextField(default ='tvm')
    features = models.TextField(default ='superb')
    flats_1bhk = models.PositiveIntegerField(default=0)
    flats_2bhk = models.PositiveIntegerField(default=0)
    flats_3bhk = models.PositiveIntegerField(default=0)
    flats_4bhk = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def allocate_flat(self, flat_type):
        """
        Decrease the count of flats of the specified type.
        Make sure to check availability before calling this method.
        """
        if flat_type == '1BHK' and self.flats_1bhk > 0:
            self.flats_1bhk -= 1
        elif flat_type == '2BHK' and self.flats_2bhk > 0:
            self.flats_2bhk -= 1
        elif flat_type == '3BHK' and self.flats_3bhk > 0:
            self.flats_3bhk -= 1
        elif flat_type == '4BHK' and self.flats_4bhk > 0:
            self.flats_4bhk -= 1
        self.save()

class UnitType(models.TextChoices):
    ONE_BHK = '1BHK', '1BHK'
    TWO_BHK = '2BHK', '2BHK'
    THREE_BHK = '3BHK', '3BHK'
    FOUR_BHK = '4BHK', '4BHK'

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)
    unit_type = models.CharField(max_length=5, choices=UnitType.choices, default=UnitType.ONE_BHK)
    agreement_end_date = models.DateField(default=datetime.date.today)  # Corrected spelling
    monthly_rent_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"{self.name} - {self.property.name if self.property else 'No Property'} - {self.unit_type}"

    def save(self, *args, **kwargs):
        if self.pk is None and self.property:  # Check if this is a new agreement and property is set
            self.property.allocate_flat(self.unit_type)
        super().save(*args, **kwargs)
    #document = models.FileField(upload_to='tenant_documents/', null=True, blank=True)  # Updated upload path

   

