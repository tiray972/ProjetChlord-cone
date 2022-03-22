from django.shortcuts import render
from django.http import HttpResponse
from affichage.models import Band,Titre


def hello(request):
    bands=Band.objects.all()
    
    return render(request,'affichage/hello.html',{'bands':bands}
    )
def about(request):
    titre=Titre.objects.all()
    return render(request,'affichage/about-us.html',{'titre':titre})
def contact_us(request):
    return render(request,'affichage/contact-us.html')
def listing(request):
    return HttpResponse("<p>la liste<p>")
