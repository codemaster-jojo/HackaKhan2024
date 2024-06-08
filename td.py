import pygame
import math
import time

pygame.init()

screen = pygame.display.set_mode((832, 704))
pygame.display.set_caption("Tower Defense")

# IMAGES
path_NE = pygame.image.load('path_sprites/NE.png')
path_NE = pygame.transform.scale(path_NE, (64, 64))

path_NS = pygame.image.load('path_sprites/NS.png')
path_NS = pygame.transform.scale(path_NS, (64, 64))

path_NW = pygame.image.load('path_sprites/NW.png')
path_NW = pygame.transform.scale(path_NW, (64, 64))

path_SW = pygame.image.load('path_sprites/SW.png')
path_SW = pygame.transform.scale(path_SW, (64, 64))

path_ES = pygame.image.load('path_sprites/ES.png')
path_ES = pygame.transform.scale(path_ES, (64, 64))

path_EW = pygame.image.load('path_sprites/EW.png')
path_EW = pygame.transform.scale(path_EW, (64, 64))

bg_tile = pygame.image.load('bg_tile.png')
bg_tile = pygame.transform.scale(bg_tile, (64, 64))

turret = pygame.image.load('turret1.png')
turret = pygame.transform.scale(turret, (64, 64))

turret2 = pygame.image.load('turret2.png')
turret2 = pygame.transform.scale(turret2, (64, 64))

turret3 = pygame.image.load('turret3.png')
turret3 = pygame.transform.scale(turret3, (64, 64))

tmp_enemy = pygame.image.load('tesla3.png')
tmp_enemy = pygame.transform.scale(tmp_enemy, (64, 64))

waypoints = [[0, 5, 'E'], [2, 5, 'N'], [2, 1, 'E'], [4, 1, 'S'], [4, 7, 'W'],
             [1, 7, 'S'], [1, 9, 'E'], [8, 9, 'N'], [9, 6, 'W'], [6, 6, 'N'],
             [6, 2, 'E'], [9, 2, 'S']]

money = 1000
health = 100

class Tower:

    def __init__(self, x, y, dmg, hitspd, range, price, image):
        self.x = x * 64 + 32
        self.y = y * 64 + 32
        self.dmg = dmg
        self.hitspd = hitspd
        self.range = range
        self.price = price
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.last_shot = time.time()

    def attack(self):
        global enemies

        for i, enemy in enumerate(enemies):
            if math.sqrt((self.x - enemy.x)**2 +
                         (self.y - enemy.y)**2) <= self.range:
                # if done reloading
                if time.time() - self.last_shot >= self.hitspd:
                    pygame.draw.line(screen, (0, 0, 255), (self.x, self.y),
                     (enemy.x, enemy.y), 5)
                    enemy.hp -= self.dmg
                    print(enemy.hp)
                    self.last_shot = time.time()
                    if enemy.hp <= 0:
                        enemies.pop(i)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Turret(Tower):

    def __init__(self, x, y):
        super().__init__(x, y, 1, 1, 128, 50, turret)


class Turret2(Tower):

    def __init__(self, x, y):
        super().__init__(x, y, 0.5, 1, 128, 50, turret)


class Turret3(Tower):

    def __init__(self, x, y):
        super().__init__(x, y, 0.3, 1, 128, 50, turret)

class Enemy:

    def __init__(self, x, y, hp, speed, dmg, image):
        self.x = x + 32
        self.y = y + 32
        self.curr_waypt = 0
        self.hp = hp
        self.max_hp = hp
        self.speed = speed
        self.dmg=dmg
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def move(self):
        global waypoints
        global health

        if self.curr_waypt == len(waypoints):
            return

        x, y, d = waypoints[self.curr_waypt]
        x *= 64
        y *= 64

        try:
            x1, y1, d1 = waypoints[self.curr_waypt + 1]
            x1 *= 64
            y1 *= 64
        except:
            enemies.remove(self)
            health -= self.dmg
            return
            

        if d == 'N':
            self.y -= self.speed
        elif d == 'S':
            self.y += self.speed
        elif d == 'E':
            self.x += self.speed
        elif d == 'W':
            self.x -= self.speed

        self.rect.center = (self.x, self.y)

        if (d == "N" and self.y - 32 - y1 <= 0) or \
        (d == "E" and self.x - 32 - x1 >= 0) or \
        (d == "S" and  self.y - 32 - y1 >= 0) or \
        (d == "W" and self.x - 32 - x1 <= 0):
                self.curr_waypt += 1
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)


