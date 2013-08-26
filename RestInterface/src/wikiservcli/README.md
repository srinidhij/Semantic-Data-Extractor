#Module wikiservcli 

##Module servf.py

Help on module servf:

NAME
    servf - #TCP server program

FILE
    wikiservcli/servf.py

FUNCTIONS
    adminMode(connSocket, addr)
        interactive menu generator for running 
        wikidb module
        
    guestMode(connSocket, addr)
        Serves for guests
    
    handle_child(childSocket, childAddr)
        Thread to handle tcp requests

    main()
        Runs the database server


##Module tcpclient.py

FUNCTIONS

    main()
        Main function to run tcp client
    
    parseargs()
        Parse command line args and 
        check them for correctness

    DATA
    AF_INET = 2
    SOCK_STREAM = 1
