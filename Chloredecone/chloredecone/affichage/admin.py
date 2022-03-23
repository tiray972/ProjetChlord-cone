
from affichage.models import Band,Titre
from django.contrib import admin



class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste
class TitreAdmin(admin.ModelAdmin):  
    list_display = ('titre', 'year_created','band') 


admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Titre,TitreAdmin)