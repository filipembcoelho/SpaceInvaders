import pygame

# Initialize pygame package (mandatory)
pygame.init()

# Create the screen using the set_mode with width x height
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(pygame.image.load('images/ufo.png'))

# Player
playerImg = pygame.image.load('images/player.png')
playerX = 368  # (800 / 2) - (64 / 2) = 368 (half of the screen)
playerY = 480


def player(x, y):
    screen.blit(playerImg, (x, y))


# listen for the QUIT event on the screen - infinite loop
running = True
while running:
    # screen background with a RGB value
    screen.fill((0, 128, 128))  # teal color

    # everything that happens inside the game window, should be inside this infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # for illusion of movement only
    # playerX += 0.1
    # playerY -= 0.1
    player(playerX, playerY)
    pygame.display.update()


