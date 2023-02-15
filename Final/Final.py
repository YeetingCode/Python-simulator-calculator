# a simple python example for SIS at BPS,   bill,  Jan 2017
# using turtle graphics 
#
# simulate the effect of gravity on ball thrown upwards
# using first order equations
#


from turtle import *

# setup variables for time, x step, gravity, initial velocity 
t=0
tstep = 0.25    # seconds   
delx = 2        # uniform motion in x axis 
dely = 2        # fixed accel (downwards) 
yvel = 5        # motion in y
y=0             # y position 

# draw a cliff that the ball can be thrown from 
#penup()
#goto(-100,0)
#pendown()
#color("green")
#forward(150)
#right(90)
#forward(100)
#penup()
#goto(0,0)

pendown()
color("blue")

print("run the simulation for 50 seconds ")
# main loop -- uniform motion in x and acceleration in y axis 
while (t<50):
    t=t+tstep
    x=t*delx
    if y>=0:
        yvel = yvel - dely * tstep     # change in y vel = accel * time interval
    if y<0:
        yvel = yvel + dely * tstep
    y=y + yvel * tstep          # change in y posn = vel + time interval 
    
    goto(x,y)
    dot(2, "blue")              # draw dot at current position 

print("final y position is " + str(y) + " m")
write(" python rules! ")
print("that's all folks")
