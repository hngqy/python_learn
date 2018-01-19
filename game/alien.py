# -*- coding:utf-8 -*-
import pygame
from pygame import *
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self,ai_settings,screen):
        """初始化外星人，并设置起始位置"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #设置外星人照片，并设置rect属性
        self.image = pygame.image.load("image/alien3.PNG")
        self.rect = self.image.get_rect()

        #设置初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """指定外星人位置"""
        self.screen.blit(self.image,self.rect)
        pass