#coding:utf-8
from __future__ import print_function
from apiclient import discovery

from collections import defaultdict
import sys,json
import os
import datetime
import calendar


#c'est test unitaire servent  a tester différents cas sur l'algorithme de vérifications de conflits

date1 = datetime.datetime(2018,03,01,10,30)
date2 = datetime.datetime(2018,03,01,12,00)
date3 = datetime.datetime(2018,03,01,11,30)
date4 = datetime.datetime(2018,03,01,12,30)
date5 = datetime.datetime(2018,03,04,10,30)
date6 = datetime.datetime(2018,03,04,13,30)

datatest = ([date3, date4],
            [date5, date6],
            [date1, date2])


def check_conflict(setdatas):
    bydate = sorted(setdatas, key=lambda dates: dates[0])  # tri en fonction des dates de début.
    print(bydate)

    for rangeA, rangeB in zip(bydate[0:], bydate[1:]):
        # on fais sur les deux range   la Range  A prend les éléments de la premiere tuple
        # print rangeA, rangeB
        if rangeA[1] < rangeA[0] or rangeB[1] < rangeB[0]:
            raise Exception('Invalid date range ... : rangeA=%s, rangeB=%s' % (rangeA, rangeB))
        if rangeB[0] < rangeA[0]:
            raise Exception('Invalid chronology ... : rangeA=%s, rangeB=%s' % (rangeA, rangeB))
        rangeAstop = rangeA[1]
        rangeBstart = rangeB[0]
        if rangeAstop > rangeBstart:
            print("Attention il y'a un chevauchement")
            return False
        else:
            print("Rien a signale")

    return True

def test_overlap():
    dataset = [[date1, date2], [date3, date4]]
    assert check_conflict(dataset) == False

def test_no_overlap():
    dataset = [[date1, date2], [date5, date6]]
    assert check_conflict(dataset) == True

def test_invalid_chronology():
    dataset = [[date5, date6], [date1, date2]]
    assert check_conflict(dataset) == True

def test_invalid_range():
    from nose.tools import assert_raises
    dataset = [[date6, date5], [date1, date2]]
    with assert_raises( Exception ):
        check_conflict(dataset)

def test_small_dataset():
    from nose.tools import assert_raises
    dataset = [[date1, date2]]
    assert check_conflict(dataset) == True

