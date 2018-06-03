from django import forms
from django.forms import ModelForm
from .models import Report
from leaflet.forms.widgets import LeafletWidget
from leaflet.forms.fields import PointField

class ReportForm(forms.ModelForm):
    geom = PointField()

    class Meta:
        model =Report
        fields = '__all__'

class IncidenceForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50, required=True)
    description = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    coordinates=forms.CharField(max_length=200, required=True)