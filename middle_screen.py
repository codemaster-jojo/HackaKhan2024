import pygame
import sys
import main

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 832
screen_height = 704
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("American History EdTech Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Add description function
def display_description():
    # Clear the screen
    
    # Display description
    font = pygame.font.SysFont('Arial', 16, bold=True)
    description_text = [
        "American Odyssey is an educational game designed to teach American history in an engaging way.",
        "Players will embark on a journey through key events and periods in American history,",
        "answering questions and if correct, will fight valiantly in a tower defense game.",
        "Explore, learn, and experience the story of America like never before!"
    ]
    y_offset = 450
    for line in description_text:
        desc = font.render(line, True, WHITE)
        desc_rect = desc.get_rect(center=(screen_width/2, y_offset))
        screen.blit(desc, desc_rect)
        y_offset += 30
    
    # Update the display
    pygame.display.flip()


# Button class
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.description_displayed = False

    def draw(self):
        # Change button color if hovered
        #color = self.hover_color if self.rect.collidepoint(pygame.mouse.get_pos()) else self.color
        color = GRAY
        pygame.draw.rect(screen, color, self.rect)
        
        # Render text
        font = pygame.font.SysFont(None, 30)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def update(self):
        # Execute action if button is clicked
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if self.action:
                self.action()
                self.description_displayed = True 


# Start game function
def start_game():
    main.main()

# Main menu function
def main_menu():
    # Load background image
    background_image = pygame.image.load("colonialbg.webp").convert() # colonialbg is our actual bg, not middlebg
    background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

    # Create buttons
    start_button = Button(screen_width/2 - 100, 250, 200, 50, "Start Game", GRAY, BLACK, start_game)
    about_button = Button(screen_width/2 - 100, 350, 200, 50, "About This Game", GRAY, BLACK, display_description)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw background
        screen.blit(background_image, (0, 0))

        # Draw title
        font = pygame.freetype.Font("font.ttf", 100)
        text_surface, rect = font.render("Colonial America", (0, 0, 0))
        text_width, text_height = text_surface.get_size()
        font.render_to(screen, (screen_width/2-text_width/2, 100), 'Colonial America', BLACK)
        # screen.blit(text_surface, rect)
        
        # Draw description
        '''
        font = pygame.font.SysFont(None, 14)
        desc = font.render("By Jonathan, Diya, Mishti, and Benjamin", True, WHITE)
        desc = pygame.transform.scale(desc, (desc.get_width() * 3, desc.get_height() * 3))
        desc_rect = desc.get_rect(center=(screen_width/2, 575))
        screen.blit(desc, desc_rect)
        '''

        font = pygame.freetype.Font("font.ttf", 25)
        text_surface, rect = font.render("By Jonathan, Diya, Mishti, and Benjamin", (0, 0, 0))
        text_width, text_height = text_surface.get_size()
        font.render_to(screen, (screen_width/2-text_width/2, 575), 'By Jonathan, Diya, Mishti, and Benjamin', WHITE)


        start_button.update()
        about_button.update()
        start_button.draw()
        about_button.draw()
        if about_button.description_displayed:
            about_button.draw()  # Redraw button
            display_description()  # Display description
        else:
            # Draw description
            font.render_to(screen, (screen_width/2-text_width/2, 575), 'By Jonathan, Diya, Mishti, and Benjamin', WHITE)

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    main_menu()
