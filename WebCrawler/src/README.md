#Usage 

First build the database:

    $python transfer.py

Start the server

    $python wikihttp.py 8888


#Module wikihttpserver

##Name
###wikihttpserver.wikihttp

###CLASSES
        BaseHTTPServer.BaseHTTPRequestHandler(SocketServer.StreamRequestHandler)
            WikiServer
        ThreadingMixIn
            ThreadedHTTPServer(ThreadingMixIn, BaseHTTPServer.HTTPServer)
        
        class ThreadedHTTPServer(ThreadingMixIn, BaseHTTPServer.HTTPServer)
         |  Handle requests in a separate thread.
         |  
         |  Method resolution order:
         |      ThreadedHTTPServer
         |      ThreadingMixIn
         |      BaseHTTPServer.HTTPServer
         |      SocketServer.TCPServer
         |      SocketServer.BaseServer
         |  
         |  Methods inherited from ThreadingMixIn:
         |  
         |  process_request(self, request, client_address)
         |      Start a new thread to process the request.
         |  
         |  process_request_thread(self, request, client_address)
         |      Same as in BaseServer but as a thread.
         |      
         |      In addition, exception handling is done here.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from ThreadingMixIn:
         |  
         |  daemon_threads = True
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from BaseHTTPServer.HTTPServer:
         |  
         |  server_bind(self)
         |      Override server_bind to store the server name.
         |  
         |      Override server_bind to store the server name.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from BaseHTTPServer.HTTPServer:
         |  
         |  allow_reuse_address = 1
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from SocketServer.TCPServer:
         |  
         |  __init__(self, server_address, RequestHandlerClass, bind_and_activate=True)
         |      Constructor.  May be extended, do not override.
         |  
         |  close_request(self, request)
         |      Called to clean up an individual request.
         |  
         |  fileno(self)
         |      Return socket file number.
         |      
         |      Interface required by select().
         |  
         |  get_request(self)
         |      Get the request and client address from the socket.
         |      
         |      May be overridden.
         |  
         |  server_activate(self)
         |      Called by constructor to activate the server.
         |      
         |      May be overridden.
         |  
         |  server_close(self)
         |      Called to clean-up the server.
         |      
         |      May be overridden.
         |  
         |  shutdown_request(self, request)
         |      Called to shutdown and close an individual request.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from SocketServer.TCPServer:
         |  
         |  address_family = 2
         |  
         |  request_queue_size = 5
         |  
         |  socket_type = 1
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from SocketServer.BaseServer:
         |  
         |  finish_request(self, request, client_address)
         |      Finish one request by instantiating RequestHandlerClass.
         |  
         |  handle_error(self, request, client_address)
         |      Handle an error gracefully.  May be overridden.
         |      
         |      The default is to print a traceback and continue.
         |  
         |  handle_request(self)
         |      Handle one request, possibly blocking.
         |      
         |      Respects self.timeout.
         |  
         |  handle_timeout(self)
         |      Called if no new request arrives within self.timeout.
         |      
         |      Overridden by ForkingMixIn.
         |  
         |  serve_forever(self, poll_interval=0.5)
         |      Handle one request at a time until shutdown.
         |      
         |      Polls for shutdown every poll_interval seconds. Ignores
         |      self.timeout. If you need to do periodic tasks, do them in
         |      another thread.
         |  
         |  shutdown(self)
         |      Stops the serve_forever loop.
         |      
         |      Blocks until the loop has finished. This must be called while
         |      serve_forever() is running in another thread, or it will
         |      deadlock.
         |  
         |  verify_request(self, request, client_address)
         |      Verify the request.  May be overridden.
         |      
         |      Return True if we should proceed with this request.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from SocketServer.BaseServer:
         |  
         |  timeout = None
        
        class ThreadingMixIn
         |  Mix-in class to handle each request in a new thread.
         |  
         |  Methods defined here:
         |  
         |  process_request(self, request, client_address)
         |      Start a new thread to process the request.
         |  
         |  process_request_thread(self, request, client_address)
         |      Same as in BaseServer but as a thread.
         |      
         |      In addition, exception handling is done here.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  daemon_threads = True
        
        class WikiServer(BaseHTTPServer.BaseHTTPRequestHandler)
         |  Class for handling requests for the wiki people database
         |  
         |  Method resolution order:
         |      WikiServer
         |      BaseHTTPServer.BaseHTTPRequestHandler
         |      SocketServer.StreamRequestHandler
         |      SocketServer.BaseRequestHandler
         |  
         |  Methods defined here:
         |  
         |  do_GET(self)
         |      Perform `GET` request
         |  
         |  do_POST(self)
         |      Perform `POST` request
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from BaseHTTPServer.BaseHTTPRequestHandler:
         |  address_string(self)
         |      Return the client address formatted for logging.
         |      
         |      This version looks up the full hostname using gethostbyaddr(),
         |      and tries to find a name that contains at least one dot.
         |  
         |  date_time_string(self, timestamp=None)
         |      Return the current date and time formatted for a message header.
         |  
         |  end_headers(self)
         |      Send the blank line ending the MIME headers.
         |  
         |  handle(self)
         |      Handle multiple requests if necessary.
         |  
         |  handle_one_request(self)
         |      Handle a single HTTP request.
         |      
         |      You normally don't need to override this method; see the class
         |      __doc__ string for information on how to handle specific HTTP
         |      commands such as GET and POST.
         |  
         |  log_date_time_string(self)
         |      Return the current time formatted for logging.
         |  
         |  log_error(self, format, *args)
         |      Log an error.
         |      
         |      This is called when a request cannot be fulfilled.  By
         |      default it passes the message on to log_message().
         |      
         |      Arguments are the same as for log_message().
         |      
         |      XXX This should go to the separate error log.
         |  
         |  log_message(self, format, *args)
         |      Log an arbitrary message.
         |      
         |      This is used by all other logging functions.  Override
         |      it if you have specific logging wishes.
         |      
         |      The first argument, FORMAT, is a format string for the
         |      message to be logged.  If the format string contains
         |      any % escapes requiring parameters, they should be
         |      specified as subsequent arguments (it's just like
         |      printf!).
         |      
         |      The client host and current date/time are prefixed to
         |      every message.
         |  
         |  log_request(self, code='-', size='-')
         |      Log an accepted request.
         |      
         |      This is called by send_response().
         |  
         |  parse_request(self)
         |      Parse a request (internal).
         |      
         |      The request should be stored in self.raw_requestline; the results
         |      are in self.command, self.path, self.request_version and
         |      self.headers.
         |      
         |      Return True for success, False for failure; on failure, an
         |      error is sent back.
         |  
         |  send_error(self, code, message=None)
         |      Send and log an error reply.
         |      
         |      Arguments are the error code, and a detailed message.
         |      The detailed message defaults to the short entry matching the
         |      response code.
         |      
         |      This sends an error response (so it must be called before any
         |      output has been generated), logs the error, and finally sends
         |      a piece of HTML explaining the error to the user.
         |  
         |  send_header(self, keyword, value)
         |      Send a MIME header.
         |  
         |  send_response(self, code, message=None)
         |      Send the response header and log the response code.
         |      
         |      Also send two standard headers with the server software
         |      version and the current date.
         |  
         |  version_string(self)
         |      Return the server software version string.
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from BaseHTTPServer.BaseHTTPRequestHandler:
         |  
         |  MessageClass = <class mimetools.Message>
         |  
         |  default_request_version = 'HTTP/0.9'
         |  
         |  error_content_type = 'text/html'
         |  
         |  error_message_format = '<head>\n<title>Error response</title>\n</head>...
         |  
         |  monthname = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'A...
         |  
         |  protocol_version = 'HTTP/1.0'
         |  
         |  responses = {100: ('Continue', 'Request received, please continue'), 1...
         |  
         |  server_version = 'BaseHTTP/0.3'
         |  
         |  sys_version = 'Python/2.7.2'
         |  
         |  weekdayname = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from SocketServer.StreamRequestHandler:
         |  
         |  finish(self)
         |  
         |  setup(self)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes inherited from SocketServer.StreamRequestHandler:
         |  
         |  disable_nagle_algorithm = False
         |  
         |  rbufsize = -1
         |  
         |  timeout = None
         |  
         |  wbufsize = 0
         |  
         |  ----------------------------------------------------------------------
         |  Methods inherited from SocketServer.BaseRequestHandler:
         |  
         |  __init__(self, request, client_address, server)

###FUNCTIONS
        main()
        Runs the module by initializing a server.

###DATA
        curdir = '.'
        port = 8888
        sep = '/'

##Name
###wikihttpserver.crawler

###CLASSES
        Crawler
        
        class Crawler
         |  Class for crawling and screen-scraping from 
         |  the list of sites specified in a file
         |  
         |  Methods defined here:
         |  
         |  __init__(self, ipfile='tocrawl.txt', opfile='output')
         |  
         |  main(self)
         |      Main method to crawl data from the sites specified


##NAME
    wikihttpserver.parsehtml

###CLASSES
        HTMLParser
        
        class HTMLParser
         |  Class for parsing html from 
         |  wikipedia
         |  
         |  Methods defined here:
         |  
         |  __init__(self, html=None)
         |      Initialize the HTMLParser by creating a
         |      BeautifulSoup object and Initialize the 
         |      table which contains the data to be 
         |      parsed
         |  
         |  convert(self, data)
         |      Convert the non-ascii strings into
         |      ascii by removing non-ascii characters
         |  
         |  parse(self, category)
         |      Parse the actual table by pulling out 
         |      the data from rows abd columns.Stores the 
         |      collected data in a list of dictionaries
         |  
         |  performcleanup(self, data)
         |      Remove unwanted data present in the html 
         |      like citations and references

###FUNCTIONS
        main()
            Simulate working of the HTMLParser

##Name
###wikihttpserver.colldata

###CLASSES
        BuildDB
        
        class BuildDB
         |  Class to build the database from the 
         |  data parsed by the parser
         |  
         |  Methods defined here:
         |  
         |  __init__(self)
         |  
         |  build(self)
         |      Gets the data from the crawler and uses 
         |      parser to parse the data and returns the data

###FUNCTIONS
        getData()
            return data got from the parser
##Name
###wikihttpserver.transfer

###CLASSES
        CreateDB
        
        class CreateDB
         |  Class to create the database from the 
         |  data obtained by parser
         |  
         |  Methods defined here:
         |  
         |  create(self)
         |      Create a mongo client and get the data from parser
         |      and insert the data into the database

###FUNCTIONS
        main()

###DATA
        ALL = 2
        ASCENDING = 1
        DESCENDING = -1
        GEO2D = '2d'
        GEOHAYSTACK = 'geoHaystack'
        GEOSPHERE = '2dsphere'
        HASHED = 'hashed'
        OFF = 0
        SLOW_ONLY = 1
        version = '2.5'
        version_tuple = (2, 5)


##Name
###wikihttpserver.mongoDB


###CLASSES
        QueryDB
        
        class QueryDB
         |  Methods defined here:
         |  
         |  processQuery(self, form)
         |      Parse the query recieved from the html
         |      and process it. This converts the query entered by 
         |      the user in html to corressponding mongoDB queries, 
         |      executes the query and converts the result into 
         |      html for passing onto the client

###FUNCTIONS
        errorMongoDB(e)
            handle execption(s) occurred during processing 
            of the query
        
        time(...)
            time() -> floating point number
            
            Return the current time in seconds since the Epoch.
            Fractions of a second may be present if the system clock provides them.

###DATA
        ALL = 2
        ASCENDING = 1
        DESCENDING = -1
        GEO2D = '2d'
        GEOHAYSTACK = 'geoHaystack'
        GEOSPHERE = '2dsphere'
        HASHED = 'hashed'
        OFF = 0
        SLOW_ONLY = 1
        version = '2.5'
        version_tuple = (2, 5)
