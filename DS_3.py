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
