import pygame # type: ignore
import random

pygame.init()

screen=pygame.display.set_mode((400,600))           #все параметры и ресурсы
road=pygame.image.load("road.png")
my_car=pygame.image.load("Player.png")
cars=pygame.image.load("Enemy.png")
clock=pygame.time.Clock()
x=185
y=500
cars_x=60
cars_y=0
speed=5
number=0

num_font = pygame.font.Font(None, 36)

run=True
while run:
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            pygame.quit()                   #управление
                                                
        qimyl=pygame.key.get_pressed()
        if qimyl[pygame.K_RIGHT]:x+=20
        if qimyl[pygame.K_LEFT]:x-=20

    if cars_y==600:                     #рандомные дбижение обекты
        cars_y=0
        number+=1
        cars_x=random.uniform(60,240)
    else:
        cars_y+=speed

    if ( cars_x<=x<=(cars_x+40) or cars_x<=(x+40)<=(cars_x+40) ) and (cars_y+80)==y:             #авария
        screen.fill((255,0,0))
        font = pygame.font.Font(None, 75)
        game_over = font.render("GAME OVER!", True, (0,0,0))
        screen.blit(game_over,(30,300))
        pygame.display.update()
        pygame.time.wait(4000)
        exit()
                                

    num_f = num_font.render(str(number), True, (0,0,0))         #счетчик
    screen.blit(road,(0,0))                                     #перевернуть и обнавит скрин
    screen.blit(num_f,(20,20))             
    screen.blit(my_car,(x,y))
    screen.blit(cars,(cars_x,cars_y))
    pygame.display.flip()
    clock.tick(60)


