import random as rn
width = 1200
height = 600

state = []

totalCircles = 10
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


for n in range(totalCircles):
    print(state)
    def zeroRad(state):
        if state[n][4] > 0:
            return state[n]
    filter(zeroRad, state)
