import pygame, sys
from pygame.locals import *
import random
 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 10
FramePerSec = pygame.time.Clock()
 
# Setting up color objects
RED   = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((400,400))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Jeu de serpent simple")


class BodyPart:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.apple = BodyPart(random.randrange(1, 40, 2) * 10, random.randrange(1, 40, 2) * 10)
        self.dx = 20
        self.dy = 0
        self.w = 10
        self.head = BodyPart(10, 50)
        self.queu = [ 
            BodyPart(self.head.x - self.dx*3, self.head.y),
            BodyPart(self.head.x - self.dx*2, self.head.y),
            BodyPart(self.head.x - self.dx*1, self.head.y)
        ]        

    def start(self):
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                self.handleDirections()

            DISPLAYSURF.fill(WHITE)

            self.moveSnake()
        
            FramePerSec.tick(FPS)
    
    def handleDirections(self):
        key_input = pygame.key.get_pressed()   
        if key_input[pygame.K_LEFT]:
            self.dx = -20
            self.dy = 0
        if key_input[pygame.K_UP]:
            self.dx = 0
            self.dy = -20
        if key_input[pygame.K_RIGHT]:
            self.dx = 20
            self.dy = 0
        if key_input[pygame.K_DOWN]:
            self.dx = 0
            self.dy = 20

    def moveSnake(self):
        # check collision
        self.checkCollisionWall()

        # check game over
        for bp in self.queu:
            if bp.x == self.head.x and bp.y == self.head.y:
                self.head = BodyPart(10, 50)
                self.queu = [ 
                    BodyPart(self.head.x - self.dx*3, self.head.y),
                    BodyPart(self.head.x - self.dx*2, self.head.y),
                    BodyPart(self.head.x - self.dx*1, self.head.y)
                ]
        
        # check eat apple 
        self.checkEatApple()

        # draw the snake
        self.drawSnake()
    
    def checkCollisionWall(self):
        if self.head.x > 390 and self.dx > 0:
            self.head.x = 10
        elif self.head.x < 10 and self.dx < 0:
            self.head.x = 390
        
        if self.head.y > 390 and self.dy > 0:
            self.head.y = 10
        elif self.head.y < 10 and self.dy < 0:
            self.head.y = 390

    def checkEatApple(self):
        if self.apple.x == self.head.x and self.apple.y == self.head.y:
            self.apple.x = random.randrange(1, 40, 2) * 10
            self.apple.y = random.randrange(1, 40, 2) * 10
        else:
            del self.queu[0]

        self.queu += [BodyPart(self.head.x, self.head.y)]
        self.head.x += self.dx
        self.head.y += self.dy

    def drawSnake(self):
        pygame.draw.circle(DISPLAYSURF, BLACK, (self.head.x, self.head.y), self.w)
        pygame.draw.circle(DISPLAYSURF, RED, (self.apple.x, self.apple.y), self.w)
        for bp in self.queu:
            pygame.draw.circle(DISPLAYSURF, BLUE, (bp.x, bp.y), self.w)


if __name__ == '__main__':
    s = Snake()
    s.start()
