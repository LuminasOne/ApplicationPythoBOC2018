
adresse utilisé pour la connexion et utilisation de l’API:nkstageboc@gmail.com

mot de passe : password

adresse de test pour  des messages réception : masterzabi@gmail.com

la réalisation du projet c’est faite sur Windows 8.1 64 bits. 

Le code comporte des test unitaires

liste COMPLÈTE des imports utilisé dans le cadre de la réalisation du script

//coding:utf-8

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
//os  se refere au système d'exploitation

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

liens pertinents : 	https://developers.google.com/calendar/quickstart/python 
			https://developers.google.com/calendar/v3/reference/events 
installation des packets noses pour les test unitaires.
