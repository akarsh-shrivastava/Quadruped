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

import Read
from Dynamixel import Dynamixel
from time import sleep,time


# constraints for m2,m5,m8 : -98 to  100
# constraints for m11      :  98 to -100

if __name__=='__main__':
	dxl=Dynamixel()
	raw_input("press Enter to continue ")

	#Read.do_motion(dxl, "motions/stand_up.mot", 1)
	Read.do_motion(dxl, "motions/left_turn.mot")
	#Read.do_motion(dxl, "motions/init_walk.mot", 1)
	#Read.do_motion(dxl, "motions/walk.mot")
	#Read.do_motion(dxl, "motions/sit_down.mot", 1)
