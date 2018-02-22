from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


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

def main():
    
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print(u' Voici les 14 prochains  évenements de votre agenda ') ;#  petite subiltié pour prendre en compte les accents il faut mettrre un u devantt nos chaione de caractères comme ça elle seront traité comme des chaines unicodes 
    eventsResult = service.events().list(
        calendarId='fmjgmpfde73ivaib832214h6cc@group.calendar.google.com', timeMin=now, maxResults=14, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
  
    #  on affiche ce qui est recupéré dans events , le print montre la séquence de recuperations de toutes les informations 
    
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        informations =print(start, event['summary'],"\n")
        if 'location' not in event:
            print(u'salle non définie')
        else:
            print('salle: %s'%(event['location']))
        nomfichier="donnees.json"
        fichier=open(nomfichier,'w')
           import  json 
        json.dump(eventsResult,fichier)
        print (u"salle non définie")
     

    fichier=open(nomfichier,'r')

    fichier.close() 
    if fichier  is not 'null':
        print(u'les informations ont   été enregistré\n')
        #condition inutile je voulais verifier si les informations étaient bien enregistré  et afficher un message si c'était le cas mais la condition toujours vraie car même en cas d'erreur il écrit "null" dans le fichier
        #pourquoi mon ficher  écrit null?   c'est comme il a rien trouvé c'est un message par défaut? 
        #None équivaut a Null en python  et on affiche un message pour voir si le fichier a bien été crée et  si il n'est pas vide 
    else:
        print(u'informations invalides')

    print(type(eventsResult))

if __name__ == '__main__':
    main()