
# def fun():
#     list1 = 20,30,40,50,12,13,14
#     list2 = 10,9,8,7,6,5,4
#     return(list1,list2)
# obj = fun()
# print(obj)
# # plotting graph between list1 and list2
# import matplotlib.pyplot as plt
# # plt.plot(obj)
# # plt.xlabel ('list1')
# # plt.ylabel ('list2')
# # plt.legend()
# # plt.grid()
# # plt.show()
# # fitting a best regression line by np.polyfit()
# import numpy as np
# # a, b = np.polyfit(obj, 1,1)
# # # Print the results to the screen
# # print('slope =', a)
# # print('intercept =', b)
# # # Add regression line to  plot
# # plt.plot(x, y)
# # plt.show()

# # visualizing bootstrap samples
# for i in range(50):
#     # generate bootstrap sample
#     bs_sample = np.random.choice(obj,size = len(obj))
#     # compute and plot ECDF from bootstrap sample
#     x,y = ecdf(bs_sample)
#     i = plt.plot(x,y,marker = '.',linestyle = 'none',color = 'gray',alpha = 0.1)
# # compute and plot ecdf from original data
# x,y = ecdf(obj)
# i = plt.plot(x,y,marker = '.')
# # make margins and label axes
# plt.margins(0.02)
# i = plt.xlabel('objlist1points')
# i = plt.ylabel('ECDF')
# plt.show()

# applying permutation on list data by function
import numpy as np
import matplotlib.pyplot as plt
def permutation_sample(list1, list2):
    self.listx = [1,2,3,4,5,6,7,8,9,10]
    self.listy = [10,9,8,7,6,5,4,3,2,1]
    
    """Generate a permutation sample from two data sets."""

    # Concatenate the data sets: data
    data = np.concatenate((listx, listy))

    # Permute the concatenated array: permuted_data
    permuted_data = np.random.permutation(data)

    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[:len(listx)]
    perm_sample_2 = permuted_data[len(listx):]

    return perm_sample_1, perm_sample_2
# visualizing permutation sampling
for _ in range(50):
    # generate permutation samples
    perm_sample_1,perm_sample_2 = permutation_sample(listx,listy)
    # compute ECDF
    x_1, y_1 = ecdf(perm_sample_1)
    x_2, y_2 = ecdf(perm_sample_2)
    #  plot ecdf
    _ = plt.plot(x_1,y_1,marker = ".",linestyle = 'None',color = 'red',alpha = 0.2)
    _ = plt.plot(x_2,y_2,marker = ".",linestyle = 'None',color = 'red',alpha = 0.2)
    plt.show()

