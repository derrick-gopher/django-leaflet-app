from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.core.serializers import serialize
from .models import Lawyer
from .forms import LawyerForm,DataForm
from django.contrib.gis.geos import Point


def index(request):
    return render(request, 'index.html')
    
def portal(request):
    return render(request, 'portal.html')
def about(request):
    return render(request, 'about.html')

def lawyer_form(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            new_lawyer = LawyerForm()
            cd = form.cleaned_data
            # print(cd)
            new_lawyer.first_name = cd['first_name']
            new_lawyer.last_name = cd['last_name']
            new_lawyer.phone = cd['phone']
            coordinates = cd['coordinates'].split(',')
            new_lawyer.location = Point(float(coordinates[0]), float(coordinates[1]))
            # print(new_lawyer)
            # new_lawyer.save()

            return redirect('index')
    else:
        form = DataForm()
    return render(request, 'lawyer/lawyer-form.html', {'form': form})

def reported(request):
    lawyers = serialize('geojson', Lawyer.objects.all())
    return HttpResponse(lawyers, content_type='json')