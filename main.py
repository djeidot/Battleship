import pygame

from pygame.rect import Rect

from attackboard import AttackBoard
from vars import *


def main():
    pygame.init()
    pygame.display.set_caption("Battleship")


    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill(background_color)

    attack_board = AttackBoard()
    attack_board.draw()
    
    top_outer_rect = Rect(screen_middle_h - 150, 30, 300, 300)
    top_inner_rect = top_outer_rect.inflate(-10, -10)

    pygame.draw.rect(screen, border_color, top_outer_rect)
    pygame.draw.rect(screen, water_color, top_inner_rect)
    
    pygame.draw.polygon(screen, border_color, [
        (screen_middle_h - 150, 350),
        (screen_middle_h + 150, 350),
        (screen_width - 50, screen_height - 30),
        (50, screen_height - 30)
    ])
    
    pygame.display.flip()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
if __name__ == "__main__":
    main()