import pygame

# Initialize Pygame
pygame.init()

#making 2d list big buba
board = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2]
]
for x in range(8):
    print(board[x])

# Set up the game window
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Hello Pygame")
def move_piece(x,y):
    
    #print(x,y)
    if board[x][y] == 1:
        if board[x+1][y-1] == 0:
            board[x+1][y-1] = 1
        if board[x+1][y+1] ==0:
            board[x+1][y-1] = 1
    if board[x][y] == 2:
        print (board[x][y])
        print (board[x][y])
    
    selected = board[x][y]
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #print(f"Mouse button {event.button} pressed at {event.pos}")
            move_piece(event.pos[1]//100,event.pos[0]//100)
            #board[event.pos[1]//100][event.pos[0]//100] = 0
            
    """ elif event.type == pygame.MOUSEBUTTONUP:
            print(f"Mouse button {event.button} released at {event.pos}")
        elif event.type == pygame.MOUSEMOTION:
            print(f"Mouse moved to {event.pos}")"""
    screen.fill((140, 111, 88))

    for x in range(8):
        for y in range(8): 
            if x % 2 == 1 and y % 2 == 0:
                pygame.draw.rect(screen, (105,51,9),(x*100,y*100,100,100))
            if x % 2 == 0 and y % 2 == 1:
                pygame.draw.rect(screen, (105,51,9),(x*100,y*100,100,100))    

    for x in range(8):
        for y in range(8):
            if board[x][y] == 1:
                pygame.draw.circle(screen, (255,255,255),(y*100+50,x*100+50), 40)
            if board[x][y] == 2:
                pygame.draw.circle(screen, (0,0,0),(y*100+50,x*100+50), 40)
    pygame.display.flip()
pygame.quit()





















