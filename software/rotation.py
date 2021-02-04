import numpy as np
import math

def rotate(frame):
    a = 0.138066667
    b = -9.1233
    c = -3.426233333
    g = math.sqrt(a**2 + b**2 + c**2)
    R = [[1 - (g**2*a**2/(1 - g*b)), -1*g*a, -g**2*a*c/(1 - g*b)], \
        [g*a, 1 + (g**2*(c**2 - a**2)/(1 - g*b)), g*c], \
        [-1*(g**2*a*c)/(1-g*b), -g*c, 1-g**2*c**2/(1-g*b)]]

    [frame["x_accel_one"], frame["y_accel_one"], frame["z_accel_one"]] = np.matmul(R, [frame["x_accel_one"], frame["y_accel_one"], frame["z_accel_one"]])
    [frame["x_gyro"], frame["y_gyro"], frame["z_gyro"]] = np.matmul(R, [frame["x_gyro"], frame["y_gyro"], frame["z_gyro"]])

    a = 7.452222222
    b = 5.908148148
    c = 2.201851852
    g = math.sqrt(a**2 + b**2 + c**2)


    R = [[1 - (g**2*a**2/(1 - g*b)), -1*g*a, -g**2*a*c/(1 - g*b)], \
        [g*a, 1 + (g**2*(c**2 - a**2)/(1 - g*b)), g*c], \
        [-1*(g**2*a*c)/(1-g*b), -g*c, 1-g**2*c**2/(1-g*b)]]

    [frame["x_accel_two"], frame["y_accel_two"], frame["z_accel_two"]] = np.matmul(R, [frame["x_accel_two"], frame["y_accel_two"], frame["z_accel_two"]])

    return frame