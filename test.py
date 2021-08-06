import pygame
from pygame.locals import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 450))  # 窗口的大小
    pygame.display.set_caption('pygame程序的界面的中文设置')  # 窗口标题，中文不需要特别的设置
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    # font = pygame.font.Font(None, 60) #原始代码，使用默认字体，不能显示中文
    font = pygame.font.Font('C:/Windows/Fonts/simsun.ttc', 60)  # 显示中文的设置和字体，及路径
    text = font.render("最高分：", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.center = background.get_rect().center
    background.blit(text, textpos)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
                screen.blit(background, (0, 0))
                pygame.display.flip()


if __name__ == '__main__':
    main()