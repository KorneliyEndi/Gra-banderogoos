import random
from os import listdir
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()
FPS = pygame.time.Clock()

screen = width, heigth = 800, 600
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

font = pygame.font.SysFont('Verdana', 20)

main_surface = pygame.display.set_mode(screen)

IMGS_PATH = 'goose'

#ball = pygame.Surface((20, 20))
#ball.fill(WHITE)
ball_imgs = [pygame.image.load(IMGS_PATH + '/' + file).convert_alpha() for file in listdir(IMGS_PATH)]
ball = ball_imgs[0]
ball_rect = ball.get_rect()
ball_speed = 5

def create_enemy():
    #enemy = pygame.Surface((20, 20))
    #enemy.fill(RED)
    enemy = pygame.transform.scale(pygame.image.load('enemy.png').convert_alpha(), (100, 50))
    enemy_rect = pygame.Rect(width, random.randint(0, heigth), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]

def create_bonus():    # Функція створення бонусів
    #bonus = pygame.Surface((20, 20))
    #bonus.fill(GREEN)
    bonus = pygame.transform.scale(pygame.image.load('bonus.png').convert_alpha(), (75, 75))
    bonus_rect = pygame.Rect(random.randint(0, width), -75, *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]

bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3



CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 3500)

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 2500)

CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 125)


img_index = 0
scores = 0
enemies = []
bonuses = []

is_woking = True
while is_woking:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_woking = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMG:
            img_index += 1
            if img_index == len(ball_imgs):
                img_index = 0
            ball = ball_imgs[img_index]

    pressed_keys = pygame.key.get_pressed()

    #main_surface.fill(WHITE)
    #main_surface.blit(bg, (0, 0))

    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():
        bgX = bg.get_width()
    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()

    main_surface.blit(bg, (bgX, 0))
    main_surface.blit(bg, (bgX2, 0))
    main_surface.blit(ball, ball_rect)
    main_surface.blit(font.render(str(scores), True, BLUE), (width - 30, 0))
    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < -100:
            enemies.pop(enemies.index(enemy))
        if ball_rect.colliderect(enemy[1]):
            is_woking = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom > heigth + 70:
            bonuses.pop(bonuses.index(bonus))
        if ball_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            scores += 1


    if pressed_keys[K_DOWN] and not ball_rect.bottom >= heigth:
        ball_rect = ball_rect.move(0, ball_speed)
    if pressed_keys[K_UP] and not ball_rect.top <= 0:
        ball_rect = ball_rect.move(0, -ball_speed)
    if pressed_keys[K_RIGHT] and not ball_rect.right >= width:
        ball_rect = ball_rect.move(ball_speed, 0)
    if pressed_keys[K_LEFT] and not ball_rect.left <= 0:
        ball_rect = ball_rect.move(-ball_speed, 0)

    print(len(enemies), len(bonuses))
    pygame.display.flip()
