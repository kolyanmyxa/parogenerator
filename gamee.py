import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))


x = 100
y = 300
x1 = 250
y1 = 200
dir = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    x = x + (1 * dir)
    if x > 500:
        dir = -1
    if x < 0:
        dir = 1

    x1 = x1 + (1 * dir)
    if x1 > 500:
        dir = -1
    if x1 < 0:
        dir = 1


    win.fill((255, 0, 225))
    pygame.draw.rect(win, (0, 225, 225), (100, 300, 100, 100))
    pygame.draw.rect(win, (0, 225, 225), (300, 300, 100, 100))
    pygame.draw.circle(win, (0, 225, 225), (x1, y1), radius=20)
    pygame.draw.rect(win, (0, 225, 225), (x, y, 50, 100))


    pygame.time.delay(10)
    pygame.display.update()