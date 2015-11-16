import runWorld as rw
import pygame as pg

pg.init()

state = (1, 1, 1, 1, 1)

# Initialize world (height, width, flags, depth)
width = 1200
height = 600
DISPLAYSURF = pg.display.set_mode((width, height), 0, 30)
pg.display.set_caption('CircleTest')

# Display

def updateDisplay(state):
    pg.draw.circle(DISPLAYSURF, (255, 255, 255),
                   (state[0], state[2]), state[4], 0)

# Update State

def updateState(state):
    return((state[0], state[1], state[2], state[3], state[4]))

# End State

def endState(state):
    if (state[0] > width or state[0] < 0):
        return True
    if (state[2] > height or state[2] < 0):
        return True
    if (state[4] < 1):
        return True
    else:
        return False

# WASD controls

def handleEvent(state, event):
    if (event.type == pg.KEYDOWN):
        if (event.key == pg.K_w):
            newStatey = -20
            return((state[0], state[1], state[2]+newStatey, state[3], state[4]))
        if (event.key == pg.K_a):
            newStatex = -20
            return((state[0]+newStatex, state[1], state[2], state[3], state[4]))
        if (event.key == pg.K_s):
            newStatey = 20
            return((state[0], state[1], state[2]+newStatey, state[3], state[4]))
        if (event.key == pg.K_d):
            newStatex = 20
            return((state[0]+newStatex, state[1], state[2], state[3], state[4]))
        if (event.key == pg.Q_q):
            newStateR = 10
            return((state[0], state[1], state[2], state[3], state[4]+newStateR))
        if (event.key == pg.E_q):
            newStateR = -10
            return((state[0], state[1], state[2], state[3], state[4]+newStateR))
        else:
            return(state)
    else:
        return(state)

# Initial states
initState = (600, 0, 300, 0, 30)

frameRate = 30

print(state)

rw.runWorld(initState, updateDisplay, updateState, handleEvent, endState, frameRate)

