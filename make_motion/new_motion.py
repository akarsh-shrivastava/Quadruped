from math import sqrt,atan,acos,degrees,pi,asin,sin,tan,cos
import pypot.dynamixel
from time import sleep


NO_OF_MOTORS=12		# change this for different bots

def init():
	ports=pypot.dynamixel.get_available_ports()
	if not ports :
		raise IOError("No ports found")

	print "Connecting to ",ports[0]

	global dxl
	dxl=pypot.dynamixel.DxlIO(ports[0])
	ids=dxl.scan(range(25))
	dxl.set_moving_speed(dict(zip(range(1,NO_OF_MOTORS+1),[70]*NO_OF_MOTORS)))
	print ids

	raw_input()



if __name__=='__main__':

	init()

	motion_file=open("motion.txt",'a')

	
	while True:
		try:
			angles=raw_input('Enter angles:')
			anglesl=angles.split()
			if not len(anglesl)==NO_OF_MOTORS:
				print "incorrect number of values"
				continue
		except KeyboardInterrupt:
			print 'stopped'
			break

		try:
			ang_dict=dict(zip(range(1,NO_OF_MOTORS+1),anglesl))
			dxl.set_goal_position(ang_dict)
		except Exception as e:
			print e
			continue

		dec=raw_input('Enter in file? (y/n) : ')
		if(dec=='y'):
			motion_file.write(angles+'\n')

	
	motion_file.close()
	print "closed"



