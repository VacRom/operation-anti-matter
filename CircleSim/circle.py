import pygame as pg

pg.init()

# Set the width and height of the screen [width, height]
width = 1200
height = 600
size = (width, height)
screen = pg.display.set_mode(size)

# Initial state
state = (600, 0, 300, 0, 30)

pg.display.set_caption("Circle_Test")

# Loop until the user clicks the close button.
done = False

# Like frame rate
clock = pg.time.Clock()

while not done:  
    print(state, done, clock)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    if state[4] < 0:
        done = True
    if state[0] < 0:
        done = True
    if state[0] > width:
        done = True
    if state[2] < 0:
        done = True
    if state[2] > height:
        done = True
# Logic

    # WASD QE Controls
    if (event.type == pg.KEYDOWN):
        if (event.key == pg.K_w):
            newStatey = -20
            state = (state[0], state[1], state[2]+newStatey, state[3], state[4])
        if (event.key == pg.K_a):
            newStatex = -20
            state = (state[0]+newStatex, state[1], state[2], state[3], state[4])
        if (event.key == pg.K_s):
            newStatey = 20
            state = (state[0], state[1], state[2]+newStatey, state[3], state[4])
        if (event.key == pg.K_d):
            newStatex = 20
            state = (state[0]+newStatex, state[1], state[2], state[3], state[4])
        # Grow and shrink ball radius.
        if (event.key == pg.K_q):
            newStateR = 10
            state = (state[0], state[1], state[2], state[3], state[4]+newStateR)
        if (event.key == pg.K_e):
            newStateR = -10
            state = (state[0], state[1], state[2], state[3], state[4]+newStateR)
        else:
            state = state

# Draw
    screen.fill((255, 255, 255))
    pg.draw.circle(screen, (0, 0, 0), (state[0], state[2]), state[4], 0)

# Update
    pg.display.flip()

# Frame rate
    clock.tick(30)

pg.quit()
