# this file is used for one line import
from imports import *
import ctypes
wave1 = False
myappid = r'assets\images\heart.png' # arbitrary string
entities = []
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Undertale: Shades of Darkness")

screen = pygame.display.set_mode([1000,1000])
clock = pygame.time.Clock()
torielTheme = pygame.mixer.Sound(r"assets\other\UndertaleTorielTheme.mp3")
determination = pygame.mixer.Sound(r"assets\other\Undertale OST_ 011 - Determination.mp3")

seconds = 0
torielTheme.play(loops=-1)
inArea = True
torielTheme.set_volume(.06)
def end():
    torielTheme.stop()
    determination.set_volume(0.01)
    determination.play(loops=-1)
class Entity:
    def __init__(self,speed : int, xy : list, face : str,size : int,type : str):
        self._speed = speed
        self._face = pygame.image.load(face).convert_alpha()
        self._face = pygame.transform.scale(self._face,size)
        self._xy = xy
        self._type = type
    # set func
    def setPos(self,newXY : list):
         self._xy = newXY
    def move(self,byXY : list):
        self._xy = [self._xy[0]+ (byXY[0] * self._speed), self._xy[1] + (byXY[1] * self._speed)]
    def blit(self):
        screen.blit(self._face,self._xy)
    def setType(self,newType : str): # probably useless
        self._type = newType
    # get func
    def getImage(self):
        return self._face
    def getPos(self):
        return self._xy
    def getType(self):
        return self._type
Player = Entity(5,[500-(45/2),675-(45/2)],r'assets\images\heart.png',[45,45],"player")
entities.append(Player)
Gengar = Entity(5,[500-(220/2),350-(220/2)],r'assets\images\gengar_fixed.png',[220,220],"enemyStatue")
pygame.display.set_icon(Player.getImage())
entities.append(Gengar)
while True:
    playerXY =Player.getPos()
    playerX =playerXY[0]
    playerY =playerXY[1]
    playerHitbox = [playerX+5,playerY+5,35,35]
    playerRect = pygame.draw.rect(screen,[200,200,200],playerHitbox,1)
    screen.fill([0,0,0])

    keys = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
    if playerX > 350:    
        if keys[K_a] or keys[K_LEFT]:
            pygame.key.set_repeat(30)            
            Player.move([-1,0])
    if playerX < 605:
        if keys[K_d] or keys[K_RIGHT]:
            pygame.key.set_repeat(30)
            Player.move([1,0])    
    if playerY > 500:
        if keys[K_w] or keys[K_UP]:
            pygame.key.set_repeat(30)            
            Player.move([0,-1])
    if playerY < 751:
        if keys[K_s] or keys[K_DOWN]:
            pygame.key.set_repeat(30)
            Player.move([0,1])
    # time 
    timeNow = pygame.time.get_ticks()
    timeNow = timeNow//1000
    for entity in entities:
        entity.blit()
    # game system:
    if timeNow >= 2:
        if wave1 == False:
            wave1 = True
            rect2 = Entity(3.5,[425-(75/3),-100-(75/2)],r"assets\images\rect.png",[50,50],"wave1")
            rect3 = Entity(3.5,[500-(75/3),-100-(75/2)],r"assets\images\rect.png",[50,50],"wave1")
            rect4 = Entity(3.5,[575-(75/3),-100-(75/2)],r"assets\images\rect.png",[50,50],"wave1")
            rect5 = Entity(3.5,[650-(75/3),-100-(75/2)],r"assets\images\rect.png",[50,50],"wave1")
            rect1 = Entity(3.5,[350-(75/3),-100-(75/2)],r"assets\images\rect.png",[50,50],"wave1")            
            entities.append(rect1)
            entities.append(rect2)
            entities.append(rect3)
            entities.append(rect4)
            entities.append(rect5)
            x = 0

        rect1Hitbox = rect1.getPos() + [15,40]
        rect1Hitbox[0]+=18
        rect1Hitbox[1]+=4

        
        rect2Hitbox = rect2.getPos() + [15,40]
        rect2Hitbox[0]+=18
        rect2Hitbox[1]+=4


        rect3Hitbox = rect3.getPos() + [15,40]
        rect3Hitbox[0]+=18
        rect3Hitbox[1]+=4


        rect4Hitbox = rect4.getPos() + [15,40]
        rect4Hitbox[0]+=18
        rect4Hitbox[1]+=4


        rect5Hitbox = rect5.getPos() + [15,40]
        rect5Hitbox[0]+=18
        rect5Hitbox[1]+=4


        rect1Hitbox = pygame.draw.rect(screen,[255,255,255],rect1Hitbox,10)
        rect2Hitbox = pygame.draw.rect(screen,[255,255,255],rect2Hitbox,10)
        rect3Hitbox = pygame.draw.rect(screen,[255,255,255],rect3Hitbox,10)
        rect4Hitbox = pygame.draw.rect(screen,[255,255,255],rect4Hitbox,10)
        rect5Hitbox = pygame.draw.rect(screen,[255,255,255],rect5Hitbox,10)
        wave1Hitboxes = [rect1Hitbox,rect2Hitbox,rect3Hitbox,rect4Hitbox,rect5Hitbox]
        for wave1Hitboxe in wave1Hitboxes:
            if wave1Hitboxe.colliderect(playerRect):
                end()
        for entity in entities:
            if entity.getType() == "wave1":
                entity.move([0,2])
                x+=0.015
                y = cos(x)
                pos = entity.getPos()
                entity.move([y,0])
    pygame.draw.rect(screen,[255,255,255],[350,500,300,300],7)
    clock.tick(60)
    pygame.display.update()