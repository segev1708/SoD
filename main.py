# this file is used for one line import
from imports import *
import ctypes
myappid = r'assets\images\heart.png' # arbitrary string
soundOn = input("sound? Y/N")
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
wave1,wave2,wave3,wave4 = False,False,False,False
entities = []
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Undertale: Shades of Darkness")
timeNow = 0
screen = pygame.display.set_mode([1000,1000])
clock = pygame.time.Clock()
torielTheme = pygame.mixer.Sound(r"assets\other\UndertaleTorielTheme.mp3")
determination = pygame.mixer.Sound(r"assets\other\Undertale OST_ 011 - Determination.mp3")
ghostFight = pygame.mixer.Sound(r"assets\other\ghostFight.mp3")
won = False
seconds = 0
ghostFight.play(loops=-1)
inArea = True
ended = False
oldTime = 0
playSize = [350,500,300,300]
def end(ended):
    if ended == False:
        ghostFight.stop()
        determination.stop()
        determination.play(loops=-1)
    print(ended)
    return False

class Text():
    def __init__(self,text,size,location,font,fontColor):
        self._text = text
        self._size = size
        self._location = location
        self._font = font
        self._fontColor = fontColor
    def get_text(self):
        return self._text
    def get_size(self):
        return self._size
    def get_location(self):
        return self._location
    def get_font(self):
        return self._font
    def get_fontColor(self):
        return self._fontColor

    def blit(self):
        Font = pygame.font.Font(self._font, self._size) 
        Text = Font.render(self._text, True,self._fontColor)
        screen.blit(Text,self._location)

class Button():
    def __init__(self,data=list,image=str,click=bool,colorKey=list[int,int,int]):
        self._data = data
        self._location = [data[0],data[1]]
        self._size = [data[2],data[3]]
        self._click = click
        self._colorKey = colorKey
        try:
            self._image =  image
            self._image = pygame.image.load(self._image)
            isImage = True
        except:
            isImage = False
        self._area = [data[0],data[1],data[0]+data[2],data[1]+data[3]]
    def get_click(self):
        return self._click
    def get_location_and_size(self):
        return self._data
    def get_image(self):
        return self._image
    def get_area(self):
        return self._area
    def setcolor_key(self):
        self._image.set_colorkey(self._colorKey)
    def blit(self):
        screen.blit(self._image,self._location)

    def check_hovered(self):
        if mouseX >= self._area[0] and mouseX <= self._area[2] and mouseY >= self._area[1] and mouseY <= self._area[3]:
            return True
        else:
            return False
    def check_clicked(self):
        if mouseX >= self._area[0] and mouseX <= self._area[2] and mouseY >= self._area[1] and mouseY <= self._area[3]:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                return True
        else:
            return False

class Entity():
    def __init__(self,speed : int, xy : list, face : str,size : int,group : str):
        self._speed = speed
        self._face = pygame.image.load(face).convert_alpha()
        self._face = pygame.transform.scale(self._face,size)
        self._xy = xy
        self._group = group
    # set func
    def setPos(self,newXY : list):
         self._xy = newXY
    def move(self,byXY : list):
        self._xy = [self._xy[0]+ (byXY[0] * self._speed), self._xy[1] + (byXY[1] * self._speed)]
    def blit(self):
        screen.blit(self._face,self._xy)
    def setGroup(self,newType : str): # probably useless
        self._type = newType
    # get func
    def getImage(self):
        return self._face
    def getPos(self):
        return self._xy
    def getGroup(self):
        return self._group
    def getSpeed(self):
        return self._speed

Player = Entity(5,[500-(45/2),675-(45/2)],r'assets\images\heart.png',[45,45],"player")
entities.append(Player)
Gengar = Entity(5,[500-(220/2),350-(220/2)],r'assets\images\gengar_fixed.png',[220,220],"enemyStatue")
pygame.display.set_icon(Player.getImage())
entities.append(Gengar)
soundOn = soundOn.capitalize()

if soundOn in ["YES","Y","1"]:
    ghostFight.set_volume(.06)
    determination.set_volume(0.022) 
else:
    ghostFight.set_volume(0)
    determination.set_volume(0) 


