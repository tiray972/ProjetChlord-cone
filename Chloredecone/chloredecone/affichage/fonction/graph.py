from affichage.fonction.ApiExport import tabl
import pandas as pd
from matplotlib import pyplot as plt

def nouveau():
    var=pd.DataFrame(tabl(1, '2010-05-01' , '2020-05-29'))
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

    plt.figure()
    plt.plot(date,res,label='hold')
    # plt.plot(,label='solde')
    plt.xlabel('temp avec interval de 15min')
    plt.ylabel('montant en $')
    plt.legend()
    plt.savefig('graph.png')

