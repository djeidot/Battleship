import pygame

from api import Api
from attackboard import AttackBoard
from defenseboard import DefenseBoard
from menu import Menu
from vars import *


def main():
    # Initiate api
    r = Api.startGame("joao1", "joao2")
    api_id = r["id"]
    
    pygame.init()
    pygame.display.set_caption("Battleship")

    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(background_color)

    menu = Menu()

    if menu.menuOn():
        menu.draw(screen)
    else:
        attack_board = AttackBoard()
        attack_board.draw(screen)
        
        pygame.draw.polygon(screen, border_color, [
            (screen_middle_h - 150, 330),
            (screen_middle_h + 150, 330),
            (screen_middle_h + 200, 330+150),
            (screen_middle_h - 200, 330+150)
        ])
    
        defense_board = DefenseBoard()
        defense_board.draw(screen)
    
    pygame.display.flip()
    
    running = True
    
    while running:
        if menu.menuOn():
            pass
        else:
            if attack_board.mouse_hover(pygame.mouse.get_pos()) is None:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                attack_board.make_move(pygame.mouse.get_pos(), api_id)
                attack_board.draw(screen)
                pygame.display.flip()
                
if __name__ == "__main__":
    main()