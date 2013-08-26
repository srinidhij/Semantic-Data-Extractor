#!/usr/bin/python
import sys
from socket import socket,AF_INET,SOCK_STREAM
from argparse import ArgumentParser

def parseargs():
	'''Parse command line args and 
	check them for correctness'''
	parser = ArgumentParser()
	parser.add_argument('-c',metavar='host',help='host name on which server runs')
	parser.add_argument('-p',metavar='port',help='port on which server runs')
	args = parser.parse_args()
	if not args.c or not args.p :
	    print 'Error : Invalid command line args'
	    print '''usage: servf.py [-h] [-c host] [-p port]

	optional arguments:
	-h, --help  show this help message and exit
	-c host     host name on which server runs
	-p port     port on which server runs
	    '''
	    sys.exit(1)
	serverName = args.c
	try:
	    serverPort = int(args.p)
	except:
	    print 'Error : Port number has to be an integer'
	    sys.exit(1)
	return (serverName,serverPort)    

def main():
	'''Main function to run tcp client'''
	adminCount = 0
	flag = True
	try :
		clientSocket = socket(AF_INET, SOCK_STREAM)
		clientSocket.connect(parseargs())
	except:
		print 'Error : Unable to create socket'
		sys.exit(1)
	while flag:
		try:
			message = clientSocket.recv(1048576)
			if not not message:
				if 'Enter' in message:
					sendMsg = raw_input(message)
					clientSocket.send(sendMsg)
				elif message=='Exiting':
					print 'Done'
					flag = False
					break
				else:
					print message
					continue
			else:
				break
		except:
			print 'Error occured'
			break
	clientSocket.close()

if __name__ == "__main__":
	main()