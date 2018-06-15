from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lawyer_form', views.lawyer_form, name='lawyer_form'),
    url(r'^portal', views.portal, name='portal'),
    url(r'^data$', views.reported, name='lawyers'),
    url(r'^about$', views.about, name='about'),
]