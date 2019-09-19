import pygame

from api import Api
from attackboard import AttackBoard
from defenseboard import DefenseBoard
from menu import Menu
from vars import *

def clear_previous_games(player_name):
# Clears all previous games with this player
    player_info = Api.getPlayerInfo(player_name)
    for gameId in player_info['games']:
        Api.deleteGame(gameId)


def update_boards(screen, attack_board, defense_board, game, player1):
    is_attacking = game['move'] == player1
    screen.fill(background_color)
    attack_board.update_board(game['player1']['knowledge'], is_attacking)
    attack_board.draw(screen)
    defense_board.update_board(game['player2']['knowledge'], is_attacking)
    defense_board.draw(screen)



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

    if menu.menuOn():
        menu.draw(screen)
    else:
        game = Api.getGame(game_id)
        is_attacking = game['move'] == player1
        attack_board = AttackBoard()
        defense_board = DefenseBoard()
        update_boards(screen, attack_board, defense_board, game, player1)
        pygame.display.flip()

    running = True
    counter = 100

    while running:
        if menu.menuOn():
            pass
        else:
            if is_attacking:
                if attack_board.mouse_hover(pygame.mouse.get_pos()) is None:
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                else:
                    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)

            if not is_attacking:
                counter = counter - 1
                if counter == 0:
                    counter = 100
                    game = Api.getGame(game_id)
                    is_attacking = game['move'] == player1
                    update_boards(screen, attack_board, defense_board, game, player1)
                    pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if is_attacking:
                        attack_board.make_move(pygame.mouse.get_pos(), game_id)
                        game = Api.getGame(game_id)
                        is_attacking = game['move'] == player1
                        update_boards(screen, attack_board, defense_board, game, player1)
                        pygame.display.flip()
                    
                
            
                    
if __name__ == "__main__":
    main()