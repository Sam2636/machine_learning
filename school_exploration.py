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
#plt.show()


#------------->missing value
print(df.isna().sum())  #to check the missing values #isna() return boolen values


#filling the missing values
from sklearn.impute import SimpleImputer
#how to treat missing values
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')

print(df['state_percentile_15'].isna().sum())

mean_imputer=mean_imputer.fit(df['state_percentile_15'].values.reshape(-1,1))
df3=mean_imputer.transform(df['state_percentile_15'].values.reshape(-1,1))
print(df3)

#needs to treat a outlier 