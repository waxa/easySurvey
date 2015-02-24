#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf8")
import web
import json

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
		fich.write(web.data())

class basura:
	def GET(self, basura):
		return "<h1>Nop</h1>"

if __name__ == "__main__":
	app.run()
