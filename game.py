import pygame

from api import Api
from attackboard import AttackBoard
from defenseboard import DefenseBoard
from vars import background_color


class Game:

    def __init__(self, game_id, screen, player1, player2, local_player) -> None:
        super().__init__()
        self.game_id = game_id
        self.screen = screen
        self.local_player = player1 if local_player else player2
        self.remote_player = player2 if local_player else player1
        self.local_player_tag = 'player1' if local_player else 'player2'
        self.remote_player_tag = 'player2' if local_player else 'player1'
        self.local_player = local_player
        self.attack_board = AttackBoard(self.game_id, self.local_player)
        self.defense_board = DefenseBoard()
        self.update_game()

    def update_game(self):
        self.game = Api.getGame(self.game_id)
        self.is_attacking = self.game['move'] == self.local_player
        self.attack_board.update_board(self.game[self.local_player_tag]['knowledge'], self.is_attacking)
        self.defense_board.update_board(self.game[self.remote_player_tag]['knowledge'], self.is_attacking)

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

        
