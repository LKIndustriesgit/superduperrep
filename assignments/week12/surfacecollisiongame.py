#pytorch
#framework for training AI models
#Ollama
#for locally hosted models
#also supports API
#little demo of model (Potential usage, i.e. answers and questions)
import pygame
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
BACKGROUND_COLOR = (255,255,255) # RGB
up_pressed = False
left_pressed = False
right_pressed = False
class Dino:
    def __init__(self, pos_x=100, pos_y= 650):
        self._img = pygame.transform.scale(pygame.image.load("../week12/dino_s.png"), (100,100))
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._speed = 2

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

font = pygame.font.Font(None, 100)
dino = Dino()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

start_screen = pygame.Surface(screen.get_size())
start_screen.fill("white")

ground_rect = pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
floor_rect = pygame.Rect(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.7 , SCREEN_WIDTH * 0.5, 50)
floor2_rect = pygame.Rect(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.56 , SCREEN_WIDTH * 0.2, 50)
floor3_rect = pygame.Rect(0, SCREEN_HEIGHT * 0.4 , SCREEN_WIDTH * 0.2, 50)
floor4_rect = pygame.Rect(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.2 , SCREEN_WIDTH * 0.5, 50)
winning_rect = pygame.Rect(SCREEN_WIDTH * 0.9, SCREEN_HEIGHT * 0.013 , SCREEN_WIDTH * 0.2, 200)
ground_checker = pygame.Rect(dino.pos_x, dino.pos_y + dino._img.get_height() * 0.5, dino._img.get_width(), dino._img.get_height() * 0.5)
pygame.display.set_caption('Jump and collide!')


flag = False
starting = True
while starting:
    pygame.draw.circle(start_screen, "aquamarine", (SCREEN_WIDTH / 2, SCREEN_HEIGHT *0.75), 40)
    pygame.draw.circle(start_screen, "aquamarine", (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.25), 40)
    screen.blit(start_screen, [0, 0])
    text_surface = font.render("Press Enter to start", True, (0, 0, 0))
    screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2,
                               SCREEN_HEIGHT // 2 - text_surface.get_height() // 2))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                flag = True
                starting = False
clock = pygame.time.Clock()
waiting = False
event_start_time = 0
while flag:
    screen.fill(BACKGROUND_COLOR)
    dino.draw()
    pygame.draw.rect(screen, pygame.Color("blue"), ground_rect)
    pygame.draw.rect(screen, pygame.Color("blue"), floor_rect)
    pygame.draw.rect(screen, pygame.Color("blue"), floor2_rect)
    pygame.draw.rect(screen, pygame.Color("blue"), floor3_rect)
    pygame.draw.rect(screen, pygame.Color("green"), winning_rect)
    pygame.draw.rect(screen, pygame.Color("blue"), floor4_rect)
    #pygame.draw.rect(screen, pygame.Color("red"), ground_checker)
    ground_checker.x = dino.pos_x
    ground_checker.y = (dino.pos_y + dino._img.get_height() * 0.5) +10

    if waiting:
        if pygame.time.get_ticks() - event_start_time >= 250:
            air = True
            while air:
                dino.pos_y += 1
                if dino.get_rect().colliderect(ground_rect):
                    air = False
                    waiting = False
                    dino.pos_y -= 10
                if dino.get_rect().colliderect(floor_rect):
                    air = False
                    waiting = False
                    dino.pos_y -= 10
                if dino.get_rect().colliderect(floor2_rect):
                    air = False
                    waiting = False
                    dino.pos_y -= 10
                if dino.get_rect().colliderect(floor3_rect):
                    air = False
                    waiting = False
                    dino.pos_y -= 10
                if dino.get_rect().colliderect(floor4_rect):
                    air = False
                    waiting = False
                    dino.pos_y -= 10
    if (not ground_checker.colliderect(ground_rect)
    and not ground_checker.colliderect(floor_rect)
    and not ground_checker.colliderect(floor2_rect)
    and not ground_checker.colliderect(floor3_rect)
    and not ground_checker.colliderect(floor4_rect)
    and not up_pressed
    and not waiting):
        air = True
        while air:
            dino.pos_y += 1
            if dino.get_rect().colliderect(ground_rect):
                air = False
                waiting = False
                dino.pos_y -= 10
            if dino.get_rect().colliderect(floor_rect):
                air = False
                waiting = False
                dino.pos_y -= 10
            if dino.get_rect().colliderect(floor2_rect):
                air = False
                waiting = False
                dino.pos_y -= 10
            if dino.get_rect().colliderect(floor3_rect):
                air = False
                waiting = False
                dino.pos_y -= 10
            if dino.get_rect().colliderect(floor4_rect):
                air = False
                waiting = False
                dino.pos_y -= 10
    if up_pressed:
        dino.pos_y -= 190
        waiting = True
        up_pressed = False
        event_start_time = pygame.time.get_ticks()
    if left_pressed:
        dino.pos_x -= dino.speed
    if right_pressed:
        dino.pos_x += dino.speed
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_pressed = True
            if event.key == pygame.K_RIGHT:
                right_pressed = True
            if event.key == pygame.K_LEFT:
                left_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            if event.key == pygame.K_LEFT:
                left_pressed = False
        if event.type == pygame.QUIT:
            flag = False
    if dino.get_rect().colliderect(winning_rect):
        text_surface = font.render("You Won!", True, (0, 0, 0))
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2,
                                   SCREEN_HEIGHT // 2 - text_surface.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        flag = False
    pygame.display.flip()
pygame.quit()
exit(0)
