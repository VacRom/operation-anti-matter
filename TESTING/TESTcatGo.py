# from trepan.api import debug

# import pdb
# pdb.set_trace()

import runWorld as rw
import drawWorld as dw


# Initialize world
name = "Cat Go!"
width = 500
height = 500
rw.newDisplay(width, height, name)

# World state will be single x coordinate at left edge of world
initState = 0

# Initial velocity.
initVelocity = 1

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")

def updateDisplay(state, velocity):
    dw.fill(dw.black)
    dw.draw(myimage, (state, width))
    
def updateVelocity(state, velocity):
    if state is width:
        velocity = 0
    if state is 0:
        velocity = 1

def updateState(state, velocity):
    if velocity is 1:
        state = state+1
    if velocity is 0:
        state = state-1

# We'll terminate when the x stateinate reaches the screen edge

def endState(state, velocity):
   return False

# For now we'll handle events just logging them to the console
#
def handleEvent(state, event):
    return(state)

# Off we go! Start the cat at the left edge, and try for 30 FPS
frameRate = 60
initState = 0
initVelocity = 1
# debug()
rw.runWorld(initVelocity, initState, updateDisplay, updateVelocity,
            updateState, handleEvent, endState, frameRate)
