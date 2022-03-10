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
    axes.plot(timeStepArr, aliveArr, label="Alive", color='b', marker='o')
    axes.plot(timeStepArr, deadArr, label="Dead",color='g', marker='x')
    if i == time_steps:
        plt.close()
    
fig = plt.figure(figsize=(15, 7))
axes = fig.add_subplot(1,1,1)
anim = FuncAnimation(fig, animate, frames=time_steps, interval=50, repeat=False)

plt.xlabel('Timesteps-->')
plt.ylabel('Alive and dead-->')

plt.legend()
plt.show()