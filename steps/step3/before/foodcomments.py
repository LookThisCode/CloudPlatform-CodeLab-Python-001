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

#alimento_predeterminado = 'alimento_predeterminado'


#class Comentario(ndb.Model):



#class Home(webapp2.RequestHandler):
#    def get(self):

        #Manejando la sesion del usuario
#        if users.get_current_user():
#            url = users.create_logout_url(self.request.uri)
#            url_linktext = 'Logout'
#        else:
#            url = users.create_login_url(self.request.uri)
#            url_linktext = 'Login'
        
       # parametros_ingreso = urllib.urlencode({'consulta_comentario': consulta_comentario})
       # self.response.write(pagina %
       #                     (parametros_ingreso, cgi.escape(consulta_comentario),
       #                      url,
       #                      url_linktext))

"""
Funcionalidad que maneja los comentarios de la solucion
1-Obtenemos el usuario actual si esta autenticado
2-Mostramos el contenido utilizado en el formulario web
"""
#class Comentarios(webapp2.RequestHandler):
#        def post(self):
                                    
        
       #     parametro_alimento = {'consulta_alimento': consulta_comentario}
       #     self.redirect('/?' + urllib.urlencode(parametro_alimento))
        
#application = webapp2.WSGIApplication([
#    ('/', Home),
#    ('/comentarios', Comentarios),
#], debug=True)