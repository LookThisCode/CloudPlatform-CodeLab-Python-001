'''
Created on Mar 18, 2014
@author: nickbortolotti
'''
import webapp2

class FoodTestHelloWorld(webapp2.RequestHandler):
    def get(self):
        self.response.write('Welcome to FoodComments')
        