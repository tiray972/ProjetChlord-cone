
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from affichage.models import Band,Titre,releve_Ville
from affichage.forms import ContactUsForm,RechercheForm



def hello(request):
    ville=['Basse-Pointe (97203)', 'Saint-Pierre (97225)', 'Prêcheur (97219)', 'Morne-Rouge (97218)', 'Marigot (97216)', 'Lorrain (97214)', 'Carbet (97204)', 'Fort-de-France (97209)', 'Bellefontaine (97234)', 'Saint-Joseph (97224)', 'Gros-Morne (97212)', 'Robert (97222)', 'Trinité (97230)', 'Case-Pilote (97205)', 'Schœlcher (97229)', 'Lamentin (97213)', 'Ducos (97207)', 'François (97210)', 'Trois-Îlets (97231)', "Anses-d'Arlet (97202)", 'Rivière-Pilote (97220)', 'Vauclin (97232)', 'Diamant (97206)', 'Sainte-Luce (97227)', 'Sainte-Anne (97226)', 'Marin (97217)']
    return render(request,'affichage/hello.html',{"ville":ville}
    )

def search(request):
    
    if request.method == 'POST':
        print(request.POST['recherche_page'],"<---------------")
        recherche= request.POST['recherche_page']

        ville=releve_Ville.objects.all()
        
        print(recherche,"<---------------------")
        code = ville[0].data['Commune'][recherche.strip()]['code']

        return render(request,'affichage/search.html',{"data":recherche,'ville':code})
    
    return render(request,'affichage/hello.html')


def about(request):
    titre=Titre.objects.all()
    return render(request,'affichage/about-us.html',{'titre':titre})


def contact_us(request):
    form = ContactUsForm()
    print('La méthode de requete est: ', request.method)
    print('Les données POST sont: ',request.POST)
    if request.method == "POST":
        form = ContactUsForm(request.POST)
    else:
        form= ContactUsForm()
    return render(request,'affichage/contact-us.html',{'form':form})





def listing(request):
    return HttpResponse("<p>la liste<p>")





def bands_list(request):
    bands=Band.objects.all()
    titre=Titre.objects.all()
    return render(request,"affichage/bands_list.html",{'titre':titre,'bands':bands})






def bands_list_detail(request,id):
    band = Band.objects.get(id=id)
    return render(request,'affichage/bands_list_detail.html',{'band':band})


    
