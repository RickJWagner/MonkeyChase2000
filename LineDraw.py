import pygame, sys, random, math, random

SCREEN_WIDTH = 1200
SCREEN_DEPTH = 600
lane_width = 50
line_bends = 1

import random



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







while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.time.delay(200)
    pygame.draw.lines(screen, [255,0,0],False, pts, lane_width)
    screen.blit(monkey.image, monkey.rect)  # 25 is about half of monkey
    pygame.display.flip()