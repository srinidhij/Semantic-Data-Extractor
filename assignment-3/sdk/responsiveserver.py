#!/usr/bin/python
import time,cgi,string,threading
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import sdk

class ResponsiveServer(BaseHTTPRequestHandler):

	def do_GET(self):
		global useragent
		try:
			print self.path
			self.send_response(200)
			self.send_header('Content-Type','text/html')
			self.end_headers()
			#s = 'Your user agent %s'%self.headers['user-agent']
			s = genrespdata(self.headers['user-agent'])
			print s
			self.wfile.write(s)
		except error,msg:
			print 'Error : '+str(msg)+' occured'
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

def genrespdata(useragent):
	respstr = '<html><head><title>Responsive Server</title></head><body bgcolor="#eeeeee"><h1>Details of your device</h1><table border="1">'
	
	os = sdk.getOS(useragent)
	touch = sdk.isTouch(useragent)
	resolution = sdk.getDisplayResolution(useragent)
	g3 = sdk.is3G(useragent)
	wifi = sdk.isWifi(useragent)
	ram = sdk.getRAM(useragent)
	width = sdk.getDisplayWidth(useragent)
	height = sdk.getDisplayHeight(useragent)
	qwerty = sdk.isQwerty(useragent)
	camres = sdk.getPrimCamRes(useragent)

	respstr += '<tr><td>OS</td><td>'+str(os)+'</td></tr>'
	respstr += '<tr><td>Touch</td><td>'+str(touch)+'</td></tr>'
	respstr += '<tr><td>3G</td><td>'+str(g3)+'</td></tr>'
	respstr += '<tr><td>WIFI</td><td>'+str(wifi)+'</td></tr>'
	respstr += '<tr><td>RAM</td><td>'+str(ram)+'</td></tr>'
	respstr += '<tr><td>WIDTH</td><td>'+str(width)+'</td></tr>'
	respstr += '<tr><td>HEIGHT</td><td>'+str(height)+'</td></tr>'
	respstr += '<tr><td>QWERTY</td><td>'+str(qwerty)+'</td></tr>'
	respstr += '<tr><td>CAMERA RESOLUTION</td><td>'+str(camres)+'</td></tr>'

	respstr += '</table></body></html>'
	print respstr
	return respstr

def main():
	try:
		server = ThreadedHTTPServer(('localhost', 8888), ResponsiveServer)
		print 'started server ...'
		server.serve_forever()
	except KeyboardInterrupt:
		print '\nKeyboard interrupt. Bye'
	except:
		print 'Done bye'
		raise
if __name__ == '__main__':
	main()
