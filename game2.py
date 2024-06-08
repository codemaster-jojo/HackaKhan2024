import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_SIZE = 50
PLAYER_SPEED = 5
ENEMY_SIZE = 30
OBSTACLE_SIZE = 40
LEVELS = ["Colonial America", "Revolutionary War", "Civil War", "World War I", "World War II", "Vietnam War"]

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chronos Quest")

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_SIZE, OBSTACLE_SIZE))
        self.image.fill((255, 0, 0))  # Red color for obstacles
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.image.fill((0, 0, 255))  # Blue color for enemies
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.rect.right = 0

# Level class
class Level:
    def __init__(self, name):
        self.name = name
        self.obstacles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

    def start(self):
        print("Starting level:", self.name)
        if self.name == "Colonial America":
            # Add some obstacles and enemies for this level
            for _ in range(5):
                x = random.randint(0, WIDTH)
                y = random.randint(0, HEIGHT)
                obstacle = Obstacle(x, y)
                self.obstacles.add(obstacle)

            for _ in range(3):
                x = random.randint(0, WIDTH)
                y = random.randint(0, HEIGHT)
                enemy = Enemy(x, y)
                self.enemies.add(enemy)

    def finish(self):
        print("Finishing level:", self.name)

# Function to handle events
def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Main function
def main():
    clock = pygame.time.Clock()
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    current_level = 0
    levels = [Level(name) for name in LEVELS]

    levels[current_level].start()

    while True:
        event_handler()

        player.update()

        # Check for collisions with obstacles
        obstacle_collisions = pygame.sprite.spritecollide(player, levels[current_level].obstacles, False)
        if obstacle_collisions:
            print("Player collided with an obstacle!")
            # Handle collision behavior here (e.g., reset player position)

        # Check for collisions with enemies
        enemy_collisions = pygame.sprite.spritecollide(player, levels[current_level].enemies, False)
        if enemy_collisions:
            print("Player collided with an enemy!")
            # Handle collision behavior here (e.g., decrease player health)

        screen.fill(BLACK)
        for obstacle in levels[current_level].obstacles:
            screen.blit(obstacle.image, obstacle.rect)
        for enemy in levels[current_level].enemies:
            enemy.update()
            screen.blit(enemy.image, enemy.rect)

        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()