while True:
    try:
        sparkleHitbox = pygame.draw.rect(screen,[0,0,0],[sparklePos[0],sparklePos[1],50,50],5)
    except:
        sparkleHitbox = pygame.draw.rect(screen,[0,0,0],[570,370,50,50],5)
    playerXY =Player.getPos()
    mousePos = pygame.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]
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
    if ended == False:
        if playerX > playSize[0]:    
            if keys[K_a] or keys[K_LEFT]:
                pygame.key.set_repeat(30)            
                Player.move([-1,0])
        
        if playerX < (playSize[0]+playSize[2])-45:
            if keys[K_d] or keys[K_RIGHT]:
                pygame.key.set_repeat(30)
                Player.move([1,0])    
        elif playerX > (playSize[0]+playSize[2])-40:
            Player.setPos([(playSize[0]+playSize[2])-45-1,playerY])
        if playerY > playSize[1]:
            if keys[K_w] or keys[K_UP]:
                pygame.key.set_repeat(30)            
                Player.move([0,-1])
        if playerY < (playSize[1]+playSize[3])-49:
            if keys[K_s] or keys[K_DOWN]:
                pygame.key.set_repeat(30)
                Player.move([0,1])
    # time 
    ticks, timeNow = pygame.time.get_ticks(), pygame.time.get_ticks()
    
    timeNow = timeNow//1000
    if timeNow != oldTime:
        oldTime = timeNow
        print(timeNow)
    for entity in entities:

        entity.blit()
    # game system:
    # wave 1
    if timeNow >= 5:
        if wave1 == False:
            wave1 = True
            rect1 = Entity(3.5,[350-(75/3),-100-(75/2)],r"assets\images\rect.png",[50,50],"wave1")            
            rect2 = Entity(3.5,[425-(75/3),-100-(75/2)],r"assets\images\rect.png",[50,50],"wave1")
            rect3 = Entity(3.5,[500-(75/3),-100-(75/2)],r"assets\images\rect.png",[50,50],"wave1")
            rect4 = Entity(3.5,[575-(75/3),-100-(75/2)],r"assets\images\rect.png",[50,50],"wave1")
            rect5 = Entity(3.5,[650-(75/3),-100-(75/2)],r"assets\images\rect.png",[50,50],"wave1")
            entities.append(rect1)
            entities.append(rect2)
            entities.append(rect3)
            entities.append(rect4)
            entities.append(rect5)
            x = 0
            wave1dir = 1
            wave1start = True

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
        for wave1Hitbox in wave1Hitboxes:
            if wave1Hitbox.colliderect(playerRect):
                ended = end(ended)
        for entity in entities:
            if entity.getGroup() == "wave1":
                entity.move([0,2*wave1dir])
                x+=0.015
                y = cos(x)
                pos = entity.getPos()
                entity.move([y,0])
        if timeNow >=8:
            wave1start = False
            wave1dir = -1.2
    # wave 2
    if timeNow >= 10:
        if wave2 == False:
            wave2 = True
            circle1 = Entity(3.5,[-50-(75/3),100-(75/2)],r"assets\images\circle7x7.png",[30,30],"wave2")
            circle2 = Entity(3.5,[1050-(75/3),100-(75/2)],r"assets\images\circle7x7.png",[30,30],"wave2")
            entities.append(circle1)
            entities.append(circle2)
            deleteColor = [0,0,0]
            deleteColorMultiplier = 1
            deleteFinished = False
            deleteEnd = False
        try:
            circle1.move([2,2])
            circle1x = circle1.getPos()
            circle1y = circle1x[1]+8
            circle1x = circle1x[0]+8
            circle1Hitbox = pygame.draw.circle(screen,[255,255,255],(circle1x,circle1y),15)

            circle2.move([-2,2])
            circle2x = circle2.getPos()
            circle2y = circle2x[1]+8
            circle2x = circle2x[0]+15+8
            circle2Hitbox = pygame.draw.circle(screen,[255,255,255],(circle2x,circle2y),15)
        except:
            pass
        for hitbox in [circle1Hitbox,circle2Hitbox]:
            if hitbox.colliderect(playerRect):
                ended = end(ended)
        
        if timeNow >= 12:

            if deleteFinished == False:
                if deleteColor[0] < 252 and deleteEnd == False:
                    deleteColorMultiplier = deleteColorMultiplier + 0.0022
                    deleteColor = [int(deleteColor[0]*deleteColorMultiplier)+deleteColorMultiplier,0,0]
                if deleteColor[0]>240:
                    if deleteCube.colliderect(playerHitbox):
                        ended = end(ended)
     
            try:
                deleteCube = pygame.draw.rect(screen,deleteColor,[350,700,300,100])
            except: 
                deleteFinished = True
        # wave 3        
        if timeNow >=14 and timeNow < 24:
            if playSize[2] != 500 and timeNow < 17:
                playSize[2] += 5
                if wave3 == False:
                    wave3 = True
                    sparkle = Entity(1.5,[570,370],f'assets\images\purpleSparkle.png',[50,50],"wave3")
                    bullet1 = Entity(12,[-200+randint(-1000,100),600+randint(-25,25)+randint(-100,100)],r'assets\images\BulletLeft.png',(50,50),"wave3")
                    bullet2 = Entity(12,[-200+randint(-1000,100),600+randint(-25,25)+randint(-100,100)],r'assets\images\BulletLeft.png',(50,50),"wave3")
                    bullet3 = Entity(12,[-200+randint(-1000,100),600+randint(-25,25)+randint(-100,100)],r'assets\images\BulletLeft.png',(50,50),"wave3")
                    bullet4 = Entity(12,[-200+randint(-1000,100),600+randint(-25,25)+randint(-100,100)],r'assets\images\BulletLeft.png',(50,50),"wave3")
                    bullet5 = Entity(12,[-200+randint(-1000,100),600+randint(-25,25)+randint(-100,100)],r'assets\images\BulletLeft.png',(50,50),"wave3")
                    bullet6 = Entity(12,[-200+randint(-1000,100),600+randint(-25,25)+randint(-100,100)],r'assets\images\BulletLeft.png',(50,50),"wave3")
                    bullet7 = Entity(12,[-200+randint(-1000,100),600+randint(-25,25)+randint(-100,100)],r'assets\images\BulletLeft.png',(50,50),"wave3")
                    bullet8 = Entity(12,[-200+randint(-1000,100),600+randint(-25,25)+randint(-100,100)],r'assets\images\BulletLeft.png',(50,50),"wave3")
                    bullet9 = Entity(12,[-200+randint(-1000,100),600+randint(-25,25)+randint(-100,100)],r'assets\images\BulletLeft.png',(50,50),"wave3")
                    bullet10 = Entity(12,[-200+randint(-1000,100),600+randint(-25,25)+randint(-100,100)],r'assets\images\BulletLeft.png',(50,50),"wave3")
            elif playSize[2] != 200 and timeNow > 17: 
                playSize[2] -= 10

            bullet1Pos = bullet1.getPos()
            bullet1Hitbox = pygame.draw.rect(screen,[0,0,0],[bullet1Pos[0]+5,bullet1Pos[1]+15,40,40/2],3)

            bullet2Pos = bullet2.getPos()
            bullet2Hitbox = pygame.draw.rect(screen,[0,0,0],[bullet2Pos[0]+5,bullet2Pos[1]+15,40,40/2],3)

            bullet3Pos = bullet3.getPos()
            bullet3Hitbox = pygame.draw.rect(screen,[0,0,0],[bullet3Pos[0]+5,bullet3Pos[1]+15,40,40/2],3)
            
            bullet4Pos = bullet4.getPos()
            bullet4Hitbox = pygame.draw.rect(screen,[0,0,0],[bullet4Pos[0]+5,bullet4Pos[1]+15,40,40/2],3)
            
            bullet5Pos = bullet5.getPos()
            bullet5Hitbox = pygame.draw.rect(screen,[0,0,0],[bullet5Pos[0]+5,bullet5Pos[1]+15,40,40/2],3)

            bullet6Pos = bullet6.getPos()
            bullet6Hitbox = pygame.draw.rect(screen,[0,0,0],[bullet6Pos[0]+5,bullet6Pos[1]+15,40,40/2],3)

            bullet7Pos = bullet7.getPos()
            bullet7Hitbox = pygame.draw.rect(screen,[0,0,0],[bullet7Pos[0]+5,bullet7Pos[1]+15,40,40/2],3)

            bullet8Pos = bullet8.getPos()
            bullet8Hitbox = pygame.draw.rect(screen,[0,0,0],[bullet8Pos[0]+5,bullet8Pos[1]+15,40,40/2],3)

            bullet9Pos = bullet9.getPos()
            bullet9Hitbox = pygame.draw.rect(screen,[0,0,0],[bullet9Pos[0]+5,bullet9Pos[1]+15,40,40/2],3)

            bullet10Pos = bullet10.getPos()
            bullet10Hitbox = pygame.draw.rect(screen,[0,0,0],[bullet10Pos[0]+5,bullet10Pos[1]+15,40,40/2],3)











            wave3Bullets = [bullet1,bullet2,bullet3,bullet4,bullet5,bullet6,bullet7,bullet8,bullet9,bullet10]
            wave3Hitboxes =[bullet1Hitbox,bullet2Hitbox,bullet3Hitbox,bullet4Hitbox,bullet5Hitbox,bullet6Hitbox,bullet7Hitbox,bullet8Hitbox,bullet9Hitbox,bullet10Hitbox]
            for bullet in wave3Bullets:
                bullet.move((1,0))
                bullet.blit()
            for hitbox in wave3Hitboxes:
                if playerRect.colliderect(hitbox):
                    ended = end(ended)
            if timeNow >= 20:
                
                sparklePos = sparkle.getPos()
                sparkleM = angleMath(sparklePos[0],sparklePos[1],playerX,playerY,sparkle.getSpeed())
                sparkleMX = sparkleM[0]
                sparkleMY = sparkleM[1]
                if sparklePos[0] < playerX:
                    sparkle.move([sparkleMX*-1,sparkleMY*-1])
                else:
                    sparkle.move([sparkleMX,sparkleMY])
                
                sparkle.blit()
                if playerRect.colliderect(sparkleHitbox):
                    ended = end(ended)
        # wave 4
        elif timeNow >= 25 :
            if wave4 == False:
                wave4 = True
                deleteColor1, deleteColor2 = [0,0,0], [0,0,0]
                deleteColorMultiplier1, deleteColorMultiplier2 = 1, 1
                deleteFinished1, deleteFinished2 = False, False
                deleteEnd1, deleteEnd2 = False, False
                circle1Pos = [400,-120] # add random PLEASE
                circle2Pos = [450,-150] # add random PLEASE
                circle3Pos = [500,-140] # add random PLEASE
                circle4Pos = [550,-150] # add random PLEASE
                circle5Pos = [600,-180] # add random PLEASE
            if playSize[2] < 300:
                playSize[2]+= 5

            if deleteFinished2 == False:
                if deleteColor2[0] < 252 and deleteEnd2 == False:
                    deleteColorMultiplier2 = deleteColorMultiplier2 + 0.0022
                    deleteColor2 = [int(deleteColor2[0]*deleteColorMultiplier2)+deleteColorMultiplier2,0,0]
                if deleteColor2[0]>240:
                    if deleteCube2.colliderect(playerRect):
                        ended = end(ended)
     
            try:
                deleteCube2 = pygame.draw.rect(screen,deleteColor2,[350,500,300,100])
            except: 
                deleteFinished2 = True
                
            if deleteFinished1 == False:
                if deleteColor1[0] < 252 and deleteEnd1 == False:
                    deleteColorMultiplier1 = deleteColorMultiplier1 + 0.0022
                    deleteColor1 = [int(deleteColor1[0]*deleteColorMultiplier1)+deleteColorMultiplier1,0,0]
                if deleteColor1[0]>240:
                    if deleteCube1.colliderect(playerRect):
                        ended = end(ended)
     
            try:
                deleteCube1 = pygame.draw.rect(screen,deleteColor1,[350,700,300,100])
            except: 
                deleteFinished1 = True

            if timeNow >= 27:
                circle1 = pygame.draw.circle(screen,[255,255,255],circle1Pos,12.0)   

                circle2= pygame.draw.circle(screen,[255,255,255],circle2Pos,12.0)    

                circle3 = pygame.draw.circle(screen,[255,255,255],circle3Pos,12.0)

                circle4 = pygame.draw.circle(screen,[255,255,255],circle4Pos,12.0)

                circle5 = pygame.draw.circle(screen,[255,255,255],circle5Pos,12.0)

                circle1Pos[1] += 5
                circle2Pos[1] += 5
                circle3Pos[1] += 5
                circle4Pos[1] += 5
                circle5Pos[1] += 5
                print(circle5Pos)



    #DONT
    #DONT
    #DONT
    pygame.draw.rect(screen,[255,255,255],playSize,7)
    if ended:
        screen.fill([0,0,0])
        Gengar.blit()
        pygame.draw.rect(screen,[255,255,255],[350,500,300,300],7)
        Player.blit()
        pressHeart = Text("PRESS YOUR HEART TO TRY AGAIN",40,(190,150),r"assets\other\Determination.ttf",(255,255,255)) #,[playerHitbox[2],playerHitbox[3]],[playerHitbox[0],playerHitbox[1]])
        pressHeart.blit()
        heartButton = Button([playerHitbox[0],playerHitbox[1],playerHitbox[2],playerHitbox[3]],"",True,[0,0,0])
        if heartButton.check_clicked():
            pass # reset ALL variables here!
    if timeNow == 50:
        won = True
        print("ggig")    
    clock.tick(60)
    pygame.display.update()