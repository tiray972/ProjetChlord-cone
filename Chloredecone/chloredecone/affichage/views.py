
import imp
from mmap import PAGESIZE
from django.shortcuts import render ,redirect
from django.http import HttpResponse
# from Chloredecone.chloredecone.affichage.fonction.graph import nouveau
from affichage.models import Band,Titre,releve_Ville,summary_pdf
from affichage.forms import ContactUsForm,RechercheForm
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
from affichage.fonction.ApiExport import jsonAffiche,tabl
from affichage.fonction.graph import nouveau,pie
from affichage.fonction.carte import mapmaxmin,surfandsouter,littoraux
from affichage.fonction.create_pdf import make_pdf
from affichage.fonction.util import try_radio


def hello(request):
    date  = [1990+i for i in range(32)]
    liste=[]
    # sumary =summary_pdf.objects.all()
    # [liste.append(sumary[i].titre) for i in range(len(sumary))]
    
    # print(liste)
    ville=['Basse-Pointe (97203)', 'Saint-Pierre (97225)', 'Prêcheur (97219)', 'Morne-Rouge (97218)', 'Marigot (97216)', 'Lorrain (97214)', 'Carbet (97204)', 'Fort-de-France (97209)', 'Bellefontaine (97234)', 'Saint-Joseph (97224)', 'Gros-Morne (97212)', 'Robert (97222)', 'Trinité (97230)', 'Case-Pilote (97205)', 'Schœlcher (97229)', 'Lamentin (97213)', 'Ducos (97207)', 'François (97210)', 'Trois-Îlets (97231)', "Anses-d'Arlet (97202)", 'Rivière-Pilote (97220)', 'Vauclin (97232)', 'Diamant (97206)', 'Sainte-Luce (97227)', 'Sainte-Anne (97226)', 'Marin (97217)']
    return render(request,'affichage/hello.html',{"ville":ville,'date':date,"sum":list(liste)}
    )

def search(request):
    
    if request.method == 'POST':

        recherche= request.POST['recherche_page']
        date_debut=request.POST['date_deb']
        date_fin=request.POST['date_fin']
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
            
        # ss_terr=try_radio(request.POST['sous_terrain'])

        

        ville=releve_Ville.objects.all()

        print(date_debut,'--',date_fin,"<---------------------",ss_terr,surface_terr,eau_surface)
        code = ville[0].data['Commune'][recherche.strip()]['code']
        JSON=None
        # for elm in code:
        #     JSON[elm]=jsonAffiche(elm)
        
            #print(type(JSON[elm]),'<-----------------------------------')
        # pdf=summary_pdf()
        # day=str(datetime.datetime.today().date())
        # titre=day+"okok"
       
        # pdf.titre=titre
        # make_pdf(titre,recherche)
        
        # check="ville/tmp/"+titre+".pdf"
        # print(check,"<---------------------")
        # path = Path(str(check))
        
        # with path.open(mode='rb') as f:
        #     pdf.file = File(f, name=path.name)
        #     pdf.save()
        id=33
        T1=None
        T2=None
        T3=None
        # print(JSON['1166ZZ0026/NF8'].keys())
        if ss_terr or surface_terr or eau_surface:
            choix=0
            if ss_terr:
                T1=tabl(3, str(date_debut) , str(date_fin) )
            if surface_terr:
                T2=tabl(2, str(date_debut) , str(date_fin) )
            if eau_surface:
                T3=tabl(1, str(date_debut) , str(date_fin) )
            notre_json=releve_Ville()
            notre_json.data={"tab1":T1,"tab2":T2,"tab3":T3}
            notre_json.nom='votrejson'
            notre_json.save()
            id = notre_json.id
            return render(request,'affichage/search.html',{"data":recherche,
                                                       'ville':code,'JSON':JSON,
                                                       "id":id,"tab1":T1,"tab2":T2,"tab3":T3})
    
    return render(request,'affichage/hello.html')

def maping(request):
    return render(request,'affichage/map.html')

def graph(request):
    chart=nouveau()
    camenbert=pie()
    return render(request,'affichage/graph.html',{'graph':chart,'pie':camenbert})

def about(request):
    titre=Titre.objects.all()
    return render(request,'affichage/about-us.html',{'titre':titre})

def presentation(request):
    
    map={'m1':mapmaxmin,'m2':surfandsouter,'m3':littoraux}
    return render(request,'affichage/amap.html',map)

def Tableau(request):
    
    data=tabl(1,'2020-05-01','2022-05-06')
    T1=tabl(3, '2020-05-01' , '2022-05-06' )
    T2=tabl(2, '2020-05-01' , '2020-05-29' )
    T3=tabl(1, '2020-05-01' , '2020-05-29' )

    data2=tabl(2,'2020-05-01','2022-05-06')
    context = {'d': T3,'deux': data2}
  
    return render(request, 'affichage/tableau.html', context)

def contact_us(request):
    form = ContactUsForm()
    print('La méthode de requete est: ', request.method)
    print('Les données POST sont: ',request.POST)
    if request.method == "POST":
        form = ContactUsForm(request.POST)
    else:
        form= ContactUsForm()
    return render(request,'affichage/contact-us.html',{'form':form})

def new_base(req):
    return render(req,'affichage/new_base.html')
 
def upload_file(request, id):
        data=releve_Ville.objects.get(id=id)
        buf=io.BytesIO()
        c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
        textob=c.beginText()
        textob.setTextOrigin(inch, inch)
        textob.setFont("Helvetica",14)
        lines=[
            str(data.data),

            "ligne 1",
            "ligne2"
        ]
        for line in lines:
            textob.textLine(line)
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)
        return FileResponse(buf, as_attachment=True,filename="test.pdf")

    # project =summary_pdf.objects.get(id=id)
    # fl_path = project.file.path
    # print(fl_path,"---------------")
    # filename = project.file.name
    # fl = codecs.open(fl_path, 'r', encoding='ISO-8859-1')
    # mime_type = "application/zip"
    # response = HttpResponse(fl, content_type=mime_type)
    # response['Content-Disposition'] = "attachment; filename=%s" % filename
    # return response
    # """if request.method == "POST":
    #     form = summary_pdf(request.POST,request.FILES)
    #     if form.is_valid():
    #         return redirect(hello)
    # else : form = summary_pdf()
    # return render(request, "affichage/upload.html",{"form":form})"""

def listing(request):
    return HttpResponse("<p>la liste<p>")





def bands_list(request):
    bands=Band.objects.all()
    titre=Titre.objects.all()
    return render(request,"affichage/bands_list.html",{'titre':titre,'bands':bands})






def bands_list_detail(request,id):
    band = Band.objects.get(id=id)
    return render(request,'affichage/bands_list_detail.html',{'band':band})


    
