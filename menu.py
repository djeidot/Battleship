from enum import Enum

import pygame
import thorpy

from api import Api
from vars import *


class Menu:
    def __init__(self, screen) -> None:
        self.game_id = None
        self.screen = screen
        
        self.startNewButton = thorpy.make_button("Start Game", func=self.add_players)
        self.joinButton = thorpy.make_button("Join Game", func=self.join_game)

        self.player1Edit = thorpy.Inserter.make("Player 1 name: ")
        self.player2Edit = thorpy.Inserter.make("Player 2 name: ")

        self.box = thorpy.Box.make(elements=[self.startNewButton, self.joinButton], size=(300, 300))
        thorpy.store(self.box)
        self.box.set_center((screen_middle_h, screen_middle_v))

        self.menu = thorpy.Menu(self.box)
        for el in self.menu.get_population():
            el.surface = self.screen

        self.box.blit()
        self.box.update()
        
    def replace_elements(self, new_elements):
        self.box.unblit()
        for el in self.box.get_elements():
            el.unblit()
        self.box.update()
        self.box.remove_all_elements()
        self.box.add_elements(new_elements)
        for el in self.box.get_descendants():
            el.surface = self.screen
        thorpy.store(self.box)
        self.menu.rebuild(self.box)
        self.box.blit()
        self.box.update()
        
    def add_elements(self, new_elements):
        self.box.unblit()
        self.box.update()
        self.box.add_elements(new_elements)
        for el in self.box.get_descendants():
            el.surface = self.screen
        thorpy.store(self.box)
        self.menu.rebuild(self.box)
        self.box.blit()
        self.box.update()
        
    def start_menu(self):
        self.replace_elements([self.startNewButton, self.joinButton])
        
    def add_players(self):
        gameStartNewButton = thorpy.make_button("Start Game", func=self.start_game)
        goBackButton = thorpy.make_button("Go Back", func=self.start_menu)
        buttonsGroup = thorpy.make_group([gameStartNewButton, goBackButton])
        self.replace_elements([self.player1Edit, self.player2Edit, buttonsGroup])

    def start_game(self):
        self.player1 = self.player1Edit.get_value()
        self.player2 = self.player2Edit.get_value()
        self.local_player = 1
        r = Api.startGame(self.player1, self.player2)
        self.end_menu()
        self.game_id = r["id"]
        
    def start_game_join(self, event):
        game_id_local = event.value
        r = Api.getGame(game_id_local)
        self.player1 = r["player1"]["name"]
        self.player2 = r["player2"]["name"]
        self.local_player = 1 if self.playerJoiningEdit.get_value() == self.player1 else 2
        self.end_menu()
        self.game_id = game_id_local
    
    def join_game(self):
        self.playerJoiningEdit = thorpy.Inserter.make("Player name: ")
        playerJoiningEnterReaction = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                                     reac_func=self.get_games_list,
                                                     event_args={"id": thorpy.constants.EVENT_INSERT})
        self.playerJoiningEdit.add_reaction(playerJoiningEnterReaction)
        self.replace_elements([self.playerJoiningEdit])

    def get_games_list(self, event):
        player_name = event.el.get_value()
        r = Api.getPlayerInfo(player_name)
        games_list = [id for id in r["games"]] if r is not None else []
        label = thorpy.OneLineText.make("Here's a list of games " + player_name + " is in:")
        self.gamesListEdit = thorpy.DropDownList.make(games_list, size=(250,150), x=5)
        self.gamesListEdit.finish()
        gameSelectReaction = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                             reac_func=self.start_game_join,
                                             event_args={"id": thorpy.constants.EVENT_DDL})
        self.gamesListEdit.add_reaction(gameSelectReaction)
        goBackButton = thorpy.make_button("Go Back", func=self.start_menu)
        self.replace_elements([label, self.gamesListEdit, goBackButton])

    
    def get_game_id(self):
        return self.game_id
    
    def react(self, event):
        if self.menu is not None:
            self.menu.react(event)

    def draw(self, screen):
        title = pygame.image.load("res/Title.png").convert_alpha()
        screen.blit(title, (screen_middle_h - 150, 30))
        
    def end_menu(self):
        self.box.remove_all_elements()
        self.menu.remove_from_population(self.box)
        self.box = None
        self.menu = None
    
    def get_player_info(self):
        return (self.player1, self.player2, self.local_player)
