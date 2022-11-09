# -*- coding: utf-8 -*-
"""
Original: Created on Wed Sep 11 11:05:00 2013
@author: Leo

2022-10-26
OSSProj team SGC
"""

import pygame
from sys import exit
from pygame.locals import *
from gameRole import *
import random


# initial
pygame.init()
pygame.display.set_caption('PLAY')

SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()

# sounds
bullet_sound = pygame.mixer.Sound('resource/sound/bullet.wav')
enemy1_down_sound = pygame.mixer.Sound('resource/sound/enemy1_down.wav')
game_over_sound = pygame.mixer.Sound('resource/sound/game_over.wav')
bullet_sound.set_volume(0.3)
enemy1_down_sound.set_volume(0.3)
game_over_sound.set_volume(0.3)
pygame.mixer.music.load('resource/sound/game_music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# images
background = []
background.append(pygame.image.load(
    'resource/image/space_bg.png').convert())
background.append(pygame.image.load(
    'resource/image/chess_bg.png').convert())
background.append(pygame.image.load(
    'resource/image/green_bg.png').convert())
background.append(pygame.image.load(
    'resource/image/pirate_bg.png').convert())
background.append(pygame.image.load(
    'resource/image/card_bg.png').convert())
background.append(pygame.image.load(
    'resource/image/desert_bg.png').convert())

widths = 3000
heights = 5000

bg_widths = -(3000-SCREEN_WIDTH)/2
bg_h = -(5000-SCREEN_HEIGHT)
bg_heights = [bg_h, bg_h, bg_h, bg_h, bg_h, bg_h]

game_over = pygame.image.load('resource/image/blackhole.png')

filename = 'resource/image/shoot.png'
plane_img = pygame.image.load(filename)

# display
player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))
player_rect.append(pygame.Rect(165, 360, 102, 126))
player_rect.append(pygame.Rect(165, 234, 102, 126))
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))
player_pos = [200, 650]
player = Player(plane_img, player_rect, player_pos)

# Define parameters ; bullet object
bullet_rect = pygame.Rect(1004, 987, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)

# Define parameters ; enemy aircraft object
enemy1_img_space = plane_img
enemy1_img_chess = pygame.image.load('resource/image/chess-black_knight.png')
enemy1_img_green = plane_img
enemy1_img_pirate = pygame.image.load('resource/image/pirate-anchor.png')
enemy1_img_card = pygame.image.load('resource/image/card_jack.png')
enemy1_img_desert = plane_img

enemy1_rect = []
enemy1_rect.append(pygame.Rect(534, 612, 57, 43))
enemy1_rect.append(enemy1_img_chess.get_rect())
enemy1_rect.append(pygame.Rect(534, 612, 57, 43))
enemy1_rect.append(enemy1_img_pirate.get_rect())
enemy1_rect.append(enemy1_img_card.get_rect())
enemy1_rect.append(pygame.Rect(534, 612, 57, 43))

enemy1_img = []
enemy1_img.append(enemy1_img_space.subsurface(enemy1_rect[0]))
enemy1_img.append(enemy1_img_chess.subsurface(enemy1_rect[1]))
enemy1_img.append(enemy1_img_green.subsurface(enemy1_rect[2]))
enemy1_img.append(enemy1_img_pirate.subsurface(enemy1_rect[3]))
enemy1_img.append(enemy1_img_card.subsurface(enemy1_rect[4]))
enemy1_img.append(enemy1_img_desert.subsurface(enemy1_rect[5]))

# Define parameters ; enemy type 2 aircraft object
enemy2_img_space = plane_img
enemy2_img_chess = pygame.image.load('resource/image/chess-white_king.png')
enemy2_img_green = plane_img
enemy2_img_pirate = pygame.image.load('resource/image/pirate_kraken.png')
enemy2_img_card = pygame.image.load('resource/image/card_queen.png')
enemy2_img_desert = plane_img

enemy2_rect = []
enemy2_rect.append(pygame.Rect(267, 347, 57, 43))
enemy2_rect.append(enemy2_img_chess.get_rect())
enemy2_rect.append(pygame.Rect(267, 347, 57, 43))
enemy2_rect.append(enemy2_img_pirate.get_rect())
enemy2_rect.append(enemy2_img_card.get_rect())
enemy2_rect.append(pygame.Rect(267, 347, 57, 43))

enemy2_img = []
enemy2_img.append(enemy2_img_space.subsurface(enemy2_rect[0]))
enemy2_img.append(enemy2_img_chess.subsurface(enemy2_rect[1]))
enemy2_img.append(enemy2_img_green.subsurface(enemy2_rect[2]))
enemy2_img.append(enemy2_img_pirate.subsurface(enemy2_rect[3]))
enemy2_img.append(enemy2_img_card.subsurface(enemy2_rect[4]))
enemy2_img.append(enemy2_img_desert.subsurface(enemy2_rect[5]))

enemies1 = pygame.sprite.Group()
enemies2 = pygame.sprite.Group()

# Define parameters ; coin object
coin1_img = pygame.image.load('resource/image/coin1.png')
coin_rect = coin1_img.get_rect()
coin_shine = coin1_img.subsurface(coin_rect)

coins = pygame.sprite.Group()

shoot_frequency = 0
enemy_frequency = 0

player_down_index = 16

score = 0

clock = pygame.time.Clock()
n = 0

running = True

