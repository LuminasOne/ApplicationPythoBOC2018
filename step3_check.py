#coding:utf-8
#verifications des anomalies

from apiclient import discovery

from collections import defaultdict
import sys,json
import os

file="cleandatav1.json"
outfile="verification.json"
global fd
fd=open(file,"r")
datas_postriage=json.load(fd)
#print(datas_postriage)
#je stocke le conflit dans un dictionnaire
conflit=defaultdict(list)

# pas indispensable mais pourrait être utile service = discovery.build('calendar', 'v3', http=http)
def check():
        for datas  in datas_postriage.iteritems():
               # on regarde  si on accède bien au fichier json
               for data in datas['items']:
                #variables de temps pour le début  et la fin   pour  l'objet "salle"  on a besoin de 2 objets "salles"
                rez=False
                data["datatime"]=(data["start"],data["end"])
                datetimestartx=data["start"]
                datetimestarty=data["start"]
                datetimestopx=data["end"]
                datetimestopy=data["end"]
                #if data in datas["lication"]
                if data in eventsbysalle["location"]:
                    roomx=data["location"]
                    roomy=data["location"]
                    #on regarde si c"est la même salle
                    if roomx==roomy:
                        print("afficher nom de la salle %s")%(data["location"])
                        if datetimestopx>datetimestartx:
                            print("Attention anomalie")
                            # rez  correspond au résultalt de l'analyse  c'est  l'anomalie/le conflit, je veux afficher ce conflit et l'écrire mais sous quel forme?
                            print("Salle qui rencontre un conflit : %s")%(data["location"])
                            conflit.append((data["location"]))
                            rez=True
                            with open(outfile,'w')  as fd:
                                json.dump(conflit,outfile)
eventsbysalle=datas_postriage
# if   "location" not in eventsbysalle:
#    print("pas de salle renseigné, la detection est arreté " )
#  else:
#   print('salle: %s'%(event['location']))
#
#  for  salle in eventsbysalle["location"]:
#   check(eventsbysalle)
#
#       on utilise sorted  pour trier directement la structure car sort tout seul va copier notre structure et trier uniquement la structure copié/.
#       bydate=srted
print(eventsbysalle)