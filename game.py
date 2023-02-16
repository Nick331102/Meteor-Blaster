import pygame
from pygame.sprite import Sprite

# Define a class called ShipSprite that inherits from the Sprite class
class ShipSprite(Sprite):
    
    # Define the constructor method for the class
    def __init__(self, image, x, y):
        
        # Call the constructor of the parent class (Sprite)
        super().__init__()
        
        # Store the image of the spaceship in the image attribute
        self.image = image
        
        # Create a rectangle that is the same size as the image
        self.rect = self.image.get_rect()
        
        # Set the x and y position of the rectangle
        self.rect.x = x
        self.rect.y = y

        
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

# calculate the center of the screen
center_x = screen.get_width()
center_y = screen.get_height()

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    #update the ships velocity and acceleration based on user input.  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.accleration.y = -0.1
            if event.key == pygame.K_DOWN:
                ship.accleration.y = 0.1
            if event.key == pygame.K_LEFT:
                ship.accleration.x = -0.1
            if event.key == pygame.K_RIGHT:
                ship.accleration.x = 0.1
    # ship stops moving when up, down, left, or right key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ship.acceleration.y = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ship.acceleration.x = 0     
                
    screen.blit(surface, (0,0))
    # display the ship at the center of the screen
    screen.blit(ship, (900, 360))
    pygame.display.update()
    
    # control the framerate
    clock.tick(120)



