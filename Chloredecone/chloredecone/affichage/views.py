#importation
import csv
import encodings
import imp
from pickle import NONE
from tkinter import Variable
import pandas as pd
from mmap import PAGESIZE
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.core.files import File
import codecs
from pathlib import Path
import datetime
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# importation local
from affichage.fonction.ApiExport import tabl
from affichage.fonction.graph import nouveau,pie
from affichage.fonction.carte import mapmaxmin,surfandsouter,littoraux
from affichage.fonction.create_pdf import make_pdf
from affichage.models import Band,Titre,releve_Ville,summary_pdf
from affichage.forms import ContactUsForm,RechercheForm


#page d'acceuil
def hello(request):
    #ajout des difféérentes année(obselète) 
    date  = [1990+i for i in range(32)] 
    liste=[]
    
    # Ajout des différentes villes
    ville=['Basse-Pointe (97203)', 'Saint-Pierre (97225)', 'Prêcheur (97219)', 'Morne-Rouge (97218)', 'Marigot (97216)', 'Lorrain (97214)', 'Carbet (97204)', 'Fort-de-France (97209)', 'Bellefontaine (97234)', 'Saint-Joseph (97224)', 'Gros-Morne (97212)', 'Robert (97222)', 'Trinité (97230)', 'Case-Pilote (97205)', 'Schœlcher (97229)', 'Lamentin (97213)', 'Ducos (97207)', 'François (97210)', 'Trois-Îlets (97231)', "Anses-d'Arlet (97202)", 'Rivière-Pilote (97220)', 'Vauclin (97232)', 'Diamant (97206)', 'Sainte-Luce (97227)', 'Sainte-Anne (97226)', 'Marin (97217)']
    return render(request,'affichage/hello.html',{"ville":ville,'date':date,"sum":list(liste)}
    )
#page de recherche
def search(request):
    #détection de la meethode
    if request.method == 'POST':
        #Récupération et traitement des données du POST
        recherche= request.POST['recherche_page']
        date_debut=request.POST['date_deb']
        date_fin=request.POST['date_fin']
        #(gestion a amélioré)
        insee=[recherche[i] for i in range(len(recherche)) if recherche[i] in ["0","1","2","3","4","5","6","7","8","9"]]
        insee_code=""
        for chiffre in insee:
            insee_code += chiffre
        print(insee_code)
        try:
            ss_terr=request.POST['sous_terrain']
        except:
            ss_terr=0
        try:
            eau_surface=request.POST['eau_surface']
        except:
            eau_surface=0
        try:
            surface_terr=request.POST['surface_terr']
        except:
            surface_terr=0
            
        

        
        #importation des différent code de relevé d'eau (obselète)
        """
        
        ville=releve_Ville.objects.all()

        print(date_debut,'--',date_fin,"<---------------------",ss_terr,surface_terr,eau_surface)
        code = ville[0].data['Commune'][recherche.strip()]['code']
        JSON=None
        for elm in code:
            JSON[elm]=jsonAffiche(elm)
        
            print(type(JSON[elm]),'<-----------------------------------')
        """
        #création du pdf 
        # pdf=summary_pdf()                       #Création d'un objet pdf qui sera mit en base de donné
        # titre=str(datetime.datetime.today().date())   # création du titre du PDF                           
        # pdf.titre=titre                           
        #                                           # création du pdf en lui meme en fonction de la ville souhaité
        
         
        # pdf.save()                           # puis on le met en base de donné
        id_pdf=33                          # très important on récupère son id
        #Instanciation des 3 tableaux de données
        T1=None
        T2=None
        T3=None
        
        # séléction des type de recherche 
        if ss_terr or surface_terr or eau_surface:
            choix=0
            if ss_terr:
                T1=tabl(3, str(date_debut) , str(date_fin) ,code_insee= insee_code) #création des tableaux
            if surface_terr:
                T2=tabl(2, str(date_debut) , str(date_fin) )
            if eau_surface:
                T3=tabl(1, str(date_debut) , str(date_fin) , code_insee= insee_code)
            notre_json=releve_Ville()                       #création de l'objet JSON
            notre_json.data={"tab1":T1,"tab2":T2,"tab3":T3} # Incorporation des 3 tableau dans l'objet
            notre_json.nom='votrejson'   
            notre_json.save()                               #enregistrement en base de donné (sans cela impossible d'nvoyer les donnés a la contruction du csv)
            id = notre_json.id                              #récupération de l'id du JSON
                                        #débug
            return render(request,'affichage/search.html',{"data":recherche,
                                                       'ville':NONE,'JSON':NONE,
                                                       "id":id,"id_pdf":id_pdf,"tab1":T1['data'],"tab2":T2['data'],"tab3":T3['data']})
    
    return render(request,'affichage/hello.html')
#==========================================(debug)=========================================
def maping(request):
    return render(request,'affichage/map.html')
#==========================================(debug)=========================================
def graph(request):
    chart=nouveau()
    camenbert=pie()
    return render(request,'affichage/graph.html',{'graph':chart,'pie':camenbert})

def about(request):
    titre=Titre.objects.all()
    return render(request,'affichage/about-us.html',{'titre':titre})
#==========================================(debug)=========================================
def presentation(request):
    
    map={'m1':mapmaxmin,'m2':surfandsouter,'m3':littoraux}
    return render(request,'affichage/amap.html',map)
