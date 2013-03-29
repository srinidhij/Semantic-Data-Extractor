#Clarification regarding UNknown and No
#REST should remove order of params
#exception at server?
#Should we add excep for INVALID and improper query
#***************************
#default values fo sim and cores
#many value are None
#LCD,LED
#Device Server Error
import sys
import httplib
import re
import urllib
import json

#Exception Classes

class DevModelError(Exception):
    
    def __init__(self,mod):
        self.name=mod
        
    def __str__(self):
        return "DEVICE Details OF" +repr(self.name)+"NOT FOUND"
    
class DevBrandError(Exception):
    
    def __init__(self,mod):
        self.name=mod
        
    def __str__(self):
        return "MANUFACTURER" + repr(self.name)+"NOT SUPPORTED"
    
class DevServerError(Exception):
    
    def __init__(self,mod):
        self.name=mod
        
    def __str__(self):
        return "ERROR ON THE SERVER " +repr(self.name)
    
class DevUnknownError(Exception):
    
    def __init__(self,mod,par):
        self.name=mod
        self.par
        
    def __str__(self):
        return "PAREMETER "+repr(self.par)+" OF "+repr(self.name)+" IS UNKNOWN"


#For building the query
def buildquery(userstring,lst):
    para=",".join(lst)
    dic=[]
    #userstring=userstring.replace(";","")
    dic.append(("ua",userstring))
    dic.append(("params",para))
    dic.append(("resp","json"))
    path="/usecase1/v2?"+urllib.urlencode(dic)
    conn = httplib.HTTPConnection("tantramsh-specs.rhcloud.com")
    print path
    req = conn.request("GET", path)
    res = conn.getresponse()
    return res.read()


#________________________________________________________________*** UMASHREE ***___________________________________________________________________

