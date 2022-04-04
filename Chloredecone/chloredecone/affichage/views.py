
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from affichage.models import Band,Titre
from affichage.forms import ContactUsForm,RechercheForm



def hello(request):

    return render(request,'affichage/hello.html',{}
    )

def search(request):
    if request.method == 'POST':
        print(request.POST['recherche_page'],"<---------------")
        data= request.POST['recherche_page']
        return render(request,'affichage/search.html',{"data":data})
    
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


    
