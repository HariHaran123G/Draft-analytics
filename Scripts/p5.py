# Possession efficiency analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('Data/MOCK_Data.xlsx.xls')
team_analysis =df.groupby('home_team')[['goals_home','possession_home']].mean()
team_analysis = team_analysis.reset_index()

team_analysis['Efficiency_score']=(team_analysis['goals_home']/team_analysis['possession_home'])
efficient_teams=team_analysis.sort_values(by='Efficiency_score',ascending=false)
top10=efficient_teams.head(10)
print(top10)

plt.figure(figsize=(12,6))
plt.bar(top10['home_team'],top10['Efficiency_score']
plt.title('Top Teams by Possession Efficiency')
plt.xlabel('Teams')
plt.ylabel('Efficiency Score')
plt.xticks(rotation=45)
plt.show()       
