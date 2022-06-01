
from affichage.models import Band,Titre,releve_Ville,summary_pdf
from django.contrib import admin



class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste
class TitreAdmin(admin.ModelAdmin):  
    list_display = ('titre', 'year_created','band') 
class releve_Ville_admin(admin.ModelAdmin):
    list_display = ("data","nom")
class pdf_admin(admin.ModelAdmin):
    list_display=("titre","file","ville")


admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Titre,TitreAdmin)
admin.site.register(releve_Ville,releve_Ville_admin)
admin.site.register(summary_pdf,pdf_admin)