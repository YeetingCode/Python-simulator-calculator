from turtle import *
import pygame
import math
import turtle
import time
pygame.init()



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
                turtle.clearscreen()
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
                        yvel = - 0.01 * bounce * yvel
                    y=y + yvel * tstep
                    if y + yvel * tstep < 0:
                        y=0
                     
                        
                    
                        
                    pendown()
                    goto(x,y)
                    list_of_exits.append(y)
                    if (y == 0 and (yvel > 5 or yvel < -5)):
                        print("y = 0 on x = " ,x)
                        print("maximum y = ", max(list_of_exits))
                    elif (y==0 and yvel < 5 and yvel > -5):
                        t = t + 1
                    penup()
            else:
                print("Please enter a percentage between 0 and 100")
                print("Please enter a simulation speed between 0.01 and 0.1")
                print("Please enter a speed between 0 and 75")
        if choice == ('3'):
                        WIDTH, HEIGHT =  1600, 850
            WIN = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.set_caption("Planet Simulation")   #dit geeft de naam van de vierkant, waarin de simulatie in gemaakt zal worden

            WHITE = (255, 255, 255)
            YELLOW = (255, 255, 0)
            BLUE = (41, 143, 245.)
            RED = (188, 39, 50)
            DARK_GREY = (80, 78, 81)
            ORANGE = (255,165,0)
            CLEAR_GOLD = (255,215,0)
            DARK_BLUE = (0,0,54)
            LIGHT_BLUE = (173,216,230)



            FONT = pygame.font.SysFont("comicsans", 16)

            class Planet:
	            AU = 149.6e6 * 1000 # deze variabele wordt in de sterrekunde gebruikt om de afstand tussen de kern an de zon en de kern van de aarde weer te geven
	            G = 6.67428e-11    # dit is een natuurkundige constante voor de gravitatiekracht die werkt tussen planeten
	            SCALE = 23 / AU   # zonder de schaal zou de simulatie er niet op passen. nu zou een AU ongeveer 100 pixels moeten zijn
	            TIMESTEP = 3600*24    # natuurlijk kunnen we niet elke seconden weergeven, dus wordt er per frame 1 dag weergegeven: 60*60*24 = 86400

	            def __init__(self, x, y, radius, color, mass): # elke planeet heeft deze eigenschappen
		            self.x = x
		            self.y = y
		            self.radius = radius  # zorgt voor een ronde planeet
		            self.color = color
		            self.mass = mass # dit verwijst naar het feit, dat elke keer dat er een planeet wordt aangemaakt ze een unieke x, radius, kleur enz krijgen

		            self.orbit = [] # das het cirkeltje dat de koers van de planeet aangeeft
		            self.sun = False # dit betekent dat de zon niet beweegt
		            self.distance_to_sun = 0

		            self.x_vel = 0
		            self.y_vel = 0

	            def draw(self, win):
		            x = self.x * self.SCALE + WIDTH / 2   # dit zorgt dat de planeten op schaal zijn en centraal zijn
		            y = self.y * self.SCALE + HEIGHT / 2

		            if len(self.orbit) > 2: # dit tekent zegmaar een lijn door 2 punten en met 1 punt kan je gaan lijn tekenen
			            updated_points = []
			            for point in self.orbit:
				            x, y = point
				            x = x * self.SCALE + WIDTH / 2
				            y = y * self.SCALE + HEIGHT / 2
				            updated_points.append((x, y))

			            pygame.draw.lines(win, self.color, False, updated_points, 2) # de orbit wordt getekent, tussen de x-as en de y-as coordinaten

		            pygame.draw.circle(win, self.color, (x, y), self.radius)

		            if not self.sun:
			            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
			            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

	            def attraction(self, other):
		            other_x, other_y = other.x, other.y
		            distance_x = other_x - self.x
		            distance_y = other_y - self.y # hier wordt de afstand berekend tussen het huidige object en een ander object
		            distance = math.sqrt(distance_x ** 2 + distance_y ** 2)    # dit is de stelling van pythagoras, die nodig is om de snelheid te kunnen berkenen, waarmee de planeten bewegen. aangezien het volgens de gravitale consstante objecten aan elkaar trekken, moet er worden berkend wat het verschil in afstand is tussen de planeet en de andere planeet om de snelheid te kunnen bepalen

		            if other.sun:
			            self.distance_to_sun = distance# ik wil alleen maar de afstand naar de zon weten

		            force = self.G * self.mass * other.mass / distance**2      # in deze lines of code wordt the force of attraction berekend
		            theta = math.atan2(distance_y, distance_x) # bepaalt de hoek
		            force_x = math.cos(theta) * force
		            force_y = math.sin(theta) * force
		            return force_x, force_y

	            def update_position(self, planets): # ik kijk naar alle planeten en bereken de force of attraction per planeet in verhouding tot de rest van de planeten, de uitleg is volgensmij dat de dit betkenst tijd maal  de vernelling + de normale snelheid
		            total_fx = total_fy = 0
		            for planet in planets:
			            if self == planet:
				            continue

			            fx, fy = self.attraction(planet) # de force van de x-as en de y-as zijn gelijk aan de attraction
			            total_fx += fx
			            total_fy += fy

		            self.x_vel += total_fx / self.mass * self.TIMESTEP# DIT IS GEBASSEERD OP F = m / a, maar de formule klopt niet en moet F = m * a
		            self.y_vel += total_fy / self.mass * self.TIMESTEP
            
		            self.x += self.x_vel * self.TIMESTEP # dit is de afstand
		            self.y += self.y_vel * self.TIMESTEP
		            self.orbit.append((self.x, self.y))   # nu kunnen we eindelijk de as tekenen


            def main():
	            run = True
	            clock = pygame.time.Clock() # dit zorgt ervoor dat het programma op elke computer even snel runt en niet op de ene wat sneller dan de ander

	            sun = Planet(0, 0, 6, YELLOW, 1.98892 * 10**30)# massa is in kg btw en
	            sun.sun = True

	            earth = Planet(-1 * Planet.AU, 0, 1, BLUE, 5.9742 * 10**24)
	            earth.y_vel = 29.783 * 1000  # deze snelhedem zijn hier gebruikt, omdat de planeten ook de andere kant van de zon bewegen, zodat ze niet allemaal in de zon opgeslokt worden, deze kracht heet in het engels ook wel de Mean orbit velocity

	            mars = Planet(-1.524 * Planet.AU, 0, 0.8, RED, 6.39 * 10**23)
	            mars.y_vel = 24.077 * 1000

	            mercury = Planet(0.387 * Planet.AU, 0, 0.6, DARK_GREY, 3.30 * 10**23)
	            mercury.y_vel = -47.4 * 1000

	            venus = Planet(0.723 * Planet.AU, 0, 1, WHITE, 4.8685 * 10**24)
	            venus.y_vel = -35.02 * 1000
            
	            jupiter = Planet(5.203 * Planet.AU, 0, 2, ORANGE, 1.8981 * 10**27)
	            jupiter.y_vel = -13.072 * 1000
	            
	            saturnus = Planet(9.58 * Planet.AU, 0, 1, CLEAR_GOLD, 5.6832 * 10**26)
	            saturnus.y_vel = -9.6391 * 1000
	            
	            uranus = Planet(19.22 * Planet.AU, 0, 1, LIGHT_BLUE, 8.6810* 10**25)
	            uranus.y_vel = -6.7991  * 1000
            
	            neptunes = Planet(30.10 * Planet.AU, 0, 1, DARK_BLUE, 1.0241* 10**26)
	            neptunes.y_vel = -5.4349 * 1000

	            planets = [sun, earth, mars, mercury, venus, jupiter, saturnus, uranus, neptunes]

	            while run:
		            clock.tick(120)
		            WIN.fill((0, 0, 0)) # er wordt zegmaar nieuwe planeten getekend, en om de oude weg te krijgen, moeten we de nieuwe de achtergrond verversen
            
		            for event in pygame.event.get():
			            if event.type == pygame.QUIT:
				            run = False

		            for planet in planets:
			            planet.update_position(planets)
			            planet.draw(WIN)
            
            		pygame.display.update()  # zonder deze line met code, zal het zwarte canvas nooit updaten en komt er nooit wat op te staan
            
            	pygame.quit()
            
            
            main()
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
