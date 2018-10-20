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

import pypot.robot
from time import sleep,time

import Read
from robot import quadruped


if __name__=='__main__':
	robot=pypot.robot.from_config(quadruped)
	raw_input("press Enter to continue ")

	Read.do_motion(robot, "motions/stand_up.mot", 1)
