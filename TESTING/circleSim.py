import pygame as pg
import random as rn

pg.init()

width = 1200
height = 600
size = (width, height)
screen = pg.display.set_mode(size)
pg.display.set_caption("Circles Simulation")

totalCircles = 5

state0 = (100, 0, 100, 0, 30)
state1 = (200, 0, 100, 0, 20)
state2 = (200, 0, 100, 0, 10)
state3 = (300, 0, 100, 0, 40)
state4 = (400, 0, 100, 0, 50)
state = (state0, state1, state2, state3, state4)


done = False

clock = pg.time.Clock()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill((255, 255, 255))
    for n in range(totalCircles-1):
        pg.draw.circle(screen, (0, 0, 0), (state[n][0], state[n][2]), state[n][4], 0)
    pg.display.flip()

    clock.tick(60)
pg.quit()
