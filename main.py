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

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class PageTemplates():
    def header(self,title):
        return ("""\
<html>
    <head>
        <title>%s</title>
    </head>
    
    <body bgcolor="#F4FFE4">\
        """ % title)
    
    def tail(self):
        return ("""
    </body>
</html>\
        """)
    def table_head(self):
        return("""\
        <table cellspacing="0" width="1040" height="600">
            <tr id="slides">\
        """)
    
    def table_tail(self):
        return("""
            </tr>
        </table>""")
    
    def chat_iframe(self):
        return ("""
                <td id="slide" bgcolor="f4ffff">
                    <iframe src="http://webchat.freenode.net?nick=EvidosolOuvinte.&channels=evidosol-secretaria%2Cevidosol-1%2Cevidosol-2%2Cevidosol-3%2Cevidosol-4&uio=OT10cnVlJjEwPXRydWUmMTE9MTIze7" width="550" height="600">
                    </iframe>
                </td>""")

    def slide_iframe(self):
        # TODO: Implement this with a native way
        return("""
                <td id="slide" bgcolor="f4ffff">
                    <iframe src="http://portugueslivre.org/chatslide/slide.php" width="550" height="600">
                    </iframe>
                </td>""")
    
class MainPage(webapp.RequestHandler):
    StartPage = PageTemplates()
    def get(self):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.headers['Cache-Control'] = 'no-cache'
        self.response.headers['Pragma'] = 'no-cache'
        self.response.out.write(self.StartPage.header('Página Principal ChatSlide'))
        self.response.out.write("""
        <img src="http://portugueslivre.org/TextoLivre.png" alt="textolivre"/>
        <h4>VII EVIDOSOL e IV CILTEC Online</h4>
""")
        self.response.out.write(self.StartPage.table_head())
        self.response.out.write(self.StartPage.chat_iframe())
        self.response.out.write(self.StartPage.slide_iframe())
        self.response.out.write(self.StartPage.table_tail())
        self.response.out.write(self.StartPage.tail())

application = webapp.WSGIApplication(
                                    [('/', MainPage)],debug=False)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
