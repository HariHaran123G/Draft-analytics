#Possession vs Goals analysis
#Average possession winners vs losers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_excel(Data/'MOCK_DATA.xlsx.xls')
df['possession_away']=(100-df['possession_home'])

home_stats=df['home_team','possession_home','goals_home']
home_stats.columns=['team','possession','goals']
away_stats=df['away_team','possession_away','goals_away']
away_stats.columns=['team','possession','goals']
all_stats=pd.concat([home_stats,away_stats])
print(all_stats.head())

plt.figure(figsize=(10,6))
plt.scatter(all_stats['possession'],all_stats['goals'])
plt.title('Possession vs goals')
plt.xlabel('possession %')
plt.ylabel('Goals scored')
plt.show()

# Winners vs losers possessions
