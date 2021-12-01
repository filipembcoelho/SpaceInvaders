import pygame
import random

# Initialize pygame package (mandatory)
pygame.init()

# Create the screen using the set_mode with width x height
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Title and Icon
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(pygame.image.load('images/ufo.png'))
shipWidth = 64

# Player
playerImg = pygame.image.load('images/player.png')
playerX = 368  # (800 / 2) - (64 / 2) = 368 (half of the screen)
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('images/enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 200)
enemyX_change = 0

speed = 0.1

boundaryLeft = 0
boundaryRight = 800


# player coordinates
def player(x, y):
    screen.blit(playerImg, (x, y))


# enemy coordinates
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# listen for the QUIT event on the screen - infinite loop
running = True
while running:
    # screen background with a RGB value
    screen.fill((0, 128, 128))  # teal color

    # everything that happens inside the game window, should be inside this infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed, check whether is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -speed
            if event.key == pygame.K_RIGHT:
                playerX_change = speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # boundary control for X axis
    if playerX < boundaryLeft:
        playerX = 0
    elif playerX > boundaryRight - shipWidth:
        playerX = boundaryRight - shipWidth

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
