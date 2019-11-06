# '''plotting the graph for gravitational body
# F = Gm1*m2/r**2
# lets taking m1 = 0.5 kg
# m2 = 1.5kg
# value of G is 6.674*10 raise to the power -11 nm**2'''
# # the relation between gravitational force and distance between two bodies

# import matplotlib.pyplot as plt
# def draw_graph(x,y):
#     plt.plot(x,y,marker = 'o')
#     plt.xlabel('Distance in metres')
#     plt.ylabel('Gravitational force in newtons')
#     plt.title('Gravitational force and distanve')
#     plt.show()

# def generate_F_r():
#     # generate values for r
#     r = range(100,1001,50)
#     # empty list to calculate the values of F
#     F = []
#     # constant G
#     G = 6.674*(10**-11)
#     # two mases
#     m1 = 0.5
#     m2 = 1.5

#     # calculate force and to the the list F
#     for dist in r:
#         force = G*(m1*m2)/(dist**2)
#         F.append(force)
#     # call the draw_graph function
#     draw_graph(r,F)
# if __name__ == '__main__':
#     generate_F_r

# drawing the trajectory
'''draw the trejectory which is in the motion'''
import matplotlib.pyplot as plt
import math
def frange(start,final,interval):
    numbers = []
    while start<final:
        numbers.append(start)
        start = start + interval
    return numbers
def draw_trajectory(u,theta):
    theta = math.radians(theta)
    g = 9.8

    # time of flight
    t_flight = 2*u*math.sin(theta)/g
    # find the time intervals
    intervals = frange(0,t_flight,0.001)
def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel('x coordinate')
    plt.ylabel('y coordinate')
    plt.title('projectile motion of ball')

    # list of x and y
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    draw_graph(x,y)

if __name__ == '__main__':
    try:
        u = float(input('enter the velocity in the (m/s): '))
        theta = float(input('enter the angle of projection(degrees): '))
    except valuerror:
        print('you entered and invalid input')
    else:
        draw_trajectory(u,theta)
        plt.show()