while running:
    # set frame rate
    clock.tick(45)
    n += 1/45
    SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()

    # set firing bullets
    if not player.is_hit:
        if shoot_frequency % 15 == 0:
            # bullet_sound.play()
            player.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0

    # set enemy planes
    if enemy_frequency % 60 == 0:
        enemy1_pos = [random.randint(
            0, SCREEN_WIDTH - enemy1_rect[0].width), 0]
        enemy1 = Enemy(enemy1_img, 2, enemy1_pos, 1)
        enemies1.add(enemy1)
    elif enemy_frequency % 100 == 0:
        enemy2_pos = [random.randint(
            0, SCREEN_WIDTH - enemy2_rect[0].width), 0]
        enemy2 = Enemy(enemy2_img, 1.5, enemy2_pos, 3)
        enemies2.add(enemy2)
    enemy_frequency += 1
    if enemy_frequency >= 120:
        enemy_frequency = 0

    # move the bullet, and delete it
    for bullet in player.bullets:
        bullet.move()
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)

    # move the enemy plane, and delete it
    for enemy in enemies1:
        enemy.move()
        # determine if the player has been hit
        if pygame.sprite.collide_circle(enemy, player):
            enemies1.remove(enemy)
            player.is_hit = True
            game_over_sound.play()
            break
        if enemy.rect.top > SCREEN_HEIGHT:
            enemies1.remove(enemy)
        if n > 20 and n <= 40:
            enemy.image = enemy1_img[1]
        elif n > 40 and n <= 60:
            enemy.image = enemy1_img[2]
        elif n > 60 and n <= 80:
            enemy.image = enemy1_img[3]
        elif n > 80 and n <= 100:
            enemy.image = enemy1_img[4]
        else:
            enemy.image = enemy1_img[5]

    for enemy in enemies2:
        enemy.move()
        # determine if the player has been hit
        if pygame.sprite.collide_circle(enemy, player):
            enemies2.remove(enemy)
            player.is_hit = True
            game_over_sound.play()
            break
        if enemy.rect.top > SCREEN_HEIGHT:
            enemies2.remove(enemy)
        if enemy.rect.top > SCREEN_HEIGHT:
            enemies2.remove(enemy)
        if n > 20 and n <= 40:
            enemy.image = enemy2_img[1]
        elif n > 40 and n <= 60:
            enemy.image = enemy2_img[2]
        elif n > 60 and n <= 80:
            enemy.image = enemy2_img[3]
        elif n > 80 and n <= 100:
            enemy.image = enemy2_img[4]
        else:
            enemy.image = enemy2_img[5]

    # add the hit enemy aircraft object
    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
    # 1, 0 하면 한 총알로 여럿 죽여서 난이도 낮아짐 -> 랜덤박스 혜택?

    enemies2_down = pygame.sprite.groupcollide(enemies2, player.bullets, 0, 1)
    for enemy_hit in enemies2_down:
        enemy_hit.hp -= 1
        if enemy_hit.hp < 1:
            enemies2.remove(enemy_hit)
            enemies1.add(enemy_hit)

    # set coins
    if enemies1_down:
        coin_pos = list(enemy.rect.topleft)
        coin = Coin(coin_shine, coin_pos)
        coins.add(coin)

    for coin in coins:
        coin.move()
        if pygame.sprite.collide_circle(coin, player):
            coins.remove(coin)
            score += 1000
            # sound.play()

    # draw background
    SCREEN.fill(0)
    if n <= 20:
        SCREEN.blit(background[0], (bg_widths, bg_heights[0]))
        bg_heights[0] += 3
    elif n <= 40:
        SCREEN.blit(background[1], (bg_widths, bg_heights[1]))
        bg_heights[1] += 5
    elif n <= 60:
        SCREEN.blit(background[2], (bg_widths, bg_heights[2]))
        bg_heights[2] += 3
    elif n <= 80:
        SCREEN.blit(background[3], (bg_widths, bg_heights[3]))
        bg_heights[3] += 4
    elif n <= 100:
        SCREEN.blit(background[4], (bg_widths, bg_heights[4]))
        bg_heights[4] += 3
    else:
        SCREEN.blit(background[5], (bg_widths, bg_heights[5]))
        bg_heights[5] += 5

    # draw player plane
    if not player.is_hit:
        SCREEN.blit(player.image[player.img_index], player.rect)
        # Change the picture index to plane's animation effect
        player.img_index = shoot_frequency // 8
    else:
        player.img_index = player_down_index // 8
        SCREEN.blit(player.image[player.img_index], player.rect)
        player_down_index += 1
        if player_down_index > 47:
            running = False
    if player.rect.left >= SCREEN_WIDTH - player.rect.height:
        # 화면 비율 축소시 플레이어 위치 화면 안으로 자동 조절
        player.rect.left = SCREEN_WIDTH - player.rect.height

    # draw bullets and enemy planes and coins
    player.bullets.draw(SCREEN)  # background moving
    enemies1.draw(SCREEN)
    enemies2.draw(SCREEN)
    coins.draw(SCREEN)

    # draw score
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    SCREEN.blit(score_text, text_rect)

    # update screen
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # keyboard events
    key_pressed = pygame.key.get_pressed()

    if not player.is_hit:
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            player.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            player.moveRight()


font = pygame.font.Font(None, 48)
text = font.render('Score: ' + str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = SCREEN.get_rect().centerx
text_rect.centery = SCREEN.get_rect().centery + 24
SCREEN.blit(game_over, (0, 0))
SCREEN.blit(text, text_rect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
