import pygame
import sys

# Initialise pygame
pygame.init()

# Constant variables for screen dimensions
WIDTH, HEIGHT = 800, 800
# Creating the window and setting dimensions
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# Setting the title of the window
pygame.display.set_caption("Pygame Tutorial")

# Initialise the clock object
CLOCK = pygame.time.Clock()


# Loading an image against a variable
ICON = pygame.image.load("Assets/pixel_tomato.jpg")
# Using that image as the window icon
pygame.display.set_icon(ICON)

# Chosing which font to use and saving to variable
FONT = pygame.font.SysFont("segouilack", 64)
# Making a text object (Text, anti-aliasing, font-colour)
text = FONT.render("Hello World!", True, "white")
# This is now giving our text variable postiion information using a rectangle
text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))


# This is the game loop
while True:
    # Runs through all events, mouse clicks or keyboard inputs etc
    for event in pygame.event.get():
        # If an event is pygame.QUIT, the x on the window
        if event.type == pygame.QUIT:
            # Exit pygame and system with no errors
            pygame.quit()
            sys.exit()
    
    # Change the colour of the screen to red
    SCREEN.fill("red")
    # This is using the blit method to attach an object to a surface, in this case our text object to our text_rect
    SCREEN.blit(text, text_rect)
    # Update the display to reflect the colour change
    pygame.display.update()

    #Set fps to 60
    CLOCK.tick(60)

