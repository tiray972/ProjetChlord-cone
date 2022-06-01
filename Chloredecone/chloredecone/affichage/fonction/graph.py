import base64
from io import BytesIO
# from Chloredecone.chloredecone.affichage.views import graph
from affichage.fonction.ApiExport import tabl
import pandas as pd
from matplotlib import pyplot as plt

# permet dencoder les graphique mathplotlib pour pouvoir obtenir les photo dans une page html avec django

def get_graph():
    buffer =BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf_8')
    buffer.close()
    return graph


# recuperent les donne grace a table et les traite avec pandas et mathplotlib pour obtenir un graph
#
def nouveau():
    var=pd.DataFrame(tabl(1, '2010-05-01' , '2020-05-29')["data"])
    print(var.keys())
    date=[]
    res=[]
    for i in var.itertuples():
        if i.libelle_parametre=='Dichlorobenzène-1,4':
            print(i.libelle_parametre,end='')
            print( ' ',end='')
            print( i.resultat)
            date.append(i.heure_prelevement+i.date_prelevement)
            res.append(i.resultat)

    plt.switch_backend('AGG')
    plt.figure()
    plt.plot(date,res,label='hold')
    # plt.plot(,label='solde')
    plt.xlabel('temp avec interval de 15min')
    plt.ylabel('montant en $')
    plt.legend()
    # plt.savefig('static/graph.png')
    graph=get_graph()
    return graph

# recuperent les donne grace a table et les traite avec pandas et mathplotlib pour obtenir un diagrame camenbert
def pie():
    var=pd.DataFrame(tabl(1, '2010-05-01' , '2020-05-29')["data"])
    print(var.keys())
    # date=[]
    lib=[]
    for i in var.itertuples():
        
        # print(i.libelle_parametre,end='')
        # print( ' ',end='')
        # print( i.resultat)
        # date.append(i.heure_prelevement+i.date_prelevement)
        lib.append(i.libelle_parametre)
    print(type(var['libelle_parametre'].value_counts()))
    plt.switch_backend('AGG')
    plt.figure()
    plt.pie(var['libelle_parametre'].value_counts())
    # plt.plot(,label='solde')
    # plt.xlabel('temp avec interval de 15min')
    # plt.ylabel('montant en $')
    # plt.legend()
    # plt.savefig('static/graph.png')
    graph=get_graph()
    return graph



