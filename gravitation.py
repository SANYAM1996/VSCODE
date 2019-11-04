'''plotting the graph for gravitational body
F = Gm1*m2/r**2
lets taking m1 = 0.5 kg
m2 = 1.5kg
value of G is 6.674*10 raise to the power -11 nm**2'''
# the relation between gravitational force and distance between two bodies

import matplotlib.pyplot as plt
def draw_graph(x,y):
    plt.plot(x,y,marker = 'o')
    plt.xlabel('Distance in metres')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distanve')
    plt.show()

def generate_F_r():
    # generate values for r
    r = range(100,1001,50)
    # empty list to calculate the values of F
    F = []
    # constant G
    G = 6.674*(10**-11)
    # two mases
    m1 = 0.5
    m2 = 1.5

    # calculate force and to the the list F
    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)
    # call the draw_graph function
    draw_graph(r,F)
if __name__ == '__main__':
    generate_F_r