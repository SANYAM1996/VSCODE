
def fun():
    list1 = 20,30,40,50,12,13,14
    list2 = 10,9,8,7,6,5,4
    return(list1,list2)
obj = fun()
print(obj)
# plotting graph between list1 and list2
import matplotlib.pyplot as plt
plt.plot(obj)
plt.xlabel ('list1')
plt.ylabel ('list2')
plt.legend()
plt.grid()
plt.show()
# fitting a best regression line by np.polyfit()
import numpy as np
a, b = np.polyfit(obj, 1,1)
# Print the results to the screen
print('slope =', a)
print('intercept =', b)
# Add regression line to  plot
plt.plot(x, y)
plt.show()

