import sys
import pygame
import random
import math
import heapq
import numpy as np

from constants import *



pygame.init()
# MAIN SCREEN
screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT),pygame.NOFRAME)
pygame.display.set_caption('Shortest Path Finder')
screen.fill(BGCOLOR)

clock = pygame.time.Clock()

class Board:
    def __init__(self):
        self.squares = np.zeros(( ROWS, COLS ))
        screen.fill(BGCOLOR)
        self.obstacle()
        self.Start = self.start()
        self.End = self.end()
        
    
    def obstacle(self):
        numberOfObstacles = random.randint(100,1000)
        for i in range(numberOfObstacles):
            row = random.randint(0,49)
            col = random.randint(0,49)

            rect = pygame.Rect(col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)
            pygame.draw.rect(screen, OBSTACLECOLOR, rect)
            self.squares[row][col] = 5
    
    def start(self):
        row = random.randint(0,24)
        col = random.randint(0,24)

        while self.squares[row][col] != 0:
            row = random.randint(0,24)
            col = random.randint(0,24)
        rect = pygame.Rect(col*SQSIZE,row*SQSIZE,SQSIZE,SQSIZE)
        pygame.draw.rect(screen,STARTCOLOR,rect)
        self.squares[row][col] = 1
        return row,col
    
    def end(self):
        row = random.randint(25,49)
        col = random.randint(25,49)

        while self.squares[row][col] != 0:
            row = random.randint(25,49)
            col = random.randint(25,49)
        rect = pygame.Rect(col*SQSIZE,row*SQSIZE,SQSIZE,SQSIZE)
        pygame.draw.rect(screen,ENDCOLOR,rect)
        self.squares[row][col] = 2
        return row,col
    
    def colorBox(self,x,y,color):
        rect = pygame.Rect(y*SQSIZE,x*SQSIZE,SQSIZE,SQSIZE)
        pygame.draw.rect(screen,color,rect)
        self.squares[x][y] = 3
        clock.tick(38)
        pygame.display.update()
        
        

    def reset(self):
        self.squares = np.zeros(( ROWS, COLS ))
        screen.fill(BGCOLOR)
        self.obstacle()
        self.Start = self.start()
        self.End = self.end()
        

class AI:
    def __init__(self,board):
        self.rows = ROWS
        self.cols = COLS
        self.board = board
        self.start = board.Start
        self.end = board.End
        pass

    def heuristic(self,a,b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def neighbors(self,node):
        x,y = node
        for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1),(-1,-1),(-1,1),(1,-1),(1,1)]:
            cost = math.sqrt(dx**2 + dy**2)
            nx,ny = x+dx,y+dy
            if (0<=nx<self.rows and 0<=ny<self.cols) and self.board.squares[nx][ny] != 5:
                self.board.colorBox(nx,ny,YELLOW)
    
                yield (nx,ny),cost
                
    
    def recontruct_path(self,came_from,current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path
    
    def astar(self):
        rows,cols = ROWS,COLS
        open_list = []
        heapq.heappush(open_list,(0+self.heuristic(self.start,self.end),0,self.start))
        came_from = {}
        cost_so_far = {self.start:0}

        while open_list:
            _,current_cost,current = heapq.heappop(open_list)

            if current == self.end:
                return self.recontruct_path(came_from,current)
            
            for neighbor,cost in self.neighbors(current):
                new_cost = cost_so_far[current] + cost
                if (neighbor not in cost_so_far) or (new_cost<cost_so_far[neighbor]):
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor,self.end)
                    heapq.heappush(open_list,(priority,new_cost,neighbor))
                    came_from[neighbor] = current
                    x,y = neighbor
                    self.board.colorBox(x,y,MAROON)
                    
        return None

def main():

    

    board = Board()
    ai = AI(board)
    while True:

        for event in pygame.event.get():
                 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                # r - reset
                if event.key == pygame.K_r:
                    board.reset()
                    ai = AI(board)
                

                
                if event.key == pygame.K_SPACE:
                    path = ai.astar()
                    for x,y in path:
                        board.colorBox(x,y,ENDCOLOR)

                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                        

                
        
        pygame.display.update()


main()