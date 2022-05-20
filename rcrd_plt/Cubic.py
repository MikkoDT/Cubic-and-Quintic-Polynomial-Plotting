import numpy as np
import matplotlib.pyplot as plt

# degrees to radian converter
def deg_to_rad(T):
    return (T/180)*np.pi

qi = float(input('qi = ')) # initial position
qi = deg_to_rad(qi)

vi = float(input('vi = ')) # initial velocity
vi = deg_to_rad(vi)

qf = float(input('qf = ')) # final position
qf = deg_to_rad(qf)

vf = float(input('vf = ')) # final velocity
vf = deg_to_rad(vf)

ti = float(input('ti = ')) # initial time
tf = float(input('tf = ')) # final time

# Cubic
# Solve the solution for q(t) = a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

x = np.arange(ti,tf,0.05)

def cubic(t,a,b,c):
    return a + (3*(b-a)/c**2)*t**2 - (2*(b-a)/c**3)*t**3

y = cubic(x,qi,qf,tf)