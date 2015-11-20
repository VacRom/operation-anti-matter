import matplotlib.pyplot as plt
import circleSim as cS
 
# Data to plot
labels = 'black', 'red', 'green', 'blue'
sizes = [cS.ratioState[0], cS.ratioState[1], cS.ratioState[2], cS.ratioState[3]]
colors = ['black', 'red', 'green', 'blue']

if cS.ratioState[0] > cS.ratioState[1] and cS.ratioState[2] and cS.ratioState[3]:
    explode = (.3,0,0,0)
if cS.ratioState[1] > cS.ratioState[0] and cS.ratioState[2] and cS.ratioState[3]:
    explode = (0,.3,0,0)
if cS.ratioState[2] > cS.ratioState[0] and cS.ratioState[1] and cS.ratioState[3]:
    explode = (0,0,.3,0)
else:
    explode = (0,0,0,.3)

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
