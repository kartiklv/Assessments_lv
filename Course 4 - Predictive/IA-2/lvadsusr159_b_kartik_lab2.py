# -*- coding: utf-8 -*-
"""lvadsusr159_b_kartik_lab2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bV-S44SStBhsRmfRILqofSreKkanNx1G
"""

from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder

mall_df = pd.read_csv('/content/Mall_Customers.csv')

mall_df.info()

mall_df.head(5)

mall_df.isnull().sum()

mall_df = mall_df.bfill(axis='columns')
mall_df.isnull().sum()

import matplotlib.pyplot as plt

plt.boxplot(mall_df['Age'])

plt.boxplot(mall_df['Annual Income (k$)'])

mall_df = mall_df[mall_df['Annual Income (k$)']<130]

lbl = LabelEncoder()

km = KMeans(n_clusters=3)
mall_df['Gender'] = lbl.fit_transform(mall_df['Gender'])
y_predicted = km.fit_predict(mall_df[['Gender','Age','Annual Income (k$)','Spending Score (1-100)']])

mall_df['cluster']=y_predicted
print(mall_df.head())

print(km.cluster_centers_)

df1 = mall_df[mall_df.cluster==0]
df2 = mall_df[mall_df.cluster==1]
df3 = mall_df[mall_df.cluster==2]
plt.scatter(df1.Age,df1['Spending Score (1-100)'],color='green')
plt.scatter(df2.Age,df2['Spending Score (1-100)'],color='red')
plt.scatter(df3.Age,df3['Spending Score (1-100)'],color='black')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Age')
plt.ylabel('Spending Score (1-100)')
plt.legend()

scaler = MinMaxScaler()
scaler.fit(mall_df[['Spending Score (1-100)']])
mall_df['Spending Score (1-100)'] = scaler.transform(mall_df[['Spending Score (1-100)']])
scaler.fit(mall_df[['Age']])
mall_df['Age'] = scaler.transform(mall_df[['Age']])
print(mall_df.head())
plt.scatter(mall_df.Age,mall_df['Spending Score (1-100)'])

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(mall_df[['Age','Spending Score (1-100)']])
mall_df['cluster']=y_predicted
mall_df.head(25)
print(km.cluster_centers_)

sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(mall_df[['Age','Spending Score (1-100)']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)