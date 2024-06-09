import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("American History EdTech Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Load background image

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.hovered = False

    def draw(self):
        # Change button color if hovered
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        
        # Render text
        font = pygame.font.SysFont(None, 30)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def update(self):
        # Check if mouse is hovering over the button
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(mouse_pos)

        # Execute action if button is clicked
        if self.hovered and pygame.mouse.get_pressed()[0]:
            if self.action:
                self.action()

# Start game function
def start_game():
    print("Starting game...")

# Quit game function
def quit_game():
    pygame.quit()
    sys.exit()

# Main menu function
def main_menu():

    background_image = pygame.image.load("world_war_one/static/background.jpg").convert()
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
    screen.blit(background_image, (0, 0))
    # Draw title
    font = pygame.font.SysFont('Times New Roman', 70, bold=True)
    title = font.render("American Odyssey", True, WHITE)
    title_rect = title.get_rect(center=(screen_width/2, 100))
    screen.blit(title, title_rect)
    font = pygame.font.SysFont('Times New Roman', 24)
    desc = font.render("By Jonathan, Diya, Mishti, and Benjamin", True, WHITE)
    desc_rect = desc.get_rect(center=(screen_width/2, 525))
    screen.blit(desc, desc_rect)
    # Create buttons
    start_button = Button(screen_width/2 - 100, 250, 200, 50, "Start Game", GRAY, BLACK, start_game)
    quit_button = Button(screen_width/2 - 100, 350, 200, 50, "Quit Game", GRAY, BLACK, quit_game)

    # Add buttons to sprite group
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        #screen.fill(WHITE)

        # Draw buttons
        start_button.draw()
        quit_button.draw()

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main_menu()
