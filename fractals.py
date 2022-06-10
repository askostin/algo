%matplotlib inline
import matplotlib.pyplot as plt

import math

def divide_line(point_1, point_2, alpha):
    A_x = point_1[0]
    A_y = point_1[1]
    B_x = point_2[0]
    B_y = point_2[1]
    C_x = A_x * (1 - alpha) + B_x * alpha
    C_y = A_y * (1 - alpha) + B_y * alpha
    return (C_x, C_y)
    
def extract_coords(points_list, axis):
    if (axis == 'x'):
        axis_index = 0
    elif (axis == 'y'):
        axis_index = 1
    coords = []
    for point in points_list:
        coords.append(point[axis_index])
    return coords

def fractal_rectangle(points, depth, alpha):
    if (depth == 0):
        plt.show()
        return
    else:
        coords_x = extract_coords(points, 'x')
        coords_x.append(coords_x[0])
        coords_y = extract_coords(points, 'y')
        coords_y.append(coords_y[0])
        
        plt.plot(coords_x, coords_y)
        
        numof_points = len(points)
        new_points = []
        for i in range(numof_points):
            new_point = divide_line(points[i], points[(i+1) % numof_points], alpha)
            new_points.append(new_point)
        
        return fractal_rectangle(new_points, depth - 1, alpha)
