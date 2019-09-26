import pygame

from api import Api
from game import Game
from menu import Menu
from vars import *


def clear_previous_games(player_name):
    # Clears all previous games with this player
    player_info = Api.getPlayerInfo(player_name)
    for gameId in player_info['games']:
        Api.deleteGame(gameId)


def init_game(game_id, screen, player1, player2, local_player):
    print("Starting game ", game_id, ": ", player1, " v. ", player2)
    return Game(game_id, screen, player1, player2, local_player)


def main():
    game_id = None
    
    # Initiate api
    #clear_previous_games("joao1")

    pygame.init()
    pygame.display.set_caption("Battleship")

    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(background_color)
    pygame.display.flip()
    
    menu = Menu(screen)

    running = True
    while running:
        needs_redraw = False
        if game_id is None:
            game_id = menu.get_game_id()
            if game_id is not None:
                game = init_game(game_id, screen, *menu.get_player_info())
                needs_redraw = True
        else:
            game_id = game.get_game_id()
            if game_id is None:
                menu.__init__(screen)
        
        if game_id is not None:
            needs_redraw = needs_redraw or game.frame_update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if game_id is None:
                    menu.react(event)
                else:
                    needs_redraw = needs_redraw or game.handle_events(event)
                    
        if needs_redraw:
            game.draw()
                    
if __name__ == "__main__":
    main()