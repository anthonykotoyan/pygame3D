import pygame

import math
import time

pygame.init()
width, length = 1280, 720
screen = pygame.display.set_mode((width, length))
clock = pygame.time.Clock()
running = True
dt = 0

cam_pos = pygame.Vector3(width / 2, length / 2, 0)
cam_x_fov = 90
screen_distance = (width / 2) / math.tan(math.radians(cam_x_fov / 2))

speed = 100

d = 500
l = 100

square1 = [
        pygame.Vector3(width / 2 - l/2, length / 2 - l/2, d),
        pygame.Vector3(width / 2 + l/2, length / 2 - l/2, d),
        pygame.Vector3(width / 2 + l/2, length / 2 + l/2, d),
        pygame.Vector3(width / 2 - l/2, length / 2 + l/2, d)
]
square2 = [
        pygame.Vector3(width / 2 - l/2, length / 2 - l/2, d+l),
        pygame.Vector3(width / 2 + l/2, length / 2 - l/2, d+l),
        pygame.Vector3(width / 2 + l/2, length / 2 + l/2, d+l),
        pygame.Vector3(width / 2 - l/2, length / 2 + l/2, d+l)
]

square3 = [
        pygame.Vector3(width / 2 - l / 2, length / 2 - l / 2, d),
        pygame.Vector3(width / 2 - l/2, length / 2 - l/2, d+l),
        pygame.Vector3(width / 2 - l/2, length / 2 + l/2, d+l),
        pygame.Vector3(width / 2 - l/2, length / 2 + l/2, d)
]
square4 = [
        pygame.Vector3(width / 2 + l/2, length / 2 - l/2, d),
        pygame.Vector3(width / 2 + l/2, length / 2 - l/2, d+l),
        pygame.Vector3(width / 2 + l/2, length / 2 + l/2, d+l),
        pygame.Vector3(width / 2 + l/2, length / 2 + l/2, d)
]


# scuffed prob
def screen_space(point):

    dx = (point.x - cam_pos.x)
    dy = (point.y - cam_pos.y)

    dz = (point.z - cam_pos.z)

    x = screen_distance * dx / dz + width/2
    y = screen_distance * dy / dz + length/2

    return pygame.Vector2(x, y)


def draw_square(square):
    for i in range(len(square)):
        if i == 3:
            j = -1
        else:
            j = i
        pygame.draw.line(screen, "white", screen_space(square[i]), screen_space(square[j+1]), 5)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    if pygame.key.get_pressed()[pygame.K_w]:
        cam_pos.z += speed*dt
    if pygame.key.get_pressed()[pygame.K_s]:
        cam_pos.z -= speed*dt
    if pygame.key.get_pressed()[pygame.K_t]:
        cam_pos.y -= speed*dt
    if pygame.key.get_pressed()[pygame.K_g]:
        cam_pos.y += speed*dt
    if pygame.key.get_pressed()[pygame.K_a]:
        cam_pos.x -= speed*dt
    if pygame.key.get_pressed()[pygame.K_d]:
        cam_pos.x += speed*dt



    draw_square(square1)
    draw_square(square2)
    draw_square(square3)
    draw_square(square4)
    pygame.draw.circle(screen, "green", screen_space(pygame.Vector3(width / 2 - l / 4, length / 2, d)), 10)
    pygame.draw.circle(screen, "green", screen_space(pygame.Vector3(width / 2 + l / 4, length / 2, d)), 10)
    pygame.draw.line(screen, "green", screen_space(pygame.Vector3(width / 2 - l / 3, length / 2 + l / 5, d)), screen_space(pygame.Vector3(width / 2 + l / 3, length / 2 + l / 5, d)), 5)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
