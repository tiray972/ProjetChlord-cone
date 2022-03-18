import requests
import time

tableauexemple='/resultats?debut=18-03-2019&fin=18-03-2022'

reponce=requests.get('http://www.naiades.eaufrance.fr/acces-donnees#/physicochimie')
print('\n')
print(reponce.status_code)
print(reponce)