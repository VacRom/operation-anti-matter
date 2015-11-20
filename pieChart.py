import matplotlib.pyplot as plt
import circleSim as cS
 
# Data to plot
labels = 'black', 'red', 'green', 'blue'
sizes = [cS.ratioState[0], cS.ratioState[1], cS.ratioState[2], cS.ratioState[3]]
colors = ['black', 'red', 'green', 'blue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 


plt.axis('equal')
plt.show()
