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

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


#ce code est fournit par l'API et sert a récuperes les code des identifiants
def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials



#1er Partie Foncton  qui va réucperes les informations des googles agendas  calid  signifie calendar identifier
def get_calendar(service, calid, outfile=None, starttime=None, display=False):

    if starttime:
        now = starttime
    else:
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    calendarv2= service.calendars().get(calendarId=calid).execute()
    print (calendarv2['summary'])
    eventsResultv2 = service.events().list(
        calendarId=calid, timeMin=now, maxResults=14, singleEvents=True,
        orderBy='startTime').execute()
    if outfile:
        fd = open(outfile, 'w')
        json.dump(eventsResultv2, fd)

    if display:
        eventsv2 = eventsResultv2.get('items', [])
        if not eventsv2:
            print('No upcoming events found.')
        for event in eventsv2:
            startv2 = event['start'].get('dateTime', event['start'].get('date'))
            informationsv2 =print(startv2,event['summary'],"\n")
            if 'location' not in event:
                print(u'salle non définie')
            else:
                print('salle: %s'%(event['location']))
            #nomfichier="donneesv1.json"
            #fichier=open(nomfichier,'a')
    print(type(eventsResultv2))
    return eventsResultv2

global fichier
fichier ="donnees_full.json"

# ici je déclare mon dictionnaire

def my_getcalendar():
    dict_promotion = {
        #"sdcM1"  : 'pepm73g6gnd0194p4g9s7afops@group.calendar.google.com',
        #"ifagM1" : 'cf5ak16baeqfm7ipote2653vc8@group.calendar.google.com',
        #"epsiI4" : 'tcko1254t2qinqvvfha22ajai8@group.calendar.google.com',
        #"epsiI5": 'g22d877b9j49pq8sc33mcbnj0k@group.calendar.google.com',
        #"agendattest1":'nkstageboc@gmail.com',
        #"ifagM2":"07k9bfg5gbm14812ff8t05aom4@group.calendar.google.com",
        #"epsib1":"fmjgmpfde73ivaib832214h6cc@group.calendar.google.com",
        #"agendatest2":'s34vu9qfjb9h0oumorq0hpbb58@group.calendar.google.com'
        "sdcb1": 'qh1unrm92qt6i154p7tq8i5a3o@group.calendar.google.com',
        #  pas actualisé il faudra remplacer   ancien id gc5dap9h0lh78tujae8i9nmk48@group.calendar.google.com
        "sdcb2": 'bkjbg8l58ahc3p6goqvbhs3tn0@group.calendar.google.com',
        "ifagb1": 'a7ml849fqhjgiujk9cf2bu96l4@group.calendar.google.com',
        "ifagb2": 'sbvq638tlbctld0pfh9g8pqh4k@group.calendar.google.com',
        "epsib1": 'fmjgmpfde73ivaib832214h6cc@group.calendar.google.com',
        "epsib2": 'k99icqnlruoptl3kd523dl2ddk@group.calendar.google.com',
        "sdcb3": 'f9h4an4d7upfpgi5fci7ltbh4k@group.calendar.google.com',
        "ifagb3": 'o1ma8vp6shcob15l9jn166r63o@group.calendar.google.com',
        "epsb3": 'c87udq6uoulgekts93el4fg9ik@group.calendar.google.com',
        "sdcM1": 'pepm73g6gnd0194p4g9s7afops@group.calendar.google.com',
        "sdcM2": '7tirda22q5iln8l7pv8g6tmsoo@group.calendar.google.com',
        "ifagM1": 'cf5ak16baeqfm7ipote2653vc8@group.calendar.google.com',
        "ifagM2": "07k9bfg5gbm14812ff8t05aom4@group.calendar.google.com",
        "epsiI4": 'tcko1254t2qinqvvfha22ajai8@group.calendar.google.com',
        "epsiI5": 'g22d877b9j49pq8sc33mcbnj0k@group.calendar.google.com',
        "agendattest1": 'nkstageboc@gmail.com',
        "agendatest2": 's34vu9qfjb9h0oumorq0hpbb58@group.calendar.google.com'
    }

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    # ici je fais un calendrier par promotion
    cal_by_promo = {}
    # cette boucle va permettre
    for promoid, calid in dict_promotion.iteritems():
            res = get_calendar(service, calid) #outfile="donnes_v1_"+promid+".json")
            cal_by_promo[promoid] = res
    #variable global fichier comme ça je peux le réutiliser ailleurs dans le code
    #global fichier
    #fichier ="donnees_full.json"
    json.dump(cal_by_promo, open(fichier, 'w'))
    #fichier.close()
# on verifie si les informations ont bien été enregistré dans le fichier
    if fichier is not None:
        print(u'les informations ont   été enregistré\n')
    else:
        print(u'informations invalides')

