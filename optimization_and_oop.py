import pygame
pygame.init()

screenwidth=480

win= pygame.display.set_mode((screenwidth,screenwidth))
caption=pygame.display.set_caption("Character Animation & Optimized")

walkRight=[pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walkLeft=[pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png'),]
bg=pygame.image.load('bg.jpg')
char=pygame.image.load('standing.png')

clock=pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if character.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))

def redrawGameWindow():
    win.blit(bg,(0,0))
    character.draw(win)
    pygame.display.update()

run=True
character=player(50,415,64,64)
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and character.x>character.vel:
        character.x-=character.vel
        character.left=True
        character.right=False
    elif keys[pygame.K_RIGHT] and character.x<screenwidth-character.width-character.vel:
        character.x+=character.vel
        character.left=False
        character.right=True
    else:
        character.right=False
        character.left=False
        character.walkCount=0
    if not(character.isJump):
        if keys[pygame.K_SPACE]:
            character.isJump=True
            character.right=False
            character.left=False
            character.walkCount=0
    else:
        if character.jumpCount >= -10:
            neg = 1
            if character.jumpCount < 0:
                neg = -1
            character.y -= (character.jumpCount ** 2) * 0.5 * neg
            character.jumpCount-=1
        else:
            character.isJump = False
            character.jumpCount = 10

    redrawGameWindow()

pygame.quit()