import pygame
import sys
from button import Button
from timer import TimerButton

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
#text = FONT.render(f"Time: {NUMBER}", True, "white")
#text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))

# Uses an attribufte to execute our userevent every second
pygame.time.set_timer(TIMER_EVENT, 1000)

start_button = Button(WIDTH/2 - 300, HEIGHT/2 + 100, 250, 60, "Start", FONT)
stop_button = Button(WIDTH/2, HEIGHT/2 + 100, 250, 60, "Stop", FONT)

main_timer = TimerButton(10, FONT, 200, 75)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # If our user event executes, -1 off of the number
        elif event.type == TIMER_EVENT:
            main_timer.countdown()
    
    SCREEN.fill("red")
    #SCREEN.blit(text, text_rect)

    # Update the text object
    #text = FONT.render(f"Time: {NUMBER}", True, "white")

    start_button.draw(SCREEN)
    stop_button.draw(SCREEN)

    main_timer.update(SCREEN)

    pygame.display.update()

    CLOCK.tick(60)

