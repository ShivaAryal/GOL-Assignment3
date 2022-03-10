from this import d
from main import conway_assignment_two
from main import conway_assignment_three
import numpy as np
import matplotlib.pyplot as plt
import datetime

# point num 4
board_sizes = [1000, 1250, 1500, 1750]
time_two = []
time_three = []
time_steps = 100

# timesteps per milles

def get_current_time():
    return datetime.datetime.now()

for size in board_sizes:
    random_grid_array = np.random.randint(2, size=(size, size))
    # assigent_two function
    starttime_two = get_current_time()
    for i in range(time_steps):
        random_grid_array = conway_assignment_two(random_grid_array, size)
    endtime_two = get_current_time()
    time_two.append(time_steps/((endtime_two-starttime_two).total_seconds()*1000))

    ################

    random_grid_array = np.random.randint(2, size=(size, size))
    # assigent_three function
    starttime_three = get_current_time()
    for i in range(time_steps):
        random_grid_array = conway_assignment_three(random_grid_array, size)
    endtime_three = get_current_time()
    time_three.append(time_steps/((endtime_three-starttime_three).total_seconds()*1000))
    ####
    
print(time_two, time_three)
    
plt.plot(board_sizes, time_two, label='Conway Assignment Two', marker='o')
plt.plot(board_sizes, time_three, label='Conway Assignment Three', marker='x')
plt.legend()
plt.show()
        