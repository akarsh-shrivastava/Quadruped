# yeah, its the same as rMinus but I couldn't
# find the code so i wrote this again
# it would have taken me more time to find it


import pypot.dynamixel
from time import sleep

# positive angle - anticlockwise rotation

class Dynamixel:
	def __init__(self):
		ports=pypot.dynamixel.get_available_ports()
		if not ports :
			raise IOError("No ports found")

		print "Connecting to ",ports[0]
		self.dxl=pypot.dynamixel.DxlIO(ports[0])
		self.ids=self.dxl.scan(range(25))
		print self.ids

		self.set_speed(500)

	def initial_position(self):
		self.set_position( [0]*12 )

	def set_speed(self,speed):
		speeds=[speed]
		speeds=speeds*len(self.ids)
		speed_dict=dict(zip(self.ids,speeds))
		self.dxl.set_moving_speed(speed_dict)

	def set_position(self,positions):
		position_dict=dict(zip(self.ids,positions))
		self.set_speed(70)
		self.dxl.set_goal_position(position_dict)
