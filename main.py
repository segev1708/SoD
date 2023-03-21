# this file is used for one line import
from imports import *
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("SoL")
screen = pygame.display.set_mode([1000,1000])
clock = pygame.time.Clock()
megalovania = pygame.mixer.Sound("assets\other\Megalovania.mp3")

seconds = 0
megalovania.play(loops=-1)
inArea = True
megalovania.set_volume(.08)
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
    # get func
    def getImage(self):
        return self._face
    def getPos(self):
        return self._xy
player = Entity(5,[500-(45/2),675-(45/2)],r'assets\images\heart.png',[45,45])
while True:
    screen.fill([0,0,0])
    keys = pygame.key.get_pressed()
    playerXY =player.getPos()
    playerX =playerXY[0]
    playerY =playerXY[1]
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
    if playerX > 350:    
        if keys[K_a] or keys[K_LEFT]:
            pygame.key.set_repeat(30)            
            player.move([-1,0])
    if playerX < 605:
        if keys[K_d] or keys[K_RIGHT]:
            pygame.key.set_repeat(30)
            player.move([1,0])    
    if playerY > 500:
        if keys[K_w] or keys[K_UP]:
            pygame.key.set_repeat(30)            
            player.move([0,-1])
    if playerY < 751:
        if keys[K_s] or keys[K_DOWN]:
            pygame.key.set_repeat(30)
            player.move([0,1])

    # time 
    timeNow = pygame.time.get_ticks()
    timeNow = timeNow//1000
    player.blit()
    pygame.draw.rect(screen,[255,255,255],[350,500,300,300],7)
    clock.tick(60)
    pygame.display.update()