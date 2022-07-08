import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("./dataset/SalaryGender.csv",delimiter=',')

data=df.corr()
sns.heatmap(data,square=True,                           cmap="bwr")
plt.yticks(rotation=0)
plt.xticks(rotation=90)
#plt.show()
#data exploring--------------    -------->
#print(df)
print(df.head())
print(df.info())
print(df.describe().round(2))   #describe() is used to get the statistical information of the dataframe
salary=np.array(df['Salary'])

gender=np.array(df['Gender'])  #type casting 
phd=np.array(df['PhD'])
age=np.array(df['Age'])

age1=df['Age'].values   #prefferd way of doing
age2=df['Age'].dtype  #prefferd way of doing
print(type(age1))
print(age2)

#to check no of rows and cloumns
print(df.shape)

#to fetch the multiple columns
df_fetch=df[['Salary','Age']]   #provide list of the column names

print(df_fetch)

#fetching a row 
fetch_row1=df.loc[0:10]  #loc gives 0 to 10 rows
fetch_row2=df.iloc[0:10,0:2]  #iloc gives ddta 0 to 9 rows   i represents indxed location
print(fetch_row2)


#filling the missing values
from sklearn.impute import SimpleImputer
#how to treat missing values
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')

print(df['Age'].isna().sum())

''' impute_data=mean_imputer.fit(df.values)
df3=pd.DataFrame(data=impute_data,columns=cols)
print(df3) '''

#needs to treat a outlier 