from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
from main import conway_assignment_three

size = 1000
time_steps = 500

random_grid_array = np.random.choice((0,1),size=(size, size), p=[0.5,0.5])
board = random_grid_array
aliveArr = []
deadArr = []
timeStepArr = []

def animate(i):
    global board
    global aliveArr
    global deadArr
    global timeStepArr
    board = conway_assignment_three(board, size) 
    alive = np.sum(board) # total alive
    dead = (size*size) - alive # total dead
    aliveArr.append(alive)
    deadArr.append(dead)
    timeStepArr.append(i)
    axes.clear()
    axes.plot(timeStepArr, aliveArr, label="Alive", color='b')
    axes.plot(timeStepArr, deadArr, label="Dead",color='g')
    axes.set_xlim(0,500)
    axes.set_ylim(0,1000*1000)
    axes.ticklabel_format(style='plain')
    axes.set_xlabel('Timesteps-->')
    axes.set_ylabel('Alive and dead-->')
    axes.legend(loc = 'upper left')
    if i == time_steps:
        plt.close()
    
fig = plt.figure(figsize=(15, 7))
axes = fig.add_subplot(1,1,1)
anim = FuncAnimation(fig, animate, interval=50, repeat=False)

# plt.xlabel('Timesteps-->')
# plt.ylabel('Alive and dead-->')

# plt.legend(loc ="lower right")
plt.show()