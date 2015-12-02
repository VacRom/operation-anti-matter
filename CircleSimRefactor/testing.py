import pygame as pg
import random as rn

width = 1200
height = 800
totalCircles = 500
TeamRedSizeAdvantage = 1
TeamBlueSpeedAdvantage = 5


pit = []
screen = pg.display.set_mode(width, height)
pg.display.set_caption("sim v2.0")

class Ball():
    def mkBall(color):
        x = rn.randint(10, width-10)
        velx = rn.randint(-7, 7)
        y = rn.randint(10, height-10)
        vely = rn.randint(-7, 7)
        radius = rn.randint(6, 8)
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
        global state
        state = [x, velx, y, vely, radius, color]
        pit.append(state)

    def mkPit(allCircles):
        for someCircle in range(allCircles):
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

Ball.mkPit(totalCircles)

done = False
clock = pg.time.Clock()

pg.init()

while not done:
    for event in pg.event.get():
        if event.type is pg.QUIT:
            done = True

    screen.fill((255, 255, 255))


print('done')
