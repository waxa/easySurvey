#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import web
import json
import time
import claves as claves
import requests

fname = "movilId.txt"

urls = (
	'/guardarId/', 'guardarId',
	'/(.*)', 'basura'
)

app = web.application(urls, globals())

class guardarId:
	def POST(self):
		fich = open (fname, "w")
		aux = json.loads(web.data())
		print aux
		print "intento de"
		print aux["registrationId"]
		fich.write(json.dumps(aux))

		data = { "registration_ids" : [str(aux["registrationId"])],
			 "data" : { "mensaje" :"desde aki mando"}}

		print "enviando peticion"
		r = requests.post(claves.url, data = json.dumps(data), headers = claves.headers)

		print r



class basura:
	def GET(self, basura):
		return "<h1>Nop</h1>"

if __name__ == "__main__":
	app.run()
