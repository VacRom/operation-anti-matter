import pygame as pg
import random as rn
import array
import math

pg.init()

width = 1200
height = 600
size = (width, height)
screen = pg.display.set_mode(size)
pg.display.set_caption("Circles Simulation")
totalCircles = 100

state = []
for n in range(totalCircles):
    state.append([rn.randint(0, width), rn.randint(0,10), rn.randint(0, height), rn.randint(0, 10), rn.randint(1, 5)])

done = False

clock = pg.time.Clock()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill((255, 255, 255))

    # Draw circles and apply velocity.
    for n in range(totalCircles):
        if state[n][4] != 0:
            pg.draw.circle(screen, (0, 0, 0), (state[n][0], state[n][2]), state[n][4], 0)
        state[n][0] = state[n][0]+state[n][1]
        state[n][2] = state[n][2]+state[n][3]
        # Boundaries
        if state[n][0] < state[n][4]:
            state[n][0] = state[n][0] - state[n][1]
            state[n][1] = - state[n][1]
        if state[n][0] > width-state[n][4]:
            state[n][0] = state[n][0] - state[n][1]
            state[n][1] = - state[n][1]
        if state[n][2] < state[n][4]:
            state[n][2] = state[n][2] - state[n][3]
            state[n][3] = - state[n][3]
        if state[n][2] > height-state[n][4]:
            state[n][2] = state[n][2] - state[n][3]
            state[n][3] = - state[n][3]
        # Collisions
        for m in range(totalCircles):
            if n != m:
                if math.hypot(state[m][0]-state[n][0],state[m][2]-state[n][2]) < state[n][4]+state[m][4]:
                    if state[n][4] == state[m][4]:
                        x = rn.randint(0,1)
                        if x == 0:
                            state[n][4] = state[n][4]+1
                    if state[n][4] > state[m][4]:
                        state[n][4] = state[n][4]+state[m][4]
                        state[m][4] = 0
    pg.display.flip()
    clock.tick(30)
pg.quit()
