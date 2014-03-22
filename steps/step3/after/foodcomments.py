'''
Created on Mar 18, 2014

@author: nickbortolotti
'''

from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2
import cgi
import urllib

pagina = """\
<html>
  <body>
    <img src="/images/cap_1.jpg" alt="food" width="100" height="100">
    <form action="/comentarios?%s" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Comentar"></div>
    </form>
    
    <hr>
    
    <form>Seleccionar Alimento:
      <input value="%s" name="consulta_comentario">
      <input type="submit" value="cambiar">
    </form>

    <a href="%s">%s</a>
    
  </body>
</html> """

alimento_predeterminado = 'alimento_predeterminado'

def comentario_key(consulta_comentario=alimento_predeterminado):
    return ndb.Key('Comentario',consulta_comentario)

"""
class descripcion:this class allows representing the model to handle persistence.
-
descripcion de la clase: esta clase permite representar el modelo para manejar la persistencia.
"""
class Comentario(ndb.Model):
    autor = ndb.UserProperty()
    contenido = ndb.StringProperty(indexed=False)
    fecha = ndb.DateTimeProperty(auto_now_add=True) 

"""
class description:
descripci—n de la clase: This class provides an object comments on food, 
manage the user's session 
select foods to comment.
-
descripcion de la clase: esta clase permite obtener los comentarios sobre un objeto alimento, 
manejar la sesi—n del usuario
seleccionar alimentos para comentar.
"""
class Home(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><body>')
        consulta_comentario = self.request.get('consulta_comentario', alimento_predeterminado)
        
        consulta_comentarios = Comentario.query(ancestor=comentario_key(consulta_comentario)).order(-Comentario.fecha)
        comentarios = consulta_comentarios.fetch(10)
        
        for c in comentarios: 
            if c.autor:
                self.response.write('<b>%s</b> ha comentado :' % c.autor.nickname()) 
            else:
                self.response.write('El comentario fue enviada por una persona anonima') 
            self.response.write('<blockquote>%s</blockquote>' % 
                                cgi.escape(c.contenido))
        
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        
        parametros_ingreso = urllib.urlencode({'consulta_comentario': consulta_comentario})
        self.response.write(pagina %
                            (parametros_ingreso, cgi.escape(consulta_comentario),
                             url,
                             url_linktext))

"""
class description:This class allows comments persist about food.
-
descripcion de la clase: esta clase permite persistir los comentarios sobre los alimentos.
"""
class Comentarios(webapp2.RequestHandler):
        def post(self):
            consulta_comentario = self.request.get('consulta_comentario',alimento_predeterminado)
        
            c = Comentario(parent=comentario_key(consulta_comentario))
        
            if users.get_current_user():                
                c.autor = users.get_current_user()       
                                                        
                c.contenido = self.request.get('content')   
                c.put()                                     
        
            parametro_alimento = {'consulta_alimento': consulta_comentario}
            self.redirect('/?' + urllib.urlencode(parametro_alimento))
        
application = webapp2.WSGIApplication([
    ('/', Home),
    ('/comentarios', Comentarios),
], debug=True)