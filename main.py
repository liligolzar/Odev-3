import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris=pd.read_csv("C:\\Users\\Lili\\Desktop\\pythonProjectiris\\iris.csv")
iris.head()

iris.describe()
iris.info
print(iris.groupby('species').size())
sns.pairplot(data=iris,hue='species')
sns.heatmap(iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_length','petal_width']].corr(), annot=True)

sns.boxplot(x='species', y='petal_length', data=iris)
plt.figure(figsize=(8,8))
sns.boxplot(data=iris, x = 'species',y = 'petal_length')
sns.stripplot(data=iris, x='species', y='petal_length', jitter=True, edgecolor='green')
sns.boxenplot(data=iris,palette='rainbow')
plt.show()






