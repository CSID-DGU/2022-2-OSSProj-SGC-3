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
from Defs import *
import random
import dataLoad
from register import user


def startGame(running_start):

    pygame.init()
    pygame.display.set_caption(Content.gameplay.value)

    SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()

    # Sounds
    star_sound = pygame.mixer.Sound(Sounds.star.value)
    gameover_sound = pygame.mixer.Sound(Sounds.gameover.value)
    coin_sound = pygame.mixer.Sound(Sounds.coin.value)
    meteor_sound = pygame.mixer.Sound(Sounds.meteor.value)
    bomb_sound = pygame.mixer.Sound(Sounds.bomb.value)
    blind_sound = pygame.mixer.Sound(Sounds.blind.value)
    coinx2_sound = pygame.mixer.Sound(Sounds.coins.value)
    mirror_sound = pygame.mixer.Sound(Sounds.mirror.value)
    bullet_sound = pygame.mixer.Sound(Sounds.bullet.value)
    bullet_sound.set_volume(Sounds.volume_small.value)

    # backgorund image setting  # space - chess - green - pirate - card - desert
    background = []
    background.append(pygame.image.load(
        Images.bg_space.value).convert_alpha())
    background.append(pygame.image.load(
        Images.bg_chess.value).convert_alpha())
    background.append(pygame.image.load(
        Images.bg_green.value).convert_alpha())
    background.append(pygame.image.load(
        Images.bg_pirate.value).convert_alpha())
    background.append(pygame.image.load(
        Images.bg_card.value).convert_alpha())
    background.append(pygame.image.load(
        Images.bg_desert.value).convert_alpha())
    background.append(pygame.image.load(
        Images.bg_planet.value).convert_alpha())
    background.append(pygame.image.load(
        Images.bg_world.value).convert_alpha())

    bg_widths = -(Game.d_weight.value-SCREEN_WIDTH)/Display.width_divide3.value
    bg_h = -(Game.d_height.value-SCREEN_HEIGHT-Game.p_margin.value)
    bg_e = -(Game.e_height.value-SCREEN_HEIGHT-Game.p_margin.value)
    bg_heights = [bg_h, bg_h, bg_h, bg_h, bg_h,
                  bg_h, bg_h, bg_h, bg_h, bg_h, bg_h, bg_e]

    dim0 = Game.dim.value*Dimension.dim1.value
    dim1 = Game.dim.value*Dimension.dim2.value
    dim2 = Game.dim.value*Dimension.dim3.value
    dim3 = Game.dim.value*Dimension.dim4.value
    dim4 = Game.dim.value*Dimension.dim5.value
    dim5 = Game.dim.value*Dimension.dim6.value
    dim6 = Game.dim.value*Dimension.dim7.value
    dim7 = Game.dim.value*Dimension.dim8.value
    dim8 = Game.dim.value*Dimension.dim9.value
    dim9 = Game.dim.value*Dimension.dim10.value
    dim_end = Game.dim.value*Dimension.dim11.value

    ending = False

    plane_img = pygame.image.load(Images.shoot.value).convert_alpha()

    # Player display
    player_rect = []
    player_rect.append(pygame.Rect(Plane.p1.value))
    player_rect.append(pygame.Rect(Plane.p2.value))
    player_rect.append(pygame.Rect(Plane.p3.value))
    player_rect.append(pygame.Rect(Plane.p4.value))
    player_rect.append(pygame.Rect(Plane.p5.value))
    player_rect.append(pygame.Rect(Plane.p6.value))
    player_pos = [SCREEN_WIDTH/Display.width_divide2.value,
                  SCREEN_HEIGHT-Game.p_margin.value]
    player = Player(plane_img, player_rect, player_pos)

    # Define parameters ; bullet object
    weapon = dataLoad.item_apply_get(user)

    if weapon == Content.basic.value:
        bullet_rect = pygame.Rect(Plane.bullet.value)
        bullet_img = plane_img.subsurface(bullet_rect)
    else:
        if weapon == Content.items.value[-1]:  # last item == special item
            ending = True
        image_path = Content.img_path.value + weapon + Content.img_size16.value
        bullet_img = pygame.image.load(image_path).convert_alpha()

    # Define parameters ; enemy aircraft object
    enemy1_img_space = plane_img
    enemy1_img_chess = pygame.image.load(
        Images.black_knight.value).convert_alpha()
    enemy1_img_green = pygame.image.load(
        Images.bat.value).convert_alpha()
    enemy1_img_pirate = pygame.image.load(
        Images.pirate_ship.value).convert_alpha()
    enemy1_img_card = pygame.image.load(
        Images.card_jack.value).convert_alpha()
    enemy1_img_desert = pygame.image.load(
        Images.snake.value).convert_alpha()

    enemy1_rect = []
    enemy1_rect.append(pygame.Rect(Plane.e1.value))
    enemy1_rect.append(enemy1_img_chess.get_rect())
    enemy1_rect.append(enemy1_img_green.get_rect())
    enemy1_rect.append(enemy1_img_pirate.get_rect())
    enemy1_rect.append(enemy1_img_card.get_rect())
    enemy1_rect.append(enemy1_img_desert.get_rect())

    enemy1_img = []
    enemy1_img.append(enemy1_img_space.subsurface(enemy1_rect[0]))
    enemy1_img.append(enemy1_img_chess.subsurface(enemy1_rect[1]))
    enemy1_img.append(enemy1_img_green.subsurface(enemy1_rect[2]))
    enemy1_img.append(enemy1_img_pirate.subsurface(enemy1_rect[3]))
    enemy1_img.append(enemy1_img_card.subsurface(enemy1_rect[4]))
    enemy1_img.append(enemy1_img_desert.subsurface(enemy1_rect[5]))

    # Define parameters ; enemy type 2 aircraft object
    enemy2_img_space = plane_img
    enemy2_img_chess = pygame.image.load(
        Images.white_king.value).convert_alpha()
    enemy2_img_green = pygame.image.load(
        Images.lizard.value).convert_alpha()
    enemy2_img_pirate = pygame.image.load(
        Images.kraken.value).convert_alpha()
    enemy2_img_card = pygame.image.load(
        Images.card_queen.value).convert_alpha()
    enemy2_img_desert = pygame.image.load(
        Images.desert_scolpion.value).convert_alpha()

    enemy2_rect = []
    enemy2_rect.append(pygame.Rect(Plane.e2.value))
    enemy2_rect.append(enemy2_img_chess.get_rect())
    enemy2_rect.append(enemy2_img_green.get_rect())
    enemy2_rect.append(enemy2_img_pirate.get_rect())
    enemy2_rect.append(enemy2_img_card.get_rect())
    enemy2_rect.append(enemy2_img_desert.get_rect())

    enemy2_img = []
    enemy2_img.append(enemy2_img_space.subsurface(enemy2_rect[0]))
    enemy2_img.append(enemy2_img_chess.subsurface(enemy2_rect[1]))
    enemy2_img.append(enemy2_img_green.subsurface(enemy2_rect[2]))
    enemy2_img.append(enemy2_img_pirate.subsurface(enemy2_rect[3]))
    enemy2_img.append(enemy2_img_card.subsurface(enemy2_rect[4]))
    enemy2_img.append(enemy2_img_desert.subsurface(enemy2_rect[5]))

    enemy1_hp = Display.hp_low.value
    enemy2_hp = Display.hp_high.value

    enemies1 = pygame.sprite.Group()
    enemies2 = pygame.sprite.Group()

    # Define parameters ; coin object
    coin1_img = pygame.image.load(Images.coin1.value).convert_alpha()
    coin2_img = pygame.image.load(Images.coin2.value).convert_alpha()
    coin3_img = pygame.image.load(Images.coin3.value).convert_alpha()
    coin4_img = pygame.image.load(Images.coin4.value).convert_alpha()
    coin5_img = pygame.image.load(Images.coin5.value).convert_alpha()
    coin6_img = pygame.image.load(Images.coin6.value).convert_alpha()

    coin_rect = coin1_img.get_rect()
    coin_img = coin1_img.subsurface(coin_rect)

    shine_imgs = []
    shine_imgs.append(coin1_img.subsurface(coin_rect))
    shine_imgs.append(coin2_img.subsurface(coin_rect))
    shine_imgs.append(coin3_img.subsurface(coin_rect))
    shine_imgs.append(coin4_img.subsurface(coin_rect))
    shine_imgs.append(coin5_img.subsurface(coin_rect))
    shine_imgs.append(coin6_img.subsurface(coin_rect))

    coins = pygame.sprite.Group()

    # Define parameters ; star (random box) object
    star1_img = pygame.image.load(Images.star1.value).convert_alpha()
    star2_img = pygame.image.load(Images.star2.value).convert_alpha()
    star3_img = pygame.image.load(Images.star3.value).convert_alpha()
    star4_img = pygame.image.load(Images.star4.value).convert_alpha()
    star5_img = pygame.image.load(Images.star5.value).convert_alpha()
    star6_img = pygame.image.load(Images.star6.value).convert_alpha()
    star7_img = pygame.image.load(Images.star7.value).convert_alpha()

    star1_rect = star1_img.get_rect()
    star2_rect = star2_img.get_rect()
    star3_rect = star3_img.get_rect()
    star4_rect = star4_img.get_rect()
    star5_rect = star5_img.get_rect()
    star6_rect = star6_img.get_rect()
    star7_rect = star7_img.get_rect()

    star_img = star1_img.subsurface(star1_rect)

    spin_imgs = []
    spin_imgs.append(star1_img.subsurface(star1_rect))
    spin_imgs.append(star2_img.subsurface(star2_rect))
    spin_imgs.append(star3_img.subsurface(star3_rect))
    spin_imgs.append(star4_img.subsurface(star4_rect))
    spin_imgs.append(star5_img.subsurface(star5_rect))
    spin_imgs.append(star6_img.subsurface(star6_rect))
    spin_imgs.append(star7_img.subsurface(star7_rect))

    stars = pygame.sprite.Group()

    # stars effect mode
    blind_img = pygame.image.load(
        Images.blind.value).convert_alpha()
    blind_rect = blind_img.get_rect()
    blind = blind_img.subsurface(blind_rect)
    blinds = pygame.sprite.Group()

    bomb_img = pygame.image.load(Images.bomb.value).convert_alpha()
    bomb_rect = bomb_img.get_rect()
    bomb = bomb_img.subsurface(bomb_rect)
    bombs = pygame.sprite.Group()

    mirror_img = pygame.image.load(
        Images.mirror.value).convert_alpha()
    mirror_rect = mirror_img.get_rect()
    mirror = mirror_img.subsurface(mirror_rect)
    double_img = pygame.image.load(Images.double.value).convert_alpha()
    double_rect = double_img.get_rect()
    double = double_img.subsurface(double_rect)
    modes = pygame.sprite.Group()

    mirror_mode = False

    # meteorite
    meteor_img = pygame.image.load(
        Images.meteor.value).convert_alpha()
    meteor_rect = meteor_img.get_rect()
    meteor = meteor_img.subsurface(meteor_rect)
    meteors = pygame.sprite.Group()

    # Setting others
    shoot_frequency = Frequency.fq_init.value
    enemy_frequency = Frequency.fq_init.value
    random1_frequency = random.randint(
        Frequency.random1_fq_min.value, Frequency.random1_fq_max.value)
    star_frequency = Frequency.fq_medium.value
    random2_frequency = random.randint(
        Frequency.random2_fq_min.value, Frequency.random2_fq_max.value)
    meteor_frequency = Frequency.fq_low.value

    player_down_index = Divide.player.value

    score = Score.score_init.value
    km = 0

    clock = pygame.time.Clock()
    n = Display.clock_init.value
    t = Display.clock_t.value

    running = running_start

    while running:
        # set frame rate
        clock.tick(t)
        n += 1/t
        km += 1/t

        SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN.get_size()

        freq_shoot = (Resize.standard.value-(SCREEN_WIDTH //
                                             Resize.display.value))*Resize.shoot.value
        freq_enemy1 = (Resize.standard.value-(SCREEN_WIDTH //
                                              Resize.display.value))*Resize.enemy1.value
        freq_enemy2 = (Resize.standard.value-(SCREEN_WIDTH //
                                              Resize.display.value))*Resize.enemy2.value

        # set firing bullets
        if (not player.is_hit) and (n < dim_end):
            if shoot_frequency % freq_shoot == Frequency.fq_init.value:
                bullet_sound.play()
                player.shoot(bullet_img)
            shoot_frequency += 1
            if shoot_frequency >= freq_shoot:
                shoot_frequency = Frequency.fq_init.value

        # set enemy planes
        if (enemy_frequency % freq_enemy1 == Frequency.fq_init.value) and (n < dim_end):
            enemy1_pos = [random.randint(
                Utilization.edge.value, SCREEN_WIDTH - enemy1_rect[Utilization.x.value].width), Utilization.edge.value]
            enemy1 = Enemy(enemy1_img, Speed.enemy1.value,
                           enemy1_pos, enemy1_hp)
            enemies1.add(enemy1)
        elif (enemy_frequency % freq_enemy2 == Frequency.fq_init.value) and (n < dim_end):
            enemy2_pos = [random.randint(
                Utilization.edge.value, SCREEN_WIDTH - enemy2_rect[Utilization.x.value].width), Utilization.edge.value]
            enemy2 = Enemy(enemy2_img, Speed.enemy2.value,
                           enemy2_pos, enemy2_hp)
            enemies2.add(enemy2)
        enemy_frequency += 1

        # move the bullet, and delete it
        for bullet in player.bullets:
            bullet.move()
            if bullet.rect.bottom < Utilization.edge.value:
                player.bullets.remove(bullet)

        # move the enemy plane, and delete it
        for enemy in enemies1:
            enemy.move()
            # determine if the player has been hit
            if pygame.sprite.collide_circle(enemy, player):
                enemies1.remove(enemy)
                player.is_hit = True
                gameover_sound.play()
                break
            if enemy.rect.top > SCREEN_HEIGHT:
                enemies1.remove(enemy)
            if n < dim0:
                enemy.image = enemy1_img[BackGround.space.value]
            elif n > dim0 and n <= dim1:
                enemy.image = enemy1_img[BackGround.chess.value]
            elif n > dim1 and n <= dim2:
                enemy.image = enemy1_img[BackGround.green.value]
            elif n > dim2 and n <= dim3:
                enemy.image = enemy1_img[BackGround.pirate.value]
            elif n > dim3 and n <= dim4:
                enemy.image = enemy1_img[BackGround.card.value]
            elif n > dim4 and n <= dim5:
                enemy.image = enemy1_img[BackGround.desert.value]
            elif n > dim5 and n <= dim6:
                enemy.image = enemy1_img[BackGround.chess.value]
            elif n > dim6 and n <= dim7:
                enemy.image = enemy1_img[BackGround.green.value]
            elif n > dim7 and n <= dim8:
                enemy.image = enemy1_img[BackGround.pirate.value]
            elif n > dim8 and n <= dim9:
                enemy.image = enemy1_img[BackGround.card.value]
            else:
                enemy.image = enemy1_img[BackGround.desert.value]

        for enemy in enemies2:
            enemy.move()
            # determine if the player has been hit
            if pygame.sprite.collide_circle(enemy, player):
                enemies2.remove(enemy)
                player.is_hit = True
                gameover_sound.play()
                break
            if enemy.rect.top > SCREEN_HEIGHT:
                enemies2.remove(enemy)
            if n < dim0:
                enemy.image = enemy2_img[BackGround.space.value]
            elif n > dim0 and n <= dim1:
                enemy.image = enemy2_img[BackGround.chess.value]
            elif n > dim1 and n <= dim2:
                enemy.image = enemy2_img[BackGround.green.value]
            elif n > dim2 and n <= dim3:
                enemy.image = enemy2_img[BackGround.pirate.value]
            elif n > dim3 and n <= dim4:
                enemy.image = enemy2_img[BackGround.card.value]
            elif n > dim4 and n <= dim5:
                enemy.image = enemy2_img[BackGround.desert.value]
            elif n > dim5 and n <= dim6:
                enemy.image = enemy2_img[BackGround.chess.value]
            elif n > dim6 and n <= dim7:
                enemy.image = enemy2_img[BackGround.green.value]
            elif n > dim7 and n <= dim8:
                enemy.image = enemy2_img[BackGround.pirate.value]
            elif n > dim8 and n <= dim9:
                enemy.image = enemy2_img[BackGround.card.value]
            else:
                enemy.image = enemy2_img[BackGround.desert.value]

        # add the hit enemy aircraft object
        enemies1_down = pygame.sprite.groupcollide(
            enemies1, player.bullets, True, True)

        enemies2_down = pygame.sprite.groupcollide(
            enemies2, player.bullets, False, True)
        for enemy_hit in enemies2_down:
            enemy_hit.hp -= 1
            if enemy_hit.hp < enemy1_hp:
                enemies2.remove(enemy_hit)
                enemies1.add(enemy_hit)

        # set coins
        if enemies1_down:
            coin_pos = [random.randint(
                Utilization.edge.value, SCREEN_WIDTH - coin_rect.width), Utilization.edge.value]
            coin = Coin(coin_img, shine_imgs, coin_pos)
            coins.add(coin)

        # set stars
        if (not player.is_hit) and (n < dim_end):
            if random1_frequency % star_frequency == Frequency.fq_init.value:
                type = random.randint(
                    Frequency.random_star_start.value, Frequency.random_star_end.value)
                star_sound.play()
                star = Star(star_img, spin_imgs, type)
                stars.add(star)
            random1_frequency += 1

        # set meteors
        if (not player.is_hit) and (n < dim_end):
            if random2_frequency % meteor_frequency == Frequency.fq_init.value:
                meteor_sound.play()
                meteor_pos = [random.randint(
                    Utilization.edge.value, SCREEN_WIDTH - meteor_rect.width), Utilization.edge.value]
                meteor = Meteor(meteor_img, meteor_pos)
                meteors.add(meteor)
            random2_frequency += 1

        # draw background
        SCREEN.fill(0)
        if n < dim0:
            SCREEN.blit(background[BackGround.space.value],
                        (bg_widths, bg_heights[Dimension.dim0.value]))
            bg_heights[Dimension.dim0.value] += Speed.bg.value+1
        elif n < dim1:
            SCREEN.blit(background[BackGround.chess.value],
                        (bg_widths, bg_heights[Dimension.dim1.value]))
            bg_heights[Dimension.dim1.value] += Speed.bg.value
        elif n < dim2:
            SCREEN.blit(background[BackGround.green.value],
                        (bg_widths, bg_heights[Dimension.dim2.value]))
            bg_heights[Dimension.dim2.value] += Speed.bg.value
        elif n < dim3:
            SCREEN.blit(background[BackGround.pirate.value],
                        (bg_widths, bg_heights[Dimension.dim3.value]))
            bg_heights[Dimension.dim3.value] += Speed.bg.value
        elif n < dim4:
            SCREEN.blit(background[BackGround.card.value],
                        (bg_widths, bg_heights[Dimension.dim4.value]))
            bg_heights[Dimension.dim4.value] += Speed.bg.value
        elif n < dim5:
            SCREEN.blit(background[BackGround.desert.value],
                        (bg_widths, bg_heights[Dimension.dim5.value]))
            bg_heights[Dimension.dim5.value] += Speed.bg.value
        elif n < dim6:
            SCREEN.blit(background[BackGround.chess.value],
                        (bg_widths, bg_heights[Dimension.dim6.value]))
            bg_heights[Dimension.dim6.value] += Speed.bg.value
        elif n < dim7:
            SCREEN.blit(background[BackGround.green.value],
                        (bg_widths, bg_heights[Dimension.dim7.value]))
            bg_heights[Dimension.dim7.value] += Speed.bg.value
        elif n < dim8:
            SCREEN.blit(background[BackGround.pirate.value],
                        (bg_widths, bg_heights[Dimension.dim8.value]))
            bg_heights[Dimension.dim8.value] += Speed.bg.value
        elif n < dim9:
            SCREEN.blit(background[BackGround.card.value],
                        (bg_widths, bg_heights[Dimension.dim9.value]))
            bg_heights[Dimension.dim9.value] += Speed.bg.value
        elif n < dim_end:
            SCREEN.blit(background[BackGround.desert.value],
                        (bg_widths, bg_heights[Dimension.dim10.value]))
            bg_heights[Dimension.dim10.value] += Speed.bg.value
        else:
            if ending == False:
                SCREEN.blit(background[BackGround.ending.value],
                            (bg_widths, bg_heights[Dimension.dim11.value]))
                bg_heights[Dimension.dim11.value] += 1
                ending_font = pygame.font.Font(None, Font.e_size.value)
                ending_text1 = ending_font.render(
                    Game.end_message1.value, True, Font.e_color.value)
                ending_text2 = ending_font.render(
                    Game.end_message2.value, True, Font.e_color.value)
                ending_text3 = ending_font.render(
                    Game.end_message3.value, True, Font.e_color.value)
                text_rect1 = ending_text1.get_rect()
                text_rect2 = ending_text2.get_rect()
                text_rect3 = ending_text3.get_rect()
                text_rect1.midtop = [SCREEN_WIDTH/Display.width_divide2.value,
                                     SCREEN_HEIGHT/Display.width_divide2.value-Font.e_size.value]
                text_rect2.midtop = [
                    SCREEN_WIDTH/Display.width_divide2.value, SCREEN_HEIGHT/Display.width_divide2.value]
                text_rect3.midtop = [SCREEN_WIDTH/Display.width_divide2.value,
                                     SCREEN_HEIGHT/Display.width_divide2.value+Font.e_size.value]
                SCREEN.blit(ending_text1, text_rect1)
                SCREEN.blit(ending_text2, text_rect2)
                SCREEN.blit(ending_text3, text_rect3)
            elif ending == True:
                SCREEN.blit(background[BackGround.s_ending.value],
                            (bg_widths, bg_heights[Dimension.dim11.value]))
                bg_heights[Dimension.dim11.value] += 1
                ending_font = pygame.font.Font(None, Font.e_size.value)
                ending_text1 = ending_font.render(
                    Game.close_message1.value, True, Font.e_color.value)
                ending_text2 = ending_font.render(
                    Game.close_message2.value, True, Font.e_color.value)
                text_rect1 = ending_text1.get_rect()
                text_rect2 = ending_text2.get_rect()
                text_rect1.midtop = [SCREEN_WIDTH/Display.width_divide2.value,
                                     SCREEN_HEIGHT/Display.width_divide2.value-Font.e_size.value]
                text_rect2.midtop = [
                    SCREEN_WIDTH/Display.width_divide2.value, SCREEN_HEIGHT/2]
                SCREEN.blit(ending_text1, text_rect1)
                SCREEN.blit(ending_text2, text_rect2)
            if n > dim_end + Game.end.value:
                # player.is_hit = True
                running = False

        # draw player plane
        if not player.is_hit:
            SCREEN.blit(player.image[0], player.rect)
        else:
            # Change the picture index to plane's animation effect
            player.img_index = player_down_index // Divide.player_i.value
            SCREEN.blit(player.image[player.img_index], player.rect)
            player_down_index += 1
            if player_down_index > Divide.player_d.value:
                running = False
        # 화면 비율 축소시 플레이어 위치 화면 안으로 자동 조절
        if player.rect.left >= SCREEN_WIDTH - player.rect.width:
            player.rect.left = SCREEN_WIDTH - player.rect.width
        if player.rect.top >= SCREEN_HEIGHT - player.rect.height:
            player.rect.top = SCREEN_HEIGHT - player.rect.height

        # draw shine animation
        for coin in coins:
            coin.move()
            if pygame.sprite.collide_circle(coin, player):
                coins.remove(coin)
                score += Score.score_coin.value
                coin_sound.play()
            if coin.rect.top > SCREEN_HEIGHT:
                coins.remove(coin)

        # draw spin animation
        for star in stars:
            star.move()
            if pygame.sprite.collide_circle(star, player):
                stars.remove(star)
                if star.type == StarMode.mode0.value:
                    # blind mode
                    blind1 = Blind(blind)
                    blinds.add(blind1)
                    blind_sound.play()
                elif star.type == StarMode.mode1.value:
                    # mirror mode
                    mode1 = Mode(mirror)
                    modes.add(mode1)
                    mirror_mode = True
                    mirror_sound.play()
                elif star.type == StarMode.mode2.value:
                    # bomb
                    bomb1 = Bomb(bomb)
                    bombs.add(bomb1)
                    bomb_sound.play()
                elif star.type == StarMode.mode3.value:
                    # score double
                    mode1 = Mode(double)
                    modes.add(mode1)
                    score += score
                    coinx2_sound.play()
            if star.rect.top > SCREEN_HEIGHT:
                stars.remove(star)

        for blinds1 in blinds:
            blinds1.move()
            if blinds1.rect.left > SCREEN_WIDTH:
                blinds.remove(blinds1)

        for modes1 in modes:
            modes1.show()
            if modes1.rect.left > SCREEN_WIDTH:
                modes.remove(modes1)
                mirror_mode = False

        for bombs1 in bombs:
            bombs1.attack()
            pygame.sprite.groupcollide(
                enemies1, bombs, True, False)
            pygame.sprite.groupcollide(
                enemies2, bombs, True, False)
            if bombs1.rect.bottom < Utilization.edge.value:
                bombs.remove(bombs1)

        # draw meteor animation
        for meteor in meteors:
            meteor.move()
            if pygame.sprite.collide_circle(meteor, player):
                player.is_hit = True
                gameover_sound.play()
                break
            if meteor.rect.top > SCREEN_HEIGHT:
                meteors.remove(meteor)

        # draw bullets and enemy planes and coins
        player.bullets.draw(SCREEN)
        enemies1.draw(SCREEN)
        enemies2.draw(SCREEN)
        coins.draw(SCREEN)
        stars.draw(SCREEN)
        meteors.draw(SCREEN)
        bombs.draw(SCREEN)
        blinds.draw(SCREEN)
        modes.draw(SCREEN)

        # draw score
        score_font = pygame.font.Font(None, Font.size.value)
        score_text = score_font.render(str(score), True, Font.color.value)
        text_rect = score_text.get_rect()
        text_rect.topleft = [Font.margin.value, Font.margin.value]
        SCREEN.blit(score_text, text_rect)

        # draw way (the distance player've been through)
        way = int(km)
        way_font = pygame.font.Font(None, Font.size.value)
        way_text = way_font.render(str(way)+"ly", True, Font.color.value)
        way_rect = way_text.get_rect()
        way_rect.topright = [SCREEN_WIDTH-Font.margin.value, Font.margin.value]
        SCREEN.blit(way_text, way_rect)

        # update screen
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == VIDEORESIZE:
                width, height = event.size
                if width < Display.minscreen_x.value:
                    width = Display.minscreen_x.value
                if height < Display.minscreen_y.value:
                    height = Display.minscreen_y.value
                pygame.display.set_mode(
                    (width, height), HWSURFACE | DOUBLEBUF | RESIZABLE)

        # keyboard events
        key_pressed = pygame.key.get_pressed()

        if not player.is_hit:
            if mirror_mode == False:
                if key_pressed[K_a] or key_pressed[K_LEFT]:
                    player.moveLeft()
                if key_pressed[K_d] or key_pressed[K_RIGHT]:
                    player.moveRight()
            elif mirror_mode == True:
                if key_pressed[K_a] or key_pressed[K_LEFT]:
                    player.moveRight()
                if key_pressed[K_d] or key_pressed[K_RIGHT]:
                    player.moveLeft()

    if running == False:
        global total_score
        total_score = score
        import gameEnd

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == VIDEORESIZE:
                width, height = event.size
                if width < Display.minscreen_x.value:
                    width = Display.minscreen_x.value
                if height < Display.minscreen_y.value:
                    height = Display.minscreen_y.value
                pygame.display.set_mode(
                    (width, height), HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.update()
