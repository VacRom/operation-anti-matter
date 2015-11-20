import pygame as pg
import random as rn
import math
import matplotlib.pyplot as plt

'This simulation is based on the motions of microbes on a dish. The idea was based on the game Agario where players, represented by circles, consume other players to grow larger. In this simulation we have four different bacteria species: Black, Red, Green, and Blue. Each one of them has their own behaviors which may give them advantages or disadvantages depending on the game parameters.'

'The Black species move around the screen with a moderate velocity and bounce off any walls. They are our control species where there are no advantages or disadvantages.'

'The Red species cannot move deterministically. They follow random, Brownian, motion. On average they are larger than other species.'

'The Green species move towards each other in order to work together to increase their size rapidly; however, this advantageous adaptation is compensated by reduced speed compared to other species.'

'The Blue species move like the Black species, in straight lines, but with an increased speed. Due to their great speed their initial sizes is smaller than average.'

'Here are user input parameters:'
screenWidth = 1200
screenHeight = 650
totalCircles = 500

TeamRedSizeAdvantage = 1
TeamBlueSpeedAdvantage = 5

'End of parameters'

'The purpose of this simulation is to change the parameters to investigate which species will naturally dominate the others. Note that the percentage remaining of different color types is indicated in the head text as [Black, Red, Green, Blue].'

pg.init()

width = screenWidth
height = screenHeight
size = (width, height)
screen = pg.display.set_mode(size)
pg.display.set_caption("sim")

state = []
time = 0
bspeed = TeamBlueSpeedAdvantage

# This generates the initial conditions for our circles.
for n in range(totalCircles):
    radius = rn.randint(6,8)
    x = rn.randint(0, 3)
    velx = 0
    vely = 0
    while velx == 0 and vely == 0:
        velx = rn.randint(-7,7)
        vely = rn.randint(-7,7)
    if x == 0:
        radius = TeamRedSizeAdvantage + radius
        color = (255, 0, 0)
    if x == 1:
        color = (0, 255, 0)
    if x == 2:
        radius = radius - 1
        color = (0, 0, 255)
        velx = rn.randint(-7,7)
        vely = rn.randint(-7,7)
        if velx < 0:
            velx = velx - bspeed
        if velx > 0 or velx == 0:
            velx = velx + bspeed
        if vely< 0:
            vely = vely - bspeed
        if vely > 0 or vely == 0:
            vely = vely + bspeed

    if x == 3:
        color = (0, 0, 0)
    state.append([rn.randint(10, width-10), velx, rn.randint(10, height-10), vely, radius, color])

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
            # Black: 0 Constant Speed.
            # Red: + Size, - Random Movement
            if state[n][5] == (255,0,0):
                state[n][1] = rn.randint(-15, 15)
                state[n][3] = rn.randint(-15, 15)
            # Green: + Smart Movement, - Slower movement and no
            # movement when t is large.
            if state[n][5] == (0,255,0):
                stateGx = []
                stateGy = []
                for m in range(totalCircles):
                    if state[m][5] == (0,255,0) and state[m][4] != 0:
                        stateGx.append(state[m][0])
                        stateGy.append(state[m][2])
                c = [stateGx,stateGy]
                centroid = (sum(c[0])/len(c[0]),sum(c[1])/len(c[1]))
                if state[n][0] < centroid[0]:
                    state[n][0] = state[n][0] + rn.randint(2,5)
                if state[n][0] > centroid[0]:
                    state[n][0] = state[n][0] - rn.randint(2,5)
                if state[n][2] < centroid[1]:
                    state[n][2] = state[n][2] + rn.randint(2,5)
                if state[n][2] > centroid[1]:
                    state[n][2] = state[n][2] - rn.randint(2,5)
            # Blue: + Speed, - Size
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
    subR = []
    subG = []
    subU = []
    subB = []
    # Draws the centroid.
    for m in range(totalCircles):
        if state[m][4] != 0:
            if (0,255,0) in state[m] and state[m][4] != 0:
                pg.draw.circle(screen, (0, 100, 0), (int(centroid[0]),int(centroid[1])), 10, 0)
            # Counts the remaining circles and their respective colors.
            if state[m][5] == (255,0,0):
                subR.append(state[m])
            if state[m][5] == (0,255,0):
                subG.append(state[m])
            if state[m][5] == (0,0,255):
                subU.append(state[m])
            if state[m][5] == (0,0,0):
                subB.append(state[m])
    colorState = [len (subB), len (subR), len (subG), len (subU), time]
    ballsExist = len (subB) + len(subR) + len (subG) + len (subU)
    ratioState = [int(100 * (len (subB) / ballsExist)), int(100 * (len (subR) / ballsExist)), int((100 * len (subG) / ballsExist)), int((100 * len (subU) / ballsExist))]
    #labels = 'Black', 'Red', 'Green', 'Blue'
    #sizes = [ratioState[0], ratioState[1], ratioState[2], ratioState[3]]
    #colors = [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
    #explode = (0,0,0,0)
    #plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=90)
    #plt.axis('equal')
    #fig=plt.figure()
    #ax = fig.gca()
    
    pg.display.flip()
    clock.tick(20)
    pg.display.set_caption(str(ratioState))
    time = time + 1
pg.quit()

