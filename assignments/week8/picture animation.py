import pygame
import random
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (50, 175, 255)

#creating a random tint for the fishes that always results in a nice colour
def soft_tint():
    channels = [0, 0, 0]
    strong_index = random.randint(0, 2)
    for i in range(3):
        if i == strong_index:
            channels[i] = random.randint(200, 255)  # Strong channel
        else:
            channels[i] = random.randint(0, 10)  # Subtle channels
    return tuple(channels)

class fish:
    def __init__(self):
        img = pygame.image.load('Fish.png').convert_alpha()
        self.img = pygame.transform.scale(img, (100, 100))
        self.original_img = self.img.copy()
        self.pos_x = 0
        self.pos_y = random.randint(50, 400)
        self.velocity = random.randint(1, 5)
        self.tint_color = soft_tint()
        self.apply_tint()

    def animate(self):
        if self.pos_x < SCREEN_WIDTH:
            self.pos_x += self.velocity
        else:
            self.pos_x = -100

    def apply_tint(self):
        self.img = self.original_img.copy()

        tint_surface = pygame.Surface(self.img.get_size(), flags=pygame.SRCALPHA)

        tint_surface.fill(self.tint_color)

        self.img.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
    def draw(self, screen):
        screen.blit(self.img, (self.pos_x, self.pos_y))
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Aquarium')
aquarium = [fish() for _ in range(5)]
clock = pygame.time.Clock()

flag = True
while flag:
    clock.tick(60)

    screen.fill(BACKGROUND_COLOR)

    for a in aquarium:
        a.animate()
        a.draw(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

pygame.quit()
exit(0)