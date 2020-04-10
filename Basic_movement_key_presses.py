import pygame
pygame.init()

screenwidth=int(input("Enter the screen size in pixels : "))

win= pygame.display.set_mode((screenwidth,screenwidth))
caption=pygame.display.set_caption("Basic Movements")

x=250
y=250
width=50
height=20
vel=10

run=True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>vel:
        x-=vel
    if keys[pygame.K_RIGHT] and x<screenwidth-width-vel:
        x+=vel
    if keys[pygame.K_UP] and y>vel:
        y-=vel
    if keys[pygame.K_DOWN] and y<screenwidth-height-vel:
        y+=vel

    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()
pygame.quit()