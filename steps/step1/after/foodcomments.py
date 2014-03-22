'''
Created on Mar 18, 2014
@author: nickbortolotti
'''

from google.appengine.api import users
import webapp2

"""
class description:This class gets the authenticated user, then generates a welcome message.
descripcion de la class: Esta clase obtiene el usuario autenticado, luego genera un mensaje de bienvenida
"""            
class FoodTestHelloWorld(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user() 
        if usuario:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Welcome to FoodComments:, ' + usuario.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))
                   
application = webapp2.WSGIApplication([
    ('/',FoodTestHelloWorld),
], debug=True)