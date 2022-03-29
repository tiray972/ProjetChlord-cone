from bs4 import BeautifulSoup
import requests,json
import time


def concatenation(deb,fin):
    url="http://www.naiades.eaufrance.fr/acces-donnees#/physicochimie/resultats?debut="
    url=url+deb+"&fin="+fin
    return url
    

urlexemple='http://www.naiades.eaufrance.fr/acces-donnees#/physicochimie/resultats?debut=18-03-2019&fin=18-03-2022'

r=requests.get(urlexemple)
print('\n')
soup=BeautifulSoup(r.text,features="html.parser")
# print(reponce.status_code)
# print(reponce.headers)
# print(reponce.text)
# print(reponce.headers)
titre=soup.find('title')
resultat=soup.find_all('div')
print(titre)
for elm in resultat:
    print(elm.content,'\n')


import pandas as pd
import csv

# r=requests.get("http://services.ades.eaufrance.fr/ServicesPublic/ServicesAdesTableau/1/DataSheet_1.asmx?op=GetCapabilities")
print('\n')
dico= { 'service':'ADES:Fiche', 'request' :'GetCapabilities', 'version' :'1.0.0'}
hed={'Content-Type':'application/xml'}
url1 = 'https://ades.eaufrance.fr'
# donnees = json.loads()
url='https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/analyse_pc.csv'
r2 = requests.get(url)
# j = requests.get(url1,params=dico,headers=hed) 

print(r2.headers,'\n')
# print(j.headers['Content-Type'])


with open('donne_extraite.csv','w') as file:
    file.write(r2.text)
    
u=0

'''
def CreationUrlnaiades(types,region,deb,fin):
    url="http://www.naiades.eaufrance.fr/acces-donnees#/physicochimie"
    url=url+"/resultats/exportCsv?debut="+deb+"&fin="+fin+'&departements='
    return url
pointDeau_='http://services.ades.eaufrance.fr/adesfiche/?version=1.0.0&service=ades%3AFiche&request=getFichepointeau&code=BSS002NMFY'

nul='http://ADES:Fiche/request=GetFicheReseau/version=1.0.0/code=0000000029'
urlexemple='http://naiades.eaufrance.fr/acces-donnees#/physicochimie/resultats/exportCsv?debut=08-11-2013&fin=08-11-2016&departements=31&fractions=145'
'''
'\n'