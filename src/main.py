import pygame
import arena

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))  # Fill the screen with black color
pygame.display.set_caption("Hello Pygame")

# Game loop
running = True

arena_instance = arena.Arena(5, 5)
arena_instance.generate_map()
pygame.display.flip()  # Update the display to show the generated map

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()