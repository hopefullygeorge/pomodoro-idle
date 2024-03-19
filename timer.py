import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 25
PADDING = 10

FONT = pygame.font.SysFont(None, FONT_SIZE)

pygame.init()

ScreenInfo = pygame.display.Info()
SCREEN = pygame.display.set_mode((ScreenInfo.current_w, ScreenInfo.current_h))
pygame.display.set_caption("Timer Dev")

clock = pygame.time.Clock()

# Define text
display_text = "Hello George"
# Render text onto surface
text_surface = FONT.render(display_text, True, BLACK)
# Get size of text surface
text_w, text_h = text_surface.get_size()
# Add rectangle to text
text_rect = text_surface.get_rect(0, 0)

# Create textbox_surface
textbox_surface = pygame.Surface((text_w + PADDING, text_h + PADDING))
# Add rectangle for textbox
textbox_rect = textbox_surface.get_rect(0, 0)





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    SCREEN.fill(WHITE)






    pygame.display.flip()


pygame.quit()
sys.exit()
