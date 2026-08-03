import pygame
import arena

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
screen.fill((100, 150, 100))  # Fill the screen with green color
pygame.display.set_caption("Hello Pygame")


dialogue_box = pygame.Rect(0, 400, 800, 200)
pygame.draw.rect(screen, (0, 100, 0), dialogue_box)

arena_instance = arena.Arena(5, 5)
arena_instance.generate_map()
pygame.display.flip()  # Update the display to show the generated map

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()