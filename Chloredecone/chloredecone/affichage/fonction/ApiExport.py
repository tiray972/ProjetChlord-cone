
# from bs4 import BeautifulSoup
from msilib.schema import tables
from tkinter import N
from tkinter.messagebox import NO
from django import http
import requests,json,xmltodict
import time
import pandas as pd

#les commune avec tout leur code de point d'eau ressencer par ades(sandres)
commune={'Commune': {'Basse-Pointe (97203)': {'code': ['1166ZZ0026/NF8', '1168ZZ0043/MBF1', '1168ZZ0054/PZ']},
 'Saint-Pierre (97225)': {'code': ['1167ZZ0023/RBS1', '1167ZZ0029/SP1', '1167ZZ0045/NF6']},
'Prêcheur (97219)': {'code': ['1167ZZ0024/PRS1']},
'Morne-Rouge (97218)': {'code': ['1168ZZ0037/F1', '1168ZZ0038/S1']},
'Marigot (97216)': {'code': ['1169ZZ0006/F', '1169ZZ0184/F2']}, 
'Lorrain (97214)': {'code': ['1169ZZ0084/NF7']}, 
'Carbet (97204)': {'code': ['1172ZZ0048/SC1', '1172ZZ0049/SC2']}, 
'Fort-de-France (97209)': {'code': ['1173ZZ0072/SP2']},
'Bellefontaine (97234)': {'code': ['1173ZZ0082/NF5']},
'Saint-Joseph (97224)': {'code': ['1174ZZ0087/PZ']},
'Gros-Morne (97212)': {'code': ['1174ZZ0088/PZ']}, 
'Robert (97222)': {'code': ['1175ZZ0030/S1', '1175ZZ0191/MVF1', '1179ZZ0095/FCS1', '1179ZZ0300/NF3']}, 
'Trinité (97230)': {'code': ['1175ZZ0154/NF4', '1175ZZ0190/BF1', '1175ZZ0192/MTF1']}, 
'Case-Pilote (97205)': {'code': ['1177ZZ0077/CCS3', '1177ZZ0173/PZ']}, 
'Schœlcher (97229)': {'code': ['1177ZZ0078/CNS1', '1177ZZ0079/CNS2', '1177ZZ0080/CNS3', '1177ZZ0161/FLF1', '1177ZZ0165/CNF2', '1177ZZ0177/PZ2']}, 
'Lamentin (97213)': {'code': ['1179ZZ0023/S', '1179ZZ0035/F2', '1179ZZ0037/1F01', '1179ZZ0039/P.6', '1179ZZ0040/F3', '1179ZZ0069/2F01', '1179ZZ0070/2F02', '1179ZZ0158/PR-S1', '1179ZZ0159/PR-S2', '1179ZZ0185/SC1', '1179ZZ0202/OFO6', '1179ZZ0203/1F07']},
'Ducos (97207)': {'code': ['1179ZZ0157/CR-S2']}, 'François (97210)': {'code': ['1179ZZ0229/S12', '1179ZZ0248/PZ114', '1179ZZ0249/PZ24', '1179ZZ0250/PZ31BI', '1179ZZ0251/PZ28', '1179ZZ0252/PZ36', '1179ZZ0253/PZ54', '1179ZZ0299/NF2']},
'Trois-Îlets (97231)': {'code': ['1181ZZ0116/VATA1', '1181ZZ0117/VATA2', '1181ZZ0132/PZ']}, 
"Anses-d'Arlet (97202)": {'code': ['1181ZZ0131/PZ']},
'Rivière-Pilote (97220)': {'code': ['1183ZZ0024/S2', '1183ZZ0028/SFG1', '1183ZZ0052/PZ']}, 
'Vauclin (97232)': {'code': ['1183ZZ0026/S1']}, 
'Diamant (97206)': {'code': ['1184ZZ0001/S1', '1184ZZ0002/S2', '1184ZZ0015/DF1', '1184ZZ0016/DF2', '1184ZZ0026/EOL1', '1184ZZ0028/N-3', '1184ZZ0029/N-4', '1184ZZ0030/N-5']}, 
'Sainte-Luce (97227)': {'code': ['1185ZZ0120/PZ']}, 
'Sainte-Anne (97226)': {'code': ['1186ZZ0090/S2']}, 
'Marin (97217)': {'code': ['1186ZZ0118/SMA4', '1186ZZ0119/CMF1', '1186ZZ0185/P', '1186ZZ0186/PZ', '1186ZZ0187/P2']}}}
#creation dune url qui pour etre utiliser par lutilisateur pour avoir acces sur le site niades 
def CreationUrlnaiades(types="physicochimie",region="972",deb="28-07-1993",fin="29-03-2022"):
    url="http://www.naiades.eaufrance.fr/acces-donnees#/"
    url=url+types+"/resultats/exportCsv?debut="+deb+"&fin="+fin+'&departements='+region
    return url
    
# la nous avonr la fonction qui fait une request a partir du code du point d'eau telechart le xml 
def CreationUrlAdes(code):
    url="http://services.ades.eaufrance.fr/TableauStatistique/PtEau?Code="+code+"&mode=1&referentiel=Prof"
    return url
#creation de d'url hubeau
def creationDurlHubeau(code_departement='972',code_station=''):
    Parametre={'code_departement':code_departement,"code_station":code_station}
    Base ='https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/analyse_pc'
    url=requests.get(Base,params=Parametre)
    return url.url

# pour faciliter lappele des APi nous avons mis la fonction tabl qui permet d'alimenter nos tableau avec les donneé voulu 
# nous avons 3 choix qui sont les type de donnée rechercher(eau de surface ,eau sousterraine,littoraux)
#                           format de la date 2014-07-06
def tabl(choix,dateDeb,dateFin,dep='972',code_insee="97230"): #les paarrametre seront les form et bouttons dispos sur la page de recherche
    littoraux='https://hubeau.eaufrance.fr/api/vbeta/surveillance_littoral/lieux_surv?distance=70&latitude=14.6&longitude=-61'
    eausurface='https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/analyse_pc'
    eausouter="https://hubeau.eaufrance.fr/api/v1/qualite_nappes/analyses"
    # httpjson='https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/analyse_pc'
    dico={'code_departement':dep,'date_debut_prelevement':dateDeb,'date_fin_prelevement':dateFin,'size':5000,'code_commune':code_insee}# eau surface
    dico1={}# litoraux
    dicosouter={'num_departement':dep,'date_debut_prelevement':dateDeb,'date_fin_prelevement':dateFin,"code_insee_actuel":code_insee}#eau ss-terrain
    if choix==1:
        
        try:    
            
            h=json.loads(requests.get(eausurface,dico).text)# la nous utilisons la fonction donné json créé au prealable 
            print(h)
            if h['data']:
                return h
            else:
                return {'data':[]}
        except:
            return  {'data':[]}
    if choix==2:
        try:    
            h= json.loads(requests.get(littoraux,dico1).text)# nous retournous unique ment les donnée qui est une liste de json qui a pour clé data
            if h['data']:
                return h
            else:
                return {'data':[]}
        except:
            return  {'data':[]}
    if choix==3:
        try:    
            h= json.loads(requests.get(eausouter,dicosouter).text)#
            
            if h['data']:
                return h
            else:
                return {'data':[]}
        except:
            return  {'data':[]}


