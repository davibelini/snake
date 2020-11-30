import pygame

class Snake():
  def __init__(self, size, pos):
    self.surface = pygame.Surface((16, 16))
    self.size = size
    self.pos = pos
    self.rect = pygame.Rect(self.pos, self.size)
    self.speed = 5
    self.color = (0, 0, 0)
    self.direction = None
    self.cell_number = 2
  def show(self):
    self.surface.fill(self.color)
  def move(self):
    if self.cell_number == 1:
      if self.direction == 'up':
        self.pos[1] -= self.speed
      if self.direction == 'right':
        self.pos[0] += self.speed
      if self.direction == 'down':
        self.pos[1] += self.speed
      if self.direction == 'left':
        self.pos[0] -= self.speed
    elif self.cell_number > 1:
      if self.direction != 'down':
        if self.direction == 'up':
          self.pos[1] -= self.speed
      if self.direction != 'left':
        if self.direction == 'right':
          self.pos[0] += self.speed
      if self.direction != 'up':
        if self.direction == 'down':
          self.pos[1] += self.speed
      if self.direction != 'right':
        if self.direction == 'left':
          self.pos[0] -= self.speed
  def manipulate_size(self):
    for i in range(self.cell_number):
      self.size[1] *= i