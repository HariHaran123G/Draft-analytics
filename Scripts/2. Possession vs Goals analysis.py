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
home_result = np.where(
    df['winner'] == df['home_team'],
    'Win',
    'Loss'
)

# Home Possession Table
home_possession = pd.DataFrame({
    'team': df['home_team'],
    'possession': df['possession_home'],
    'result': home_result
})

# Away Team Result

away_result = np.where(
    df['winner'] == df['away_team'],
    'Win',
    'Loss'
)

# Away Possession Table
away_possession = pd.DataFrame({
    'team': df['away_team'],
    'possession': df['possession_away'],
    'result': away_result
})

# Combine Both Tables
combined = pd.concat(
    [home_possession, away_possession]
)

# Average Possession By Result
avg_possession = combined.groupby(
    'result'
)['possession'].mean()

# Convert To DataFrame

avg_possession = avg_possession.reset_index()

# Display Results
print(avg_possession)

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(
    avg_possession['result'],
    avg_possession['possession']
)
plt.title(
    'Average Possession: Winners vs Losers'
)
plt.xlabel('Match Result')
plt.ylabel('Average Possession %')
plt.show()
