import pygame
import os

# Initialize pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the colors
WHITE = (255, 255, 255)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Load the background image
background_image = pygame.image.load("background_ww1.jpg")

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Background Image")

# title text
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('World War One', True, WHITE)
textRect = text.get_rect()
textRect.center = (400,200)

mouse = [0,0]

# Main loop
running = True
while running:
    # Event handling
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
    
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if SCREEN_WIDTH/2 <= mouse[0] <= SCREEN_WIDTH/2+140 and SCREEN_HEIGHT/2 <= mouse[1] <= height/2+40: 
                pygame.quit() 

    # mouse position
    mouse = pygame.mouse.get_pos() 

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the background image on the screen
    screen.blit(background_image, (0, 0))
    screen.blit(text, textRect)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()