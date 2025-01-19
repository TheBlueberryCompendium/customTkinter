import pygame

screen = pygame.display.set_mode((1200, 600))

background = pygame.image.load("blueberries.png")
image = pygame.image.load("Pororo and Friends.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.fill("red")
    screen.blit(background, (0, 0))
    pygame.display.flip()
