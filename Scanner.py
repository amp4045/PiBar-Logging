from datetime import datetime
now = datetime.now(); #this will be used to print out the timestamp of each scan
import os #this will be used to shut down the device, when the termination value is scanned

#this is the idNumber or barcode number on whatever you're scanning
global idNumber
idNumber = raw_imput(' ')

#the "777777777" can be anything that you know will NEVER be scanned, if you'd like to use a string, just cast it
while idNumber != 777777777:
	if idNUmber == 'terminate' #this will look for a termination value to turn off the Raspberry Pi 
		os.system('Shutdown now -h') #when termination is scanned, this shuts down the pi, immediately..the -h takes care of that for us
	appendFile = open('/media/usbName', 'a')  #make sure you change this line to the exact name of your flash drive
	appendFile.write(str(idNumber) + str(' ') + str(now) + '\n')
	appendFile.close()
	idNumber = raw_input(' ')