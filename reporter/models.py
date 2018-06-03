from django.db import models
from django.contrib.gis.db import models
import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import TextInput

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = PhoneNumberField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    photo = models.FileField(upload_to='uploads', null=True, blank=True)
    geom = models.PointField(srid=4326)
    objects=models.GeoManager()

    def __str__(self):
        return f"Report {self.first_name} {self.description}"

    class Meta:
        verbose_name_plural = "All Cases"