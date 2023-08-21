import pygame
from sys import exit

status = 0

FPS = 120

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# about line pattern
line_color = (255, 255, 254)
line_width = 2
line_spacing = 800
padding = 1

pygame.init()
if not pygame.get_init():
    exit(1)

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("HackerPack")

width, height = screen.get_size()
centerx = width // 2
centery = height // 2

status = 1

def draw():

    status = 2

    if status != 3:
        # draw black bg
        screen.fill(BLACK)

        # Draw the vertical pattern lines
        for y in range(0, height, line_spacing):
            pygame.draw.line(screen, line_color, (padding, y), (width - padding, y), line_width)

        # Draw the horizontal pattern lines
        for x in range(0, width, line_spacing):
            pygame.draw.line(screen, line_color, (x, padding), (x, height - padding), line_width)

        pygame.display.update()


def main():

    status = 2

    # setup pygame clock(tick) for FPS
    clock = pygame.time.Clock()
    
    while status != 3:
        # init FPS clock
        clock.tick(FPS)
        # check pygame.quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = 3
        
        # fill black as bg
        draw()


    pygame.quit()
    exit(1)

if __name__ == "__main__":
    main()
    