towers = [Turret(3, 2)]
enemies = [Enemy(0, 320, 2, 2, 1, tmp_enemy)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(10):
        for j in range(11):
            screen.blit(bg_tile, (i * 64, j * 64))

    # draw path
    screen.blit(path_EW, (waypoints[0][0] * 64, waypoints[0][1] * 64))
    for i in range(0, len(waypoints) - 1):
        if waypoints[i][2] == 'N':
            for j in range(abs(waypoints[i][1] - waypoints[i + 1][1])):
                screen.blit(path_NS, ((waypoints[i][0]) * 64,
                                      (waypoints[i][1] - j - 1) * 64))
        if waypoints[i][2] == 'E':
            for j in range(abs(waypoints[i][0] - waypoints[i + 1][0])):
                screen.blit(path_EW, ((waypoints[i][0] + j + 1) * 64,
                                      (waypoints[i][1]) * 64))
        if waypoints[i][2] == 'S':
            for j in range(abs(waypoints[i][1] - waypoints[i + 1][1])):
                screen.blit(path_NS, ((waypoints[i][0]) * 64,
                                      (waypoints[i][1] + j + 1) * 64))
        if waypoints[i][2] == 'W':
            for j in range(abs(waypoints[i][0] - waypoints[i + 1][0])):
                screen.blit(path_EW, ((waypoints[i][0] - j - 1) * 64,
                                      (waypoints[i][1]) * 64))

        # CORNERS
        if i >= 1:
            if waypoints[i][2] == 'N':
                if waypoints[i - 1][2] == 'E':
                    screen.blit(path_NW, ((waypoints[i][0]) * 64,
                                          (waypoints[i][1]) * 64))
                if waypoints[i - 1][2] == 'W':
                    screen.blit(path_NE, ((waypoints[i][0]) * 64,
                                          (waypoints[i][1]) * 64))
            if waypoints[i][2] == 'E':
                if waypoints[i - 1][2] == 'N':
                    screen.blit(path_ES, ((waypoints[i][0]) * 64,
                                          (waypoints[i][1]) * 64))
                if waypoints[i - 1][2] == 'S':
                    screen.blit(path_NE, ((waypoints[i][0]) * 64,
                                          (waypoints[i][1]) * 64))
            if waypoints[i][2] == 'S':
                if waypoints[i - 1][2] == 'E':
                    screen.blit(path_SW, ((waypoints[i][0]) * 64,
                                          (waypoints[i][1]) * 64))
                if waypoints[i - 1][2] == 'W':
                    screen.blit(path_ES, ((waypoints[i][0]) * 64,
                                          (waypoints[i][1]) * 64))
            if waypoints[i][2] == 'W':
                if waypoints[i - 1][2] == 'N':
                    screen.blit(path_SW,
                                ((waypoints[i][0] - 1) * 64,
                                 (waypoints[i][1]) *
                                 64))  # PATCH HERE: THE -1 SHOULDNT EXIST
                if waypoints[i - 1][2] == 'S':
                    screen.blit(path_NW, ((waypoints[i][0]) * 64,
                                          (waypoints[i][1]) * 64))

    for tower in towers:
        tower.draw(screen)
        tower.attack()

    for enemy in enemies:
        enemy.draw(screen)
        enemy.move()

    pygame.display.update()

pygame.quit()
