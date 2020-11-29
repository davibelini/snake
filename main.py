# Import modules
import pygame
import os
import sys
import time

# Import classes
import Snake as snake_class

# Pygame configuration
pygame.init()

width = 700
height = 550
window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

# Snake
snake = snake_class.Snake((16, 16), [124, 124])
snake.show()

# Game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    snake.move()
  print(snake.direction)
  clock.tick(60)

  # Show graphics
  window.fill((255, 255, 255))
  window.blit(snake.surface, snake.pos)
  pygame.display.update()