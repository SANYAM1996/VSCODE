# plotting cube by list and for loops
import matplotlib.pyplot as plt
import seaborn as sns
x_values = list(range(1,5000001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,edgecolors='none',c=y_values,cmap=plt.cm.Reds)
plt.xlabel('numbers in range')
plt.ylabel('cubes')
plt.grid()
plt.show()

# random walk problem
from random import choice
class randomwalk():
    ''' a class to generate random walks
    this class needs 3 attributes 1 for store the numbers in the walk other 2 are for making list to store the x and y coordinate '''
    def __init__(self,num_points = 5000):
        '''initialize attribute to the class'''
        self.num_points = num_points
        # all walk starts from (0,0)
        self.x_values = [0]
        self.y_values = [0]
        # i am using fill_walk function for determining the steps
    def fill_walk(self):
        '''calculate all the points in the walk'''
        # keep taking steps untill the steps reaches to the desired numbers.
        while len(self.x_values)<self.num_points:
            # decide which direction to go and how far by the coordinate
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction*x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction*y_distance
            # rejects move which go nowhere
            if x_step == 0 and y_step == 0:
                continue
            # calculate the next step
            next_x = self.x_values[-1]+x_step
            next_y = self.y_values[-1]+y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)





