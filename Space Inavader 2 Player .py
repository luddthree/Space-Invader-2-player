import math
import random
import pygame
from pygame import mixer


pygame.init()


screen = pygame.display.set_mode((800, 600))


background = pygame.image.load('background.png')


mixer.music.load('background.wav')
mixer.music.play(-1)


playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0


playerImg2 = pygame.image.load('player2.png')
playerX2 = 370
playerY2 = 400
playerX_change2 = 0




enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 12

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)


bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


bulletImg2 = pygame.image.load('bullet.png')
bulletX2 = 0
bulletY2 = 480
bulletX_change2 = 0
bulletY_change2 = 10
bullet_state2 = "ready"



score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10


over_font = pygame.font.Font('freesansbold.ttf', 64)


player1_font = pygame.font.Font('freesansbold.ttf', 10)

playertextX = 10
playertextY = 425


player2_font = pygame.font.Font('freesansbold.ttf', 10)

player2textX = 10
player2textY = 505

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player1_text(x, y):
    player1_text = player1_font.render("Player 1 - WASD", True, (255, 255, 255))
    screen.blit(player1_text, (x, y))

def player2_text(x, y):
    player2_text = player2_font.render("Player 2 - Arrows", True, (255, 255, 255))
    screen.blit(player2_text, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def player2(x, y):
    screen.blit(playerImg2, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def fire_bullet2(x, y):
    global bullet_state2
    bullet_state2 = "fire"
    screen.blit(bulletImg2, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False




def isCollision(enemyX, enemyY, bulletX2, bulletY2):
    distance = math.sqrt(math.pow(enemyX - bulletX2, 2) + (math.pow(enemyY - bulletY2, 2)))
    if distance < 27:
        return True
    else:
        return False



running = True
while running:

    
    screen.fill((0, 0, 0))
    
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_UP:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change2 = -5
            if event.key == pygame.K_d:
                playerX_change2 = 5
            if event.key == pygame.K_w:
                if bullet_state2 is "ready":
                    bulletSound2 = mixer.Sound("laser.wav")
                    bulletSound2.play()
                    bulletX2 = playerX2
                    fire_bullet2(bulletX2, bulletY2)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change2 = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    playerX2 += playerX_change2
    if playerX2 <= 0:
        playerX2 = 0
    elif playerX2 >= 736:
        playerX2 = 736

    
    for i in range(num_of_enemies):

        if enemyY[i] > 390:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3.5
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        collision = isCollision(enemyX[i], enemyY[i], bulletX2, bulletY2)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY2 = 400
            bullet_state2 = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    if bulletY2 <= 0:
        bulletY2 = 390
        bullet_state2 = "ready"

    if bullet_state2 is "fire":
        fire_bullet2(bulletX2, bulletY2)
        bulletY2 -= bulletY_change2

    player(playerX, playerY)
    player2(playerX2,playerY2)
    show_score(textX, testY)
    player1_text(playertextX, playertextY)
    player2_text(player2textX, player2textY)
    pygame.display.update()

