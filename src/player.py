import pygame

class Player:
    def __init__(self, speed, strength, charisma,  cell_size=28, margin=4, offset_x=600, offset_y=44):
        self.speed = speed
        self.strength = strength
        self.charisma = charisma
        self.position = (2, 2)  # Position is a tuple (x, y)
        self.health = 100  # Player's health
        self.food = 0
        self.rest = 10

        self.cell_size = cell_size
        self.margin = margin
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.next_move_time = 0  # Initialize next move time

    def draw(self, screen):
        square_x = 600 + self.position[0] * (self.cell_size + self.margin)
        square_y = self.offset_y + self.position[1] * (self.cell_size + self.margin)

        center_x = square_x + self.cell_size // 2
        center_y = square_y + self.cell_size // 2

        pygame.draw.circle(screen, (255, 0, 0), (center_x, center_y), 10)

    def move(self, keys):
        now = pygame.time.get_ticks()

        if now < self.next_move_time:
            return

        old_position = self.position

        if keys[pygame.K_UP] and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif keys[pygame.K_DOWN] and self.position[1] < 4:
            self.position = (self.position[0], self.position[1] + 1)
        elif keys[pygame.K_LEFT] and self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])
        elif keys[pygame.K_RIGHT] and self.position[0] < 4:
            self.position = (self.position[0] + 1, self.position[1])

        if self.position != old_position:
            self.next_move_time = now + 250
  