# Import modules
import pygame
import os
import sys
import time

# Import classes
from snake_class import Snake

# Pygame configuration
pygame.init()

width = 700
height = 550
window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

# Snake
snake = Snake((16, 16), [124, 124])


# Game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
        #if snake.direction != 'down':
        if event.key == pygame.K_UP:
          snake.direction = 'up'
        #if snake.direction != 'left':
        if event.key == pygame.K_RIGHT:
          snake.direction = 'right'
        #if snake.direction != 'up':
        if event.key == pygame.K_DOWN:
          snake.direction = 'down'
        #if snake.direction != 'right':
        if event.key == pygame.K_LEFT:
          snake.direction = 'left'

  snake.move()
  snake.show()
  clock.tick(60)

  # Show graphics
  window.fill((255, 255, 255))
  window.blit(snake.surface, snake.pos)
  pygame.display.update()