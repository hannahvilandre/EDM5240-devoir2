#2019 Hannah Raphaëlle Petitclerc-Vilandre
#Coding : utf-8

import json
import csv
import requests

fichier = "banq.csv" #on donne d'abord un nom au fichier qui sera créé par la suite.
adresse = "http://collections.banq.qc.ca/api/service-notice?handle=52327/"
# premier essai avec "http://collections.banq.qc.ca/api/service-notice?handle=52327/1000" pour tester

entete = {
	"User-Agent":"Hannah Raphaelle Petitclerc-Vilandré",
	"From":"hannahvilandre@gmail.com"
} 

for chiffre in range(1000,2001):
	urlcomplet = "http://collections.banq.qc.ca/api/service-notice?handle=52327/{0}".format(chiffre)# format() is the primary API method. It takes a format string and an arbitrary set of positional and keyword arguments. format() is just a wrapper that calls vformat().Trouvé sur https://www.python.org/dev/peps/pep-3101/
	print(chiffre)
	print(urlcomplet)# ici on obtient toute les adresses jusqu'à "/" suivies du chiffre 1000 jusqu'à 2000 (après avoir testé je dois mettre range 1000, 2001 sinon on obtient pas "/"2000) 
	
	req = requests.get(urlcomplet,headers=entete)

	print(req)	
	
	if req.status_code != 200:         # cela done bien [200] donc tout fonctionne jusque là ! OUF parce que maintenant ça se corse !!! 
		print("ne marche pas")
	else: 
		infos = req.json()
		#print (infos)# On obtient toutes les données mélangées mais nous on veut obtenir juste les fichiers "audio" donc je dois isoler chaque composante.

		if infos["type"]== "audio": # merci pour le tuyau ici :) !!!!
			    listes = []
			    listes.append(infos["titre"].split(" /")] # pour ne voir que le titre et rien d'autre après.
			    listes.append(infos["createurs"][0]) # utilisation du [0] pour avoir uniquement le premier createur de la liste. 
			    listes.append(infos["dateCreation"])
			    listes.append(infos["descriptionMat"])
			    print("titre")
			    print("createurs")
			    print("dateCreation")
			    print("descriptionMat")
			    print(listes)
			    print("~"*80)


		f2 = open(fichier,"a")
		prout= csv.writer(f2)
		prout.writerow(listes)    
		
		
		
		
		
		
		
		
		
		
		
		
		
