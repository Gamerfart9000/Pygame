import math
import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

PLAYER_START_X = 370
PLAYER_START_Y = 700
PLAYER_SPEED = 5

ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150

BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")

background = pygame.image.load("bg space.jpeg")
icon = pygame.image.load("ig.jpeg")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("player.jpeg")
enemyImg = pygame.image.load("Enemy.jpeg")
bulletImg = pygame.image.load("bullet.jpeg")

# -------- SOUND EFFECTS --------
bullet_sound = pygame.mixer.Sound("laser.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")

pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)
# --------------------------------

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyX = []
enemyY = []

rows = 3
cols = 6
spacing_x = 80
spacing_y = 60
start_x = 100
start_y = 50

for row in range(rows):
    for col in range(cols):
        enemyX.append(start_x + col * spacing_x)
        enemyY.append(start_y + row * spacing_y)

enemy_direction = 1
enemy_speed = 2
enemy_drop = 30

bulletX = 0
bulletY = PLAYER_START_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score():
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (10,10))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200,250))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.hypot(enemyX-bulletX, enemyY-bulletY)
    return distance < COLLISION_DISTANCE

running = True

while running:

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -PLAYER_SPEED

            if event.key == pygame.K_RIGHT:
                playerX_change = PLAYER_SPEED

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)
                    bullet_sound.play()   # 🔫 play shooting sound

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH-64))

    # Enemy movement
    move_down = False

    for i in range(len(enemyX)):
        enemyX[i] += enemy_speed * enemy_direction

        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH-64:
            move_down = True

    if move_down:
        enemy_direction *= -1
        for i in range(len(enemyY)):
            enemyY[i] += enemy_drop

    # Enemy logic
    for i in range(len(enemyX)):

        if enemyY[i] > 440:
            game_over_text()
            running = False

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)

        if collision:
            explosion_sound.play()   

            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1

            enemyX[i] = random.randint(0, SCREEN_WIDTH-64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i])

    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= BULLET_SPEED_Y

    player(playerX, playerY)
    show_score()

    pygame.display.update()

pygame.quit()