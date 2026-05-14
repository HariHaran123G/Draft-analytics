# Attendence vs home team performance
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('Data/MOCK_DATA.xlsx.xls')
df['Performance_score']=((df['goals_home']*5)+(df['possession_home'])+(df['shots_home']*2)+(df['passes_home']/50)-(df['red_cards_home']*5))

df['crowd_type']=np.where(df['attendance']<30000, 'Low crowd', np.where(df['attendance']<=60000,'Medium crowd','Massive crowd'))

#display sample data
print(df[['attendance','crowd_type','Performance_score']].head())
crowd_analysis=df.groupby('crowd_type')['Performance_score'].mean()  
crowd_analysis=crowd_analysis.reset_index()
print("\n Average performance by the crowd type:\n")
print(crowd_analysis)

#correlation
correlation=df[['attendance','Performance_score']].corr()
print("\n Correlation Matrix:")
print(correlation)

#scatter plot
plt.figure(figsize=(12,6))
plt.scatter(df['attendance'],df['Performance_score'])
plt.title('Attendance and Home team performance')
plt.xlabel('Attendance')
plt.ylabel('Performance score')
plt.show()
                              
