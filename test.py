import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pattern Lines")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the pattern line parameters
line_color = WHITE
line_width = 2
line_spacing = 500
padding = 8

# Clear the screen
screen.fill(BLACK)

# Draw the vertical pattern lines
for y in range(0, height, line_spacing):
    pygame.draw.line(screen, line_color, (padding, y), (width - padding, y), line_width)

# Draw the horizontal pattern lines
for x in range(0, width, line_spacing):
    pygame.draw.line(screen, line_color, (x, padding), (x, height - padding), line_width)

# Update the display
pygame.display.flip()

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit the program
pygame.quit()
