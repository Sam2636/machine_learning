import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df=pd.read_csv("./dataset/middle_tn_schools.csv",delimiter=',')


#data exploring---------------------->using heatmap sns.heatmap(data,square=True,cmap="bwr")
data=df.corr()
sns.heatmap(data,square=True,annot=True,cmap="bwr")
plt.yticks(rotation=0)
plt.xticks(rotation=90)
#plt.show()   #to show the heatmap

#data ifo and describe()
print(df.head())
print(df.tail())
print(df.info())
print(df.describe().round(2))
print(df['name'].values)
print(df['name'].dtypes)
print(df.shape)

#to check the corellation of reduced_lunch and school_ratinngs
data2=df[['reduced_lunch','school_rating']]
school_data=data2.corr()
sns.heatmap(school_data,square=True,annot=True,cmap="bwr")
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()