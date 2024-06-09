import pygame
import math
import time
import questions

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

tesla = pygame.image.load('tesla1.png')
tesla = pygame.transform.scale(tesla, (64, 64))

tesla2 = pygame.image.load('tesla2.png')
tesla2 = pygame.transform.scale(tesla2, (64, 64))

tesla3 = pygame.image.load('tesla3.png')
tesla3 = pygame.transform.scale(tesla3, (64, 64))

enemy1 = pygame.image.load('basicEnemy1.png')
enemy1 = pygame.transform.scale(enemy1, (64, 64))
enemy2 = pygame.image.load('basicEnemy2.png')
enemy2 = pygame.transform.scale(enemy2, (64, 64))

strongEnemy1 = pygame.image.load('strongEnemy1.png')
strongEnemy1 = pygame.transform.scale(strongEnemy1, (64, 64))
strongEnemy2 = pygame.image.load('strongEnemy2.png')
strongEnemy2 = pygame.transform.scale(strongEnemy2, (64, 64))


shop_bg = pygame.image.load('shopbg.png')
shop_bg = pygame.transform.scale(shop_bg, (192, 704))

shop_button = pygame.image.load('shopButton.png')
shop_button = pygame.transform.scale(shop_button, (64, 64))

waypoints = [[0, 5, 'E'], [2, 5, 'N'], [2, 1, 'E'], [4, 1, 'S'], [4, 7, 'W'],
             [1, 7, 'S'], [1, 9, 'E'], [8, 9, 'N'], [9, 6, 'W'], [6, 6, 'N'],
             [6, 2, 'E'], [9, 2, 'S']]

money = 50
health = 100

shop_indexes = []

is_selecting = False

def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect

angle = 0

class Tower:

    def __init__(self, x, y, dmg, hitspd, range, price, image):
        self.x = x + 32
        self.y = y + 32
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
        global angle

        x, y = pygame.mouse.get_pos()

        for i, enemy in enumerate(enemies):
            if math.sqrt((self.x - enemy.x)**2 +
                         (self.y - enemy.y)**2) <= self.range:
                # if done reloading
                if time.time() - self.last_shot >= self.hitspd:
                    pygame.draw.line(screen, (0, 0, 255), (self.x, self.y),
                                     (enemy.x, enemy.y), 5)
                    enemy.hp -= self.dmg
                    self.last_shot = time.time()
                    if enemy.hp <= 0:
                        enemies.pop(i)

                '''
                # calculate angle
                print(enemy)
                deltax, deltay = self.x-enemy.x, self.y-enemy.y
                self.image, self.rect = rot_center(self.image, self.rect, -1*angle)
                last_angle = angle
                angle = math.degrees(math.atan(deltay/deltax))
                print(angle-last_angle)
                self.image, self.rect = rot_center(self.image, self.rect, angle-last_angle)
                '''

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Turret(Tower):

    def __init__(self, x, y):
        super().__init__(x, y, 1, 1, 256, 50, turret)


class Turret2(Tower):

    def __init__(self, x, y):
        super().__init__(x, y, 1, 0.5, 256, 75, turret2)


class Turret3(Tower):

    def __init__(self, x, y):
        super().__init__(x, y, 1, 0.3, 256, 100, turret3)

class Tesla(Tower):
    def __init__(self, x, y):
        super().__init__(x, y, 1, 1, 128, 100, tesla)

    def attack(self):
        global enemies
        global angle

        x, y = pygame.mouse.get_pos()

        for i, enemy in enumerate(enemies):
            if math.sqrt((self.x - enemy.x)**2 +
                         (self.y - enemy.y)**2) <= self.range:
                # if done reloading
                if time.time() - self.last_shot >= self.hitspd:
                    pygame.draw.circle(screen, (125, 249, 255), (self.x, self.y), self.range)
                    break

        for i, enemy in enumerate(enemies):
            if math.sqrt((self.x - enemy.x)**2 +
                         (self.y - enemy.y)**2) <= self.range:
                # if done reloading
                if time.time() - self.last_shot >= self.hitspd:
                    enemy.hp -= self.dmg
                    if enemy.hp <= 0:
                        enemies.pop(i)
        
        for i, enemy in enumerate(enemies):
            if math.sqrt((self.x - enemy.x)**2 +
                         (self.y - enemy.y)**2) <= self.range:
                # if done reloading
                if time.time() - self.last_shot >= self.hitspd:
                    self.last_shot = time.time()
                    break

        



