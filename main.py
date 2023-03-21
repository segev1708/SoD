# this file is used for one line import
from imports import *
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("SoL")
screen = pygame.display.set_mode([1000,1000])
clock = pygame.time.Clock()

seconds = 0
class Entity:
    def __init__(self,speed : int, xy : list, face : str,size : int):
        self._speed = speed
        self._face = pygame.image.load(face).convert_alpha()
        self._face = pygame.transform.scale(self._face,size)
        self._xy = xy
    # set func
    def setPos(self,newXY : list):
         self._xy = newXY
    def move(self,byXY : list):
        self._xy = [self._xy[0]+ (byXY[0] * self._speed), self._xy[1] + (byXY[1] * self._speed)]
    def blit(self):
        screen.blit(self._face,self._xy)

    def getImage(self):
        return self._face
        
player = Entity(5,[500-(45/2),675-(45/2)],r'assets\images\heart.png',[45,45])
while True:
    screen.fill([0,0,0])
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
    if keys[K_a] or keys[K_LEFT]:
        pygame.key.set_repeat(30)            
        player.move([-1,0])
    if keys[K_w] or keys[K_UP]:
        pygame.key.set_repeat(30)            
        player.move([0,-1])
    if keys[K_s] or keys[K_DOWN]:
        pygame.key.set_repeat(30)
        player.move([0,1])
    if keys[K_d] or keys[K_RIGHT]:
        pygame.key.set_repeat(30)
        player.move([1,0])
    # time 
    timeNow = pygame.time.get_ticks()
    timeNow = timeNow//1000
    player.blit()
    pygame.draw.rect(screen,[255,255,255],[350,500,300,300],7)
    clock.tick(60)
    pygame.display.update()