import pygame
import os

import pygame
import os

# Initialize pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the colors
WHITE = (255, 255, 255)

# Set the background image path
background_image_path = "background.jpg"

# Load the background image
background_image = pygame.image.load(background_image_path)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense")

waypoints = []

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the background image on the screen
    screen.blit(background_image, (0, 0))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