#==========================================(debug)=========================================
def Tableau(request,id):
    importation=releve_Ville.objects.get(id=id)
    listjson=importation.data["tab3"]['data']
    # print(listjson)
    dfjson=pd.DataFrame(listjson)
    # print(dfjson)
    # print((dfjson['libelle_parametre'].value_counts()).keys())
    libelle_parametre=[i for i in (dfjson['libelle_parametre'].value_counts()).keys()]
    # libelle_parametre=[i for i in (dfjson['libelle_parametre'].value_counts()).values()]
    print(len(libelle_parametre))
    nombre=[i for i in range(len(libelle_parametre))]
   
            


    
    return render(request, 'affichage/tableau.html',{"n":nombre,"l":libelle_parametre})
#==========================================(debug)=========================================
def new_base(req):
    return render(req,'affichage/new_base.html')
 #========================(gestion du téléchargement pdf)==========================
def upload_file(request, id,id_json):
    pdf=summary_pdf.objects.get(id=id) 
    json=releve_Ville.objects.get(id=id_json)                     #Création d'un objet pdf qui sera mit en base de donné
    print(json.data['tab1'])
    titre=str(datetime.datetime.today().date())   # création du titre du PDF                           
    pdf.titre=titre                           
    make_pdf(titre,recherche)               # création du pdf en lui meme en fonction de la ville souhaité
        
    check="ville/tmp/"+titre+".pdf"          #Définition d'un chemin relatif 
    print(check,"<---------------------")    #Debug
    path = Path(str(check))                 #Formatage du format du chemin
        
    with path.open(mode='rb') as f:          # on ouvre le  pdf depuis le dossier temporaire
        pdf.file = File(f, name=path.name)   #on enregistre le pdf dans dans l'objet pdf
        pdf.save()           
     # récupération du bon pdf grace a l'ID prit dans le lien(faire un hash de l'id pour éviter toute modification de l'url)
    fl_path = project.file.path             #récupération du chemin du fichier 
    print(fl_path,"---------------")         # degug
    filename = project.file.name            # récupération du nom du fichier
    with open(fl_path, 'rb') as pdf:        #ouverture du fichier
                response = HttpResponse(pdf.read(), content_type='application/pdf') #création de la réponse en selectionant le mime type de fichier a retourné       
                response['Content-Disposition'] = 'attachment ; filename=%s' % filename        
                return response
    #=================(utilisation du module fpdf ,obselète )=======================
    #data=releve_Ville.objects.get(id=id)
    # buf=io.BytesIO()
    # c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    # textob=c.beginText()
    # textob.setTextOrigin(inch, inch)
    # textob.setFont("Helvetica",14)
    # lines=[
    #     str(data.data),

    #     "ligne 1",
    #     "ligne2"
    # ]
    # for line in lines:
    #     textob.textLine(line)
    # c.drawText(textob)
    # c.showPage()
    # c.save()
    # buf.seek(0)
    # return FileResponse(buf, as_attachment=True,filename="test.pdf")  
    

    #=====================(obselète)==================================================================
    # project =summary_pdf.objects.get(id=id)
    # fl_path = project.file.path
    # print(fl_path,"---------------")
    # filename = project.file.name
    # fl = codecs.open(fl_path, 'r', encoding='ISO-8859-1')
    # mime_type = "application/zip"
    # response = HttpResponse(fl, content_type=mime_type)
    # response['Content-Disposition'] = "attachment; filename=%s" % filename
    # return response

    #=========(tentative de gestion du téléchargement par une method POST pour récupéré les donnés de la page précédente)===========
    # """if request.method == "POST":
    #     form = summary_pdf(request.POST,request.FILES)
    #     if form.is_valid():
    #         return redirect(hello)
    # else : form = summary_pdf()
    # return render(request, "affichage/upload.html",{"form":form})"""


#==================(télécgargement csv)==========================
def upload_csv3(request,id):
    importer=releve_Ville.objects.get(id=id)  #récupération du JSON par son id
    print(type(importer))       #debug
    print(type(importer.data))  #debug
    if importer.data["tab3"]['data']:   
        response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="tableu3.csv"'})# on défini le type et le nom du fichier a retourner
        df=pd.DataFrame(importer.data["tab3"]['data'])                                #on tranforme le JSON en DataFrame
        writer = csv.writer(response)                                        
        for i in df.itertuples():                                              #POur chaque ligne du JSON en l'implémente dans le dataframe puis on envoie la responce
            writer.writerow(i)
            
    return response


#==================(télécgargement csv)==========================
def upload_csv1(request,id):
    importer=releve_Ville.objects.get(id=id)
   
    
    print(type(importer)) 
    print(type(importer.data))
    if importer.data["tab1"]['data']:
        response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="tablau1.csv"'})
        df=pd.DataFrame(importer.data["tab1"]['data'])
        writer = csv.writer(response)
        for i in df.itertuples():
            writer.writerow(i)
    return response

 #==================(télécgargement csv)==========================
def upload_csv2(request,id):
    importer=releve_Ville.objects.get(id=id)
    # Create the HttpResponse object with the appropriate CSV header.
    
    print(type(importer))
    print(type(importer.data))
    if importer.data["tab2"]['data']:
        response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="tableau2.csv"'})
        df=pd.DataFrame(importer.data["tab2"]['data'])
        writer = csv.writer(response)
        for i in df.itertuples():
            writer.writerow(i)
    return response
