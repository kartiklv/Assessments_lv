# -*- coding: utf-8 -*-
"""lvadsusr159_b_kartik_lab4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nNCfCIlAp4gJ5nI4oE_2IqqfALAmbtrj
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("/content/anomaly_train.csv")

df.head()

# Select the features to be used for anomaly detection
features = ["Amount", "Time", "User"]

# Create a new dataframe with the selected features
X = df[features]

# Fit an Isolation Forest model to the data
model = IsolationForest(n_estimators=100, contamination=0.1)
model.fit(X)

# Predict the anomalies in the data
y_pred = model.predict(X)

y_pred

# Add the predicted anomaly scores to the original dataframe
df["anomaly_score"] = model.decision_function(X)

df.head(3)

anomalies = df.loc[df["anomaly_score"] < 0]

anomalies

df_test= pd.read_csv("/content/anomaly_train.csv")
x=df_test[["Amount", "Time", "User"]]
df_values=x.values

find=df_values
result=[]
for i in find:
  z=model.predict([i])
  if z==[1]:
    result.append('no')
  elif z==[-1]:
    result.append('yes')

df_test['Anomaly']=result

plt.scatter(df["Amount"], df["anomaly_score"], label="Normal")
plt.scatter(anomalies["Amount"], anomalies["anomaly_score"], color="r", label="Anomaly")
plt.xlabel("Amount")
plt.ylabel("anomaly_score")
plt.legend()
plt.show()

print("************************************************************************************")
print("")
df_test.head()