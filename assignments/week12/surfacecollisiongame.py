import pygame
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
BACKGROUND_COLOR = (255,255,255) # RGB
up_pressed = False
class Dino:
    def __init__(self, pos_x=100, pos_y= 150):
        self._img = pygame.transform.scale(pygame.image.load("../week12/dino_s.png"), (100,100))
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

pygame.init()

dino = Dino()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ground_rect = pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
pygame.display.set_caption('Jump and collide!')

clock = pygame.time.Clock()
flag = True
while flag:
    screen.fill(BACKGROUND_COLOR)
    dino.draw()
    pygame.draw.rect(screen, pygame.Color("blue"), ground_rect)

    if up_pressed:
        dino.pos_y -= 80
        now = pygame.time.get_ticks()
        if pygame.time.get_ticks() - now > 1000:
            air = True
            while air:
                dino.pos_y += 1
                if dino.get_rect().colliderect(ground_rect):
                    air = False
        up_pressed = False
    # code you need to end pygame
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_pressed = True
        if event.type == pygame.QUIT:
            flag = False
    pygame.display.flip()
pygame.quit()
exit(0)
