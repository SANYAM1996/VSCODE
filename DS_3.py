import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.DataFrame(np.arange(0,20).reshape(5,4),index=['row1','row2','row3','row4','row5'],columns = ['col1','col2','col3','col4'])
df.head()

def plotpoint(col2):
    total = df[df["col1"]==col2].groupby(["col1"],as_index=False).agg({"col2": "col3"})
    total=total.sort_values("col1",ascending=True)
    ax=total.plot('col1', 'col3', kind='bar', figsize=(17,5), color='red', zorder=2, width=0.85)
    ax.set_xlabel("col1", labelpad=20, size=12)
    ax.set_ylabel("row", labelpad=20, size=12)
    ax.set_title('graph between row and column' +str(col1))
plotpoint(19)

prices = [12,13,12,23,33,21,45,50]
prices_N = [11,22,33,44,55,66,77,88]
plt.hist(x=prices,bins = 6,density=1,alpha = 0.5,label='prices')
plt.hist(x = prices_N,bins = 6,density=1,alpha = 0.5,label='prices_N')
plt.legend()
plt.savefig('layering hist.png')
plt.show()

# tuple decomposition
# we can assign the value of different variable by this function 
def func():
    return 1,2,3,4
t1 = (1,2)
t2 = (3,4,1)
x,y = t1
y,z,p = t2
print(x,y)
print(y,z,p)
# here i can get a tuple
print(func())

# Python program to concatenate 
# dataframes using Panda 
  
# Creating first dataframe 
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3'], 
                    'C': ['C0', 'C1', 'C2', 'C3'], 
                    'D': ['D0', 'D1', 'D2', 'D3']}, 
                    index = [0, 1, 2, 3]) 
  
# Creating second dataframe 
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'], 
                    'B': ['B4', 'B5', 'B6', 'B7'], 
                    'C': ['C4', 'C5', 'C6', 'C7'], 
                    'D': ['D4', 'D5', 'D6', 'D7']}, 
                    index = [4, 5, 6, 7]) 
  
# Creating third dataframe 
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'], 
                    'B': ['B8', 'B9', 'B10', 'B11'], 
                    'C': ['C8', 'C9', 'C10', 'C11'], 
                    'D': ['D8', 'D9', 'D10', 'D11']}, 
                    index = [8, 9, 10, 11]) 
  
# Concatenating the dataframes 
pd.concat([df1, df2, df3])

# Python program to merge 
# dataframes using Panda 
  
# Dataframe created 
left = pd.DataFrame({'Key': ['K0', 'K1', 'K2', 'K3'], 
                    'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3']}) 
  
right = pd.DataFrame({'Key': ['K0', 'K1', 'K2', 'K3'], 
                      'C': ['C0', 'C1', 'C2', 'C3'], 
                      'D': ['D0', 'D1', 'D2', 'D3']}) 
                        
# Merging the dataframes                       
pd.merge(left, right, how ='inner', on ='Key') 