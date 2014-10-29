import os
import webapp2
import jinja2
from google.appengine.api import mail
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("index.html")
        #aqui se renderiza el index
        self.response.write(template.render())

class secondHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("404.html")
        #aqui se renderiza el index
        self.response.write(template.render())

app = webapp2.WSGIApplication([
                                  ('/', MainHandler),
                                  ('/404.html', secondHandler),
                              ], debug=True)
