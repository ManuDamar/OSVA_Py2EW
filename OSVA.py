import logging, PyEW
import time as tm
import numpy as np
import serial
import struct
import time

PuertoSerie = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(1)

logging.getLogger().addHandler(logging.StreamHandler())
MyModule = PyEW.EWModule(1001, 168, 255, 30.0, False)
MyModule.add_ring(1001)
wave = MyModule.get_wave(0) 
MyModule.add_ring(1004)


while True :#PuertoSerie.inWaiting():

	s1 = PuertoSerie.read(2)
	s2 = PuertoSerie.read(1)
	
	
	td = np.array([s1,s2])
	
	td0 = td
	
	mywave =  {
	'station': 'OSVA-T',
	'network': 'UV',
	'channel': 'LK',
	'location': '01',
	'nsamp': 100,
	'samprate': 1,
	'startt': tm.mktime(tm.gmtime()),
	'datatype': 'i2',
    'data': td
	}
	
	MyModule.put_wave(1, mywave)
	#print (mywave)
	print (td)
	
	time.sleep(1)
	pass

