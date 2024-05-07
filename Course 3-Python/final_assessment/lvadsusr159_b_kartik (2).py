# -*- coding: utf-8 -*-
"""LVADSUSR159_b.kartik

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sUoku05X1I1YJlP1zuUvqRYd6t_cS238
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as st
import seaborn as sns

#1a
ipl_data=pd.read_csv("/content/sample_data/Final Dataset - IPL.csv")
ipl_data

#1b
ipl_data.dtypes

#1b
ipl_data.describe()

#2a
ipl_data.isnull().sum()

#while checking for missing or null values we couldn't find any null values so the dataset is cleaned.

#2b
# There are no duplicate values in the dataset.

#3

print("Average first innings score: ",ipl_data['first_ings_score'].mean())
print("\n\nMost players scored runs:\n ",ipl_data['highscore'].mode().head(1))
print("\n\nStandard deviation of first inning wickets",ipl_data['first_ings_wkts'].std())

#3
from matplotlib import pyplot as plt
_df_9['first_ings_score'].plot(kind='line', figsize=(8, 4), title='first_ings_score')
plt.gca().spines[['top', 'right']].set_visible(False)

#4

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['won_by'].value_counts()
    for x_label, grp in ipl_data.groupby('toss_decision')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('toss_decision')
_ = plt.ylabel('won_by')


##
# We can see that the toss decisions for fielding have yeilded more runs and those teams have won.

#4

from matplotlib import pyplot as plt
import seaborn as sns
ipl_data.groupby('venue').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

# Most number of matches were played in Wankhede stadium which indicates the popularity of the sport. It is an interesting data point.

#5
from matplotlib import pyplot as plt
import seaborn as sns
ipl_data.groupby('toss_decision').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

# We can see that toss decisions have been in the favor of bowling throughout the tournament

#5

from matplotlib import pyplot as plt
ipl_data['first_ings_score'].plot(kind='hist', bins=20, title='first_ings_score')
plt.gca().spines[['top', 'right',]].set_visible(False)

##
#the first inning scores of majority of teams have been around 150-160 runs

#6

plt.boxplot(ipl_data[['first_ings_score','second_ings_score',]], labels = ['1st inings','2nd inings'])



Q1 = ipl_data['second_ings_score'].quantile(0.25)
Q3 = ipl_data['second_ings_score'].quantile(0.75)

IQR = Q3-Q1

lower_bound = ipl_data["second_ings_score"]-IQR*1.5
upper_bound = ipl_data["second_ings_score"]+IQR*1.5

df = ipl_data[ (ipl_data['second_ings_score']>lower_bound) | (ipl_data['second_ings_score']<upper_bound)] #Filtering the outlier

df


# I took the data of first and second innings and tried to find anomallies.
# We can see that there are more outliers in the second inings score and we have successfuly removed them.

#7
# @title venue vs stage

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['stage'].value_counts()
    for x_label, grp in ipl_data.groupby('venue')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('venue')
_ = plt.ylabel('stage')

# We can see that most of the stage matches were played in Mumbai stadiums.

#8
df=ipl_data.groupby('player_of_the_match').agg({'player_of_the_match':'count'})
df

from matplotlib import pyplot as plt
df['player_of_the_match'].plot(kind='line', figsize=(8, 4), title='player_of_the_match')
plt.gca().spines[['top', 'right']].set_visible(False)

# from the above charts we can observe that Kuldeep Yadav has the most number of player of the match awards

#9

# From the above charts we can observe that Kuldeep Yadav has the most number of player of the match awards.
# We can see that most of the stage matches were played in Mumbai stadiums.
# The first inning scores of majority of teams have been around 150-160 runs.
# We can see that toss decisions have been in the favor of bowling throughout the tournament.
# Most number of matches were played in Wankhede stadium which indicates the popularity of the sport. It is an interesting data point.
# We can see that the toss decisions for fielding have yeilded more runs and those teams have won.




# Few more findings:
# In most matches the number of wickets taken in the first innings is 6
#

from matplotlib import pyplot as plt
ipl_data['first_ings_wkts'].plot(kind='hist', bins=20, title='first_ings_wkts')
plt.gca().spines[['top', 'right',]].set_visible(False)

from matplotlib import pyplot as plt
import seaborn as sns
figsize = (12, 1.2 * len(ipl_data['won_by'].unique()))
plt.figure(figsize=figsize)
sns.violinplot(ipl_data, x='match_id', y='won_by', inner='stick', palette='Dark2')
sns.despine(top=True, right=True, bottom=True, left=True)

# We can see that the teams have displayed excellent bowling and batting skills, as the matches won by wickets
# and won by runs are very close.
#
# Also from the below graph we can strategically say that the slight win ratio from matches won by wickets is more
# because teh teams undergo a lot of pressure while chasing a big run total.
#