from tkinter import Y
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("./dataset/Titanic.csv",delimiter=',')
print(df.tail())

new_ages=[]

#check which has nan values
print(df.isna().sum())
df2=df.copy()
df3=df.copy()
print(df2['Age'])
#grouping the data with respect to age
pclass_age_mean=df.groupby(by='Pclass').mean()['Age']
#print(pclass_age_mean)


new_age=df['Age'].values

for k,age in enumerate(df['Age'].values):
    #print(np.isnan(age))        #returns true or false
    if np.isnan(age):
        
        if df['Pclass'].iloc[k]==1:
            new_age[k]=pclass_age_mean[1]
            #print('--1--',new_age[k])
        elif df['Pclass'].iloc[k]==2:
            new_age[k]=pclass_age_mean[2]
            #print('-->--22',new_age[k])
        else:
            new_age[k]=pclass_age_mean[3]
            #print("-->--3",new_age[k])
                
            #print(df['Pclass'].iloc[k], age)

#print(new_age)            


#Best and preffferd way to fill the missing values

def age_imputer(cols):
    age=cols[0]
    pclass=cols[1] 
    if np.isnan(age):    
        if pclass==1:
            return pclass_age_mean[1]
        elif pclass==2:
            return pclass_age_mean[2]          
        else:
            return pclass_age_mean[3]
    else:
        return age   

df2['Age']=df2[['Age','Pclass']].apply(age_imputer,axis=1)
# print(df2[['Age','Pclass']].apply(age_imputer,axis=1))    
    
# print(df2.isna().sum())





#OUTLIER TREATMENT
print(df2.describe().round(2))

#quantile plot
q1=df2['Age'].quantile(0.25)
q3=df2['Age'].quantile(0.75)
IQR=q3-q1
print(q3-q1)

#uper and lower bound
upperbound=q3+1.5*IQR
lowerbound=q1-1.5*IQR
print(lowerbound,upperbound)

#check outiler above and below outliers

Above_upperbound=df2['Age']>upperbound
print('above',sum(Above_upperbound))
below_lowerbound=df2['Age']<lowerbound
print('below',sum(below_lowerbound))


#displot
# sns.displot(df2['Age'],kde=True)
# # plt.show()


#to remove outliers

# def remove_outliers(age):
#     if age> upperbound:
#         return upperbound
#     elif age< lowerbound:
#         return lowerbound
#     else:
#         return age
#this fuction only affec t the age column

# data=df2['Age'].apply(remove_outliers)
# sns.displot(data,kde=True)
# #plt.show()

# sns.boxplot(x=df2['Age'])
# #plt.show() #ser


#effective way to remove outliers in the every column

#we need a funtion to scale the data
#1.every thing has to be done in the same fuction
# for col in df2.columns:
#     print(col)
#     q1=df2[col].quantile(0.25)
#     q3=df2[col].quantile(0.75)
#     IQR=q3-q1
#     print(q3-q1)

#     #uper and lower bound
#     upperbound=q3+1.5*IQR
#     lowerbound=q1-1.5*IQR
#     print(lowerbound,upperbound)
#     df2[col] =remove_outliers(col)


# strategy2
#displot



#step1:
age_min=df3['Age'].min()
age_max=df3['Age'].max()

age_mean=df3['Age'].mean()
age_std=df3['Age'].std()

sns.displot(df3['Age'],kde=True)

plt.axvline(x=age_mean,ymin=age_min,ymax=age_max,color='red',lw=3,label='mean age')
plt.axvline(x=age_mean+2*(age_std),ymin=age_min,ymax=age_max,color='m',lw=3,label='mean age + 2*std')
plt.axvline(x=age_mean+3*(age_std),ymin=age_min,ymax=age_max,color='b',lw=3,label='mean age + 3*std')
plt.legend()
plt.show()