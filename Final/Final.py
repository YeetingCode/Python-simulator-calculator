from turtle import *

import math
import turtle
import time




#penup()
#goto(-100,0)
#pendown()
#color("brown")
#forward(300)
#right(90)
#forward(100)
#penup()
#goto(0,0)
#color("blue")





while True:

    print("[1] maximum height and distance with mass, speed and angle and without windresistance")
    print("[2] bouncing ball")
    print("[4] maximum height and distance with mass, speed, angle and windresistance")
    choice = input("choose one of the possibilities: ")
    dt = float (0.25)    # seconds   
    g = float (9.81)        # fixed accel (downwards) (m/s/s)

    list_of_exits = []
    if choice in ('1','2','4'):

        if choice == ('1'):
            try:
                v = float(input("Enter speed (m/s): "))
                angl = float(input("Enter angle (degrees): "))
                m = float(input("Enter mass of object(kg): "))
            except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            if v > 0 and angl >= 0 and m > 0:
                print("run the simulation until it hits the ground")
                #more variables
                a = float(0)                                    #acceleration
                vx = float(v*math.cos(math.radians(angl)))      #speed in the x axis
                vy = float(v*math.sin(math.radians(angl)))      #speed in the y axis
                Fz = float(-m*g)                                #force inflicted on the object by gravity
                x = float(0)                                    #the x position
                y = float(0)                                    # y position 
                t = float(0)                                    #the time
                turtle.clearscreen()                            #clear the turtle screen for reuse
                #make the turtle draw a floor and move back to (0,0)
                penup()
                goto(-400,0)
                pendown()
                color("brown")
                forward(900)
                penup()
                goto(0,0)
                pendown()
                color("blue")
                while (y >= 0):
                    #main loop
                    x += vx*dt            #get a new x variable
                    Fresy = Fz
                    ay = Fresy / m
                    vy += ay*dt
                    y += vy * dt          # change in y posn = vel + time interval 
                    t += dt
                    
                    goto(x,y)
                    dot(2, "blue")              # draw dot at current position
                    list_of_exits.append(y)
                print("maximum y position is",max(list_of_exits),"m")
                print("maximum x position is", x, "m")
            else:
                print("please insert positive values")

        


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
                    list_of_exits.append(y)
                    if (t % 2) == 0:
                        print("x = " ,x)
                        print("y = " ,y)
                        print("maximum y = ", max(list_of_exits))
            else:
                print("Please enter a percentage between 0 and 100")
                print("Please enter a simulation speed between 0.01 and 0.1")
                print("Please enter a speed between 0 and 75")
        if choice == ('4'):
            try:
                v = float(input("Enter speed (m/s): "))
                angl = float(input("Enter angle (degrees): "))
                m = float(input("Enter mass of object(kg): "))
                print("[1] sphere")
                print("[2] cube")
                print("[3] cone")
                vorm = float(input("Enter the shape: "))
            except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

            if vorm == 1:
                Cw = float(0.47)
                try:
                    r = float(input("Enter the radius of the sphere (m): "))
                except ValueError:
                    print("invalid input. Please enter a number")
                A = math.pi * r*r
            elif vorm == 2:
                Cw = float(1.05)
                try: 
                    r = float(input("Enter the length of one of the legs (m): "))
                except ValueError:
                    print("invalid input. Please enter a number")
                A = r*r
            elif vorm == 3:
                Cw = float(0.45)
                try:
                    r = float(input("Enter the radius of the bottom circle (m):"))
                except ValueError:
                    print("invalid input. Please enter a number")
                A = math.pi * r * r

            if v > 0 and angl >= 0 and m > 0 and A > 0:
                print("run the simulation until it hits the ground")
                #more variables
                a = float(0)                                    #acceleration
                vx = float(v*math.cos(math.radians(angl)))      #speed in the x axis
                vy = float(v*math.sin(math.radians(angl)))      #speed in the y axis
                Fz = float(-m*g)                                #force inflicted on the object by gravity
                k = float((A*1.293*Cw*0.5))
                x = float(0)                                    #the x position
                y = float(0)                                    # y position 
                t = float(0)                                    #the time
                turtle.clearscreen()                            #clear the turtle screen for reuse
                #make the turtle draw a floor and move back to (0,0)
                penup()
                goto(-400,0)
                pendown()
                color("brown")
                forward(900)
                penup()
                goto(0,0)
                pendown()
                color("blue")
                while (y >= 0):
                    #main loop
                    v = math.sqrt(vx*vx + vy*vy)
                    Fw = float(k*v*v)
                    Fwx = -Fw * (vx/v)
                    Fresx = Fwx
                    ax = Fresx / m
                    vx += ax*dt
                    x += vx*dt            #get a new x variable
                    
                    Fwy = -Fw * (vy/v)
                    Fresy = Fz + Fwy
                    ay = Fresy / m
                    vy += ay*dt
                    y += vy * dt          # change in y posn = vel + time interval 
                    t += dt
                    
                    goto(x,y)
                    dot(2, "blue")              # draw dot at current position

                    list_of_exits.append(y)
                print("maximum y position is",max(list_of_exits),"m")
                print("maximum x position is", x, "m")
            else:
                print("please insert positive values")
