import pygame
import random
pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprites with Custom Event")


CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 1000)  


class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.color = self.random_color()
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def random_color(self):
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def change_color(self):
        self.color = self.random_color()
        self.image.fill(self.color)


sprite1 = ColorSprite(150, 150)
sprite2 = ColorSprite(350, 150)


sprites = pygame.sprite.Group()
sprites.add(sprite1, sprite2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == CHANGE_COLOR:
            for sprite in sprites:
                sprite.change_color()
    
    screen.fill((30, 30, 30))
    sprites.draw(screen)

   
    pygame.display.flip()
    clock.tick(60)

pygame.quit()