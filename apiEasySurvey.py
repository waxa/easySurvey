#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import web
import json
import time
import claves as claves
import requests

#fname = "movilId.txt"

def crearFichero (fname) :
	fich = open (fname, "w")
	emptyJson = {}
	aux = [] 
	emptyJson["ids"] = aux
	fich.write(json.dumps(emptyJson))
	fich.close()

def cargarDatos (fname) :

	if not os.path.exists(fname) :
		crearFichero (fname)

	fich = open (fname, "r")
	aux = fich.readlines()
	fich.close()
	return json.loads(aux[0])

def hasId(aux) :
	if len(movilIds["ids"]) == 0:
		return False

	for id in movilIds["ids"] :
		if aux["registrationId"] == id["id"] :
			return True

	return False

def comprobarId(aux) :
	if not hasId(aux) :
		guardarMovilId(aux)
	else :
		for movil in movilIds["ids"] :
			if aux["registrationId"] == movil["id"] :
				movil["name"] = aux["name"]
			

def guardarMovilId(aux) :
	print "GUARDANDO NUEVA ID ------"
	movilIds["ids"].append({"id" : aux["registrationId"], "name" : aux["name"]})
	guardarDatos("movilId.txt")


def guardarDatos(fname) :
	fich = open (fname, "w")
	fich.write(json.dumps(movilIds))
	fich.close()

movilIds = cargarDatos("movilId.txt")

#print "acabo aki con:"
#print movilIds

urls = (
	'/guardarId/', 'guardarId',
	'/(.*)', 'basura'
)

app = web.application(urls, globals())

class guardarId:
	def POST(self):
		aux = json.loads(web.data())
		#if not hasId(aux) :
		#	guardarMovilId(aux)

		comprobarId(aux)

		idsSend = []
		for movil in movilIds["ids"] :
			if not movil["id"] == aux["registrationId"] :
				idsSend.append(str(movil["id"]))
		
		data = {
			"registration_ids" : idsSend, 
			"data" : {
				"mensaje" : {
					"mensaje" : str(aux["mensaje"]),
					"from" : str(aux["name"])
				}
			}
		}

		"""
		data = {
			"registration_ids" : [str(aux["registrationId"])], 
			"data" : { "mensaje" : str(aux["mensaje"])}}
		"""

		print "enviando peticion"
		print json.dumps(data)

		#print "ids = " + str(idsSend)
		r = requests.post(claves.url, data = json.dumps(data), 
			headers = claves.headers)
		print r.status_code
		#print "r = " + str(r)

class basura:
	def GET(self, basura):
		return "<h1>Nop</h1>"

if __name__ == "__main__":
	app.run()
