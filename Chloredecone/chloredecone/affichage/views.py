
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from affichage.models import Band,Titre,releve_Ville,summary_pdf
from affichage.forms import ContactUsForm,RechercheForm
import codecs
# importation local
from affichage.fonction.ApiExport import jsonAffiche
from affichage.fonction.carte import mapmaxmin,surfandsouter


def hello(request):
    date  = [1990+i for i in range(32)]
    ville=['Basse-Pointe (97203)', 'Saint-Pierre (97225)', 'Prêcheur (97219)', 'Morne-Rouge (97218)', 'Marigot (97216)', 'Lorrain (97214)', 'Carbet (97204)', 'Fort-de-France (97209)', 'Bellefontaine (97234)', 'Saint-Joseph (97224)', 'Gros-Morne (97212)', 'Robert (97222)', 'Trinité (97230)', 'Case-Pilote (97205)', 'Schœlcher (97229)', 'Lamentin (97213)', 'Ducos (97207)', 'François (97210)', 'Trois-Îlets (97231)', "Anses-d'Arlet (97202)", 'Rivière-Pilote (97220)', 'Vauclin (97232)', 'Diamant (97206)', 'Sainte-Luce (97227)', 'Sainte-Anne (97226)', 'Marin (97217)']
    return render(request,'affichage/hello.html',{"ville":ville,'date':date}
    )

def search(request):
    
    if request.method == 'POST':
        print(request.POST['recherche_page'],"<---------------")
        recherche= request.POST['recherche_page']
        date_debut=request.POST['recherche_page_date_debut']
        date_fin=request.POST['recherche_page_date_fin']
        try:
            ss_terr=request.POST['sous_terrain']
        except:
            ss_terr=0
            pass
        

        ville=releve_Ville.objects.all()
        
        print(date_debut,'--',date_fin,"<---------------------",ss_terr)
        code = ville[0].data['Commune'][recherche.strip()]['code']
        JSON={}
        for elm in code:
            JSON[elm]=jsonAffiche(elm)
            
            #print(type(JSON[elm]),'<-----------------------------------')
            
        return render(request,'affichage/search.html',{"data":recherche,'ville':code,'JSON':JSON})
    
    return render(request,'affichage/hello.html')

def maping(request):
    return render(request,'affichage/map.html')

def about(request):
    titre=Titre.objects.all()
    return render(request,'affichage/about-us.html',{'titre':titre})

def presentation(request):
    
    map={'m1':mapmaxmin,'m2':surfandsouter}
    return render(request,'affichage/amap.html',map)

def contact_us(request):
    form = ContactUsForm()
    print('La méthode de requete est: ', request.method)
    print('Les données POST sont: ',request.POST)
    if request.method == "POST":
        form = ContactUsForm(request.POST)
    else:
        form= ContactUsForm()
    return render(request,'affichage/contact-us.html',{'form':form})



def upload_file(request, id):
    project =summary_pdf.objects.get(titre="test")
    fl_path = project.file.path
    filename = project.file.name
    fl = codecs.open(fl_path, 'r', encoding='ISO-8859-1')
    mime_type = "application/zip"
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
    """if request.method == "POST":
        form = summary_pdf(request.POST,request.FILES)
        if form.is_valid():
            return redirect(hello)
    else : form = summary_pdf()
    return render(request, "affichage/upload.html",{"form":form})"""

def listing(request):
    return HttpResponse("<p>la liste<p>")





def bands_list(request):
    bands=Band.objects.all()
    titre=Titre.objects.all()
    return render(request,"affichage/bands_list.html",{'titre':titre,'bands':bands})






def bands_list_detail(request,id):
    band = Band.objects.get(id=id)
    return render(request,'affichage/bands_list_detail.html',{'band':band})


    