# si le fichier n'existe pas alors il faudra generer un fichier "donnesfull.json" vide


#2eme étape on trie les informations necessaires
#with open permet d'ouvrir et fermer le fichier automatiquement  c'est plus propre de cette façon  on peut faire fichier.close() mais j'ai une erreur car je n'opère pas sur des chaines des caracteres
with  open(fichier,'r')  as  fd:
    datas_full=json.load(fd)
#print(datas_full)
bylocation = defaultdict(list)
#bystart=defaultdict(list)

#on fais le tri des données   on pourrait ajouter un champ supplémentaire appelr displayname  pour reucperer le nom de la promotion concernée
def data_sort():
    for promoid, datas in datas_full.iteritems():
        for d in datas['items']:
            print(d)
            # on regroupe le champ datetime en un seul champ car sinon ils sont traitées independament   Amélioration il faudrait changer l'affichage et le stockage de cette donnée
            d["datetime"] = (d["start"],d["end"])
            d["displayname"]=d["organizer"]
            print("%s %s " % (d["start"], d["end"]))
            if "location" in d:
                # normé le  nom de salles pour pas avoir des erreurs
                print("Location : %s" % (d["location"]))
                # j'aboute  la  date  et le sujet  a l'entrée  "location" de mon dictionnaire  De cette façon je récuperes l'hoaire  et le sujet en fonction des sALLES
                bylocation[d["location"]].append((d["datetime"],d["displayname"],(d["summary"])))
            else:
                        print("Location : missing")

            print("\n")

# fonction qui  va  écrire les données POST triage dans un fichier
def dumpdatas():
    print("MES RESULTATS UTILES")
    resultat="cleandatav2.json"
    with open (resultat,"w")  as fp:
        #fp.write("Informations récuperées après filtrage\n")
        json.dump(bylocation,fp)

elementsInError=[]
# 3ème  étape algorithme de vérification
def check_conflict(setdatas):
    bydate = sorted(setdatas, key=lambda dates: dates[0])  # tri en fonction des dates de début.
    print(bydate)
    #elementsInError=[]
    for rangeA, rangeB in zip(bydate[0:], bydate[1:]):
        # on fais sur les deux range   la Range  A prend les éléments de la premiere tuple
        #print rangeA, rangeB
        if rangeA[1] < rangeA[0] or rangeB[1] < rangeB[0]:
            raise Exception('Invalid date range ... : rangeA=%s, rangeB=%s'%(rangeA, rangeB))
        if rangeB[0] < rangeA[0]:
            raise Exception('Invalid chronology ... : rangeA=%s, rangeB=%s'%(rangeA, rangeB))
       # print(rangeA)
        #print(rangeB)
        rangeAstop=rangeA[1]
        rangeBstart=rangeB[0]
        rangeAstart=rangeA[0]

        #lors de l'appel de cette fonction il faut préciser si ça concernent des salles identiques
        if rangeAstart== rangeBstart:
            print("Attention il y'a un chevauchement")
            with open ('anomalielist.txt','w'):
                elementsInError.append(rangeAstart)
            print(rangeAstart)

            #return rangeAstart
        #else:
         #  print("Rien a signale")
        #elementsineror or filedescriptor.("rien a signalé")
    elementsInError.append("rien a signalé")
    return elementsInError


#dictionnaire pour  stocker les salles qui comportent différents conflits
myconflit=defaultdict(list)
salle=""
events=defaultdict(list)
anomalie=defaultdict(list)

