import pygame

from player import Player
from arena import Arena

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello Pygame")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

dialogue_box = pygame.Rect(0, 400, 800, 200)

arena_instance = Arena(5, 5)
player_instance = Player(speed=5, strength=10, charisma=8)

dialogue_lines = [
    "The cave is silent.",
    "A torch flickers in the dark.",
    "You take a cautious step."
]
dialogue_index = 0
dialogue_text = dialogue_lines[0]

can_move = True
dialogue_delay = 500
dialogue_timer = 0

# Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = pygame.time.get_ticks()

    if not can_move and now >= dialogue_timer:
        can_move = True

    moved = False

    if can_move:
        keys = pygame.key.get_pressed()
        moved = player_instance.move(keys)

    if moved:
        can_move = False
        dialogue_index = (dialogue_index + 1) % len(dialogue_lines)
        dialogue_text = dialogue_lines[dialogue_index]
        dialogue_timer = now + dialogue_delay

    screen.fill((100, 150, 100))
    pygame.draw.rect(screen, (0, 100, 0), dialogue_box)

    arena_instance.generate_map(screen)
    player_instance.draw(screen)

    text_surface = font.render(dialogue_text, True, (255, 255, 255))
    screen.blit(text_surface, (20, 430))

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()