################################################################
# Name : Nontouch kongdee
# student number : 6201012610028
# File: Assignment II
# Date: 2020-07-16
################################################################

# Note this Python script requires PyGame.
import pygame 
from random import randint
import math

class circle() :
    def __init__(self) :
        self.scr_w = 800
        self.scr_h = 600
    # randomize an integer value between 10..20 for the radius
        self.R = randint(10,20)
    # randomize an integer value between 50..255 for alpha level
        self.alpha = randint(50,255)
    # randomize an integer value between 50..255 for random color
        self.r = randint(0,255)
    # randomize an integer value between 50..255 for random color
        self.g = randint(0,255)
    # randomize an integer value between 50..255 for random color
        self.b = randint(0,255) 
    # create a color with alpha level (RGBA) by random
        self.all_color = (self.r,self.g,self.b,self.alpha) 
    # randomize a position (x,y)
        self.x,self.y = randint(self.R,self.scr_w-self.R), randint(self.R,self.scr_h-self.R)
        self.Ri,self.Le= self.x + self.R , self.x - self.R
        self.Bo,self.To= self.y + self.R , self.y - self.R
        self.speed = [randint(5,10),randint(5,10)]
    def make(self) :
        pygame.draw.circle( screen, self.all_color, (self.x,self.y), self.R )
        pygame.display.update()
    def delete(self) :
        pygame.draw.circle( screen, (255,255,255), (self.x,self.y), self.R )
        pygame.display.update()

def cleck_distant(x,y,rad,x2,y2) :
    
    if ((x - x2)*(x - x2)) + ((y - y2)*(y - y2)) <= rad**2 :
        return True
    else :
        return False

        


# def for find maximum radian
def largest(tar,List):
    b_count = 0
    for k in List:
        if tar != k:
            if tar.R > k.R :
                b_count += 1
            elif tar.R == k.R :
                b_count += 1
    if b_count == len(List) - 1:
        return True
    else:
        return False

def telepatic(t) :
 

    t.x += t.speed[0]
    t.y += t.speed[1]
    t.Ri += t.speed[0]
    t.Le += t.speed[0]
    t.Bo += t.speed[1]
    t.To += t.speed[1]
        
    if t.Ri >= t.scr_w or t.Le <= 0 :
        t.speed[0] *= -1
    if t.Bo >= t.scr_h or t.To <= 0 :
        t.speed[1] *= -1
    for q in F_CIRCLE :
        if t != q :
            if int(math.hypot(t.x - q.x, t.y - q.y)) - int(t.R + q.R) <= 5 :
                itemSpeed = math.sqrt((t.speed[0] ** 2) + (t.speed[1] ** 2))
                XDiff = - (t.x - q.x)
                YDiff = - (t.y - q.y)
                if XDiff > 0:
                    if YDiff > 0:
                        Angle = math.degrees(math.atan(YDiff / XDiff))
                        XSpeed = - itemSpeed * math.cos(math.radians(Angle))
                        YSpeed = - itemSpeed * math.sin(math.radians(Angle))
                    elif YDiff < 0:
                        Angle = math.degrees(math.atan(YDiff / XDiff))
                        XSpeed = - itemSpeed * math.cos(math.radians(Angle))
                        YSpeed = - itemSpeed * math.sin(math.radians(Angle))
                elif XDiff < 0:
                    if YDiff > 0:
                        Angle = 180 + math.degrees(math.atan(YDiff / XDiff))
                        XSpeed = - itemSpeed * math.cos(math.radians(Angle))
                        YSpeed = - itemSpeed * math.sin(math.radians(Angle))
                    elif YDiff < 0:
                        Angle = -180 + math.degrees(math.atan(YDiff / XDiff))
                        XSpeed = - itemSpeed * math.cos(math.radians(Angle))
                        YSpeed = - itemSpeed * math.sin(math.radians(Angle))
                elif XDiff == 0:
                    if YDiff > 0:
                        Angle = -90
                    else:
                        Angle = 90
                    XSpeed = itemSpeed * math.cos(math.radians(Angle))
                    YSpeed = itemSpeed * math.sin(math.radians(Angle))
                elif YDiff == 0:
                    if XDiff < 0 :
                        Angle = 0
                    else:
                        Angle = 180
                    XSpeed = itemSpeed * math.cos(math.radians(Angle))
                    YSpeed = itemSpeed * math.sin(math.radians(Angle))
                t.speed[0] = int(XSpeed)
                t.speed[1] = int(YSpeed)

    pygame.draw.circle( screen, t.all_color, (t.x,t.y), t.R )


# initialize PyGame
pygame.init()

# show PyGame version
#print( 'PyGame version: {}'.format( pygame.version.ver ) ) 


# set window caption
pygame.display.set_caption('Amezing circle 2') 

# create a clock
clock = pygame.time.Clock()

# Set up the drawing window (800 x 600 pixels)
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))

# create a new surface 
#surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

CIRCLE = []
F_CIRCLE = []
##speed = [2,2]
point = 0
i = 0
N = 10


# Run until the user asks to quit
running = True
while running:
    #clock.tick(2)
    # This limits the while loop to a max of 10 times per second.

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # this loop for remove the circle when you click on the maximum circle only

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for e in F_CIRCLE :
                if cleck_distant(e.x, e.y, e.R, pos[0], pos[1]):
                    print("true target")
                    if largest(e,F_CIRCLE) :
                        e.delete()
                        F_CIRCLE.remove(e)
                        print("del")

    while point < N:
        CIRCLE.append('circle'+str(i))
        CIRCLE[i] = circle()
        draw = True
        
        for j in range(len(CIRCLE)):
            #check all circle class
            if i != j:
                dist = int(math.hypot(CIRCLE[i].x - CIRCLE[j].x, CIRCLE[i].y - CIRCLE[j].y))
                #if circle overlaped        
                if dist < int(CIRCLE[i].R+CIRCLE[j].R):
                    draw = False
            
        if draw:
            CIRCLE[j].make()
            F_CIRCLE.append(CIRCLE[j])
            point+=1
        i+=1

    for s in F_CIRCLE :
        clock.tick(120)
        telepatic(s)
    # draw the surface on the screen
    pygame.display.update()
    screen.fill((255,255,255))
    #screen.blit(surface, (0,0))

    

pygame.quit()

################################################################
# To do: modify the Python code so that it can randomly create
# circles with different filled colors (RGBA values)
################################################################