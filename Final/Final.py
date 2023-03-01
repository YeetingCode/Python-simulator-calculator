# a simple python example for SIS at BPS,   bill,  Jan 2017
# using turtle graphics 
#
# simulate the effect of gravity on ball thrown upwards
# using first order equations
#


from turtle import *


# setup variables for time, x step, gravity, initial velocity 



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
#pendown()
#color("blue")

t = float (0)
tstep = float (0.25)    # seconds   
g = float (9.81)        # fixed accel (downwards) (m/s/s)
delx = float (2)        # uniform motion in x axis 
y = float (0)             # y position 
list_of_exits = []

print("[1] eerste try")
while True:
    choice = input("choose one of the possibilities: ")
    if choice in ('1'):
        if choice == ('1'):
            try:
                yvel = float(input("Enter speed (m/s): "))
            except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            if yvel > 0:
                print("run the simulation for 50 seconds ")
                # main loop -- uniform motion in x and acceleration in y axis 
                while (t<20):
                    t=t+tstep
                    x=t*delx
                    yvel = yvel - g * tstep
                    y=y + yvel * tstep          # change in y posn = vel + time interval 
                    
                    goto(x,y)
                    dot(2, "blue")              # draw dot at current position
                    list_of_exits.append(y)
                print("maximum y position is",max(list_of_exits),"m")
        

