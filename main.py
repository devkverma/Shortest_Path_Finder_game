import sys
import pygame
import random
import numpy as np

from constants import *


pygame.init()
# MAIN SCREEN
screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Shortest Path Finder')
screen.fill(BGCOLOR)

class Board:
    def __init__(self):
        self.squares = np.zeros(( ROWS, COLS ))
        self.grid()
        self.obstacle()
        self.start()
        self.end()
        

    def grid(self):
        screen.fill(BGCOLOR)
        # vertical lines
        for x in range(SQSIZE , SCREEN_WIDTH, SQSIZE):
            pygame.draw.line(screen, GRIDCOLOR, (x, 0), (x, SCREEN_HEIGHT))

        # horizontal lines
        for y in range(SQSIZE, SCREEN_HEIGHT, SQSIZE):
            pygame.draw.line(screen, GRIDCOLOR, (0,y), (SCREEN_WIDTH,y))
    
    def obstacle(self):
        numberOfObstacles = random.randint(100,1000)
        for i in range(numberOfObstacles):
            row = random.randint(0,50)
            col = random.randint(0,50)

            rect = pygame.Rect(col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)
            pygame.draw.rect(screen, OBSTACLECOLOR, rect)
            self.squares[0][1] = 1
    
    def start(self):
        row = random.randint(0,49)
        col = random.randint(0,49)

        if self.squares[row][col] == 0:
            rect = pygame.Rect(col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)
            pygame.draw.rect(screen, STARTCOLOR, rect)
            self.squares[row][col] = 2
            return
        
        else:
            self.start()
    
    def end(self):
        row = random.randint(0,49)
        col = random.randint(0,49)

        if self.squares[row][col] == 0:
            rect = pygame.Rect(col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)
            pygame.draw.rect(screen, ENDCOLOR, rect)
            self.squares[row][col] = 2
            return
        
        else:
            self.end()

    def reset(self):
        self.__init__()

def main():

    board = Board()
    while True:

        for event in pygame.event.get():
                 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
            
            if event.type == pygame.KEYDOWN:
                # r - reset
                if event.key == pygame.K_r:
                    board.reset()
                

        pygame.display.update()

main()