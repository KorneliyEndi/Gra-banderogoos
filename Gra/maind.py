import pygame
from pygame.constants import QUIT

pygame.init()

screen = width, heigth = 800, 600

main_surface = pygame.display.set_mode(screen)

RED = 255, 0, 0
GREEN = 0, 255, 0

ball = pygame.Surface((20, 20))
ball.fill((255, 255, 255))
bal_rect = ball.get_rect()
ball_speed = [1, 1]

is_woking = True
while is_woking:
    for event in pygame.event.get():
        if event == QUIT:
            is_woking = False
    bal_rect = bal_rect.move(ball_speed)
    if bal_rect.bottom >= heigth or bal_rect.top <= 0:
        ball_speed[1] = - ball_speed[1]
        ball.fill(RED) #255, 0, 0
    if bal_rect.right >= width or bal_rect.left <= 0:
        ball_speed[0] = - ball_speed[0]
        ball.fill(GREEN) #0, 255, 0

    main_surface.fill((0, 0, 0))

    main_surface.blit(ball, bal_rect)

    #main_surface.fill((155, 155, 155))
    pygame.display.flip()