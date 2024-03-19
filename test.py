import pygame

# Creating button class
class Button:
    def __init__(self, x, y, width, height, label, font):
        # Defining variables
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.font = font
        
        # This creates a surface of width by height dimensions
        self.surface = pygame.Surface((width, height))
        # This then turns the colour of that surface to RGB(255, 255, 255)
        self.surface.fill((255, 255, 255)) 
        # This then gives the self.surface a rectangle to record data, such as dimensions
        # The rectangle colour will be black and the it will be positioned 0, 0 by width and height
        # with a border radius of 2
        pygame.draw.rect(self.surface, (255, 0, 0), (0, 0, width, height), 2)
        
        # This then adds the variable "label" to a surface, making the font black
        text_surface = self.font.render(label, True, (0, 0, 0))
        # This gives a rectangle to the text_surface, enabling the positioning of it on the screen.
        text_rect = text_surface.get_rect(center=(width // 2, height // 2))
        # This attaches the text_surface surface to the text_rect rectangle
        self.surface.blit(text_surface, text_rect)

    def draw(self, screen):
        # Draw the button onto the screen at the specified position
        screen.blit(self.surface, (self.x, self.y))

# Pygame initialization
pygame.init()
# Set the first surface, with dimensions 400 x 200
screen = pygame.display.set_mode((400, 200))
# Set the title of the screen
pygame.display.set_caption("Button Example")
# Initiliase a clock object
clock = pygame.time.Clock()

# Font initialization
font = pygame.font.SysFont(None, 36)

# Create a white button with the word "Start"
start_button = Button(150, 75, 100, 50, "Start", font)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill with white color
    
    # Draw the button
    start_button.draw(screen)

    # Update the display
    pygame.display.flip()
    # What does this do?
    clock.tick(60)

pygame.quit()
