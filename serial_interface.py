import serial

port = '/dev/ttyUSB2'
baud = 115200

ser = serial.Serial(port, baud, timeout=1)

if ser.isOpen():
	print(ser.name+' is open ...')
	
while True:
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