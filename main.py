# Import modules
import pygame
import os
import sys
import time

# Pygame configuration
width = 700
height = 550
window = pygame.display.set_mode((width, height))

pygame.init()

clock = pygame.time.Clock()

# Images
snake_size = (16, 16)
snake_pos = [100, 100]
snake = pygame.Surface(snake_size)
snake.fill((0, 0, 0))
snake_rect = pygame.Rect(snake_pos, snake_size)
snake_speed = 5

direction = None
# Game loop
while True:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      #if direction != 'down':
        if event.key == pygame.K_UP:
          direction = 'up'
      #if direction != 'left':
        if event.key == pygame.K_RIGHT:
          direction = 'right'
      #if direction != 'up':
        if event.key == pygame.K_DOWN:
          direction = 'down'
      #if direction != 'right':
        if event.key == pygame.K_LEFT:
          direction = 'left'
  # Input logic    
  if direction == 'up':
    snake_pos[1] -= snake_speed
  if direction == 'right':
    snake_pos[0] += snake_speed
  if direction == 'down':
    snake_pos[1] += snake_speed
  if direction == 'left':
    snake_pos[0] -= snake_speed

  # Show graphics
  window.fill((255, 255, 255))
  window.blit(snake, snake_pos)
  pygame.display.update()