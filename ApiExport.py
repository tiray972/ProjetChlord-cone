import code
from bs4 import BeautifulSoup
import requests,json
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