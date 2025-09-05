## https://www.physicsclassroom.com/class/1dkin/Lesson-6/Kinematic-Equations
## https://www.calctool.org/kinetics/projectile-motion
## https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/ballistic-flight-equations/

## d = (vi * t) + (1/2 * a * t^2)
## vf = vi + (a * t)
## vf^2 = vi^2 + (2 * a * d)
## d = ((vi + vf)/2) * t
## Horiz Motion:	x = x0 + Vx*t
##					Vx = V0x

## 1 m/s = 2.236936 mph

import os
import sys
import math

#############################################
################## GLOBALS ##################

MILLI 		= 1e-3
MICRO 		= 1e-6
NANO		= 1e-9
PICO		= 1e-12
KILO		= 1e3
MEGA		= 1e6
GIGA		= 1e9
TERA		= 1e12

GRAVITY		= 9.807		## m/s^2
MPS2MPH		= 2.236936 	## m/s to mph
METER2FEET	= 3.28084 	## meters to feet

###############################################
################## FUNCTIONS ##################

## y0  == initial height
## V0y == initial velocity in y direction 
def maxHeight (y0, V0y):
	ymax = y0 + (math.pow(V0y,2)/(2*GRAVITY))
	return ymax

def horiz_distance(Vx, tof):
	dist = Vx * tof
	return dist
	
def timeOfFlight(V0y, y0):
	tof = (V0y + math.sqrt((V0y*V0y)+ (2*GRAVITY*y0)))/GRAVITY
	return tof

## V0x == initial velocity in x direction
def horiz_vel (V0, angle):
	V0x = V0 * math.cos(angle)
	return V0x

## V0y == initial velocity in y direction
def vert_vel (V0, angle):
	V0y = V0 * math.sin(angle)
	return V0y

########################################
### User Interface ###
def getuserInput():
	v0 = input("Enter initial velocity:\t")
	v0 = int(v0)
	y0 = input("Enter initial hight:\t")
	y0 = int(y0)
	a0 = input("Enter angle:\t")
	a0 = int(a0)

##########################################
################## MAIN ##################

if __name__ == "__main__":

	## Uncomment this function and comment out the Test values (below)
	## to choose new user input values for the main
	
	# ~ getUserInput()

	## Test values, uncomment as needed
	V0 = 35.0	## m/s
	# ~ ## ~ V0 = 44.704006 ## 100 mph	
	# ~ ## ~ a0 = 57.2957795 ## one radian
	a0 = 45.0 	## degrees
	y0 = 1.5	## 1.5 meters initial height
	
	ang = a0 * (math.pi/180.0)
	ang = round(ang,8)
	# ~ print("ang = {0} radians".format(ang))
	ay = math.sin(ang)
	ay = round(ay,8)
	ax = math.cos(ang)
	ax = round(ax,8)
	print("\ninitial velocity V0 = {0} m/s = {1} mph\nangle = {2} radians \ninitial height y0 = {3} meters\n".format(V0, V0*MPS2MPH, ang, y0))
	print("cos(ang) = {0} \nsin(ang) = {1}\n".format(ax,ay))
	
	xvel = horiz_vel(V0, ang)
	xvel = round(xvel, 5)
	yvel = vert_vel(V0, ang)
	yvel = round(yvel,5)
	tof = timeOfFlight(yvel,y0)
	tof = round(tof,5)
	print("xvel = {0} mph\nyvel = {1} mph".format(round(xvel*MPS2MPH,5), round(yvel*MPS2MPH,5)))
	print("xvel = {0} m/s\nyvel = {1} m/s\ntof = {2} seconds".format(xvel, yvel, tof))

	xdist = horiz_distance(xvel, tof)
	xdist = round(xdist, 5)
	ydist = maxHeight(y0, yvel)
	ydist = round(ydist,5)
	print("\nxdist = {0} meters = {1} feet\nmax height = {2} meters = {3} feet".format(round(xdist,5), 
			round(xdist*METER2FEET,5), round(ydist,5), round(ydist*METER2FEET,5)))


#########################################
#########################################

# ~ ## V0 == initial velocity
# ~ def angleOfLaunchVertical (V0, Vy):
	# ~ angle = math.asin(Vy/V0)
	# ~ return angle

# ~ ## V0 == initial velocity
# ~ def angleOfLaunchVertical (V0, Vy):
	# ~ angle = math.asin(Vy/V0)
	# ~ return angle
