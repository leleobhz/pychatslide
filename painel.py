#!/usr/bin/env pyhton2.6
# -*- coding: utf-8 -*-

# Copyright (C) 2010  Leonardo Silva Amaral

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from main import PageTemplates

class accesslist(db.Model):
	user = db.UserProperty(required=True)
	
class slides(db.Model):
	data = db.BlobProperty(required=True)
	uploader = db.UserProperty(required=True)
	name = db.StringProperty(required=True)
	presenter = db.StringProperty(required=True)

class MainPage(webapp.RequestHandler):
	uid
	def userTreatment(self, user):
		# TODO: Make this as a config file
		if user == "contato@leonardoamaral.com.br":
			self.admin = True
		else if db.GqlQuery("SELECT * FROM accesslist DESC LIMIT 1 WHERE user = :1", user)
	
	def get(self):
		user = users.get_current_user()

		if user:
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.out.write('Hello, ' + user.nickname())
		else:
			self.redirect(users.create_login_url(self.request.uri))

		self.response.out.write("""\
<html>
        <body>
                <form action="/upload" method="post">
                        <div><textarea name="content" rows="3" cols="60"></textarea></div>
                        <div><input type="submit" value="Sign Guestbook"></div>
                </form>
        </body>
</html>""")
