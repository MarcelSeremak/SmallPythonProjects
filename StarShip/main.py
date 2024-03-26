import pygame, sys, random
from pygame.locals import *
windowHeight = 480
windowWidth = 720
pygame.font.init()




class Ship():
    def __init__(self, x1, y1, shipImg, guns=1, speed=1):
        self.x1 = x1
        self.y1 = y1
        self.guns = guns
        self.speed = speed
        self.shipImg = shipImg
        self.mask = pygame.mask.from_surface(self.shipImg)

    def place(self, screen):
        screen.blit(self.shipImg,(self.x1,self.y1))

class Meteor():
    def __init__(self, x1, y1, meteorImage, type, speed=1):
        self.x1 = x1
        self.y1 = y1
        self.meteorImage = meteorImage
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.meteorImage)
        self.type = type

    def place(self, screen):
        screen.blit(self.meteorImage,(self.x1,self.y1))
        self.y1 += 0.3


class Shot():
    def __init__(self, x1, y1, shotImg):
        self.x1 = x1
        self.y1 = y1
        self.shotImg = shotImg
        self.mask = pygame.mask.from_surface(self.shotImg)

    def place(self, screen):
        screen.blit(self.shotImg,(self.x1,self.y1))
        self.y1 -= 2

    def collision(self, object):
        return collide(object, self)


def collide(obj1, obj2):
    offset_x = obj2.x1 - obj1.x1
    offset_y = obj2.y1 - obj1.y1
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
def main():
    level = 0
    points = "0"
    meteors = []
    shots = []
    lives = 3
    money = "0"

    pygame.init()
    mainFont = pygame.font.SysFont("comicsans", 40)

    x1 = 330
    y1 = 310
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('StarShip Game')
    background = pygame.image.load('background.png')
    screen.blit(background, (0,0))
    mainShipImage = pygame.image.load('mainShip.png')
    shotImage = pygame.image.load("shot.png")

    mainShip = Ship(x1,y1,mainShipImage)
    mainShip.place(screen)

    meteorImg = pygame.image.load("meteor.png")
    moneyMeteorImg = pygame.image.load("coinMeteor.png")

    pointsLabel = mainFont.render("00000", 1, (255, 255, 255))
    running = True

    heartImg = pygame.image.load("heart.png")

    coinImg = pygame.image.load("coin.png")




    while running:
        clock.tick()

        if len(meteors) == 0:
            level +=1
            for i in range(level):
                type = random.choices([1,2],[9,2])[0]
                if type == 1:
                    meteor = Meteor(random.randint(30, 670), random.randint(-400, -100),meteorImg,0)
                else:
                    meteor = Meteor(random.randint(30, 670), random.randint(-400, -100),moneyMeteorImg,1 )
                meteors.append(meteor)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if mainShip.x1 > 0:
                mainShip.x1 -= 3
        elif keys[pygame.K_UP]:
            if mainShip.y1 > 0:
                mainShip.y1 -= 3
        elif keys[pygame.K_RIGHT]:
            if mainShip.x1 < 660:
                mainShip.x1 += 3
        elif keys[pygame.K_DOWN]:
            if mainShip.y1 < 310:
                mainShip.y1 += 3

        elif keys[pygame.K_SPACE]:
            shots.append(Shot(mainShip.x1+25, mainShip.y1,shotImage))


        pointsLabel = mainFont.render(f"{points.zfill(5)}", 1, (76, 58, 5))
        levelLabel = mainFont.render(f"Level: {level}",1,(255, 255, 255))
        coinLabel = mainFont.render(f"{money.zfill(3)}", 1, (0, 0, 0))


        screen.blit(background, (0, 0))
        mainShip.place(screen)
        screen.blit(pointsLabel,(200,390))
        screen.blit(levelLabel,(20,10))
        screen.blit(coinLabel,(50,325))
        screen.blit(coinImg,(10,340))

        if lives == 3:
            screen.blit(heartImg,(590,335))
            screen.blit(heartImg, (630, 335))
            screen.blit(heartImg, (670, 335))
        elif lives == 2:
            screen.blit(heartImg,(590,335))
            screen.blit(heartImg, (630, 335))
        elif lives == 1:
            screen.blit(heartImg,(590,335))
        else:
            running = False



        for m in meteors[:]:
            m.place(screen)
            if m.y1 >= 350:
                meteors.remove(m)
                lives -= 1
            if collide(mainShip, m):
                lives -= 1
                meteors.remove(m)

        for shot in shots[:]:
            shot.place(screen)
            if shot.y1 == 0:
                shots.remove(shot)
            for meteor in meteors[:]:
                 if shot.collision(meteor):
                    points = str(int(points) + 1)
                    if meteor.type == 1:
                        money = str(int(money) + 1)
                    if shot not in shots:
                        meteors.remove(meteor)
                    else:
                        shotX = shot.x1
                        for shot1 in shots[:]:
                            if shot1.x1 == shotX:
                                shots.remove(shot1)
                        meteors.remove(meteor)







        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit ()
                sys.exit()

        pygame.display.update()


main()


