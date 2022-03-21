import argparse
from main import conway_assignment_three
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.animation import FuncAnimation

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--timesteps", required=True,
                help="Enter number of timesteps", type=int)
ap.add_argument("-g", "--size", required=True,
                help="Enter board size", type=int)
ap.add_argument("-s", "--board_initialization", required=True,
                help="Set board into some initial state (1. Blinker || 2. Glider || 3. Glider gun || 4. heptomino) ", type=str)

group = ap.add_mutually_exclusive_group()
group.add_argument('-a', "--animation", action='store_true', help='Get history of board')
            
args = vars(ap.parse_args())
print(args)

timesteps = args['timesteps']
board_initialization = args['board_initialization']
animation = args['animation']
size = args['size']

def random():
    grid_arr = np.random.randint(2, size=(size, size))
    return grid_arr

def blinker():
    grid_arr = np.zeros(shape=(size, size), dtype = 'int')
    grid_arr[2][1]=1
    grid_arr[2][2]=1
    grid_arr[2][3]=1
    return grid_arr

def glider():  # Method to set initial state as glider before the simulation starts
    grid_arr = np.zeros(shape=(size, size), dtype = 'int')
    grid_arr[1][0] = 1
    grid_arr[2][1] = 1
    grid_arr[2][2] = 1
    grid_arr[1][2] = 1
    grid_arr[0][2] = 1
    return grid_arr

grid_arr = None
if(board_initialization=='random'):
    grid_arr = random()
elif(board_initialization=='blinker'):
    grid_arr = blinker()
else:
    grid_arr = glider()


def animate(frameNum):
    global grid_arr
    grid_arr = conway_assignment_three(grid_arr, size)
    grid_board_show.set_data(grid_arr)
    if frameNum >= timesteps:
        plt.close()

if animation: 
    fig, axes = plt.subplots(figsize=(15, 8))
    fig_plot = axes.matshow(grid_arr)
    grid_board_show = plt.imshow(grid_arr)
    axes.set_title('Test Code For Conway Assignment3 function')
    ani = FuncAnimation(fig, animate, interval=10)

    plt.show()

    
