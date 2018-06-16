from django.db import models
from django.contrib.gis.db import models
import datetime
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import TextInput
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Lawyer(models.Model):
    '''
    creating a profile model for each citizen
    '''
    categories = (
        ('civil','civil'),
        ('criminal', 'criminal')
        
    )
    avatar = models.ImageField(upload_to='lawyer_avatar/', blank=True)
    bio = models.TextField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='lawyer_profile')
    phone = PhoneNumberField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    category =models.CharField(max_length=200, default="criminal")
    location = models.PointField(srid=4326)
    objects=models.GeoManager()

    def __str__(self):
        return f"Lawyer {self.first_name} - {self.last_name}"

    class Meta:
        verbose_name_plural = "All Lawyers"

class AllLawyer(models.Model):
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    geom = models.PointField(srid=4326)
    objects=models.GeoManager()


# class Report(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     phone = PhoneNumberField(null=True, blank=True)
#     date = models.DateTimeField(auto_now_add=True)
#     description = models.TextField()
#     photo = models.FileField(upload_to='uploads', null=True, blank=True)
#     geom = models.PointField(srid=4326)
#     objects=models.GeoManager()

#     def __str__(self):
#         return f"Report {self.first_name} {self.description}"

#     class Meta:
#         verbose_name_plural = "All Cases"


        