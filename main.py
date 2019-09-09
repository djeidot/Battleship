import pygame

from attackboard import AttackBoard
from defenseboard import DefenseBoard
from vars import *


def main():
    pygame.init()
    pygame.display.set_caption("Battleship")


    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(background_color)

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
if __name__ == "__main__":
    main()