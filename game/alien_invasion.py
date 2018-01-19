# -*- coding:utf-8 -*-

import pygame
from pygame import *
import sys
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    #初始化游戏并创建屏幕
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_setting,screen)
    alien = Alien(ai_setting,screen)

    bullets = Group()
    #开始游戏主循环
    while True:
        gf.check_events(ai_setting,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screan(ai_setting,screen,ship,alien,bullets)
run_game()