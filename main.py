import pygame

# Initialize pygame package (mandatory)
pygame.init()

# Create the screen using the set_mode with height x width
screen = pygame.display.set_mode((800, 600))

# listen for the QUIT event on the screen - infinite loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
