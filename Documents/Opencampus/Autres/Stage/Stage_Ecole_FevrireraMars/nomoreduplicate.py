#coding:utf-8
from __future__ import print_function
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
# os  se refere au système d'exploitation
import os
import httplib2
import  datetime
import json
from collections import defaultdict
import time
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import  encoders




if __name__ == "__main__":
    test= "testfilebis.txt"

    #with open(test,'r').readlines()  as fd:

analyse=open(test,'r').readlines()
print(analyse)
# set est une méthode qui crée un objet vide sur lequel on pourra itérer
analyse_set=set(analyse)
noduplicata= open("nodupilcate.txt",'w')
#si le fichier n'existe pas on le créee
#if test==None:
 #   fd=open(test,'w')
for  line in analyse_set:
            noduplicata.write(line)

            print(noduplicata)
print("voici la fiche")
#unique = { each e[1] : each for each in te }.values()





def dump_conflict():
    print("Liste de Salle avec conflits")
    print(myconflit,"\n")
    #myconflit["Messages"].append((salle)["comporte un conflit voici  le créneaux concerné avec les classes "].append(events[0],events[1])["\n"])

    #
    # with open('rapportconflitversioningv4.json','w') as fd:
    #     lines_seen=set(fd)
    #     outfile = open("rapportcopie.json", "w")
    #     for line in open("rapportconflitversioningv4.json", "r"):
    #         if line not in lines_seen:  # not a duplicate
    #             outfile.write(line)
    #             lines_seen.add(line)
    #     outfile.close()
    #
        #json.dump(myconflit,fd)

    #analyse = open('rapportconflitversioningv4.json', 'r').readlines()

    # set est une méthode qui crée un objet vide sur lequel on pourra itérer
    #analyse_set = set(analyse)
    #noduplicata = open("nodupilcate.json", 'w')
    # si le fichier n'existe pas on le créee
    # if test==None:
    #   fd=open(test,'w')
    #for line in analyse_set:
       # noduplicata.write(line)
        #print(noduplicata)



    #print("voici la fiche")
    #json.dump(myconflit,noduplicata)
    #après qu'on ai ajouté le message on envoie le rapport sous format de fichier texte
    #with open('rapportaconflitsv1.txt','w') as fp:
        #fp.write(myconflit)
    with open('postetriage.json','w') as fd:
        #solution alternative pas très propre mais ça fonctionne tout type inconnu est traité comme une chaine de caractères
        json.dump(myconflit,fd,default=str)
        #json.dump(myconflit,fd)
        print("Les donnees ont bien ete rajoutees")
