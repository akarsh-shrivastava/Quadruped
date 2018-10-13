from time import sleep
from Dynamixel import Dynamixel

dxl=Dynamixel()
dxl.set_position([0]*12)

while True:
	for i in range(-30,30):
		dxl.set_position([i]*12)
		sleep(0.01)
