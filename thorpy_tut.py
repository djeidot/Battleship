import pygame, thorpy

pygame.init()
pygame.key.set_repeat(300,30)
screen = pygame.display.set_mode((400,400))
screen.fill((255,255,255))
rect = pygame.Rect((0,0,50,50))
rect.center = screen.get_rect().center
clock = pygame.time.Clock()

pygame.draw.rect(screen, (255,0,0), rect)
pygame.display.flip()

slider = thorpy.SliderX(100, (12,35), "My Slider")
button = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
box = thorpy.Box(elements=[slider, button])

menu = thorpy.Menu(box)

for element in menu.get_population():
    element.surface = screen
    
box.set_topleft((100,100))
box.blit()
box.update()

playing_game = True
while playing_game:
    clock.tick(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing_game = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.draw.rect(screen, (255,255,255), rect)
                pygame.display.update(rect)
                rect.move_ip((-5,0))
                pygame.draw.rect(screen, (255,0,0), rect)
                pygame.display.update(rect)
        menu.react(event)

pygame.quit()