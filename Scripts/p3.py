# Which Home team plays the most aggressive style of football
# Defined using: Fouls, yellow and red cards
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('data/MOCK_DATA.xlsx.xls')

# home team stats
team_aggression = df.groupby('home_team')[['fouls_home','yellow_cards_home','red_cards_home']].sum()
team_aggression = team_aggression.reset_index()

#aggression score
team_aggression['aggression_score']=(team_aggression['fouls_home']+(team_aggression['yellow_cards_home']*2)+(team_aggression['red_cards_home']*5))

#sort highest
most_aggressive=team_aggression.sort_values(by='aggression_score',ascending=False)

top10=most_aggressive.head(10)
print(top10)

# Charts
plt.figure(figsize=(12,6))
plt.bar(top10['home_team'],top10['aggression_score'])
plt.title('Most aggressive home teams')
plt.xlabel('Teams')
plt.ylabel('Aggression_score')
plt.xticks(rotation=45)
plt.show()
