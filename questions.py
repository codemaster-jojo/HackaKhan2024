import pygame
import sys
import random
import os
# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("American History Quiz")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
ORANGE = (250, 147, 95)
GREEN = (166, 237, 149)
BLUE = (166, 208, 245)
# Fonts
font = pygame.font.SysFont('Arial', 16)
answer_font = pygame.font.SysFont('Arial', 24)
index = random.randint(0,4) * 2
indices = []
while True:
    if index in indices:
        index = random.randint(0,4)*2
    else:
        break
with open('question_list.txt', 'r') as f:
    content = f.readlines()
    q_list = [line.strip() for line in content]  # Simplified list creation
    index = 0  # You need to define the index variable
    if index < len(q_list) - 1:  # Check if index is within bounds
        question = q_list[index]
        answers = q_list[index + 1]
        print(answers)
        answer_list = answers.split(',')  # Split answers by commas
        print(answer_list)
    else:
        print("Index out of range.")
    

# Sample question and answers
correct_answer = 0

# Main function to display the question and answers
# Main function to display the question and answers
# Main function to display the question and answers
# Main function to display the question and answers
# Main function to display the question and answers
# Global variables
shuffled_answers = []


# Main function to display the question and answers
# Main function to display the question and answers

# Main function to display the question and answers
def display_question():
    global screen_width
    global answer_buttons
    
    answer_buttons = []  # Clear answer_buttons list
    # Clear the screen
    screen.fill(WHITE)
    
    # Display the question
    question_text = font.render(question, True, BLACK)
    question_rect = question_text.get_rect(center=(screen_width/2, screen_height/3 - 50))
    screen.blit(question_text, question_rect)
    
    # Display the answers
    answer_y = screen_height/2
    color = WHITE
    for i in range(0, len(answer_list)):
        answer_text = answer_font.render(answer_list[i], True, WHITE)
        answer_rect = answer_text.get_rect(center=(screen_width/2, answer_y))
        answer_rect_outer = answer_rect.inflate(100, 50)  # Inflate the rectangle to create some padding
        if i == 0:
            color = ORANGE
        elif i == 1:
            color = GREEN
        else:
            color = BLUE
        pygame.draw.rect(screen, color, answer_rect_outer)  # Draw the rectangle
    
        screen.blit(answer_text, answer_rect)
        answer_button_rect = pygame.Rect(answer_rect_outer)
        answer_button_rect.center = (screen_width/2, answer_y)
        answer_buttons.append((answer_button_rect, i))
        answer_y += 100
    
    # Update the display
    pygame.display.flip()

# Function to check if the player clicked on the correct answer
def check_answer(mouse_pos):
    global correct_answer
    global answer_selected
    if not answer_selected:  # Check if an answer has already been selected
        for button_rect, answer_index in answer_buttons:
            if button_rect.collidepoint(mouse_pos):
                if answer_index == correct_answer:
                    print("Correct!")
                else:
                    print("Incorrect!")
                answer_selected = True  # Set flag to True after an answer has been selected

# Main game loop
running = True
current_question_index = 0  # Index to track the current question
answer_buttons = []
answer_selected = False  # Flag to track if an answer has been selected

while running:
    # Load the current question and answers
    index = current_question_index * 2
    question = q_list[index]
    answers = q_list[index + 1]
    answer_list = answers.split(',')
    correct_answer = 0  # Set the correct answer index
    
    # Shuffle the answers if they haven't been shuffled yet for this question
    if 'shuffled_answers' not in globals():
        shuffled_answers = random.sample(answer_list, len(answer_list))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            check_answer(mouse_pos)
            if answer_selected:  # Move to the next question after an answer has been selected
                current_question_index += 1
                if current_question_index >= len(q_list) // 2:  # End the game if all questions have been asked
                    running = False
                answer_selected = False  # Reset the answer_selected flag
    
    # Display the question GUI
    display_question()

# Quit Pygame
pygame.quit()
sys.exit()
