# ApplicationPythonBOC2018

Bonjour  à toutes et tous, dans le cadre de mon stage d'une durée de 3 semaines le BrestOpenCampus  m'as confié une mission qui a pour objectif  de  réaliser une application  qui  détecte les anomalies ou conflits  répartis  sur l'ensemble des  agendas du Brest OpenCampus. Ce script sera utile aux responsables  pédagogique  et il informera l'utilisateur des  différents conflits ou anomalie qu'il a détecté 

ICI vous pourrez trouver mes différents  travaux sur la réalisation de ce script.  Ce script va continuer a être amélioré pour être le plus complet possible.  

La version de python utilisé est la dernière version 3.6 et j'utilise l'ide pycharm. Je fais également appel a l'API  de google au début du script.


StagiaireDuBrestOpenCampus EPSIB2

Prérequis: vous devez possédez le module pip pour installer ces différentes biblithèques 

Voici les bibliothèques nécessaires  :
  
  
-[google-api-python-client](https://github.com/google/google-api-python-client)

-[nose](https://github.com/nose-devs/nose)

-[oauth2client](https://github.com/google/oauth2client) (pour l'authentifcation au google agenda)
			     
          
Bibliothèques tier installé avec la biblithèque de l'api google :

-[uritemplate](https://github.com/python-hyper/uritemplate) 

-[httplib22](https://github.com/python-hyper/uritemplate)


 Pour l'installation il faut utiliser  `pip` ou 'easy_install' 
```bash
$ pip install --upgrade google-api-python-client
```

```bash
$pip install nose
```

```bash
$pip install oauth2client
```


Par ailleurs vous aurez besoin de créer votre propre client.secret.json 
Je vous redirige vers  le tutoriel de [l'API](https://developers.google.com/calendar/quickstart/python)

#Exécutions du script.

Pour lancer le script il faudra d'abords changer les adresses dans la fonction send notifications  par des adresses personnelles , vous assurrez que vous avez bien un fichier clientsecret.json

Commande d'éxécution du script sur python 3.6
```bash 
$python BOCCalendarv1.py 
````
