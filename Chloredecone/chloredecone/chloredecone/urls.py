"""chloredecone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
#from Chloredecone.chloredecone.affichage.views import search
from affichage import views

urlpatterns = [
    path('',views.hello,name='index'),
    path('admin/', admin.site.urls),
    path('hello/',views.hello),
    path('tab/',views.Tableau,name='tableau'),
    path('new_base',views.new_base),
    path('upload/',views.upload_file),
    path('upload/<int:id>/',views.upload_file),
    path('search/',views.search,name='recherche'),
    path('map/',views.maping,name='map'),
    path('g/',views.graph,name='graph'),
    path('presentation/',views.presentation,name='presentation'),
    path('about-us/',views.about),
    path('contact-us/',views.contact_us,name='contact'),
    path('listing',views.listing),
    path('bands_list/',views.bands_list,name='band-list'),
    path('bands_list/<int:id>/',views.bands_list_detail,name='bands_list_d'),
]
