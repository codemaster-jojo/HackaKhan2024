import pygame
import random

# Initialize pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set the snake and food sizes
BLOCK_SIZE = 20

# Set the speed of the snake
SPEED = 20

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Function to draw the snake
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Function to generate food
def generate_food():
    food_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return food_x, food_y

# Main function for the game
def game():
    # Initialize the snake
    snake = [[SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]]
    snake_direction = "RIGHT"
    change_to = snake_direction

    # Initialize food
    food_x, food_y = generate_food()

    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    change_to = "RIGHT"
                elif event.key == pygame.K_UP and snake_direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and snake_direction != "UP":
                    change_to = "DOWN"

        # Change snake direction
        snake_direction = change_to

        # Move the snake
        if snake_direction == "UP":
            new_head = [snake[0][0], snake[0][1] - BLOCK_SIZE]
        elif snake_direction == "DOWN":
            new_head = [snake[0][0], snake[0][1] + BLOCK_SIZE]
        elif snake_direction == "LEFT":
            new_head = [snake[0][0] - BLOCK_SIZE, snake[0][1]]
        elif snake_direction == "RIGHT":
            new_head = [snake[0][0] + BLOCK_SIZE, snake[0][1]]

        snake.insert(0, new_head)

        # Check for collisions with walls
        if (snake[0][0] >= SCREEN_WIDTH or snake[0][0] < 0 or 
            snake[0][1] >= SCREEN_HEIGHT or snake[0][1] < 0):
            game_over()

        # Check for collisions with itself
        for block in snake[1:]:
            if snake[0] == block:
                game_over()

        # Check if snake has eaten food
        if snake[0][0] == food_x and snake[0][1] == food_y:
            food_x, food_y = generate_food()
        else:
            snake.pop()

        # Clear the screen
        screen.fill(BLACK)

        # Draw the snake and food
        draw_snake(snake)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Update the display
        pygame.display.update()

        # Set the game speed
        pygame.time.Clock().tick(SPEED)

# Function to handle game over
def game_over():
    font = pygame.font.SysFont(None, 50)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, [SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 25])
    pygame.display.update()
    pygame.time.delay(2000)
    game()

# Start the game
game()