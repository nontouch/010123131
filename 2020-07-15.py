################################################################
# Name : Nontouch kongdee
# student number : 6201012610028
# File: Assignment I
# Date: 2020-07-15
################################################################

# Note this Python script requires PyGame.
import pygame 
from random import randint
import math
# def for find maximum radian
def largest(storage):
    n = 0
    ma = rad[n]
    for i in range(len(rad)-1):
        if(ma < rad[i+1]):
            ma =  rad[i+1]
        else:
            ma = ma
    return ma

# initialize PyGame
pygame.init()

# show PyGame version
#print( 'PyGame version: {}'.format( pygame.version.ver ) ) 


# set window caption
pygame.display.set_caption('Amezing circle') 

# create a clock
clock = pygame.time.Clock()

# Set up the drawing window (500 x 500 pixels)
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))

# create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

point = []
point_tup = []
rad = []

# Run until the user asks to quit
running = True
while running:

    # This limits the while loop to a max of 10 times per second.
    clock.tick( 15 ) 

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # keep the position (x,y) of maximum radian 
    k = []
    for i in range(len(rad)):
        if(rad[i] == largest(rad)):
            k.append([point[i][0], point[i][1], rad[i]])
    # this loop for remove the circle when you click on the maximum circle only
    for j in range(len(k)):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if((k[j][0]-pos[0])**2 + (k[j][1]-pos[1])**2 <= largest(rad)**2):
                    pygame.draw.circle( surface, (255,255,255), (k[j][0],k[j][1]), k[j][2] )
                    screen.blit(surface, (0,0))
                    pygame.display.update() 

    # randomize an integer value between 10..20 for the radius
    R = randint(10,20)
    # randomize an integer value between 50..255 for alpha level
    alpha = randint(50,255)
    # randomize an integer value between 50..255 for random color
    r = randint(0,255)
    # randomize an integer value between 50..255 for random color
    g = randint(0,255)
    # randomize an integer value between 50..255 for random color
    b = randint(0,255) 
    # create a color with alpha level (RGBA) by random
    all_color = (r,g,b,alpha) 
    # randomize a position (x,y)
    x,y = randint(R,scr_w-R), randint(R,scr_h-R)
    # if it has not any circle on display
    if len(point) == 0:
        p1 = randint(R,scr_w-R)
        p2 = randint(R,scr_h-R)
        distant = math.sqrt((x - p1)**2 + (y - p2)**2)
        point.append([x,y,R])
        point_tup.append((x,y))
        rad.append(R)
        pygame.draw.circle( surface, all_color, (x,y), R )
        screen.fill((255,255,255))
        screen.blit(surface, (0,0))
        pygame.display.update()
    # if in the display has the circle more than one
    else :
        # find distant between current circle and other circle
        for i,R2 in zip(point,rad)  :
            distant = math.sqrt((x - int(i[0]))**2 + (y - int(i[1]))**2)
            # if the new circle has not overlap with other circle
            if [x,y] not in point and R + R2 < distant and len(rad) < 10 :
                point.append([x,y])
                point_tup.append((x,y))
                rad.append(R)
    # draw a circle filled with the blue color on the surface 
                pygame.draw.circle( surface, all_color, (x,y), R )
    # fill the screen with the white color
                screen.fill((255,255,255))
    # draw the surface on the screen
                screen.blit(surface, (0,0))
    # update the screen display
                pygame.display.update()
            # if the new circle has overlap with other circle ,that will not makes it
            else :
                break

    

pygame.quit()

################################################################
# To do: modify the Python code so that it can randomly create
# circles with different filled colors (RGBA values)
################################################################
