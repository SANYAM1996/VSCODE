# Write functions for the following tasks

# 1. function to read and print head of train.csv

# 2. function to read and print column names from train.csv

# 3. function to read and print data shape from train.csv


from os.path import dirname, join
current_dir = dirname('train.csv')
file_path = join(current_dir,"train.csv")

import csv
with open('train.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
# it is showing unicode error and working directory problem while running in vs code but perfectly running in jupyter notebook.
# 0 is the index of column name of train.csv
path = 'train.csv'
lines = [line for line in open(path)]
print(lines[0])
print(lines[1])

# plotting graph with function
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('train.csv')
def plot_yearly_count(Embarked):
    data_agg=df[df["Survived"]==Embarked].groupby(["Age"],as_index=False).agg({"Fare": "sum"})
    if len(data_agg)==1:
        print("No data available")
    else:
        year_df=pd.DataFrame()
        year_df["Age"]=df["Age"].unique()
        data_agg["key"]=0
        data_agg=pd.merge(year_df,data_agg,on=["Age"],how="left")
        data_agg=data_agg.sort_values("Age",ascending=True)
        ax=data_agg.plot('Age', 'Fare', kind='bar', figsize=(17,5), color='#86bf91', zorder=2, width=0.85)
        # Switch off ticks
        ax.tick_params(axis="both", which="both", bottom=False, top=False, labelbottom=True, left=False, right=False, labelleft=True)
        # Set x-axis label
        ax.set_xlabel("Age", labelpad=20, size=12)
        # Set y-axis label
        ax.set_ylabel("count of people", labelpad=20, size=12)
        # Set title
        ax.set_title('graph between age and count' +str(Embarked)+" in the past 20 years")
        ax.legend_.remove()
    plot_yearly_count('s')


 