#  Ici j'applique l'algorithme sur les agendas et le fichier.json que j'ai récupéré
#  Petit doute  rez_conflicts  ne prend pas de paramètres?
def rez_conflicts():
    eventsbysalle = json.load(open('cleandatav2.json'))
    for salle, events in eventsbysalle.iteritems():
    #print salle, events
        list_creneaux = []
        for e in events:
            # on passe l'objet datetime en un seul car avant c'était un double tuple
            ename = e[1]
            estart = e[0][0]["dateTime"]
            estop = e[0][1]["dateTime"]
            # ici je reformalise les date  et je transforme mes objet estart  et estop en objet datetime
            dtstart = datetime.datetime.strptime(estart, "%Y-%m-%dT%H:%M:%S+02:00") # attention, on considere toujours la timezone a +1h
            dtstop = datetime.datetime.strptime(estop, "%Y-%m-%dT%H:%M:%S+02:00")
            # il ne faut pas concantener c'est deux objet différents/factorisation
            #dtime=(datetime.datetime.strptime(estart,"%Y-%m-%dT%H:%M:%S+01:00"),datetime.datetime.strptime(estop, "%Y-%m-%dT%H:%M:%S+01:00"))
            #print dtstart, dtstop ename pour rajouter le nom de la promotion rectification nom du module
            list_creneaux.append([dtstart,dtstop,e])
            res = check_conflict(list_creneaux)
            # astuce faire deux objets salle pour comparer et trouver une correspodance
            print (salle)
            print(type(salle))
            print(type(res))
            if res is False:

                    # on affiche uniquement les modules et les horaires ou il y'a le chevauchement
                    #dans un premiere temps on essaye juste de recupere les salles
                    # on remplace cette lignes qui ne traité que un seul evenement(appelé 'e' )a la fois
                    #myconflit["Liste des Salles de conflit"].append((salle,e))
                    # cette ligne sert a veiller  que chaque ligne soit individuelle  et une seule fois dans le fichier. Par contre il reste a determiner  si les cours qu'ils sont plusieurs fois dans la semaine seront aussi supprimé techniquemnt non car la ligne est différente
                    # unique = {repr(each): each for each in e}.values()
                    myconflit["Liste des Salles de conflit "].append((salle,events))
                    anomalie.append(elementsInError,salle)
                    #print(unique)

                    #if  salle=="Espace médiathèque":
                        #myconfl["Les te-ti  de l'espace médaitheque ne devront pas être inclut]
                        # OU
                        #~ file.write("Concernent les TE-TI donc ce n'est pas un conflit, veuillez vérifiez l'étape suivante')
                   #if salle=="Espace médiathèque":
                    #    myconflit["C'est un conflit pendant un TE-TI donc rien a signalé "]
                    #print("%s : probleme de conflit !" % (salle))
                    #print(salle)
                    #print(myconflit)


#def  solvingconflict():
 #   for  event  in myconflit:





# je  transmets la liste des conflit dans un fichier  exemple.json pour ensuite l'envoyer dans un rapport
def dump_conflict():
    print("Liste de Salle avec conflits")
    print(myconflit,"\n")
    #myconflit["Messages"].append((salle)["comporte un conflit voici  le créneaux concerné avec les classes "].append(events[0],events[1])["\n"])
    with open('postetriage.json','w') as fd:
        #solution alternative pas très propre mais ça fonctionne tout type inconnu est traité comme une chaine de caractères
        json.dump(myconflit,fd)
        #json.dump(myconflit,fd)
        print("Les donnees ont bien ete rajoutees")


#
#def format_conflict():
    #ename1 correspond au premier evenement et  ename2 corresponed au nom du second evenement.  ligne pas très propre pour le format du mail
 #   with open("rapportconflitversioning.txt",'w') as fd:

  #      fd.write((salle).append["comporte des conflits  sur ce créneaux "].append(dtstart,dtstop).append["\n"].append["Les classes  concernées sont "].(ename).append["et "].(ename2))




#Etape 4 notification envoi du mail
def my_notification():
    #pour le test je vais utiliser mon adresse comme destinataire
    msg = MIMEMultipart()
    mail_envoi = "nkstageboc@gmail.com"
    destination = ['masterzabi@gmail.com','boynick@hotmail.fr']
    # motdepasse de votre adresse donc rempalcer par pwd une  fois up sur git le mot de passe est clair c'est TRES RISQUE.
    gmail_password = "missionCAPITAL29"
    msg['From'] = mail_envoi
    msg['To'] = destination
    msg['Subject'] = "RECEPTION DU RAPPORT?"
    body = "Bonjour voici le mail de rapport, pouvez vous faire l'accusé reception de mon fichier"
    #  précédement ",".join spéra chaque caractère donc erreur d'affichage supprimé.
    msg.attach(MIMEText(body, 'plain'))
    filename = "rapportconflit.json"
    attachment = open(filename, "rb")
    # On précise le type de données et le flux
    partie = MIMEBase('application', "octet-stream")
    partie.set_payload((attachment).read())
    encoders.encode_base64(partie)
    partie.add_header('Content-Disposition', "attachment; filename=%s" % filename)
    # J'ajoute une piece jointe
    msg.attach(partie)
    try:
        # port 465 c'est le port de gmail avec la certification SSL.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        print("Le serveur répond")
        server.login(mail_envoi, gmail_password)
        print("Mail en cours d'envoi")
        text = msg.as_string()
        server.sendmail(mail_envoi, destination, text)
        server.close()
        print("mail envoyé")

    except:
        print( "Il  y'a eu un problème")


if __name__ == "__main__":
    #j'ajoute un décompte pour mesuéré le temps d'éxécution
    start_time=time.time()
    #Récuperation des données de l'agenda
    my_getcalendar()
    #Triage    et  Sauvegarde des données après le triage
    data_sort()
    dumpdatas()
    #Phase de  vérification et détections  des éventuels  conflits
    rez_conflicts()
    dump_conflict()
    #my_notification()
    print("Temps d execution du code en secondes  : %s secondes ---" % (time.time() - start_time))




