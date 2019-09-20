import pygame

from api import Api
from attackboard import AttackBoard
from defenseboard import DefenseBoard
from game import Game
from menu import Menu
from vars import *

def clear_previous_games(player_name):
# Clears all previous games with this player
    player_info = Api.getPlayerInfo(player_name)
    for gameId in player_info['games']:
        Api.deleteGame(gameId)






def main():
    player1 = "joao1"
    player2 = "joao2"

    # Initiate api
    clear_previous_games(player1)
    r = Api.startGame(player1, player2)
    game_id = r["id"]
    
    print("Starting game " + game_id)

    pygame.init()
    pygame.display.set_caption("Battleship")

    screen = pygame.display.set_mode((screen_width, screen_height))

    menu = Menu()
    game = Game(game_id, screen, player1)

    if menu.menuOn():
        menu.draw(screen)
    else:
        game.draw()

    running = True
    counter = 100

    while running:
        needs_redraw = False
        if menu.menuOn():
            pass
        else:
            needs_redraw = game.frame_update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if menu.menuOn():
                    pass
                else:
                    needs_redraw = game.handle_events(event)
                    
        if needs_redraw:
            game.draw()
                    
if __name__ == "__main__":
    main()