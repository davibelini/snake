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

# Images
snake_size = (16, 16)
snake_pos = (100, 100)
snake = pygame.Surface(snake_size)
snake.fill((0, 0, 0))
snake_rect = pygame.Rect(snake_pos, snake_size)

# Game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  # Show graphics
  window.fill((255, 255, 255))
  window.blit(snake, snake_pos)
  pygame.display.update()