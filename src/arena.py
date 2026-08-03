import pygame


class Arena:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cannon_grid = [[0 for _ in range(width)] for _ in range(height)]
        self.tribute_grid = [[0 for _ in range(width)] for _ in range(height)]

    def generate_map(self):

        from main import screen
        ROWS, COLS = 5, 5
        CELL_SIZE = 28
        MARGIN = 4

        # Some example values for testing purposes
        self.cannon_grid[0][0] = 3
        self.cannon_grid[0][1] = 2
        self.cannon_grid[0][2] = 1

        for row in range(ROWS):
            for col in range(COLS):
                x = 600 + col * (CELL_SIZE + MARGIN)
                y = 44 + row * (CELL_SIZE + MARGIN)
                age = 255 - ((3 - self.cannon_grid[row][col]) * 85)
                pygame.draw.rect(screen, (age, 100, age), (x, y, CELL_SIZE, CELL_SIZE))


