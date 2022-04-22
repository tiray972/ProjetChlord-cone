import json
from operator import ne
from turtle import shape
import folium
from folium import plugins
import pandas as pd
import numpy as np
import requests
from affichage.fonction.ApiExport import creationDurlHubeau
def mapmaxmin():
    requette=requests.get("https://hubeau.eaufrance.fr/api/v1/qualite_rivieres/station_pc?code_departement=972")
    new=pd.DataFrame(json.loads(requette.text)['data'])
    
    new['lien']=''
    new['count']=''
    # new = old[['A', 'C', 'D']].copy()
    for i in range (new.shape[0]):
        new['lien'].iloc[i]='<a href='+str(creationDurlHubeau(code_station=new['code_station'].iloc[i]))+'>'+str(new['libelle_station'].iloc[i])+'</a>'
        new['count'].iloc[i]=json.loads(requests.get(creationDurlHubeau(code_station=new['code_station'].iloc[i])).text)['count']

    # print(new['longitude', 'latitude'])'longitude', 'latitude'
    map_enum_icons = folium.Map([14.6, -61], zoom_start=11)
    for i in new.itertuples():
        folium.Marker(location=[i.latitude, i.longitude],
                    popup=i.lien,#libelle_station
                    icon=plugins.BeautifyIcon(number=i.count,
                                                border_color='blue',
                                                border_width=1,
                                                text_color='red',
                                                inner_icon_style='margin-top:0px;')).add_to(map_enum_icons)
    #     number reste a changer mtre des valeur
    # print(new.lien)
    return map_enum_icons._repr_html_()
