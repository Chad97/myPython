import sys
import pygame


def check_keydown_events(events, ship):
    """ 响应按下 """
    if events.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif events.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(events, ship):
    """ 响应抬起 """
    if events.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif events.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """ 响应鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                

def update_screen(ai_settings, screen, ship):
    """ 更新屏幕上的图像 并切换到新屏幕 """

    #  每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #  让最近绘制的屏幕可见
    pygame.display.flip()