#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import web
import json
import time

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

		#time.sleep(10)
		
		headers = {"Authorization": "key=AIzaSyBSFHnJV7Q35CnsHcybhpQLSH6clyrltJE", "Content-Type" : "application/json", "Accept-Encoding" : "application/json" }

		data = { "registration_ids" : [str(aux["registrationId"])],
			 "data" : { "mensaje" :"desde aki mando"}}

		url = "https://android.googleapis.com/gcm/send"

		print "enviando peticion"
		r = requests.post(url, data = json.dumps(data), headers = headers)

		print r



class basura:
	def GET(self, basura):
		return "<h1>Nop</h1>"

if __name__ == "__main__":
	app.run()
