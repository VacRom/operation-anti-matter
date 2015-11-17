import pygame as pg
import random as rn
import math

pg.init()

width = 600
height = 600
size = (width, height)
screen = pg.display.set_mode(size)
pg.display.set_caption("Circles Simulation")
totalCircles = 500

state = []

for n in range(totalCircles):
    x = rn.randint(0, 3)
    if x == 0:
        color = (255, 0, 0)
    if x == 1:
        color = (0, 255, 0)
    if x == 2:
        color = (0, 0, 255)
    if x == 3:
        color = (0, 0, 0)
    state.append([rn.randint(0, width), rn.randint(-10,10), rn.randint(0, height), rn.randint(-10, 10), rn.randint(5, 10), color])

done = False

clock = pg.time.Clock()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # Clears the screen
    screen.fill((255, 255, 255))

    # Draw circles and apply velocity.
    for n in range(totalCircles):
        if state[n][4] != 0:
            pg.draw.circle(screen, state[n][5], (state[n][0], state[n][2]), state[n][4], 0)
        state[n][0] = state[n][0]+state[n][1]
        state[n][2] = state[n][2]+state[n][3]
        # Boundaries
        if state[n][0] < state[n][4] or state[n][0] > width-state[n][4] and state[n][4] != 0:
            state[n][1] = - state[n][1]
            state[n][0] = state[n][0]+state[n][1]
        if state[n][2] < state[n][4] or state[n][2] > height-state[n][4] and state[n][4] != 0:
            state[n][3] = - state[n][3]
            state[n][2] = state[n][2]+state[n][3]
            # Collisions
        for m in range(totalCircles):
            if n != m and math.hypot(state[m][0]-state[n][0],state[m][2]-state[n][2]) < state[n][4]+state[m][4] and (state[n][4] != 0 or state[m][4] != 0):
                if state[n][4] == state[m][4]:
                    state[n][1] = - state[n][1]
                    state[n][3] = - state[n][3]
                    state[m][1] = - state[m][1]
                    state[m][3] = - state[m][3]
                if state[n][4] > state[m][4]:
                    state[n][4] = int(math.sqrt(((state[n][4]) * (state[n][4])) + ((state[m][4] * state[m][4]))))
                    state[m][4] = 0

    pg.display.flip()
    clock.tick(60)
pg.quit()
