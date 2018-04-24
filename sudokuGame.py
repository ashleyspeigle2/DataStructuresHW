import pygame

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

size = (800,800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Sudoku")

done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
