import pygame

# Initialize pygame package (mandatory)
pygame.init()

# Create the screen using the set_mode with height x width
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(pygame.image.load('images/ufo.png'))

# listen for the QUIT event on the screen - infinite loop
running = True
while running:
    # everything that happens inside the game window, should be inside this infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen background with a RGB value
    screen.fill((0, 128, 128))  # teal color
    pygame.display.update()

