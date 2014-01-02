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
    
    

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_DEPTH])
screen.fill([255, 255, 255])
charter = Course_charter (SCREEN_DEPTH, SCREEN_WIDTH, lane_width, 350, 300)
pts = charter.make_line()
monkey = MyMonkeyClass("monkey1.jpeg", pts[0])
antagonists = []
antagonist = Antagonist("JonahsHead.png",[10,100], [20,20])
antagonist2 = Antagonist("LukesHead.png",[50,200], [50,40])
antagonist3 = Antagonist("SarahsHead.png",[300,300], [-10,20])


antagonists.append(antagonist)
antagonists.append(antagonist2)
antagonists.append(antagonist3)








while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(200)
    screen.fill([255, 255, 255])
    pygame.draw.lines(screen, [255,0,0],False, pts, lane_width)
    screen.blit(monkey.image, monkey.rect)  # 25 is about half of monkey
    for antagonist in antagonists:
        antagonist.move()
        screen.blit(antagonist.image, antagonist.rect)

    pygame.display.flip()