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