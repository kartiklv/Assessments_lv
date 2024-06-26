# -*- coding: utf-8 -*-
"""lvadsusr159_b_kartik LAB1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pjJYjgBili-J_hYdVW9775udxdRv1ABK

#LAB SECTION 1- LINEAR REGRESSION
"""

import pandas as pd

main_df = pd.read_csv("/content/expenses.csv")
main_df.info()

main_df.describe()

#1.
nulls = main_df.isnull().sum()
print(nulls)

#Outliers detection
import seaborn as sns
bmi_outliers = sns.boxplot(main_df['bmi'])

age_outliers = sns.boxplot(main_df['age'])

children_outliers = sns.boxplot(main_df['children'])

charges_outliers = sns.boxplot(main_df['charges'])
print(main_df[main_df['charges']>40000].count())

def remove_outliers(A, threshold):
  return main_df[A<threshold]

main_df = remove_outliers(main_df['charges'],40000)
main_df = remove_outliers(main_df['bmi'],45)
main_df.count()

main_df.info()

# 2.
from sklearn.preprocessing import LabelEncoder

lbl_enc = LabelEncoder()
main_df['sex'] = lbl_enc.fit_transform(main_df['sex'])
main_df['smoker'] = lbl_enc.fit_transform(main_df['smoker'])
main_df['region'] = lbl_enc.fit_transform(main_df['region'])

main_df.head()

# 3.
duplicates = main_df.duplicated(keep=False)
main_df['dup_bool'] = duplicates
main_df[main_df['dup_bool'] == True].count()

main_df = main_df[main_df['dup_bool'] == False]
main_df = main_df.drop('dup_bool',axis=1)

sns.pairplot(main_df)

"""#OBSERVATION: We can see that Age, number of children and region has strong impact on the Insurance costs"""

# 4.

from sklearn.model_selection import train_test_split

X = main_df.drop('charges',axis=1)
y = main_df['charges']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=30)

# 5.
from sklearn.linear_model import LinearRegression

model = LinearRegression()

trained_model = model.fit(X_train,y_train)

y_pred = trained_model.predict(X_test)

# 6
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

mse = mean_squared_error(y_test,y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,y_pred)

print('MSE: ',mse)
print('RMSE: ',rmse)
print('R-Squared: ',r2)