import pygame

pygame.init()
# Create the display surface object of specific dimension.
Window = pygame.display.set_mode((424, 424))
# Fill the screen with black color
Window.fill((0,0,0))
White = (255,255,255)
Orange = (254, 153, 0)
# Draw solid circle
pygame.draw.circle(Window, White, (324, 324), 48)
# Draw outlined circle
pygame.draw.circle(Window, Orange, (128, 124), 48, 3)
# Draws the surface object to the screen
pygame.display.update()
# Game loop
running = True
while running:
  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
# Quit pygame
pygame.quit()