def isFM(userstring):
    dic=buildquery(userstring,["FM"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        if dic["FM"]:
			if dic["FM"]=="True":
				return True
			elif dic["FM"]=="False":
				return False
	else:
			raise RuntimeError("RunTimeError")

            
#should check
def isVideoSupported(userstring):
    dic=buildquery(userstring,["Video"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        if(dic["Video"]=="No"):
            return False
        else:
            return True

def getFPS(userstring):
    dic=buildquery(userstring,["fps"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        if(dic["fps"]!="No"):
            if(int(dic["fps"])>0):
                return int(dic["fps"])
            else:
                return 0
        else:
            return 0


        
def isMusicPlayer(userstring):
    dic=buildquery(userstring,["MusicPlayer"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        if dic["MusicPlayer"]:
			if dic["MusicPlayer"]=="True":
				return True
			elif dic["MusicPlayer"]=="False":
				return False
	else:
			raise RuntimeError("RunTimeError")

        
def isHDRecording(userstring):
    dic=buildquery(userstring,["HDRecording"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        if dic["HDRecording"]:
			if dic["HDRecording"]=="True":
				return True
			elif dic["HDRecording"]=="False":
				return False
	else:
			raise RuntimeError("RunTimeError")

def getHeight(userstring, st="mm"):
    dic=buildquery(userstring,["Height"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    if(st not in ("in","mm","cm")):
        raise RuntimeError("INVALID ARGUMENTS")     #doubt
    else:
        val=float(dic["Height"])
        if(st == "mm"):
            return val
        elif(st=="cm"):
            return float(val/10)
        else:
            return round(float(val/25.4),3)         #precision
 
           
def getWidth(userstring, st="mm"):
    dic=buildquery(userstring,["Width"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    if(st not in ("in","mm","cm")):
        raise RuntimeError("INVALID ARGUMENTS")     #doubt
    else:
        val=float(dic["Width"])
        if(st == "mm"):
            return val
        elif(st=="cm"):
            return float(val/10)
        else:
            return round(float(val/25.4),3)         #precision

def getThickness(userstring, st="mm"):
    dic=buildquery(userstring,["Thickness"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    if(st not in ("in","mm","cm")):
        raise RuntimeError("INVALID ARGUMENTS")     #doubt
    else:
        val=float(dic["Thickness"])
        if(st == "mm"):
            return val
        elif(st=="cm"):
            return float(val/10)
        else:
            return round(float(val/25.4),3)         #precision      

def getWeight(userstring):
    dic=buildquery(userstring,["Weight"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        val=float(dic["Weight"])
        return val     

def isUSB(userstring):
    dic=buildquery(userstring,["USB"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        raise RuntimeError("UNKNOWN")
    else:
        if dic["USB"]:
			if dic["USB"]=="True":
				return True
			elif dic["USB"]=="False":
				return False
	else:
			raise RuntimeError("RunTimeError")


def getSimNum(userstring):
    dic=buildquery(userstring,["SimNum"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        val=int(dic["SimNum"])
        return val     

def getNumCores(userstring):
    dic=buildquery(userstring,["Cores"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        val=int(dic["Cores"])
        return val     

def getFrequency(userstring):
    dic=buildquery(userstring,["Frequency"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        val=float(dic["Frequency"])
        return val     

def getDisplayResolution(userstring):
    wid=getDisplayWidth(userstring)
    hgt=getDisplayHeight(userstring)
    return (wid,hgt)

def getDisplayWidth(userstring):
    dic=buildquery(userstring,["DisplayWidth"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        val=float(dic["DisplayWidth"])
        return val     

def getDisplayHeight(userstring):
    dic=buildquery(userstring,["DisplayHeight"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        val=float(dic["DisplayHeight"])
        return val     

def isLCD(userstring):
    dic=buildquery(userstring,["ScreenType"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    #if there is a specific message from the server send it here
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        val=str(dic["ScreenType"])
        if( "LCD" in val.upper()):
            return True
        else:
            return False
    
#______________________________________________________________*** VINDHYA ***_________________________________________________________________

def getRAM(userstring):
	query=buildquery(userstring,["RAM"])
	print query
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["RAM"]:
			return float(dic["RAM"])*1024   #change it to *1024 once you get correct database
		else:
			raise RuntimeError("RunTimeError") #which exception suits?????????????//

def getInternalMemory(userstring):
	query=buildquery(userstring,["InternalMemory"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		else:		
			raise RuntimeError("RunTimeError")
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["InternalMemory"]:
			return dic["InternalMemory"]
		else:
			raise RuntimeError("RunTimeError")

def getSecondaryMemory(userstring):
	query=buildquery(userstring,["SecondaryMemory"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["SecondaryMemory"]:
			return float(dic["SecondaryMemory"])
		else:
			raise RuntimeError("RunTimeError")

def getTalkTime(userstring,tech="2G",unit="min"):
	if tech=="2G":
		query=buildquery(userstring,["2GTalkTime"])
	else:
		query=buildquery(userstring,["3GTalkTime"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["2GTalkTime"]:
			if unit=="min":
				return float(dic["2GTalkTime"])*60
			elif unit=="hr":
				return float(dic["2GTalkTime"])
			else:
				raise DevServerError("INVALID UNIT unit must be hr or min") 
		if dic["3GTalkTime"]:
			if unit=="min":
				return float(dic["3GTalkTime"])*60
			elif unit=="hr":
				return float(dic["3GTalkTime"])
			else:
				raise DevServerError("INVALID UNIT unit must be hr or min") 
		else:
			raise RuntimeError("RunTimeError")

def getStandbyTime(userstring,tech="2G",unit="hr"):
	if tech=="2G":
		query=buildquery(userstring,["2GStandbyTime"])
	else:
		query=buildquery(userstring,["3GStandbyTime"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["2GStandbyTime"]:
			if unit=="min":
				return float(dic["2GStandbyTime"])*60
			elif unit=="hr":
				return float(dic["2GStandbyTime"])
			else:
				raise DevServerError("INVALID UNIT unit must be hr or min") 
		if dic["3GStandbyTime"]:
			if unit=="min":
				return float(dic["3GStandbyTime"])*60
			elif unit=="hr":
				return float(dic["3GStandbyTime"])
			else:
				raise DevServerError("INVALID UNIT unit must be hr or min") 
		else:
			raise RuntimeError("RunTimeError")

def is2G(userstring):
	query=buildquery(userstring,["2G"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["2G"]:
			if dic["2G"]=="True":
				return True
			elif dic["2G"]=="False":
				return False
		else:
			raise RuntimeError("RunTimeError")

def is3G(userstring):
	query=buildquery(userstring,["3G"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["3G"]:
			if dic["3G"]=="True":
				return True
			elif dic["3G"]=="False":
				return False
		else:
			raise RuntimeError("RunTimeError")

def isHSDPA(userstring):  #hspa or hsdpa???????????????????//
	query=buildquery(userstring,["HSDPA"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["HSDPA"]:
			if dic["HSDPA"]=="True":
				return True
			elif dic["HSDPA"]=="False":
				return False
		else:
			raise RuntimeError("RunTimeError")

def isGSM(userstring):
	
	query=buildquery(userstring,["GSM"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["GSM"]:
			if dic["GSM"]=="True":
				return True
			elif dic["GSM"]=="False":
				return False
		else:
			raise RuntimeError("RunTimeError")

def isCDMA(userstring):
	
	query=buildquery(userstring,["CDMA"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["CDMA"]:
			if dic["CDMA"]=="True":
				return True
			elif dic["CDMA"]=="False":
				return False
		else:
			raise RuntimeError("RunTimeError")

def isGPRS(userstring):
	
	query=buildquery(userstring,["GPRS"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["GPRS"]:
			if dic["GPRS"]=="True":
				return True
			elif dic["GPRS"]=="False":
				return False
		else:
			raise RuntimeError("RunTimeError")

def isBluetooth(userstring):
	
	query=buildquery(userstring,["Bluetooth"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["Bluetooth"]:
			if dic["Bluetooth"]=="True":
				return True
			elif dic["Bluetooth"]=="False":
				return False
		else:
			raise RuntimeError("RunTimeError")

def isWifi(userstring):
	
	query=buildquery(userstring,["Wifi"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["Wifi"]:
			print dic["Wifi"]
			if dic["Wifi"]=="True":
				return True
			elif dic["Wifi"]=="False":
				return False
		else:
			raise RuntimeError("RunTimeError")

def getSensors(userstring):
	query=buildquery(userstring,["Sensors"])
	dic=eval(query)
	if dic.has_key("ERROR"):
		error=dic["ERROR"]
		if error=="BRAND NAME NOT FOUND":
			return None
		elif error=="MODEL NOT FOUND":
			return None
		elif error=="SERVER ERROR":
			raise DevServerError("SERVER ERROR")  #find out where server error is found
		
	if(dic["STATUS"]!="OK"):
		return None
	elif(dic["STATUS"]=="OK"):
		if dic["Sensors"]:
			return dic["Sensors"]

#_____________________________________________________________*** SNEHA ***__________________________________________________________________


def getOS(userstring):
    dic=buildquery(userstring,["OS"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")   
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        return (dic['OS'])



def isTouch(userstring):
    dic=buildquery(userstring,["Touch"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
           return None
        elif(err=="MODEL NOT FOUND"):
           return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        raise None
    else:
        return bool(dic['Touch'])

def isNormalKeypad(userstring):# doubt************************
    dic=buildquery(userstring,["Keypad"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")   
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        return "Normal"==dic['Keypad']




def isQwerty(userstring):
    dic=buildquery(userstring,["Keypad"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
           return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")  
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        return "Qwerty" == dic["Keypad"]
#
#
#
def isPrimCam(userstring):
    dic=buildquery(userstring,["PrimaryCamera"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")  
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]=="UNKNOWN"):
        return None#************ask if checking for resolution is ok********???same for secondary
    else:
        if(dic.has_key("PrimaryResolution") and dic["PrimaryResolution"]!="No"):
            return True
        else:
            return False


def isSecCam(userstring):
    dic=buildquery(userstring,["SecondaryCamera"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return none
        elif(err=="MODEL NOT FOUND"):
           return none
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")   
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]=="UNKNOWN"):
        return None#************ask if checking for resolution is ok********???same for secondary
    else:
        if(dic.has_key("SecondaryResolution") and dic["SecondaryResolution"]!="No"):
            return True
        else:
            return False



def getPrimCamRes(userstring):
    dic=buildquery(userstring,["PrimaryResolution"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")  
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        if(dic.has_key("PrimaryResolution") and dic["PrimaryResolution"]!="No"):  #returns no if camera doesn't exist
            return round(float(dic["PrimaryResolution"]),2)
        else:
            return None


def getSecCamRes(userstring):
    dic=buildquery(userstring,["SecondaryResolution"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
           return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic.has_key("SecondaryResolution") and dic["SecondaryResolution"]!="No"):  #returns no if camera doesn't exist
            return round(float(dic["SecondaryResolution"]),2)
    else:
            return None

def isSupportedPrimCamFeat(userstring,feature): # rerurns yes or no for a feature
    if(feature not in ["PrimaryFlash","PrimaryAutoFocus","PrimaryGeotagging","PrimaryFaceDetection"]):
        return None
    dic=buildquery(userstring,[feature])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
           return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")   
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        if(dic[feature]=="True"):
            return True
        else:
            return False


def isSupportedSecondaryCamFeat(userstring,feature): # rerurns yes or no for a feature
    if(feature not in ["SecondaryFlash"]):
        return None
    dic=buildquery(userstring,[feature])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
           return None
        elif(err=="MODEL NOT FOUND"):
           return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")   
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        if(dic[feature]=="True"):
            return True
        else:
            return False


def isAudioSupported(userstring,form):
    dic=buildquery(userstring,["AudioFormat"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
            return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")  
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        lst=[s.lower() for s in dic['AudioFormat']]
	if form.lower() in lst:
        	return True
	else:
		return False

def isVideoFileSupported(userstring,form):
    dic=buildquery(userstring,["VideoFormat"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
          return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        lst=[s.lower() for s in dic['VideoFormat']]
	if form.lower() in lst:
        	return True
	else:
		return False

def isPictureFileSupported(userstring,form):
    dic=buildquery(userstring,["PictureFile"])
    print dic
    dic=eval(dic)
    #dic=json.loads(dic)
    print "!!1!"
    if(dic.has_key("ERROR")):
        err=dic["ERROR"]
        if(err=="BRAND NAME NOT FOUND"):
          return None
        elif(err=="MODEL NOT FOUND"):
            return None
        elif(err=="SERVER ERROR"):
            raise DevServerError("SERVER ERROR")    
        else:
            raise RuntimeError("IMPROPER QUERY")
    if(dic["STATUS"]!="OK"):
        return None
    else:
        lst=[s.lower() for s in dic['PictureFile']]
	if form.lower() in lst:
        	return True
	else:
		return False


#____________________________________________________________*** CALLING ***________________________________________________________________

try:
   # print getWidth("Mozilla/5.0 (BlackBerry; U; BlackBerry 9860; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+")
   ##print getOS("LG-A133/V100 Obigo/WAP2.0 Profile/MIDP-2.1 Configuration/CLDC-1.1")
   ##print isFM("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isPictureFileSupported("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","jpg")
   ##print isVideoFileSupported("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","mp4")
   ##print getFPS("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isMusicPlayer("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isHDRecording("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getHeight("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getWidth("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getTalkTime("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isAudioSupported("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","mp3")
   ##print getPrimCamRes("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isSupportedPrimCamFeat("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","PrimaryGeotagging")
   ##print isPrimCam("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isSecCam("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isQwerty("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isWifi("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isBluetooth("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isUSB("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getSensors("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   # print isTouch("Mozilla/5.0 (Android 2.2; zh-cn; HTC Desire)/GoBrowser")
   # print isGPRS("Nokia5130/2.0 (07.97) Profile/MIDP-2.1 Configuration/CLDC-1.1")
   ##print isCDMA("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isGSM("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isHSDPA("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print is3G("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   # print getInternalMemory("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")#----------------------------------returns runtimeerror
   ##print getSecondaryMemory("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getRAM("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getFrequency("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getDisplayHeight("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getDisplayWidth("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isLCD("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getThickness("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getStandbyTime("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getWeight("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getSimNum("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getNumCores("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print isNormalKeypad("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   ##print getTalkTime("Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30")
   pass

except Exception,e:
    print e
