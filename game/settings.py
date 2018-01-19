# -*- coding:utf-8 -*-

class Settings:
    """存储所有《外星人入侵》的设置的类"""
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width=800
        self.screen_height=400
        self.bg_color=(230,230,230)

        #飞船速度
        self.ship_speed_factor=1.5

        #子弹属性
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60

        #子弹速度
        self.bullet_speed_factor=1
        self.bullet_allowed = 3

