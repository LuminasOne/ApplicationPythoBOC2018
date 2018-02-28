
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dico_test={"salle":(("start","end"),"summary")
			(("start","end"),"summary")
	       }
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    (("start","end"),"summary")
TypeError: 'tuple' object is not callable
>>> dico_test={"salle":("start,end,summary)
			
SyntaxError: EOL while scanning string literal
>>> dico_test={"salle":["start,end"]
	       }
			
>>> dico_test={"salle":[("start","end"),"sujet"]
	       }
			
>>> dico_test.has_key("salle")
			
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dico_test.has_key("salle")
AttributeError: 'dict' object has no attribute 'has_key'
>>> dico_test.key("salle")
			
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dico_test.key("salle")
AttributeError: 'dict' object has no attribute 'key'
>>> get dico_test["salle"]
			
SyntaxError: invalid syntax
>>> dico_test["salle"]
			
[('start', 'end'), 'sujet']
>>> dico_test.keys()
			
dict_keys(['salle'])
>>> dict_keys["salle2"]=[("start","end"),"sujet"]
			

 dict_keys["salle2"]=[("start","end"),"sujet"]

>>> dico_test["salle2"]=[("start","end"),"sujet"]
			
>>> dico_test.keys()
#pour obtenir les clé du dictionnaire 			
dict_keys(['salle', 'salle2'])


Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    test["chips"]=(test["lays"],test["springles"])
NameError: name 'test' is not defined
>>> test{}=


>>> test={}
			
>>> test["chips"]='bonjour'
			
>>> print(type(test))
			
<class 'dict'>

>>> test["chips"]=("lays","springles")
			
>>> test["chips"]
			
('lays', 'springles')

>>> test["chips"]=(("mai","trunks"),"age")
			
>>> print(test["chips"])
			
(('mai', 'trunks'), 'age')
>>> print(test["chips"][0])
			
('mai', 'trunks')
>>> 