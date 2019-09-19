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
        return False
        #return self.status != GuiStatus.hasGameId

    def start_game(self):
        pass
    
    def join_game(self):
        pass
    
    def draw(self, screen):
        title = pygame.image.load("res/Title.png").convert_alpha()
        screen.blit(title, (screen_middle_h - 150, 30))
        
        startNewButton = thorpy.make_button("Start Game", self.start_game)
        joinButton = thorpy.make_button("Join Game", self.join_game)