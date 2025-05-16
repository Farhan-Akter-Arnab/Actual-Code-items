import pygame
pygame.init()
screen = pygame.display.set_mode((824, 624))
done = False

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
  pygame.display.flip