import pygame
import time
import random
pygame.init()
#Yes,I can Edit
white= (255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
display_width=1000
display_height=800
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("slither")
icon=pygame.image.load('apple.png')
#music=pygame.mixer.Sound('theme-music.wav')
bg=pygame.image.load('bg.png')
pygame.display.set_icon(icon)
img=pygame.image.load('sanke.png')
appleimg=pygame.image.load('apple.png')
pygame.display.update()
clock=pygame.time.Clock()
applethickness = 30
block_size= 20
fps=10
smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",40)
largefont=pygame.font.SysFont("comicsansms",75)


def pause():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    paused=False
        gamedisplay.blit(bg,(0,0))
        message_to_print("Paused",red,-100,"large")
        message_to_print("Press c to play or q to quit", black, 100,"medium")
        pygame.display.update()
def score(score):
    text=medfont.render("Score="+str(score),True,white)
    gamedisplay.blit(text,[0,0])
def applegen():
    randapplex = round(random.randrange(0, display_width - applethickness))
    randappley = round(random.randrange(0, display_height - applethickness))
    return randapplex,randappley
randapplex,randappley=applegen()
def test_obj(text,color,size):
    if size=="small":
        textsurface=smallfont.render(text,True,color)
    elif size=="medium":
        textsurface=medfont.render(text,True,color)
    elif size=="large":
        textsurface=largefont.render(text,True,color)
    return textsurface,textsurface.get_rect()

def message_to_print(msg,color,y_display=0,size= "small"):
    textsurf,textrect= test_obj(msg,color,size)
    textrect.center=(display_width/2),(display_height/2)+y_display

    #screen=font.render(msg,True,color)
    gamedisplay.blit(textsurf,textrect)
direction='right'
def snake_intro():

    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    intro=False
        gamedisplay.blit(bg,(0,0))
        pygame.mixer.music.load('theme-music.wav')
        pygame.mixer.music.play(-1)
        message_to_print("Welcome to Slither",red,-200,"large")
        message_to_print("The Obejective is to eat red apples", black, -30,"medium")
        message_to_print("The more apple you eat, More you get longer", black, 20,"medium")
        message_to_print("If you run into yourself or edges,You die!!!!", black, 80,"medium")
        message_to_print("Press c to Play ,p to Pause or q to Quit", black, 180,"medium")
        pygame.display.update()
        clock.tick(15)
def snake(block_size,snakelist):
    if direction=='right':
        head=pygame.transform.rotate(img,270)
    if direction == 'left':
        head = pygame.transform.rotate(img, 90)
    if direction == 'up':
        head = img
    if direction == 'down':
        head = pygame.transform.rotate(img, 180)
    gamedisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for xny in snakelist[:-1]:
        pygame.draw.rect(gamedisplay,green , [xny[0],xny[1],block_size, block_size])



def gameloop():

    global direction
    gameexit = False
    gameover= False
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0
    snakelist=[]
    snakelenght=1
    randapplex,randappley=applegen()
    while not gameexit:
        while gameover== True:
            gamedisplay.blit(bg,(0,0))
            message_to_print(score(snakelenght-1),red,-10)
            message_to_print("Game Over",red,-50,"large")
            message_to_print("Press C for Continue or Q to Quit",black,50,"medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = False
                    gameexit = True
                if event.type == pygame.KEYDOWN:

                    if event.key==pygame.K_q:
                        gameexit=True
                        gameover=False
                    if event.key==pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction='left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                if event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key==pygame.K_p:
                    pause()
        if lead_x>display_width or lead_x<0 or lead_y>display_height or lead_y<0:
            gameover=True
        lead_x += lead_x_change
        lead_y += lead_y_change
        gamedisplay.fill(black)

        gamedisplay.blit(appleimg,(randapplex,randappley))
        #pygame.draw.rect(gamedisplay, red, [randapplex, randappley, applethickness, applethickness])
        snakehead=[]
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(block_size,snakelist)
        if len(snakelist)>snakelenght:
            del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameover=True
        score(snakelenght-1)
            # pygame.draw.circle(gamed,black,[lead_x,lead_y],10,10)
        pygame.display.update()

        if lead_x >= randapplex and lead_x <= randapplex + applethickness or lead_x+block_size<randapplex and lead_x+block_size>randapplex:
            if lead_y >= randappley and lead_y <= randappley + applethickness:
                randapplex,randappley=applegen()
                snakelenght += 1
            elif lead_y+block_size<randappley and lead_y+block_size>randappley:
                randapplex,randappley=applegen()
                snakelenght += 1
        clock.tick(fps)

            #print(event)

    pygame.quit()
    quit()

snake_intro()
gameloop()
