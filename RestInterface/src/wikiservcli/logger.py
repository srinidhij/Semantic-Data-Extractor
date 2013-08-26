#!/usr/bin/python
from datetime import datetime
class Logger:
	'''Class for logging server requests'''
	
	def __init__(self,fname='server.log'):
		self.logfile = open(fname,'a')

	def write(self,time,msg):
		ctim = datetime.ctime(time)
		self.logfile.write(ctim+' : '+msg+'\n')

	def close(self):
		self.logfile.close()