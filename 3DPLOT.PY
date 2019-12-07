from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection = '3d')
plt.show()
# data for a 3d line
zline = np.linspace(0,15,1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline,yline,zline,'gray')
# data for 3d scattered points
zdata = 15* np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata,c = zdata,cmap = 'Greens');
# 3d counter plots
def f(x,y):
    return np.sin(np.sqrt(x ** 2+y**2))
x = np.linspace(-6,6,30)
y = np.linspace(-6,6,30)
x,y = np.meshgrid(x,y)
z = f(x,y)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.contour3D(X,Y,Z,50,cmap = 'binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

'''
A growing circle
'''
from matplotlib import pyplot as plt
from matplotlib import animation
def create_circle():
    circle = plt.Circle((0, 0), 0.05)
    return circle
def update_radius(i, circle):
    circle.radius = i*0.5
    return circle,
def create_animation():
    u fig = plt.gcf()
    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)
    anim = animation.FuncAnimation(
fig, update_radius, fargs = (circle,), frames=30, interval=50)
    plt.title('Simple Circle Animation')
    plt.show()
if __name__ == '__main__':
create_animation()