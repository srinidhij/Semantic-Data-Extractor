import webapp2
import sdk
import jinja2
import os

class MainPage(webapp2.RequestHandler):
  def get(self):
		  val=self.request.headers['User-Agent']
		  jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))
		  ret=sdk.isTouch(val)
		  self.response.headers['Content-Type'] = 'text/html'
		  #ret=None
		  if(ret==True):
			template_values = {
		  
			}

			template = jinja_environment.get_template("index.html")
			self.response.out.write(template.render(template_values))
		  else:
			template_values = {
		  
			}

			template = jinja_environment.get_template("simp.html")
			self.response.out.write(template.render(template_values))
		  
		  #self.response.write(val)
	
		  
		  

app = webapp2.WSGIApplication([('/', MainPage)],debug=True)