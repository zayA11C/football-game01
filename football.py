import pygame
import random

pygame.init()

# écran
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Jeu de foot ⚽")

clock = pygame.time.Clock()

# joueur
player = pygame.Rect(100, 250, 20, 20)

# ballon
ball = pygame.Rect(120, 250, 10, 10)
ball_owned = True
ball_speed_x = 0
ball_speed_y = 0

# ennemis
enemies = [
    pygame.Rect(400, 150, 20, 20),
    pygame.Rect(500, 350, 20, 20)
]

# gardien
goalkeeper = pygame.Rect(760, 200, 20, 80)

# but
goal = pygame.Rect(780, 200, 10, 100)

score = 0
speed = 5

running = True

while running:
    clock.tick(60)
    screen.fill((0, 150, 0))

    # événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ⚽ tirer balle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ball_owned:
                ball_owned = False
                ball_speed_x = 8

    # clavier joueur
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed

    # balle suit joueur si possédée
    if ball_owned:
        ball.x = player.x + 10
        ball.y = player.y
    else:
        ball.x += ball_speed_x

    # 🤖 ennemis suivent la balle
    for e in enemies:
        if e.x < ball.x:
            e.x += 2
        if e.x > ball.x:
            e.x -= 2
        if e.y < ball.y:
            e.y += 2
        if e.y > ball.y:
            e.y -= 2

        # vol balle
        if e.colliderect(ball):
            ball_owned = False

    # 🧤 gardien suit balle
    if goalkeeper.y < ball.y:
        goalkeeper.y += 2
    if goalkeeper.y > ball.y:
        goalkeeper.y -= 2

    # ⚽ but
    if ball.colliderect(goal):
        score += 1
        player.x, player.y = 100, 250
        ball_owned = True
        ball_speed_x = 0

    # limites terrain
    player.x = max(0, min(780, player.x))
    player.y = max(0, min(480, player.y))

    # dessin terrain
    pygame.draw.rect(screen, (255, 255, 255), goal)
    pygame.draw.rect(screen, (200, 200, 200), goalkeeper)

    # joueur
    pygame.draw.rect(screen, (0, 0, 255), player)

    # ballon
    pygame.draw.circle(screen, (255, 255, 255), ball.center, 5)

    # ennemis
    for e in enemies:
        pygame.draw.rect(screen, (255, 0, 0), e)

    # score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (20, 20))

    pygame.display.update()

pygame.quit()