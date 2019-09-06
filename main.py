import pygame
from pygame.rect import Rect


def main():
    pygame.init()
    pygame.display.set_caption("Battleship")
    
    screen_width = 512
    screen_height = 512
    screen_middle_h = screen_width / 2
    screen_middle_v = screen_height / 2
        
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((240,240,240))
    
    top_outer_rect = Rect(screen_middle_h - 150, 30, 300, 300)
    top_inner_rect = top_outer_rect.inflate(-10, -10)
    pygame.draw.rect(screen, 0, top_outer_rect)
    pygame.draw.rect(screen, (0,0,255), top_inner_rect)
    pygame.draw.polygon(screen, 0, [
        (screen_middle_h - 150, 350),
        (screen_middle_h + 150, 350),
        (screen_width - 30, screen_height - 30),
        (30, screen_height - 30)
    ])
    
    pygame.display.flip()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
if __name__ == "__main__":
    main()