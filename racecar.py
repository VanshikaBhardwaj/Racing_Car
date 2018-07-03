import pygame
import time
import random

pygame.init()

display_width = 1000
display_height = 600

black = (0,0,0)
white = (127,127,127)
red = (255,0,0)

block_color = (53,115,255)

car_width = 50

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar40.png')
iceBall = pygame.image.load('Iceball.png')

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    #crash()
    game_loop()
    
    

def crash():
    message_display('You Crashed')
'''    
def gen_IceBall(iceX, iceY):
    while (iceY < -10):
        gameDisplay.blit(iceBall,(iceX,iceY))
        iceY -= 7 
        pygame.display.update()
'''
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    
    x_change = 0

    thing_startx = random.randrange(100, display_width-100)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    iceX = x + car_width/2-8
    iceY = y
    Iceball_speed=7
   # thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    #################################
                if event.key == pygame.K_UP:
                    #gen_IceBall(iceX,iceY)
                     #while (iceY < -10):
                     gameDisplay.blit(iceBall,(iceX,iceY))
                     iceY -= 7 
                     pygame.display.update()
                    
                    ##############################
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    
                    if event.key == pygame.K_UP:
                    #if()
                        iceY = y
                    #gen_IceBall(iceX, iceY)
                    
        
      
        
        x += x_change
        gameDisplay.fill(white)
        sides_left=pygame.image.load('side_bushes_l.png')
        sides_right=pygame.image.load('side_bushes_r.png')
        gameDisplay.blit(sides_left,(0,0))
        gameDisplay.blit(sides_right,(900,0))
        iceY-= Iceball_speed
       # gen_IceBall(iceX, iceY)

        # pygame.display.update()   
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        
        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width - 100 or x < 101:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(100,display_width-100)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()