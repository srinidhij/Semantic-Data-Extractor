#!/usr/bin/python
import time,cgi,string,threading
from os import curdir,sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class WikiServer(BaseHTTPRequestHandler):

	def do_GET(self):
		try:
			print self.path
			if self.path == '/':
				self.path = 'index.html'
			f = open(curdir+sep+self.path)
			self.send_response(200)
			self.send_header('Content-Type','text/html')
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
		except:
			pass
		return
		
	def do_POST(self):
		form = cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],})
		self.send_response(200)
		self.end_headers()
		self.wfile.write('Client: %s\n' % str(self.client_address))
		self.wfile.write('User-agent: %s\n' % str(self.headers['user-agent']))
		self.wfile.write('Path: %s\n' % self.path)
		self.wfile.write('Form data:\n')

		# Echo back information about what was posted in the form
		for field in form.keys():
		    field_item = form[field]
		    if field_item.filename:
		        # The field contains an uploaded file
		        file_data = field_item.file.read()
		        file_len = len(file_data)
		        del file_data
		        self.wfile.write('\tUploaded %s as "%s" (%d bytes)\n' % \
		                (field, field_item.filename, file_len))
		    else:
		        # Regular form value
		        self.wfile.write('\t%s=%s\n' % (field, form[field].value))
		return

class ThreadingMixIn:
    """Mix-in class to handle each request in a new thread."""

    # Decides how threads will act upon termination of the
    # main process
    daemon_threads = True

    def process_request_thread(self, request, client_address):
        """Same as in BaseServer but as a thread.

        In addition, exception handling is done here.

        """
        try:
            self.finish_request(request, client_address)
            self.shutdown_request(request)
        except:
            self.handle_error(request, client_address)
            self.shutdown_request(request)

    def process_request(self, request, client_address):
        """Start a new thread to process the request."""
        t = threading.Thread(target = self.process_request_thread,
                             args = (request, client_address))
        t.daemon = self.daemon_threads
        t.start()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    pass

def main():
	try:
		server = ThreadedHTTPServer(('localhost', 8888), WikiServer)
		print 'started server ...'
		server.serve_forever()
	except KeyboardInterrupt:
		print '\nKeyboard interrupt. Bye'
	except:
		print 'Done bye'
if __name__ == '__main__':
	main()
