import pygame, pymunk, pymunk.pygame_util
pygame.init()

size = (800, 400)
screen = pygame.display.set_mode(size)
title = "등가속도 운동 법칙 실습" 
pygame.display.set_caption(title)

clock = pygame.time.Clock() 
space = pymunk.Space()
space.gravity = (0, 9.81)
draw_options = pymunk.pygame_util.DrawOptions(screen)

floor = pymunk.Body(body_type = pymunk.Body.STATIC)
floor.position = (0, size[1]-50)
floor_shape = pymunk.Segment(floor, (0,0), (size[0],-100), 1)
floor_shape.elasticity = 1
floor_shape.friction = 0.2
space.add(floor, floor_shape)

ball = pymunk.Body(1, 1)
ball.position = (size[0]/2, 50)
ball_shape = pymunk.Circle(ball, 1)
ball_shape.mass = 1 # 질량
ball_shape.elasticity = 0.5 # 탄성
ball_shape.friction = 0.2 # 마찰
space.add(ball, ball_shape)

working = True
while working:
    clock.tick(60) 
    space.step(1/60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
            
    screen.fill((0,0,0))
    screen.
    space.debug_draw(draw_options)
    pygame.display.flip()

pygame.quit()
