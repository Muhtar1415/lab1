import pygame
from pygame import mixer
import os

playlist=[]
allmusic=os.listdir(r"C:\Users\user\Desktop\lab\lab7\music")
for song in allmusic:
    if song.endswith(".mp3"):
           playlist.append(f"music\\{song}")

pygame.init()
mixer.init()
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()
fps = 24
bg=pygame.Surface((500,500))
pygame.Surface.fill(bg,(241,203,255))
font1=pygame.font.SysFont('calibri', 30, True)
font2=pygame.font.SysFont('calibri', 20)
background=pygame.image.load("images/backgroundpic.png")
play=pygame.image.load("images/buttonplay.png")
pause=pygame.image.load("images/buttonpause.png")
kelesi=pygame.image.load("images/buttonnext.png")
artka=pygame.image.load("images/buttonprevious.png")

aplay = False
apaus = True
anext = 1
acurr = 0
aprev = len(playlist)-1
mixer.music.load(playlist[acurr])
mixer.music.play()
mixer.music.pause()
run =  True


run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_SPACE:
                        if apaus:
                              aplay = True
                              apaus = False
                              mixer.music.unpause()
                        else:
                              aplay = False
                              apaus = True
                              mixer.music.pause()
                  if event.key == pygame.K_RIGHT:
                        mixer.music.load(playlist[anext])
                        mixer.music.play()
                        acurr+=1
                        anext+=1
                        aprev+=1
                        if acurr==len(playlist):
                              acurr=0
                              anext=1
                              aprev=len(playlist)-1
                        if acurr==1:
                              aprev=0
                        if acurr==len(playlist)-1:
                              anext=0
                  if event.key == pygame.K_LEFT:
                        mixer.music.load(playlist[aprev])
                        mixer.music.play()
                        acurr-=1
                        anext-=1
                        aprev-=1
                        if acurr==0:
                              acurr=0
                              aprev=len(playlist)-1
                              anext=1    
            
    text1=font1.render("Currently playing:", True, (138,25,151))
    text2=font2.render(playlist[acurr], True, (99,20,108)) 
        
    screen.blit(background,(0,0))
    screen.blit(play,(200,500))
    screen.blit(pause,(300,500))
    screen.blit(kelesi,(400,500))
    screen.blit(artka,(500,500))
    screen.blit(bg,(150,150))
    screen.blit(text1,(175,175))
    screen.blit(text2,(250,250)) 
    
    clock.tick(fps)
    pygame.display.update()
        