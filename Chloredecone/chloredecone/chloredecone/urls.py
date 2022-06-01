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
#création de toute les url de l'application
urlpatterns = [
    path('',views.hello,name='index'),
    path('admin/', admin.site.urls),
    path('hello/',views.hello),
    path('tab/<int:id>/',views.Tableau,name='tableau'),
    path('new_base',views.new_base),
    path('upload/',views.upload_file),
    path('upload/<int:id>/<int:id_json>/',views.upload_file),       #le <int:id> fait référence au type et au champ dans la base de donnée
    path('upload_csv1/<int:id>/',views.upload_csv1),  # grace au url on récupère l'id d'une page a une autre
    path('upload_csv2/<int:id>/',views.upload_csv2),  # maintenant tout le monde peut modifier l'url depuis le navigateur et mettre l'id de son choix
    path('upload_csv3/<int:id>/',views.upload_csv3), #une solution est de hasher l'id
    path('search/',views.search,name='recherche'),
    path('map/',views.maping,name='map'),
    path('g/',views.graph,name='graph'),
    path('presentation/',views.presentation,name='presentation'),
    path('about-us/',views.about),
    
]
