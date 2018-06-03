from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.core.serializers import serialize
from .models import Report
from .forms import ReportForm,IncidenceForm
from django.contrib.gis.geos import Point


def index(request):
    return render(request, 'index.html')
    
def portal(request):
    return render(request, 'portal.html')
def about(request):
    return render(request, 'about.html')

def incidences(request):
    if request.method == 'POST':
        form = IncidenceForm(request.POST)
        if form.is_valid():
            new_point = Report()
            cd = form.cleaned_data
            new_point.first_name = cd['first_name']
            new_point.last_name = cd['last_name']
            new_point.phone = cd['phone']
            new_point.description = cd['description']
            coordinates = cd['coordinates'].split(',')
            new_point.geom = Point(float(coordinates[0]), float(coordinates[1]))
            new_point.save()

            return redirect('index')
    else:
        form = IncidenceForm()
    return render(request, 'reporter/incidence-form.html', {'form': form})

def reported(request):
    reports = serialize('geojson', Report.objects.all())
    return HttpResponse(reports, content_type='json')