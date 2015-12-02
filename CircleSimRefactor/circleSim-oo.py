import pygame as pg
import random as rn
import math

# Screen size
screenWidth = 1200
screenHeight = 600
# The total number of initial circles.
totalCircles = 300
# The total number of added circles upon pressing A
addBall = 30
# Team advantages for compensating their weaknesses.
TeamRedSizeAdvantage = 1
TeamBlueSpeedAdvantage = 5
# Option to see the current ball population by percentage. Toggle by
# pressing C.
countingOn = False
# Press ESC to exit the program.


class Ball():
    def __init__(color):
        super().__init__()
        color = color

    def mkBall(color):
        color = color
        x = rn.randint(10, width-10)
        velx = rn.randint(-12, 12)
        y = rn.randint(10, height-10)
        vely = rn.randint(-12, 12)
        radius = rn.randint(4, 6)
        color = color
        if color is 'red':
            radius += TeamRedSizeAdvantage
        if color is 'blue':
            if velx < 0:
                velx += -TeamBlueSpeedAdvantage
            elif velx > 0:
                velx += TeamBlueSpeedAdvantage
            if vely < 0:
                vely += - TeamBlueSpeedAdvantage
            elif vely > 0:
                vely += TeamBlueSpeedAdvantage
            else:
                velx += TeamBlueSpeedAdvantage
                vely += TeamBlueSpeedAdvantage
        state = [x, velx, y, vely, radius, color]
        pit.append(state)

    def mkBallPit(totalCircles):
        for circle in range(totalCircles):
            x = rn.randint(0, 3)
            if x is 0:
                color = 'black'
            elif x is 1:
                color = 'red'
            elif x is 2:
                color = 'green'
            elif x is 3:
                color = 'blue'
            Ball.mkBall(color)

    def update(pit):
        for n in range(len(pit)):
            if pit[n][4] != 0:
                if pit[n][5] is 'black':
                    color_0 = (0, 0, 0)
                elif pit[n][5] is 'red':
                    color_0 = (255, 0, 0)
                elif pit[n][5] is 'green':
                    color_0 = (0, 255, 0)
                elif pit[n][5] is 'blue':
                    color_0 = (0, 0, 255)
                pg.draw.circle(screen, color_0, (pit[n][0], pit[n][2]), pit[n][4], 0)
            if pit[n][5] is 'red':
                pit[n][1] = rn.randint(-15, 15)
                pit[n][3] = rn.randint(-15, 15)
            if pit[n][5] is 'green':
                stateGx = []
                stateGy = []
                for m in range(len(pit)):
                    if pit[m][5] is 'green' and pit[m][4] != 0:
                        stateGx.append(pit[m][0])
                        stateGy.append(pit[m][2])
                c = [stateGx, stateGy]
                if len(c[0]) is 0:
                    c[0] = [0]
                if len(c[1]) is 0:
                    c[1] = [0]
                centroid = (sum(c[0])/len(c[0]), sum(c[1])/len(c[1]))
                if pit[n][0] < centroid[0]:
                    pit[n][0] = pit[n][0] + rn.randint(2, 5)
                if pit[n][0] > centroid[0]:
                    pit[n][0] = pit[n][0] - rn.randint(2, 5)
                if pit[n][2] < centroid[1]:
                    pit[n][2] = pit[n][2] + rn.randint(2, 5)
                if pit[n][2] > centroid[1]:
                    pit[n][2] = pit[n][2] - rn.randint(2, 5)
            if pit[n][5] != 'green':
                pit[n][0] = pit[n][0]+pit[n][1]
                pit[n][2] = pit[n][2]+pit[n][3]
            if pit[n][0] < pit[n][4] or pit[n][0] > width-pit[n][4]:
                pit[n][0] = pit[n][0]-pit[n][1]
                pit[n][1] = - pit[n][1]
            if pit[n][2] < pit[n][4] or pit[n][2] > height-pit[n][4]:
                pit[n][2] = pit[n][2]-pit[n][3]
                pit[n][3] = - pit[n][3]
            for m in range(totalCircles):
                if pit[m][4] != 0:
                    if n != m and math.hypot(pit[m][0]-pit[n][0], pit[m][2]-pit[n][2]) < pit[n][4]+pit[m][4] and pit[m][4] != 0:
                        if pit[n][4] == pit[m][4]:
                            pit[n][1] = - pit[n][1]
                            pit[n][3] = - pit[n][3]
                            pit[m][1] = - pit[m][1]
                            pit[m][3] = - pit[m][3]
                        if pit[n][4] > pit[m][4]:
                            pit[n][4] = int(math.sqrt(((pit[n][4]) * (pit[n][4])) + ((pit[m][4] * pit[m][4]))))
                            pit[m][4] = 0
        for m in range(len(pit)):
            if pit[m][4] != 0:
                if 'green' in pit[m] and pit[m][4] != 0:
                    pg.draw.circle(screen, (0, 100, 0), (int(centroid[0]), int(centroid[1])), 10, 0)

    def count(pit):
        subU = []
        subR = []
        subG = []
        subB = []
        for m in range(len(pit)):
            if pit[m][4] != 0:
                if pit[m][5] is 'red':
                    subR.append(pit[m])
                elif pit[m][5] is 'green':
                    subG.append(pit[m])
                elif pit[m][5] is 'blue':
                    subU.append(pit[m])
                elif pit[m][5] is 'black':
                    subB.append(pit[m])
        colorState = [len(subB), len(subR), len(subG), len(subU)]
        ballsExist = len(subB) + len(subR) + len(subG) + len(subU)
        ratioState = [int(100*(len(subB)/ballsExist)), int(100*(len(subR)/ballsExist)), int((100*len (subG)/ballsExist)), int((100*len(subU)/ballsExist))]
        return ratioState


pg.init()

width = screenWidth
height = screenHeight
size = (width, height)
screen = pg.display.set_mode(size)
pg.display.set_caption("sim v2.0")

pit = []
Ball.mkBallPit(totalCircles)

done = False
clock = pg.time.Clock()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    if pg.key.get_pressed()[pg.K_ESCAPE] is 1:
        done = True

    if pg.key.get_pressed()[pg.K_r] is 1:
        pit = []
        Ball.mkBallPit(totalCircles)

    if pg.key.get_pressed()[pg.K_a] is 1:
        Ball.mkBallPit(addBall)
        totalCircles += addBall

    if pg.key.get_pressed()[pg.K_c] is 1:
        countingOn = not countingOn

    screen.fill((255, 255, 255))
    Ball.update(pit)
    if countingOn is True:
        Ball.count(pit)
        pg.display.set_caption('Population by percent: '+'Black:'+str(Ball.count(pit)[0])+' Red:'+str(Ball.count(pit)[1])+ ' Green:'+str(Ball.count(pit)[2])+ ' Blue:'+str(Ball.count(pit)[3]))
    else:
        pg.display.set_caption('sim v2.0')
    pg.display.flip()
    clock.tick(120)
    print(countingOn)

pg.quit()
