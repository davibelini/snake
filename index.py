import pygame, sys

# Setup pygame
pygame.init()

window_size = (900, 600)
window = pygame.display.set_mode(window_size)

# Entities
snake = [(0, 0), (16, 0), (32, 0)]
snake_size = (16, 16)
snake_skin = pygame.Surface(snake_size)
snake_skin.fill((0, 0, 0))

# Game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      break

  # Draw
  window.fill((255, 255, 255))
  for pos in snake:
    window.blit(snake_skin, pos)
  pygame.display.update()