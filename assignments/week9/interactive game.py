# importing required library
import pygame
import time
import random
from IPython.core.events import post_execute

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255,255,255) # RGB

left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False
mouse_pressed = False
explosion_start_time = 0

class Explosion:
    def __init__(self, pos_x= 10, pos_y= 10):
        self._img = pygame.transform.scale(pygame.image.load("explosion.png"), (100, 100))
        self._pos_x = pos_x
        self._pos_y = pos_y
        self.active = False
        self._start_time = 0

    @property
    def pos_x(self):
        return self._pos_x

    @pos_x.setter
    def pos_x(self, val):
        if not self.active:
            self._pos_x = val - self._img.get_width() // 2

    @property
    def pos_y(self):
        return self._pos_y

    @pos_y.setter
    def pos_y(self, val):
        if not self.active:
            self._pos_y = val - self._img.get_height() // 2

    def trigger(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.active = True
        self._start_time = time.time()

    def update(self):
        if self.active and time.time() - self._start_time > 0.5:
            self.active = False

    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self._img.get_width(), self._img.get_height())

    def draw(self):
        if self.active:
            screen.blit(self._img, (self._pos_x, self._pos_y))

class Fish:
    def __init__(self, pos_x= SCREEN_WIDTH // 2, pos_y= SCREEN_HEIGHT // 2):
        self._img = pygame.transform.scale(pygame.image.load("../week8/Fish.png"), (100,100))
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._speed = 5

    @property
    def pos_x(self):
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value):
        self._pos_x = max(0, min(SCREEN_WIDTH - 100, value))

    @property
    def pos_y(self):
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value):
        self._pos_y = max(0, min(SCREEN_HEIGHT - 100, value))

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, val):
        self._speed = max(0, val)

    def get_rect(self):
        return pygame.Rect(self.pos_x, self.pos_y, self._img.get_width(), self._img.get_height())

    def draw(self):
        screen.blit(self._img, (self.pos_x, self.pos_y))

class Enemy(Fish):
    def __init__(self, pos_x: int, pos_y: int):
        super().__init__(pos_x, pos_y)
        self._img = pygame.transform.scale(self._img, (35, 35))
        self._original_img = self._img.copy()
        self._dead = False
        self.respawn_time = 0
        self._tint_color = (0, 0, 250)
        self.apply_tint()

    @property
    def dead(self):
        return self._dead

    @dead.setter
    def dead(self, value):
        self._dead = value
        if value:
            self.respawn_time = time.time() + 2

    def apply_tint(self):
        self._img = self._original_img.copy()
        tint_surface = pygame.Surface(self._img.get_size(), pygame.SRCALPHA)
        tint_surface.fill((0, 0, 250, 0))
        self._img.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGB_ADD)

    def follow(self, parent:Fish):
        if not self.dead:
            if self.pos_x < parent.pos_x:
                self.pos_x += parent.speed / 2
            if self.pos_x > parent.pos_x:
                self.pos_x -= parent.speed / 2
            if self.pos_y < parent.pos_y:
                self.pos_y += parent.speed / 2
            if self.pos_y > parent.pos_y:
                self.pos_y -= parent.speed / 2

    def draw(self):
        if not self.dead:
            screen.blit(self._img, (self.pos_x, self.pos_y))

class StartingScreen():
    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load("starting.png"), (1200, 600))
        self.pos_x = 0
        self.pos_y = 0

    def draw(self):
        screen.blit(self.img, (self.pos_x, self.pos_y))

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

pygame.init()



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 100)
timer_font = pygame.font.Font(None, 50)

pygame.display.set_caption('image')

start = StartingScreen()
fish = Fish()
enemies = []
for _ in range(5):
    offset_x = random.randint(-500, 500)
    offset_y = random.randint(-400, 400)
    enemy = Enemy(fish.pos_x + offset_x, fish.pos_y + offset_y)
    enemies.append(enemy)

explosion = Explosion()

clock = pygame.time.Clock()

starting = True
flag = False
game_over = False
screen.fill(BACKGROUND_COLOR)
start.draw()
pygame.display.flip()
while starting:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            starting = False
            flag = True
game_start_time = time.time()
while flag:

    clock.tick(60)

    screen.fill(BACKGROUND_COLOR)
    if not game_over:
        fish.draw()

        for enemy in enemies:

            if enemy.dead and time.time() > enemy.respawn_time:
                enemy.dead = False
                enemy.pos_x = fish.pos_x + random.randint(-500, 500)
                enemy.pos_y = fish.pos_y + random.randint(-400, 400)

            if not enemy.dead:
                enemy.follow(parent=fish)

                if explosion.active and enemy.get_rect().colliderect(explosion.get_rect()):
                    enemy.dead = True
                    enemy.respawn_time = time.time() + 2


        for enemy in enemies:
            enemy.draw()

        explosion.update()
        explosion.draw()

        if left_pressed:
            fish.pos_x -= fish.speed

        if right_pressed:
            fish.pos_x += fish.speed

        if up_pressed:

            fish.pos_y -= fish.speed
        if down_pressed:
            fish.pos_y += fish.speed

        if mouse_pressed:
            if not explosion.active:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                explosion.trigger(mouse_x, mouse_y)


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right_pressed = True
                if event.key == pygame.K_LEFT:
                    left_pressed = True
                if event.key == pygame.K_UP:
                    up_pressed = True
                if event.key == pygame.K_DOWN:
                    down_pressed = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pressed = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_pressed = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    right_pressed = False
                if event.key == pygame.K_LEFT:
                    left_pressed = False
                if event.key == pygame.K_UP:
                    up_pressed = False
                if event.key == pygame.K_DOWN:
                    down_pressed = False
                if event.key == pygame.MOUSEBUTTONUP:
                    mouse_pressed = False

            if event.type == pygame.QUIT:
                flag = False
        if any(enemy.get_rect().colliderect(fish.get_rect()) for enemy in enemies if not enemy.dead):
            game_over = True
        elapsed_time = int(time.time() - game_start_time)
        timer_surface = timer_font.render(f"Time: {elapsed_time}", True, (0, 0, 0))
        screen.blit(timer_surface, (SCREEN_WIDTH - timer_surface.get_width() - 10, 10))
    else:
        text_surface = font.render("You Lost!", True, (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2,
                                   SCREEN_HEIGHT // 2 - text_surface.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        flag = False
    pygame.display.flip()
pygame.quit()
exit(0)
#For introduction to game: See starting screen