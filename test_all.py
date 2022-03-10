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

conway_assignment_three(grid_arr, size, timesteps, animation=True)

# def neighbor_condition(grid):
#     live_neighbors = neighbors_count(grid)
#     survive_underpopulation = live_neighbors >= 2
#     survive_overpopulation = live_neighbors <= 3
#     survive = grid * survive_underpopulation * survive_overpopulation
#     new_status = np.where(live_neighbors==3, True, survive)  # Reproduce
#     new_neighbors = neighbors_count(new_status)
#     return new_status, new_neighbors 

# def neighbors_count(grid):
#     """Counts the number of neighboring live cells"""
#     kernel = np.array(
#         [[1, 1, 1],
#          [1, 0, 1],
#          [1, 1, 1]]
#     )
#     c = conv2d(grid, kernel)
#     return c

# def conv2d(grid, kernel):
#     s = grid.shape + tuple(np.subtract(grid.shape, kernel.shape) + 1)
#     strd = np.lib.stride_tricks.as_strided
#     subM = strd(grid, shape = s, strides = grid.strides * 2)
#     return np.einsum('ij,ijkl->kl', filter, subM)

# def get_updated_colors(grid, c):
#     cmap = mpl.cm.Blues_r
#     rescale = c / 8  # Maximum of 8 neighbors
#     colors = [cmap(neighbors) for neighbors in rescale.flatten()]
#     is_live = grid.flatten()
#     colors = [(r, g, b, 0.9) if live else (r, g, b, 0) for live, (r, g, b, a) in zip(is_live, colors)]
#     return colors

# def simulate_and_visualize(i):
#     global grid_arr
#     # grid_arr = conway_assignment_three(grid_arr)
#     grid_arr, live_neigbors = neighbor_condition(grid_arr)
#     colors = get_updated_colors(grid_arr, live_neigbors)
#     scatter.set_facecolor(colors)
#     return scatter

# def get_board(size):
#     xs = np.arange(0, size)
#     ys = np.arange(0, size)
#     board = np.meshgrid(xs, ys)
#     return board

# board = get_board(size)

# fig, axes = plt.subplots(figsize=(15, 15))
# scatter = axes.scatter(*board, animated=True, s=300, edgecolor=None)



# FuncAnimation(fig, simulate_and_visualize, frames=timesteps, interval=50)


