import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

class Thing:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)  # Corrected spelling
        self.root = pygame.display.get_surface()
        self.image = pygame.image.load("Tkinter/blueberries.png")  # Load the image correctly

    def render(self):
        self.root.blit(self.image, (self.position.x, self.position.y))  # Use self.position correctly

object1 = Thing(50, 50)  # Create the object once, outside the loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))  # Fill with black color
    object1.render()  # Correctly call render function
    pygame.display.update()
    clock.tick(60)
