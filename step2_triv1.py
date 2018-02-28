#coding:utf-8
#Triage du fichier json
from __future__ import print_function

import os

#from apiclient import discovery
#from oauth2client import client
#from oauth2client import tools
#from oauth2client.file import Storage
#import de sys pour tenter de réparer le système
import sys,json
import datetime
from collections import defaultdict


nomfichier="donnees_full.json"


#On veut récupere  trois champs spécifiques    le datetime est spéra en  2 dates start (début de l'evenement)   et end(fin de l'évenement),summary et location
#dans la structure json  le end est placer avant le début. 
#with open('cleandata.json')  as  fd:
 #   datas=json.load(fd)
#fd = open(nomfichier,"r") 
#datas=json.load(fd)
#print( datas )



fd = open(nomfichier,"r")
datas_full = json.load(fd)
#print ('Retrieved',len(datas),'characters')
#js = json.loads(datas.encode().decode("utf-8"))

# je fais une variable qui stocke la date de début et la date de fin


print(datas_full)
bylocation = defaultdict(list)
bystart=defaultdict(list)

for promoid, datas in datas_full.iteritems():
    for d in datas['items']:
        print(d)
        d["datetime"] = (d["start"],d["end"])
        #conversion  du tuple datetime en chaine  de caractère? Bonne syntaxe?
        #print("cest un tuple").__format__(str)
        print("%s %s %s"%(d["start"],d["end"],d["summary"]))
        if "location" in d:
            print("Location : %s"%(d["location"]))
            bylocation[d["location"]].append((d["datetime"],(d["summary"])))

        else:
            print("Location : missing")

        print("\n")

print("MES RESULTATS UTILES")
resultat="cleandatav1.json"
with open (resultat,"w")  as fp:
    #fp.write("Informations récuperées après filtrage\n")
    # comment faire les accents en python lorsqu'o fais appel a write
    json.dump(bylocation,fp)

print(bylocation)
print(type(bylocation))

