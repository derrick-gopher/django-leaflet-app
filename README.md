# A simple Django Leaflet project Demo

## Description

### This app illustrates usage of django-leaflet plugin to create a app that uses location.

## Installation Instructions

+ Clone the project.
+ Run ```pip3 install requirements.txt```
+ install postgres and postgis package to add spatial capability to postgres.
+ Intall both follow this [tutorial](https://www.gis-blog.com/how-to-install-postgis-2-3-on-ubuntu-16-04-lts/).
+ If postgresql is already installed, run ```sudo apt-get update && sudo apt-get install postgis ```
+ Create a database eg *gisdb* in the *psql shell* ```psql -d gisdb ```
+ Then execute ```gisdb=#CREATE EXTENSION postgis; ``` and also followed by ```gisdb=#CREATE EXTENSION postgis_topology; ```
#####  With this all is set.
+ Execute ```python manage.py makemigrations``` followed by ```python manage.py migrate ```
+ Run serve by ```python manage.py runserver```

** NB ENSURE DATABASE YOU CREATE MATCHES WITH DATABASE NAME IN settings.py FILE **

