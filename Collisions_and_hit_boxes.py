import pygame
pygame.init()

screenwidth=480

win= pygame.display.set_mode((screenwidth,screenwidth))
caption=pygame.display.set_caption("Character Animation & Projectiles")

walkRight=[pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
walkLeft=[pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png'),]
bg=pygame.image.load('bg.jpg')

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
        self.standing=True
        self.hitbox=(self.x+20,self.y,28,64)

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
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
        self.hitbox=(self.x+20,self.y,28,64)
        pygame.draw.rect(win,(0,0,0),self.hitbox,2)

class projectile(object):
    def __init__(self,x,y,radius,colour,facing):
        self.x=x
        self.y=y
        self.vel=10*facing
        self.radius=radius
        self.colour=colour
        self.facing=facing

    def draw(self,win):
        pygame.draw.circle(win,self.colour,(self.x,self.y),self.radius)

class enemy(object):
    walkLeft=[pygame.image.load('L1E.png'),pygame.image.load('L2E.png'),pygame.image.load('L3E.png'),pygame.image.load('L4E.png'),pygame.image.load('L5E.png'),pygame.image.load('L6E.png'),pygame.image.load('L7E.png'),pygame.image.load('L8E.png'),pygame.image.load('L9E.png'),pygame.image.load('L10E.png'),pygame.image.load('L11E.png')]
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    def  __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.path=[self.x,self.end]
        self.walkCount=0
        self.vel=4
        self.hitbox=(self.x+20,self.y-5,28,64)

    def draw(self,win):
        self.move()
        if self.walkCount + 1 >=33:
            self.walkCount=0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x+20,self.y-5,28,64)
        pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel>0:
            if self.x + self.vel < self.path[1]:
                self.x+=self.vel
            else:
                self.vel = self.vel*-1
                self.walkCount=0
        else:
            if self.x + self.vel > self.path[0]:
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.walkCount = 0

    def hit(self):
        print("Goblin Hit")

goblin=enemy(40,420,64,64,400)

def redrawGameWindow():
    win.blit(bg,(0,0))
    character.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

run=True
character=player(200,415,64,64)
bullets=[]
multiple_bullets = 0
while run:
    clock.tick(27)

    if multiple_bullets > 0:
        multiple_bullets+=1
    if multiple_bullets > 3:
        multiple_bullets=0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    for bullet in bullets:
        if bullet.y + bullet.radius <= goblin.hitbox[1] + goblin.hitbox[3] and bullet.y -bullet.radius >= goblin.hitbox[1] :
            if bullet.x + bullet.radius <= goblin.hitbox[0] + goblin.hitbox[2] and bullet.x - bullet.radius >= goblin.hitbox[0] :
                goblin.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < screenwidth and bullet.x>0 :
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and multiple_bullets==0:
        if character.left:
            facing=-1
        else:
            facing=1
        if len(bullets) < 5:
            bullets.append(projectile(round(character.x+character.width//2),round(character.y+character.height//2),4,(255,0,0),facing) )
        multiple_bullets=1

    if keys[pygame.K_LEFT] and character.x>character.vel:
        character.x-=character.vel
        character.left=True
        character.right=False
        character.standing=False
    elif keys[pygame.K_RIGHT] and character.x<screenwidth-character.width-character.vel:
        character.x+=character.vel
        character.left=False
        character.right=True
        character.standing=False
    else:
        character.standing=False
        character.walkCount=0
    if not(character.isJump):
        if keys[pygame.K_UP]:
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