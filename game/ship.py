# -*- coding:utf-8 -*-

import pygame
from pygame import *

class Ship:
    """创建一个飞船类"""
    def __init__(self,ai_settings,screen):
        self.screen=screen
        #加载飞船图像并获取外接矩形
        self.image=pygame.image.load('image/plane2.PNG')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.ai_settings = ai_settings

        #将飞船放在屏幕底部中央
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = float(self.screen_rect.bottom)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left >0:
            self.rect.centerx += -1*self.ai_settings.ship_speed_factor