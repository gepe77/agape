import pygame
import sys

pygame.init

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("biru")

warna = (000,000,255)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    screen.fill(warna)
    pygame.display.flip()


pygame.quit()
sys.exit()
        

