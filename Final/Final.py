from turtle import *
import math
import turtle




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
    print("[4] maximum height and distance with mass, speed, angle and windresistance")
    choice = input("choose one of the possibilities: ")
    dt = float (0.25)    # seconds   
    g = float (9.81)        # fixed accel (downwards) (m/s/s)

    list_of_exits = []
    if choice in ('1','4'):
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