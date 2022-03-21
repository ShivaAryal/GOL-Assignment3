import numpy as np

def conway_assignment_two(grid_array,size):
    def get_neighbours(grid_array, x, y):
        total = 0
        neighbors_pos = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for pos in neighbors_pos:
            x_pos = (x + pos[0] + size) % size
            y_pos = (y + pos[1] + size) % size
            total += grid_array[x_pos][y_pos]
        return total
            
    next = np.zeros(shape=(size, size), dtype='int')
    
    for row in range(size):
        for column in range(size):
            state = grid_array[row][column]
            neighbours = get_neighbours(grid_array, row, column)   # Call get_neighbours to get total alive neighbours

            if state == 0 and neighbours == 3:  # Check condition for cell to be alive 
                next[row][column] = 1
                    
            elif state == 1 and (neighbours < 2 or neighbours > 3): # Check condition for cell to be dead 
                next[row][column] = 0
            else:
                next[row][column] = state
                
    grid_array = next    
    return grid_array  

def conway_assignment_three(grid_array, size, time_step=None, animation=False):
    wrapped_board = np.pad(grid_array,1, mode='wrap')
    wrapped_shp = wrapped_board.shape[0] 

    neighbors = np.roll(grid_array, [1, 1], axis=(0, 1)) + wrapped_board[2:,1:wrapped_shp-1] + np.roll(grid_array, [1, -1], axis=(0, 1)) + \
                wrapped_board[1:wrapped_shp-1,2:wrapped_shp] +     wrapped_board[1:wrapped_shp-1,0:wrapped_shp-2] + \
                np.roll(grid_array, [-1, 1], axis=(0, 1)) + wrapped_board[0:wrapped_shp-2, 1: wrapped_shp-1] + np.roll(grid_array, [-1, -1], axis=(0, 1))  
    

    birth = (neighbors == 3) & (grid_array == 0)
    survives= ((neighbors == 2) | (neighbors == 3)) & (grid_array == 1)
    
    grid_array[...] = 0
    grid_array[birth | survives] = 1
    return grid_array
    

def GameOfLife(animations, time_step, size,initial_grid_array):     #true or false; true->last ma ekaichoti animate garni , false-> harek timestep ma animate garni
    board_state_history = []
    new_grid_array = initial_grid_array
    for _ in range(time_step):
        new_grid_array = conway_assignment_two(new_grid_array, size)
        board_state_history.append(new_grid_array)
        
    if animations == True:
        return board_state_history




# Reference was taken from: https://www.labri.fr/perso/nrougier/from-python-to-numpy/