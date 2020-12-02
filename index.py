import pygame, sys

# Setup pygame
pygame.init()
clock = pygame.time.Clock()
window_size = (960, 640)
window = pygame.display.set_mode(window_size)

# Entities
snake = [(0, 16), (16, 16), (32, 16), (64, 16), (128, 16)]
cell_size = (8, 8)
snake_skin = pygame.Surface(cell_size)
snake_spd = 8
snake_skin.fill((0, 0, 0))
direction = None

# Game loop
while True:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      break
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        direction = 0
      if event.key == pygame.K_RIGHT:
        direction = 1
      if event.key == pygame.K_DOWN:
        direction = 2
      if event.key == pygame.K_LEFT:
        direction = 3
  # Direction check
  if direction == 0:
    snake[0] = (snake[0][0], snake[0][1] - snake_spd)
  elif direction == 1:
    snake[0] = (snake[0][0] + snake_spd, snake[0][1])
  elif direction == 2:
    snake[0] = (snake[0][0], snake[0][1] + snake_spd)
  elif direction == 3:
    snake[0] = (snake[0][0] - snake_spd, snake[0][1])
  for i in range(len(snake) - 1, 0, -1):
    snake[i] = (snake[i - 1][0], snake[i - 1][1])
  # Draw
  window.fill((255, 255, 255))
  for pos in snake:
    window.blit(snake_skin, pos)
  pygame.display.update()