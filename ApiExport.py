import code
from bs4 import BeautifulSoup
import requests,json
import time
import pandas as pd

commune={
"Basse-Pointe":{"code":[]},
"Saint-Pierre":{"code":[]},
"Prêcheur":{"code":[]},
"Morne-Rouge":{"code":[]},
"Marigot":{"code":[]},
"Lorrain":{"code":[]},
"Carbet":{"code":[]},
"Fort-de-France":{"code":[]},
"Bellefontaine":{"code":[]},
"Saint-Pierre":{"code":[]},
}
df= pd.read_csv("C:/Users/RAYAN/Documents/LICENCE MATH/ALGO/PROJECT/ProjetChlord-cone/Export.csv", sep=';' )
temp={'Commune': {'Basse-Pointe (97203)': {'code': []},
                    'Saint-Pierre (97225)': {'code': []},
                    'Prêcheur (97219)': {'code': []}, 
                    'Morne-Rouge (97218)': {'code': []},
                    'Marigot (97216)': {'code': []},
                    'Lorrain (97214)': {'code': []},
                    'Carbet (97204)': {'code': []},
                    'Fort-de-France (97209)': {'code': []},
                    'Bellefontaine (97234)': {'code': []},
                    'Saint-Joseph (97224)': {'code': []},
                    'Gros-Morne (97212)': {'code': []},
                    'Robert (97222)': {'code': []},
                    'Trinité (97230)': {'code': []},
                    'Case-Pilote (97205)': {'code': []},
                    'Schœlcher (97229)': {'code': []},
                    'Lamentin (97213)': {'code': []},
                    'Ducos (97207)': {'code': []},
                    'François (97210)': {'code': []}, 
                    'Trois-Îlets (97231)': {'code': []},
                    "Anses-d'Arlet (97202)": {'code': []},
                    'Rivière-Pilote (97220)': {'code': []},
                    'Vauclin (97232)': {'code': []},
                    'Diamant (97206)': {'code': []},
                    'Sainte-Luce (97227)': {'code': []},
                    'Sainte-Anne (97226)': {'code': []},
                    'Marin (97217)': {'code': []}}}
for i in range (len(df)):
    temp['Commune'][df['Commune'].iloc[i]]["code"].append(df["Ancien code national BSS"].iloc[i])
print(temp)