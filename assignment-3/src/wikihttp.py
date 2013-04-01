import time,cgi,string,threading
from os import curdir,sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from mongoDB import QueryDB
import datetime

class WikiServer(BaseHTTPRequestHandler):

        def do_GET(self):
                try:
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
            fname = "../logs/log"+str(datetime.date.today())+".txt"
            f = open(fname,"a")
            self.finish_request(request, client_address)
            f.write(str(self.server_address)+'\n')
            self.shutdown_request(request)
            f.close()
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
        except:
                print 'Done bye'
                raise
if __name__ == '__main__':
        main()