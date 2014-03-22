'''
Created on Mar 18, 2014

@author: nickbortolotti
'''
from google.appengine.api import users

import webapp2
import cgi

pagina = """\
<html>
  <body>
    <form action="/comentarios" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Registrar Comentario"></div>
    </form>
  </body>
</html> """

class FoodTestHelloWorld(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user() 
        if usuario:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Welcome to FoodComments:, ' + usuario.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

#class Home(webapp2.RequestHandler):
#    def get(self):
        
#class Comentarios(webapp2.RequestHandler):
#    def post(self):

application = webapp2.WSGIApplication([
    ('/', FoodTestHelloWorld),
], debug=True)