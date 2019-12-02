import pygame
pygame.init()

#Setting game screen variables
screenWidth = 825
screenHeight = 480
win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Tetris')

#Walking animation boring
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]

walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

#Setting character variables
x=150
y=400
width = 64
height = 64
velocity = 10
isJump = False
jumpCount = 10
right = False
left = False
walkCount = 0

def resetScreen():
    global walkCount
    #Filling windowblankl
    win.blit(bg,(0,0))

    #Drawing our object
    if walkCount + 1 >= 27:
        walkCount = 0
    
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))
    #Updating the game screen
    pygame.display.update()

#Main game loop 
run = True
while run:
    #Time delay for game (how fast game runs) FPS
    clock.tick(27)

    #Gets list of all events that are happening
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If we hit the X program closes.
            run = False


    #Something different happening for each key press 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-=velocity
        if x < 0:
            x = 0
        left = True
        right = False

    elif keys[pygame.K_RIGHT]:
        x+=velocity
        if x > screenWidth-width:
            x=screenWidth-width
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_ESCAPE]:
            break

        if keys[pygame.K_SPACE]: 
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y-= (jumpCount**2)/2 * neg 
            jumpCount -= 1
        
        else:
            isJump = False
            jumpCount = 10

    resetScreen()


pygame.quit()
