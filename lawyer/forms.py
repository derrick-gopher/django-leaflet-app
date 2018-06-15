from django import forms
from django.forms import ModelForm
from .models import Lawyer
from leaflet.forms.widgets import LeafletWidget
from leaflet.forms.fields import PointField

class LawyerForm(forms.ModelForm):
    location = PointField()

    class Meta:
        model = Lawyer
        fields = '__all__'

class DataForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50, required=True)
    coordinates=forms.CharField(max_length=200, required=True)