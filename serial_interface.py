import serial
import sys

ports = ['/dev/ttyUSB', '/dev/ttyACM', '\\.\COM', '/dev/tty.usbmodem1234']
baud = 115200
ser = None

def open_port():
	global ser
	for port in ports:
		if ser:
			break
		for i in xrange(0, 64):
			try:
				target_port = port + str(i)
				ser = serial.Serial(target_port, baud, timeout=1)
				print(ser.name + ' is open ...' + '\r')
				break
				
			except:
				pass
	
	
while True:
	try:
		open_port()
		cmd = raw_input("Enter command or 'exit': ")
		if cmd == 'exit':
			ser.close()
			exit()
		else:
			ser.write(cmd.encode('ascii')+'\r')
			while True:
				out = ser.readline()
				print('>>'+out)
				if not out:
					break
	
	except serial.SerialException:
		print ("Monitor: Disconnected (Serial exception)")
	except IOError:
		print ("Monitor: Disconnected (I/O Error)")
	except KeyboardInterrupt:
		print ("Monitor: Keyboard Interrupt. Exiting Now...")
		sys.exit(1)	
