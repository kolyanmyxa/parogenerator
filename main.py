import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))


x = 1 # здесь мы задаем ааааа икс вот да
y = 1 # а здесь ихрег
x1 = 250
y1 = 250
dir = 1
dir1 = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    x = x + (1 * dir)
    if x > 500:
        dir = -1
    if x < 0:
        dir = 1

    y = y + (1 * dir)
    if y > 500:
        dir = -1
    if y < 0:
        dir = 1

    x1 = x1 + (1 * dir)
    if x1 > 500:
        dir = -1
    if x1 < 0:
        dir = 1


    win.fill((255, 225, 225))
    pygame.draw.rect(win, (255, 0, 0), (100, 150, 300, 200),border_radius=50,border_top_left_radius=50,border_bottom_right_radius=50,border_top_right_radius=50,border_bottom_left_radius=50)
    pygame.draw.polygon(win, (255, 255, 255), [(240,280),(290,250), (240, 220)], False )
    pygame.draw.circle(win, (0, 255, 255),(x, y),radius= 20)
    pygame.display.set_caption("зверобоба")

    pygame.time.delay(10)
    pygame.display.update()
