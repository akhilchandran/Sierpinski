import pygame, sys
from pygame.locals import*

def midp(p1,p2):
  return ((p1[0]+p2[0])/2,(p2[1]+p1[1])/2)

fpsClock = pygame.time.Clock()

display = pygame.display.set_mode((1300,700))
pygame.display.set_caption('Sierpinski triangle')
while True:
  display.fill((0,0,0))
  pygame.draw.polygon(display, (255,255,0),((500,475),(800,475),(650,215)),1)
  a =[[(500,475),(800,475),(650,215)]]
  pygame.display.update()
  fpsClock.tick(1)
  k = 1
  while k < 7:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    d = []
    for t in a:
      b = []
      i = 0
      while i < 3:
        a=midp(t[i-1],t[i])
        c=midp(t[i],t[(i+1)%3])
        pygame.draw.line(display, (255,255,0),a,c,1)
        b += [[a,t[i],c]]
        i+=1
      d += b
    a = d
    pygame.display.update()
    fpsClock.tick(1)
    k +=1
