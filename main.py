#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#%%
dataset = pd.read_csv('data/titanic.csv')
#%%
print(dataset)
#%%
dataset.info()
#%%
dataset.isna().sum()
#%%
dataset.dropna(how='all', inplace=True)
#%%
dataset['Pclass'] = dataset['Pclass'].astype('float')
#%%
dataset.info()
#%%
dataset['Pclass'] = dataset['Pclass'].astype('int')
#%%
dataset.info()
#%%
dataset['Sex'].replace({'male':0,'female':1},inplace=True)
#%%
plt.figure(figsize=(8,8))
sns.countplot(x=dataset['Survived'],hue=dataset['Sex'])
#%%
plt.figure(figsize=(8,8))
sns.countplot(x=dataset['Survived'],hue=dataset['Pclass'])
#%%
dataset.Age.mean()
#%%
dataset.Age.median()
#%%
dataset.Age.isna().sum()
#%%
from sklearn.impute import SimpleImputer
#%%
imp = SimpleImputer(strategy='median',)
dataset.Age = imp.fit_transform(dataset.Age.values.reshape(-1,1))
#%%
dataset.Age.isna().sum()
#%%
dataset.Embarked.fillna('S', inplace=True)
#%%
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dataset.Embarked = le.fit_transform(dataset.Embarked)
dataset
#%%
dataset.Embarked.value_counts()
#%%
print(dataset.Name)
#%%
plt.figure(figsize=(15,8))
sns.heatmap(dataset.corr(),annot = True)
#%%
dataset.Name = dataset.Name.apply(lambda x: x.split(', ')[-1].split('. ')[0])
#%%
print(dataset)
#%%
dataset.rename(columns={'Name':'Title'}, inplace=True)
#%%
print(dataset)
#%%
dataset.Title.value_counts()
#%%
keep_ls = ['Mr','Miss','Mrs']
for row in range(len(dataset.Title)):
    if dataset.loc[row,'Title'] not in keep_ls:
        dataset.loc[row,'Title'] = 'Other'
#%%
print(dataset)
#%%
dataset.Title.value_counts()
#%%
dataset.Title = le.fit_transform(dataset.Title)
print(dataset)
#%%
dataset.Title.value_counts()
#%%
dataset.drop(['Ticket','Cabin'], axis=1, inplace=True)
#%%
plt.figure(figsize=(20,20))
plt.subplot(2,2,1)
sns.distplot(dataset.Age)
plt.subplot(2,2,2)
sns.distplot(dataset.Fare)
#%%
plt.figure(figsize=(20,8))
sns.boxplot(dataset.Fare)
#%%
dataset.Fare.max()
#%%
dataset.Fare.min()
#%%
plt.figure(figsize=(20,10))
sns.heatmap(dataset.corr(), annot=True)
plt.show()
#%%
q1 = np.quantile(dataset.Fare,0.25)
q3 = np.quantile(dataset.Fare, 0.75)
q2 = np.quantile(dataset.Fare,0.5)
iqr = q3-q1
# iqr
#%%
lower = q1-1.5*iqr
upper = q3+1.5*iqr
#%%
# lower,upper
#%%
# dataset
#%% md
####
# Machine Learning
###