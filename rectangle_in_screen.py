import pygame
pygame.init()
screen = pygame.display.set_mode((424, 324))
done = False
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(124, 124, 88, 88))
  pygame.display.flip()