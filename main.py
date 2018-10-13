#########################################################################################################
# Copyright 2018 SRM Team Humaniod
# All Rights Reserved
#
# Licensed under the ApashyamKiriKiri License, Version 1.13.[insertRandomNumberHere]
# you may not use this file except in compliance with the License.
#
# This is a proprietry code. No one except the Team Leads, Domain Heads
# or Coding Domain Senior Balak or Balikas of SRMTH are supposed to read this.
#
# If you are not a Team Lead, Domain Head or Coding Domain Senior Balak or Balika
# your eyes will pop out in the next 5 seconds.
#
# No one except the Owners have the right to access or modify the code.
#
#########################################################################################################

# Owner     : SRM Team Humaniod, Kattankulathur
# Author    : Akarsh Shrivastava
# Maintainer: No one tries to maintain this.
#
# Yes I was so jobless that I did all this

from time import sleep,time
from Read import Read
from Dynamixel import Dynamixel

# constraints for m2,m5,m8 : -98 to  100
# constraints for m11      :  98 to -100


if __name__=='__main__':
	dxl=Dynamixel()

	raw_input("press Enter to continue ")
	motion_set=Read.read_from_file("stand_up.mot")

	for motion in motion_set:
		dxl.set_position(motion[0])
		sleep(motion[1])
	
	motion_set=Read.read_from_file("init_walk.mot")

	for motion in motion_set:
		dxl.set_position(motion[0])
		sleep(motion[1])
			
	motion_set=Read.read_from_file("walk.mot")

	while True:
		i=0
		for motion in motion_set:
			i+=1
			dxl.set_position(motion[0])
			sleep(motion[1])
