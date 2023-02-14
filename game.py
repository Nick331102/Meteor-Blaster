import pygame

pygame.init()
# create display surface
screen = pygame.display.set_mode((1800, 720), pygame.RESIZABLE)
# create clock object
clock = pygame.time.Clock()

# create the surface and fill it with a solid color
surface = pygame.Surface((1800, 720))
surface.fill((40, 10, 10))

# load the ship image
ship = pygame.image.load("spaceship.png")

# create window title
pygame.display.set_caption("Meteor Dodger")

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(surface, (0,0))
    pygame.display.update()
    
    # control the framerate
    clock.tick(120)



