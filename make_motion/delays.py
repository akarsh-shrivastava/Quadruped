from time import sleep,time
from Read import Read
from Dynamixel import Dynamixel

# this won't edit the file like new_motion.
# you have to do that yourself


if __name__=='__main__':
	dxl=Dynamixel()

	raw_input("press Enter to continue ")
	motion_set=Read.read_from_file("normal.mot")

	
	for motion in motion_set:
		t0=time()
		dxl.set_position(motion[0])
		raw_input()
		t1=time()
		print t1-t0
