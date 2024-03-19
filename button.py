import pygame

class Button():
    def __init__(self, x_pos, y_pos, width, height, button_title, font):
        # Creates variables when the object is created
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.font = font

        # Create a surface
        self.surface = pygame.Surface((width, height))
        # Change the colour of the surface
        self.surface.fill((255, 255, 255))
        # Give surface a rectangle
        self.surface_rect = pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, x_pos, y_pos), 1)

        # Render text onto a surface with a specific font
        text_surface = self.font.render(button_title, True, (0, 0, 0))
        # Give the text surface a rect to display the text
        text_rect = text_surface.get_rect(center=(width/2, height/2))
        # Adding text to button surface
        self.surface.blit(text_surface, text_rect)


    def draw(self, screen):
        screen.blit(self.surface, (self.x_pos, self.y_pos))






