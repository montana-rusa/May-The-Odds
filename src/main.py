import pygame

from player import Player
from arena import Arena

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello Pygame")

screen.fill((100, 150, 100))  # Fill the screen with green color

running = True
clock = pygame.time.Clock()
dialogue_box = pygame.Rect(0, 400, 800, 200)

arena_instance = Arena(5, 5)
player_instance = Playerplayer_instance = Player(speed=5, strength=10, charisma=8)
pygame.draw.rect(screen, (0, 100, 0), dialogue_box)

# Game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    player_instance.move(keys)

    screen.fill((100, 150, 100))
    pygame.draw.rect(screen, (0, 100, 0), dialogue_box)

    arena_instance.generate_map(screen)
    player_instance.draw(screen)

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()