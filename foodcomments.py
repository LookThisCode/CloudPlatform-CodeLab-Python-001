'''
Created on Mar 18, 2014

@author: nickbortolotti
'''

from google.appengine.api import users
from google.appengine.ext import ndb   

import webapp2
import urllib
import jinja2
import os

plantilla_alimentos = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'],autoescape=True)

alimento_predeterminado = '1'

def comentario_key(consulta_comentario=alimento_predeterminado):
    return ndb.Key('Comentario',consulta_comentario)

class Comentario(ndb.Model):
    autor = ndb.UserProperty()
    contenido = ndb.StringProperty(indexed=False)
    fecha = ndb.DateTimeProperty(auto_now_add=True) 

class Home(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><body>')
        consulta_comentario = self.request.get('consulta_comentario', alimento_predeterminado)
        
        consulta_comentarios = Comentario.query(ancestor=comentario_key(consulta_comentario)).order(-Comentario.fecha)
        comentarios = consulta_comentarios.fetch(10)
        
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        
        valores_plantilla_alimentos = {
                                   'comentarios' : comentarios,
                                   'consulta_comentario' : urllib.quote_plus(consulta_comentario),
                                   'url' : url, 
                                   'url_linktext' : url_linktext,                            
        }
        
        plantilla = plantilla_alimentos.get_template('index.html')
        self.response.write(plantilla.render(valores_plantilla_alimentos))

class Comentarios(webapp2.RequestHandler):
        def post(self):
            consulta_comentario = self.request.get('consulta_comentario',alimento_predeterminado)
        
            c = Comentario(parent=comentario_key(consulta_comentario))
        
            if users.get_current_user():                
                c.autor = users.get_current_user()       
                                                        
                c.contenido = self.request.get('content')   
                c.put()                                     
        
            parametro_alimento = {'consulta_comentario': consulta_comentario}
            self.redirect('/?' + urllib.urlencode(parametro_alimento))
        
application = webapp2.WSGIApplication([
    ('/', Home),
    ('/comentarios', Comentarios),
], debug=True)