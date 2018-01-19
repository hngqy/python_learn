# -*- coding:utf-8 -*-

import pygame
import sys
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

#检测事件
def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
           check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
           check_keyup_events(event,ship)

#更新screen
def update_screan(ai_settings,screen,ship,alien,bullets):
    """更换屏幕中图像"""

    screen.fill(ai_settings.bg_color)
    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()

    #让最近屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    #更新子弹位置
    bullets.update()
    # 移除超越边界的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
    # 创建一个子弹，并把子弹发在bullets里面管理
    if len(bullets) < ai_settings.bullet_allowed:
        bullet = Bullet(ai_settings, screen, ship)
        bullets.add(bullet)