#!/usr/bin/python
import time,cgi,string,threading
from os import curdir,sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from mongoDB import QueryDB
import datetime
import sys


if len(sys.argv) == 2:
    try:
        port = int(sys.argv[1])
    except : 
        print 'Error : port number has to be an integer'
        sys.exit(1)
else :
    port = 8888

class WikiServer(BaseHTTPRequestHandler):
    '''Class for handling requests for the wiki people database'''

    def do_GET(self):
        ''' Perform `GET` request '''
        try:
            if self.path == "/":
                self.path = "index.html"
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
        ''' Perform `POST` request'''
        form = cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type'],})
        #print str(dict(form))
        Q = QueryDB()
        data = Q.processQuery(form)
        self.send_response(200)
        self.send_header('Content-Type','text/html')
        self.end_headers()
        self.wfile.write(data)
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
            fname = "../../logs/log"+str(datetime.date.today())+".txt"
            f = open(fname,"a")
            self.finish_request(request, client_address)
            f.write(str(self.server_address)+'\n')
            self.shutdown_request(request)
            f.close()
        except Exception as e:
            fname = "../../logs/log"+str(datetime.date.today())+".txt"
            f = open(fname,"a")
            f.write('Error occured'+str(e))
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
            server = ThreadedHTTPServer(('localhost', port), WikiServer)
            print 'started server ...'
            server.serve_forever()
        except KeyboardInterrupt :
            print '\n Ctrl-C -- Stopping server ...\nDone bye'
        except Exception as e :
            print 'Error ' + str(e) + ' occurred.\n Stopping server ...\n c'

if __name__ == '__main__':
        main()
