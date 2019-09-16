from enum import Enum

import pygame, thorpy

from vars import screen_middle_h


class GuiStatus(Enum):
    init = 1
    gameStart = 2
    gameJoin = 3
    gameJoinList = 4
    hasGameId = 5

class Menu:
    gameId = None 
    status = GuiStatus.init
    

    def menuOn(self):
        return self.status != GuiStatus.hasGameId

    def draw(self, screen):
        title = pygame.image.load("res/Title.png").convert()
        screen.blit(title, (screen_middle_h - 150, 30))