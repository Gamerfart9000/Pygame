import pygame
import sys


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "My First Pygame Window"


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


rect_x = 300
rect_y = 200
rect_width = 200
rect_height = 100


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)


font = pygame.font.SysFont("Arial", 36)
text = font.render("Hello Pygame!", True, BLACK)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(WHITE)

    
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
    screen.blit(text, (280, 100))
    pygame.display.update()

pygame.quit()