class Tesla2(Tower):
    def __init__(self, x, y):
        super().__init__(x, y, 2,1, 128, 150, tesla2)

    def attack(self):
        global enemies
        global angle

        x, y = pygame.mouse.get_pos()

        for i, enemy in enumerate(enemies):
            if math.sqrt((self.x - enemy.x)**2 +
                         (self.y - enemy.y)**2) <= self.range:
                # if done reloading
                if time.time() - self.last_shot >= self.hitspd:
                    pygame.draw.circle(screen, (125, 249, 255), (self.x, self.y), self.range)
                    break

        for i, enemy in enumerate(enemies):
            if math.sqrt((self.x - enemy.x)**2 +
                         (self.y - enemy.y)**2) <= self.range:
                # if done reloading
                if time.time() - self.last_shot >= self.hitspd:
                    enemy.hp -= self.dmg
                    if enemy.hp <= 0:
                        enemies.pop(i)
        
        for i, enemy in enumerate(enemies):
            if math.sqrt((self.x - enemy.x)**2 +
                         (self.y - enemy.y)**2) <= self.range:
                # if done reloading
                if time.time() - self.last_shot >= self.hitspd:
                    self.last_shot = time.time()
                    break



class Tesla3(Tower):
    def __init__(self, x, y):
        super().__init__(x, y, 2, 0.5, 128, 200, tesla3)

    def attack(self):
        global enemies
        global angle

        x, y = pygame.mouse.get_pos()

        for i, enemy in enumerate(enemies):
            if math.sqrt((self.x - enemy.x)**2 +
                         (self.y - enemy.y)**2) <= self.range:
                # if done reloading
                if time.time() - self.last_shot >= self.hitspd:
                    pygame.draw.circle(screen, (125, 249, 255), (self.x, self.y), self.range)
                    break

        for i, enemy in enumerate(enemies):
            if math.sqrt((self.x - enemy.x)**2 +
                         (self.y - enemy.y)**2) <= self.range:
                # if done reloading
                if time.time() - self.last_shot >= self.hitspd:
                    enemy.hp -= self.dmg
                    if enemy.hp <= 0:
                        enemies.pop(i)
        
        for i, enemy in enumerate(enemies):
            if math.sqrt((self.x - enemy.x)**2 +
                         (self.y - enemy.y)**2) <= self.range:
                # if done reloading
                if time.time() - self.last_shot >= self.hitspd:
                    self.last_shot = time.time()
                    break



class Enemy:

    def __init__(self, x, y, hp, speed, dmg, images):
        self.x = x + 32
        self.y = y + 32
        self.curr_waypt = 0
        self.hp = hp
        self.max_hp = hp
        self.speed = speed
        self.dmg = dmg
        self.images = images
        self.rect = (self.images[0].get_rect())
        self.rect.center = (self.x, self.y)
        self.anim = 0

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
        if self.anim % 30 == self.anim % 60:
            screen.blit(self.images[0], self.rect)
        else:
            screen.blit(self.images[1], self.rect)
        self.anim += 1


class BasicEnemy(Enemy):

    def __init__(self, x, y):
        super().__init__(x, y, 1, 2, 1, [enemy1, enemy2])

class StrongEnemy(Enemy):

    def __init__(self, x, y):
        super().__init__(x, y, 5, 2, 3, [strongEnemy1, strongEnemy2])


def draw_shop_item(x, y, item, price, img):
    screen.blit(shop_button, (x, y))
    font = pygame.freetype.Font("font.ttf", 12)

    screen.blit(img, (x + 4, y))

    text_surface, rect = font.render(item, (0, 0, 0))
    text_width, text_height = text_surface.get_size()
    font.render_to(screen, (x + 32 - text_width / 2, y + 8), item,
                   (255, 255, 255))

    text_surface, rect = font.render(str(price), (0, 0, 0))
    text_width, text_height = text_surface.get_size()
    font.render_to(screen, (x + 32 - text_width / 2, y + 50), str(price),
                   (255, 255, 255))

    shop_indexes.append([x + 32, y + 32, item])


def select_tower():
    global is_selecting
    global towers
    global money

    x, y = pygame.mouse.get_pos()
    if not is_selecting:
        for index in shop_indexes:
            if abs(index[0] - x) < 32 and abs(index[1] - y) < 32:
                is_selecting = index[2]
                break
    else:
        if x < 640:
            # exec(
            #     f'tmp={is_selecting}({x}//64*64,{y}//64*64);towers.append(tmp); if tmp.price>money:towers.pop(-1); else:money-=tmp.price'
            # )
            tmp = eval(f'{is_selecting}({x}//64*64,{y}//64*64)')
            towers.append(tmp)
            if tmp.price > money:
                towers.pop(-1)
            else:
                money -= tmp.price
            is_selecting = False


