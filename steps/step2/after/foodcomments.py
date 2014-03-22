"""
Created on Mar 18, 2014

@author: nickbortolotti
"""

from google.appengine.api import users

import webapp2
import cgi

pagina = """\
<html>
  <body>
    <form action="/comentarios" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Comentar"></div>
    </form>
  </body>
</html> """


"""
class description: this class loads an HTML template page.
descripcion de la clase: esta clase carga una plantilla de pagina HTML
"""
class Home(webapp2.RequestHandler):
    def get(self):
        self.response.write(pagina) 

"""
class description:This class gets the authenticated user, then displays the content of the comment concatenated with the user who made it.
descripcion de la clase:esta clase obtiene el usuario autenticado, luego muestra el contenido del comentario concatenado con el usuario que lo realiz—.
"""
class Comentarios(webapp2.RequestHandler):
    def post(self):
        usuario = users.get_current_user()
        if usuario:
            self.response.write('<html><body>' + usuario.nickname() + ' :') 
            self.response.write(cgi.escape(self.request.get('content'))) 
            self.response.write('</body></html>')
        else:
            self.redirect(users.create_login_url(self.request.uri))

        
application = webapp2.WSGIApplication([
    ('/', Home),
    ('/comentarios', Comentarios),
], debug=True)