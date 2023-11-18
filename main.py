# Imports
import os
import pygame
import random
from pygame import font
from pygame import color
from pygame.constants import K_SPACE

pygame.mixer.init()
pygame.init()
#colors
white=(255,255,255)
red=(255,0,0)
black= (0,0,0)
blue=(0,0,255)
green= (0,255,0)
purple=(119, 7, 55)
yellow=(245,199,26)
purpleish=(180,0,190)

#window variables
screen_width=1000
screen_height=600

# creating window
game_window=pygame.display.set_mode((screen_width,screen_height))
bgimg = pygame.image.load("bg.jpg")
fsimg = pygame.image.load("snakes.jpg")
esimg = pygame.image.load("end.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
fsimg=pygame.transform.scale(fsimg,(screen_width,screen_height)).convert_alpha()
esimg=pygame.transform.scale(esimg,(screen_width,screen_height)).convert_alpha()
pygame.display.set_caption("raffey - game")
pygame.display.update()
font=pygame.font.SysFont(None,45)


clock=pygame.time.Clock()

def screen_score(text,color,x,y):
    screen_score=font.render(text,True,color)
    game_window.blit(screen_score,[x,y])
def display(variable,color,x,y):
    screen_score=font.render(variable,True,color)
    game_window.blit(screen_score,[x,y])
def plot_snake(game_window,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])


def welcome():
    exit_game=False
    while not exit_game:
        game_window.fill(blue)
        game_window.blit(fsimg,(0,0))
        # screen_score("WELCOME TO SNAKES",red,100,100)
        screen_score("Press Space to Continue",yellow,80,400)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type== pygame.KEYDOWN:
                    if event.key== K_SPACE:
                        pygame.mixer.music.load("bgsong.mp3")
                        pygame.mixer.music.play()
                        game_loop()
        pygame.display.update()
        clock.tick(40)
#game loop
def game_loop():
    #game variables
    exit_game=False
    game_over=False
    snake_x=100
    snake_y=90
    snake_size=10
    velo_x=0
    velo_y=0
    snk_list=[]
    snk_length=1
    fps=30
    food_x= random.randint(80,screen_width/2)
    food_y= random.randint(80,screen_height/2)
    score=0
    while not exit_game:
        if game_over:
            game_window.fill(blue)
            game_window.blit(esimg,(0,0))
            with open ("highscore.txt",'w') as f:
                f.write(str(highscore))
            screen_score(''' press enter to continue''',red,50,550)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT :
                        velo_x = 3
                        velo_y = 0
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT :
                        velo_x = - 3
                        velo_y = 0
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP :
                        velo_y = - 3
                        velo_x = 0
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_DOWN :
                        velo_y =  3
                        velo_x = 0
            snake_x=snake_x + velo_x           
            snake_y=snake_y + velo_y         
            
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=1
                # print("Score:", score)
                food_x= random.randint(26,screen_width/2)
                food_y= random.randint(26,screen_height/2)
                snk_length+=5
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]

            
            game_window.fill(green)
            game_window.blit(bgimg,(0,0))
            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("Metal Crash.mp3")
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load("Metal Crash.mp3")
                pygame.mixer.music.play()
                game_over=True
                # screen_score("GAME OVER!",red,200,150)
            
            pygame.draw.circle(game_window,red,(food_x,food_y),5)
            with open ("highscore.txt",'r') as f:
                highscore=f.read()
            if score>int(highscore):
                highscore=score
                
            display(str(highscore),red,170,35)
            screen_score("highscore:",blue,12,35)
            plot_snake(game_window,yellow,snk_list,snake_size)
            # pygame.draw.rect
            screen_score("Score:"+str(score),blue,10,5)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

welcome()
game_loop()