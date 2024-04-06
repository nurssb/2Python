import pygame  # type: ignore
pygame.init()
import random  


screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption("Jump-Jump")
pygame.display.set_icon(pygame.image.load("ball.png")) #создание окно
clock=pygame.time.Clock()

wall_x=600
wall_y=450
ball_x=200
ball_y=250
ball_max=600-60
ball_min=0
len=250

game_over=pygame.Surface((800,500))
RedBall=pygame.image.load("RedBall.png")
ball=pygame.Surface((60,60))   #создание сурфейсс

def GameOver():
    game_over.fill((0,0,255))
    screen.blit(game_over,(110,50))
    pygame.display.update()
    pygame.time.wait(2000)
    exit()

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if ball_max>ball_y>ball_min:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:     #jump
                ball_y-=50
                
        
    wall_up=pygame.Surface((80,len))
    wall_down=pygame.Surface((80,(600-len-150)))
    wall_up.fill((0,255,100))
    wall_down.fill((0,255,100))
    ball.fill((255,0,0))
    if wall_x>0:                        #анимация стены
        wall_x-=2
    else:
        wall_x=1000
        len=random.uniform(0,450)
        wall_y=len+250
    screen.fill((0,0,0))
    screen.blit(wall_down,(wall_x,wall_y))
    screen.blit(wall_up,(wall_x,0))

    if ball_y<ball_max:                 #границы обекта
        ball_y+=1
    if ball_y<ball_min:
        ball_y=ball_min
    if ball_y==ball_max or ((ball_x+60)==wall_x and (ball_y+60)>=wall_y) or ((ball_x+60)>=wall_x and (ball_y+60)==wall_y) or ((ball_x+60)>=wall_x and ball_y<=len):
        GameOver()
    
    screen.blit(RedBall,(ball_x,ball_y))
    
    pygame.display.update()
    clock.tick(60)