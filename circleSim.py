import pygame as pg
import random as rn
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
    radius = rn.randint(5,10)
    x = rn.randint(0, 3)
    velx = rn.randint(-7,7)
    vely = rn.randint(-7,7)
    if x == 0:
        color = (255, 0, 0)
    if x == 1:
        color = (0, 255, 0)
    if x == 2:
        color = (0, 0, 255)
    if x == 3:
        color = (0, 0, 0)
    state.append([rn.randint(0, width), velx, rn.randint(0, height), vely, radius, color])

# Setting up the game.
done = False
clock = pg.time.Clock()

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # Clears the screen.
    screen.fill((255, 255, 255))
    # Clears the lists for calculating the centroid.
    stateGx = []
    stateGy = []
    # Draw circles and apply velocity.
    for n in range(totalCircles):
        if state[n][4] != 0:
            pg.draw.circle(screen, state[n][5], (state[n][0], state[n][2]), state[n][4], 0)
         # AI
            # Black - Constant Speed.
            # Red - Random Walk.
            if state[n][5] == (255,0,0):
                state[n][1] = rn.randint(-15, 15)
                state[n][3] = rn.randint(-15, 15)
            # Green - Walk towards the center of all green points.
            if state[n][5] == (0,255,0):
                stateGx = []
                stateGy = []
                for m in range(totalCircles):
                    if state[m][5] == (0,255,0):
                        stateGx.append(state[m][0])
                        stateGy.append(state[m][2])
                c = [stateGx,stateGy]
                centroid = (sum(c[0])/len(c[0]),sum(c[1])/len(c[1]))
                if state[n][0] < centroid[0]:
                    state[n][0] = state[n][0] + rn.randint(3,7)
                if state[n][0] > centroid[0]:
                    state[n][0] = state[n][0] - rn.randint(1,3)
                if state[n][2] < centroid[1]:
                    state[n][2] = state[n][2] + rn.randint(1,3)
                if state[n][2] > centroid[1]:
                    state[n][2] = state[n][2] - rn.randint(1,3)
            # Blue
            # Apply velocity
            if state[n][5] != (0,255,0):
                state[n][0] = state[n][0]+state[n][1]
                state[n][2] = state[n][2]+state[n][3]
            # Boundaries
            if state[n][0] < state[n][4] or state[n][0] > width-state[n][4]:
                state[n][0] = state[n][0]-state[n][1]
                state[n][1] = - state[n][1]
            if state[n][2] < state[n][4] or state[n][2] > height-state[n][4]:
                state[n][2] = state[n][2]-state[n][3]
                state[n][3] = - state[n][3]
             # Collisions
            for m in range(totalCircles):
                if state[m][4] != 0:
                    if n != m and math.hypot(state[m][0]-state[n][0],state[m][2]-state[n][2]) < state[n][4]+state[m][4] and state[m][4] != 0:
                        if state[n][4] == state[m][4]:
                            state[n][1] = - state[n][1]
                            state[n][3] = - state[n][3]
                            state[m][1] = - state[m][1]
                            state[m][3] = - state[m][3]
                        if state[n][4] > state[m][4]:
                            state[n][4] = int(math.sqrt(((state[n][4]) * (state[n][4])) + ((state[m][4] * state[m][4]))))
                            state[m][4] = 0

    for m in range(totalCircles):
        if (0,255,0) in state[m] and state[m][4] != 0:
            pg.draw.circle(screen, (0, 100, 0), (int(centroid[0]),int(centroid[1])), 10, 0)

    pg.display.flip()
    clock.tick(30)
pg.quit()

