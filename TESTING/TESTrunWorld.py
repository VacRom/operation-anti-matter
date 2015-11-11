import pygame as pg

'''
The playgame library (here, pg) provides global
state, which procedures in this library affect.
'''

def newDisplay(win_width, win_height, win_caption):
    '''
    Purpose: Given window height, width, and caption,
    initialize graphics system and window

    Signature: nat -> nat -> string -> clock
    Effects: initialize graphics system create window
    '''
    global clock, font, displaySurface
    pg.init()
    pg.display.set_caption(win_caption)
    displaySurface = pg.display.set_mode((win_width, win_height))
    clock = pg.time.Clock()


def runWorld(initVelocity, initState, updateDisplay,
             updateVelocity, updateState, handleEvent, endState, frameRate):
    '''Purpose: coinductively run world: exit if in end state
    otherwise set current state to init state, and then
    iteratively render the current state, update it, iterate.

    Signature: clock -> state -> (state -> { graphic IO }) ->
        (state -> state) - (state -> bool) -> unit
    Effects: display specified sequence of world states until done'''
    done = False
    currentVelocity = initVelocity
    currentState = initState
    while not done:
        updateDisplay(currentState, currentVelocity)
        pg.display.update()
        clock.tick(frameRate)
        currentVelocity = updateVelocity(currentState, currentVelocity)
        currentState = updateState(currentState, currentVelocity)
        if (endState(currentState, currentVelocity)):
            done = True
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                done = True
            else:
                currentState = handleEvent(currentState, event)
                currentVelocity = handleEvent(currentVelocity, event)
    pg.quit()
