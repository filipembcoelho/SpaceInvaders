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

# background
background = pygame.image.load('images/background.png')

# Speed
speed = 1.5
enemySpeed = 1.5
bulletSpeed = 10

# Player
playerImg = pygame.image.load('images/player.png')
playerX = 368  # (800 / 2) - (64 / 2) = 368 (half of the screen)
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('images/enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 200)
enemyX_change = enemySpeed
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = playerY
bulletY_change = bulletSpeed
# ready - No bullet on screen
# fire - Bullet is moving
bulletState = "ready"

boundaryLeft = 0
boundaryRight = 800


# player coordinates
def player(x, y):
    screen.blit(playerImg, (x, y))


# enemy coordinates
def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    # start from the middle of the player ship
    screen.blit(bulletImg, (x + 16, y + 10))


# listen for the QUIT event on the screen - infinite loop
running = True
while running:
    # screen background with a RGB value
    screen.fill((0, 128, 128))  # teal color
    # background image
    screen.blit(background, (0, 0))

    # everything that happens inside the game window, should be inside this infinite loop
    for event in pygame.event.get():
        # quit event
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed
        if event.type == pygame.KEYDOWN:
            # player spaceship: check whether is right or left
            if event.key == pygame.K_LEFT:
                playerX_change = -speed
            if event.key == pygame.K_RIGHT:
                playerX_change = speed
            # bullet event when space is pressed
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # Player: boundary control for X axis
    if playerX < boundaryLeft:
        playerX = 0
    elif playerX > boundaryRight - shipWidth:
        playerX = boundaryRight - shipWidth

    # Bullet movement
    if bulletState == "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    # Enemy movement
    enemyX += enemyX_change

    # Enemy: boundary control for X and Y axis
    if enemyX <= boundaryLeft:
        enemyX_change = speed
        enemyY += enemyY_change
    elif enemyX >= boundaryRight - shipWidth:
        enemyX_change = -speed
        enemyY += enemyY_change

    # placement of objects
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
