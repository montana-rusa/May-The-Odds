import pygame


class Arena:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cannon_grid = [[0 for _ in range(width)] for _ in range(height)]

    def generate_map(self):

        from main import screen
        ROWS, COLS = 5, 5
        CELL_SIZE = 28
        MARGIN = 4

        for row in range(ROWS):
            for col in range(COLS):
                x = 4 + col * (CELL_SIZE + MARGIN)
                y = 4 + row * (CELL_SIZE + MARGIN)
                pygame.draw.rect(screen, (255, 255, 255), (x, y, CELL_SIZE, CELL_SIZE))


