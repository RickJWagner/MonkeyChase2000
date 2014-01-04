import pygame, sys, random, math, random

SCREEN_WIDTH = 1200
SCREEN_DEPTH = 600
lane_width = 50
line_bends = 1

import random

class Antagonist(pygame.sprite.Sprite):

    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_DEPTH:
            self.speed[1] = -self.speed[1]



class MyMonkeyClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        

class Course_charter:
     
    def __init__(self, height, width, lane_width, x_adjust, y_jump):
        self.height = height
        self.width = width
        self.lane_width = lane_width
        self.xadjust = x_adjust
        self.yjump = y_jump

    def make_line(self):
        plotpoints = []
        y = self.height / 2
        for x in range(0, self.width):
            if x % self.xadjust == 0:
                y += random.randint((-1 * self.yjump), self.yjump)
            if y < (self.lane_width + 1):
                y = self.lane_width
            if (y + self.lane_width) > self.height:
                y = self.height - (self.lane_width + 1)
            plotpoints.append([x, y])
        return plotpoints
    
def animate(group):
    
    for antagonist in group:
        group.remove(antagonist)
        if pygame.sprite.spritecollide(antagonist, group, False):
            antagonist.speed[0] = -antagonist.speed[0]
            antagonist.speed[1] = -antagonist.speed[1]
    
        group.add(antagonist)
        antagonist.move()
        screen.blit(antagonist.image, antagonist.rect)
 



pygame.init()
Clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_DEPTH])
screen.fill([255, 255, 255])
charter = Course_charter (SCREEN_DEPTH, SCREEN_WIDTH, lane_width, 350, 300)
pts = charter.make_line()
monkey = MyMonkeyClass("WMonkeyR_1.png", pts[0])
monkeys = []
monkeys.append(pygame.image.load("WMonkeyR_1.png"))
monkeys.append(pygame.image.load("WMonkeyR_2.png"))
monkeys.append(pygame.image.load("WMonkeyR_3.png"))

    
antagonists = pygame.sprite.Group()
antagonist1 = Antagonist("JonahsHead.png",[10,100], [20,20])
antagonist2 = Antagonist("LukesHead.png",[50,200], [50,40])
antagonist3 = Antagonist("SarahsHead.png",[300,300], [-10,20])
monkeyspeed = 20
antagonists.add(antagonist1)
antagonists.add(antagonist2)
antagonists.add(antagonist3)

imageCount = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pressedkeys = pygame.key.get_pressed()
    if pressedkeys[pygame.K_LEFT]:
        monkey.rect[0] -= monkeyspeed
    if pressedkeys[pygame.K_RIGHT]:
        imageCount += 1
        monkey.rect[0] += monkeyspeed
    if pressedkeys[pygame.K_UP]:
        monkey.rect[1] -= monkeyspeed
    if pressedkeys[pygame.K_DOWN]:
        monkey.rect[1] += monkeyspeed
    
    print monkey.rect[0], monkey.rect[1]
    Clock.tick(10)
    screen.fill([255, 255, 255])
    animate(antagonists)    
    pygame.draw.lines(screen, [255,0,0],False, pts, lane_width)
    
    if pygame.sprite.spritecollide(monkey, antagonists, False):
        print "BAM!"
        
        
    screen.blit(monkeys[(imageCount % 3)], monkey.rect)  # 25 is about half of monkey
  

    pygame.display.flip()