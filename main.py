import pygame
import sys

# Defining starting number for timer
NUMBER = 3
# Creating first user event
TIMER_EVENT = pygame.USEREVENT

pygame.init()
        
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Tutorial")

CLOCK = pygame.time.Clock()

ICON = pygame.image.load("Assets/pixel_tomato.jpg")
pygame.display.set_icon(ICON)

FONT = pygame.font.SysFont("segouilack", 64)
text = FONT.render(f"Time: {NUMBER}", True, "white")
text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))

# Useses an attribute to execute our userevent every second
pygame.time.set_timer(TIMER_EVENT, 1000)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # If our user event executes, -1 off of the number
        elif event.type == TIMER_EVENT:
            if NUMBER > 0:
                NUMBER -= 1
    
    SCREEN.fill("red")
    SCREEN.blit(text, text_rect)

    # Update the text object
    text = FONT.render(f"Time: {NUMBER}", True, "white")
    pygame.display.update()

    CLOCK.tick(60)

