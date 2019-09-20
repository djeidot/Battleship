import pygame

from api import Api
from attackboard import AttackBoard
from defenseboard import DefenseBoard
from vars import background_color


class Game:

    def __init__(self, game_id, screen, player1) -> None:
        super().__init__()
        self.game_id = game_id
        self.screen = screen
        self.player1 = player1
        self.attack_board = AttackBoard()
        self.defense_board = DefenseBoard()

    def update_game(self):
        self.game = Api.getGame(self.game_id)
        self.is_attacking = self.game['move'] == self.player1
        self.attack_board.update_board(self.game['player1']['knowledge'], self.is_attacking)
        self.defense_board.update_board(self.game['player2']['knowledge'], self.is_attacking)

    def draw(self):
        self.screen.fill(background_color)
        self.attack_board.draw(self.screen)
        self.defense_board.draw(self.screen)
        pygame.display.flip()
    
    def frame_update(self):
        if self.is_attacking:
            needs_update = self.attack_board.frame_update()
        else:
            needs_update = self.defense_board.frame_update()
            
        if needs_update:
            self.update_game()
        
        return needs_update

    def handle_events(self, event):
        if self.is_attacking:
            needs_update = self.attack_board.handle_event(event)
        else:
            needs_update = self.defense_board.handle_event(event)
            
        if needs_update:
            self.update_game()

        return needs_update

        
