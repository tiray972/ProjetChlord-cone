import code
import io
from bs4 import BeautifulSoup
from django import http
import requests,json,xmltodict
import time
import pandas as pd

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

def CreationUrlnaiades(types="physicochimie",region="972",deb="28-07-1993",fin="29-03-2022"):
    url="http://www.naiades.eaufrance.fr/acces-donnees#/"
    url=url+types+"/resultats/exportCsv?debut="+deb+"&fin="+fin+'&departements='+region
    return url
def CreationUrlAdes(code):
    url="http://services.ades.eaufrance.fr/TableauStatistique/PtEau?Code="+code+"&mode=1&referentiel=Prof"
    return url

def testrequet(url,paramtre=None,hed=None):
    if paramtre:
        if hed:
            reponce =requests.get(url,params=paramtre,headers=hed)
        else:
            reponce =requests.get(url,params=paramtre)
    else:
        reponce=requests.get(url)
    if reponce.ok:
        return reponce.url,reponce.headers['Content-Type']
    else:
        return "L'URL n'as pas bien repondue"


def resortirData(url,paramtre=None,hed=None):

    if testrequet(url,paramtre,hed)[1]=='text/xml;charset=utf-8'  :
        return(requests.get(testrequet(url,paramtre,hed)[0]).text)

def donnejson(url,param):
    if testrequet(url,paramtre=param)[1]=='application/json;charset=UTF-8':
        return json.loads(requests.get(testrequet(url,paramtre=param)[0]).text)
        
def jsonAffiche(code):
    return json.loads(json.dumps(xmltodict.parse(resortirData(CreationUrlAdes(code=code)))))
dico={'code_departement':'972'}
ades='http://services.ades.eaufrance.fr/datasheet/?' 
httpjson='https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/analyse_pc'
parr={'service':'ADES:Tableau','request':'GetCapabilities','version':'1.0.0' }
# s=requests.get(httpjson,dico),'code':'1186ZZ0185/P','mode':'1' 
# print(s.text)
# l=donnejson(httpjson,dico),,'parameter':'1301'
j=requests.get(ades,parr)
print(j.headers)
print(j.url)