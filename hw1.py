import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Rectangle Movement")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()

player_width = 60
player_height = 60
player_x = WIDTH // 4
player_y = HEIGHT // 2
player_speed = 5

enemy_width = 100
enemy_height = 80
enemy_x = WIDTH * 3 // 4
enemy_y = HEIGHT // 2

running = True
while running:
    clock.tick(60)  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    
    player_x = max(0, min(WIDTH - player_width, player_x))
    player_y = max(0, min(HEIGHT - player_height, player_y))

    
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))
    
    pygame.display.flip()


pygame.quit()