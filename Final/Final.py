# a simple python example for SIS at BPS,   bill,  Jan 2017
# using turtle graphics 
#
# simulate the effect of gravity on ball thrown upwards
# using first order equations
#


from turtle import *
import time

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

print("[1] eerste try")
while True:
    choice = input("kies een van de mogelijkheden: ")
    if choice in ('1,2'):
        if choice == ('1'):
            try:
                yvel = float(input("Enter speed: "))
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
                print("final y position is" + str(y) + " m")

        elif choice == ('2'):
            
            delx = 15

            try:
                yvel = float(input("Enter speed between 0 and 75: "))
            except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            try:
                tstep = float(input("Enter simulation speed between 0.01 and 0.1: "))
            except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            try:
                bounce = float(input("Enter conservation of energy (in %)"))
            except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue



            if tstep > 0 and tstep <= 0.1 and bounce >= 0 and bounce <= 100 and yvel >=0 and yvel <= 75:
                print("run the simulation for 50 seconds")
                
                penup()
                goto(-500,0)
                pendown()
                begin_fill()
                goto(500,0)
                goto(500,-8)
                goto(-500,-8)
                goto(-500,0)
                end_fill()
                penup()
                x = -300
                y = 100
                goto(x,y)
                time.sleep(0.4)
                
                while (t<50):
                    t=t+tstep
                    x=x + delx * tstep
                    if y>0:
                        yvel = yvel - g * tstep
                    else:
                        y = 0
                        yvel = - 0.01 * bounce * yvel
                    y=y + yvel * tstep
                     
                        
                    
                        
                        
                    goto(x,y)
                    pendown()
                    if (t % 2) == 0:
                        print("x = " ,x)
                        print("y = " ,y)
            else:
                print("Please enter a percentage between 0 and 100")
                print("Please enter a simulation speed between 0.01 and 0.1")
                print("Please enter a speed between 0 and 75")
