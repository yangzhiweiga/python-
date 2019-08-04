# -*- coding:utf-8 -*-
import pygame
from plan_sprites import *

# 1、初始化游戏模块
pygame.init()

# 2、创建游戏窗口 宽度：480 高度：700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图片
# 2.1、加载图像数据
bg = pygame.image.load("./images/background.png")
# 2.2、绘制图像到屏幕
screen.blit(bg, (0, 0))

# 加载英雄图像数据
hero = pygame.image.load("./images/hero.gif")
# 绘制英雄图像
screen.blit(hero, (150, 150))
# 2.3、update更新屏幕显示
pygame.display.update()

hero_rect = pygame.Rect(150, 500, 102, 126)
clock = pygame.time.Clock()

# 创建敌机的精灵图像
enemy1 = GameSprites("./images/enemy1.png")
enemy2 = GameSprites("./images/enemy1.png", 2)

enemy_group = pygame.sprite.Group(enemy1, enemy2)
while True:
    clock.tick(60)

    for event in pygame.event.get():
        # 判断用户是否点击了关闭按钮
        if event.type == pygame.QUIT:
            print("退出游戏")
            # 卸载所有的模块
            pygame.quit()

            # 直接退出系统
            exit()

    if hero_rect.y <= 0:
        hero_rect.y = 700
    # 修改飞机的未知
    hero_rect.y -= 1

    # 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()
pygame.quit()
