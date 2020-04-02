import pygame
from pygame import image as img
import os

pygame.init()
print(os.getcwd())

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width,win_height))

pygame.display.set_caption("First game")
font = pygame.font.Font('.\dinosaur\comic.ttf', 32)

x = 100
y = 440
width = 20
height = 40
vel = 5

x_obst = 600
vel_obst = 15

is_jump = False
jump_count = 10
walk_count = 0
score = 0
gameover_trig = False
gameover = font.render("", False, (32, 32, 32))

char_animation = [img.load(os.path.join('.\dinosaur\gamesprites', 'char1.png')), img.load(os.path.join('.\dinosaur\gamesprites', 'char2.png')), img.load(os.path.join('.\dinosaur\gamesprites', 'char3.png')), img.load(os.path.join('.\dinosaur\gamesprites', 'char4.png'))]

def redraw():
    global walk_count
    win.fill((230,230,230))

    if walk_count == 12:
        walk_count = 0
    win.blit(char_animation[walk_count//3], (x, y))
    walk_count += 1

    win.blit(img.load(os.path.join('.\dinosaur\gamesprites', 'cactus.png')), (x_obst, 400))

    win.blit(score_t, (win_width - 150, 10))
    win.blit(gameover, (win_width / 3, win_height / 2 - 50))

    pygame.display.update()

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    #Movement
    if keys[pygame.K_LEFT] and x >0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 480:
        x += vel
    #Jumping
    if (is_jump):
        if jump_count >= -10:
            neg = 1
            if jump_count <= 0:
                neg = -1
            y -= (jump_count ** 2) * 0.3 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
    else:
        if keys[pygame.K_SPACE]:
            is_jump = True
    #Obstacle movement
    x_obst -= vel_obst
    if x_obst < -100:
        x_obst = 600

    #Game Over
    if x_obst <= x + 30 and x_obst >= x - 30:
        if win_height - y < 140:
            run = False
            gameover = font.render("Game Over", False, (32, 32, 32))
            gameover_trig = True

    #Score
    if x_obst == 0:
        score += 1

    score_t = font.render("Score: " + str(score), False, (32, 32, 32))

    redraw()

    if gameover_trig:
        pygame.time.delay(500)

pygame.quit()
