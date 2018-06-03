from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^incidences', views.incidences, name='incidences'),
    url(r'^portal', views.portal, name='portal'),
    url(r'^data$', views.reported, name='reported'),
    url(r'^about$', views.about, name='about'),
]