def shop():
    screen.blit(shop_bg, (640, 0))

    font = pygame.freetype.Font("font.ttf", 26)
    font.render_to(screen, (672, 32), f"Money: {money}", (255, 255, 255))

    font.render_to(screen, (672, 64), f"Health: {health}", (255, 255, 255))

    # draw all shop items
    # turret

    temp = Turret(0, 0)
    tmp = pygame.transform.scale(turret, (56, 56))
    draw_shop_item(672, 96, 'Turret', temp.price, tmp)
    temp = Turret2(0, 0)
    tmp = pygame.transform.scale(turret2, (56, 56))
    draw_shop_item(736, 96, 'Turret2', temp.price, tmp)
    temp = Turret3(0, 0)
    tmp = pygame.transform.scale(turret3, (56, 56))
    draw_shop_item(672, 160, 'Turret3', temp.price, tmp)
    temp = Tesla(0, 0)
    tmp = pygame.transform.scale(tesla, (56, 56))
    draw_shop_item(736, 160, 'Tesla', temp.price, tmp)
    temp = Tesla2(0, 0)
    tmp = pygame.transform.scale(tesla2, (56, 56))
    draw_shop_item(672, 224, 'Tesla2', temp.price, tmp)
    temp = Tesla3(0, 0)
    tmp = pygame.transform.scale(tesla3, (56, 56))
    draw_shop_item(736, 224, 'Tesla3', temp.price, tmp)



towers = []
enemies = [BasicEnemy(0,320)]
waves = [[[BasicEnemy(0, 320), 40], [BasicEnemy(0, 320), 40],[BasicEnemy(0, 320), 40], [BasicEnemy(0, 320), 40], [BasicEnemy(0, 320), 40], [BasicEnemy(0, 320), 40]],
         [[BasicEnemy(0, 320), 160], [BasicEnemy(0, 320), 40],[StrongEnemy(0, 320), 40], [StrongEnemy(0, 320), 40]],
         [[StrongEnemy(0, 320), 160], [StrongEnemy(0, 320), 40],[StrongEnemy(0, 320), 40], [StrongEnemy(0, 320), 40]],
         [[BasicEnemy(0, 320), 160], [BasicEnemy(0, 320), 5],[BasicEnemy(0, 320), 5], [BasicEnemy(0, 320), 5], [BasicEnemy(0, 320), 5], [BasicEnemy(0, 320), 5],[BasicEnemy(0, 320), 5], [BasicEnemy(0, 320), 5], [BasicEnemy(0, 320), 5], [BasicEnemy(0, 320), 5],[BasicEnemy(0, 320), 5], [BasicEnemy(0, 320), 5]],
         [[StrongEnemy(0, 320), 160], [StrongEnemy(0, 320), 10],[StrongEnemy(0, 320), 10], [StrongEnemy(0, 320), 10], [StrongEnemy(0, 320), 10]]]

framecount = 0
wavecount = 0
indexcount = 0

q = False

def runwaves(waves):
    global framecount, wavecount, indexcount, q
    framecount += 1

    if wavecount >= len(waves):
        return
    
    if waves[wavecount][indexcount][1] == framecount:
        indexcount += 1
        if indexcount == len(waves[wavecount]):
            # ADD QUESTIONS HERE
            q = True

            wavecount += 1
            indexcount = 0
            
            if wavecount >= len(waves):
                return
            
        enemies.append(waves[wavecount][indexcount][0])
        framecount = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            select_tower()

            if q:
                mouse_pos = pygame.mouse.get_pos()
                if questions.check_answer(mouse_pos) == True:
                    money += 50
                    q = False
                    questions.answer_selected = False
                    print('YEEEEEES!')
                elif questions.check_answer(mouse_pos) == False:
                    q = False
                    print('NOOOOOOOOOO!')
                    questions.answer_selected = False

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

    shop()
    runwaves(waves)

    # draw currently holding tower
    if is_selecting:
        x, y = pygame.mouse.get_pos()
        exec(f'{is_selecting}({x}-32,{y}-32).draw(screen)')

    if q:
        questions.display_question()

    pygame.display.update()

pygame.quit()
