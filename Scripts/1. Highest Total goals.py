#Highest total goals
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Home team goals
df=pd.read_excel(Data/'Mock_data.xlsx.xls')
Home_goals=df.groupby('home_team')['goals_home'].sum()
Home_goals=Home_goals.reset_index()
Home_goals.columns=['team','goals']

#away team goals
away_goals=df.groupby('away_team')['goals_away'].sum()
away_goals=away_goals.reset_index()
away_goals.columns=['team','goals']

#concat
all_goals=pd.concat([Home_goals,away_goals])
team_goals=all_goals.groupby('team')['goals'].sum()
team_goals=team_goals.reset_index()
highest_goals=team_goals.sort_values(by='goals',ascending=False)
top10=highest_goals.head(10)
print(top10)

#create figure
plt.figure(figsize=(12,6))
plt.bar(top10['team'],top10['goals'])
plt.title('Top 10 teams by their goals')
plt.xlabel('Teams')
plt.ylabel('Goals')
plt.xticks(rotation = 45)
plt.show()

