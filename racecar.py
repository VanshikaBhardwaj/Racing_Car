import pygame
import time
import random

pygame.init()

pygame.mixer.music.load('The_Getaway.wav')
pygame.mixer.music.play(-1)
display_width = 1000
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

blue = (0,0,100)
bright_blue = (0,0,200)

red = (200,0,0)
bright_red = (255,0,0)

block_color = (200,100,0)

car_width = 50

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar40.png')
iceBall = pygame.image.load('Iceball.png')
volcano = pygame.image.load('volcano3.png')
fireball = pygame.image.load('fireball2.png')
game_title = pygame.image.load('title.png')
wall = pygame.image.load('wall.png')

def button(text,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(gameDisplay,ac, (x, y, w, h))
        if click[0] == 1 and action != None :
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    font = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(text, font)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)
    
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        makescreen()
        gameDisplay.blit(game_title, (255,135))
        gameDisplay.blit(wall, (350,250))

        button("Go",150,450,100,50,blue,bright_blue,game_loop)
        button("Quit", 755, 450, 100, 50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def makescreen():
     gameDisplay.fill(black)
     sides_left=pygame.image.load('side_bushes_l.png')
     sides_right=pygame.image.load('side_bushes_r.png')
     gameDisplay.blit(sides_left,(0,0))
     gameDisplay.blit(sides_right,(900,0))
     #gameDisplay.blit(volcano,(100,-100))
     #things(thing_startx, thing_starty, thing_width, thing_height, block_color)

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy, thingw, thingh, color):
    #pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
     gameDisplay.blit(fireball,(thingx, thingy))
def quitgame():
    pygame.quit()
    quit()


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text,dodged):
    largeText = pygame.font.Font('freesansbold.ttf',70)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    restart(dodged)
    
def restart(score):
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        makescreen()
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Restart?", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
    
        font = pygame.font.SysFont(None, 35)
        text = font.render("Score: "+str(score), True, white)
        gameDisplay.blit(text,(450,50))

        button("Yes",150,450,100,50,blue,bright_blue,game_loop)
        button("No", 755, 450, 100, 50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def crash(dodged):
    message_display('OOPS! You Crashed.',dodged)


def collision(fireball_x, fireball_y, fireball_h, fireball_w, iceball_x, iceball_y):
    if(iceball_y < fireball_y + fireball_h):
        if ((fireball_x < iceball_x) and (fireball_x + fireball_w > iceball_x)) or (iceball_x < fireball_x and iceball_x+21 > fireball_x) or (fireball_x < iceball_x and fireball_x+fireball_w > iceball_x+21 ):
            makescreen()
            pygame.display.update()
            return 5
        else: 
            return 0

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.85)
    
    x_change = 0

    thing_startx = random.randrange(100, display_width-100)
    thing_starty = -600
    thing_speed = 4
    thing_width = 30
    thing_height = 50

    iceX = x + car_width/2-8
    iceY = y
    ice_speed=7
   # thingCount = 1

    dodged = 0

    gameExit = False
    count=0
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
                
                if event.key == pygame.K_UP:
                    gameDisplay.blit(iceBall,(iceX,iceY))
                    pygame.display.update()
                    while iceY > 0:
                        iceY -= ice_speed
                        count=collision(thing_startx, thing_starty, thing_height, thing_width,iceX,iceY)
                        
                        if(count>0):
                            dodged += count
                            thing_startx=random.randrange(100,800)
                            thing_starty=-200
                            break
                        makescreen()
                        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
                        
                        gameDisplay.blit(iceBall,(iceX,iceY))
                        thing_starty += thing_speed
                        
                        
                        things_dodged(dodged)
                        car(x,y)
                        pygame.display.update()
                        if y+1 < thing_starty+thing_height:
                             if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width or thing_startx>x and thing_startx + thing_width < x+car_width:
                                 crash(dodged)
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    x_change = -5
                                if event.key == pygame.K_RIGHT:
                                        x_change = 5
                            if event.type == pygame.KEYUP:
                                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                    x_change = 0
                        x += x_change
                    iceX=x
                    iceY=y
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    iceX=x
                    iceY=y
                
        
        makescreen()
        
        x += x_change
       
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width - 100 or x < 101:
            crash(dodged)
            pygame.display.update()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(100,display_width-100)
            dodged += 1
            thing_speed += 1
            
        if y+1 < thing_starty+thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width or thing_startx>x and thing_startx + thing_width < x+car_width:
                crash(dodged)
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()