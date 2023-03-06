# a simple python example for SIS at BPS,   bill,  Jan 2017
# using turtle graphics 
#
# simulate the effect of gravity on ball thrown upwards
# using first order equations
#


from turtle import *
import math

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


dt = float (0.25)    # seconds   
g = float (9.81)        # fixed accel (downwards) (m/s/s)
vx = float (2)        # uniform motion in x axis 
y = float (0)             # y position 
list_of_exits = []

print("[1] maximum height with mass, speed and angle")
while True:
    choice = input("choose one of the possibilities: ")
    if choice in ('1'):
        if choice == ('1'):
            try:
                v = float(input("Enter speed (m/s): "))
                angl = float(input("Enter angle (degrees): "))
                m = float(input("Enter mass of object(kg): "))
            except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            if v > 0 and angl >= 0 and m > 0:
                print("run the simulation for 50 seconds ")
                # main loop -- uniform motion in x and acceleration in y axis 
                a = float(0)
                vx = float(v*math.cos(math.radians(angl)))
                vy = float(v*math.sin(math.radians(angl)))
                Fz = float(-m*g)
                x = float(0)
                t = float(0)
                while (t < 20):
                    x += vx*dt
                    Fresy = Fz
                    ay = Fresy / m
                    vy += ay*dt
                    y += vy * dt          # change in y posn = vel + time interval 
                    t += dt
                    
                    goto(x,y)
                    dot(2, "blue")              # draw dot at current position
                    list_of_exits.append(y)
                print("maximum y position is",max(list_of_exits),"m")
            else:
                print("please insert positive values")

