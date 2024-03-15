import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
pygame.display.set_caption("CLOCK")

fps = 24
background = pygame.image.load("images\clock.png")

clock = pygame.time.Clock()

firkol = pygame.image.load("images\minhand3.png")
ekikol = pygame.image.load("images\sechand4.png")

minrect = firkol.get_rect()
minrect.center = (255,250)

secrect =ekikol.get_rect()
secrect.center = (260,250)

currenttime = datetime.datetime.now()
secvalue = currenttime.second
minvalue = currenttime.minute

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    genfirkol = pygame.transform.rotate(firkol, -1*((6*minvalue)%360))
    ledfirrect = genfirkol.get_rect()
    ledfirrect.center = minrect.center

    screen.blit(genfirkol,ledfirrect)

    genekikol = pygame.transform.rotate(ekikol, -1*((6*secvalue+180)%360))
    gensecrect = genekikol.get_rect()
    gensecrect.center = secrect.center

    screen.blit(genekikol, gensecrect)

    currenttime = datetime.datetime.now()
    secvalue = currenttime.second
    minvalue = currenttime.minute

    pygame.display.update()
    clock.tick(fps)

