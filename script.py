import codecademylib3_seaborn
import matplotlib from pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')


df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())
sns.set_style('whitegrid')
sns.set_context('poster',font_scale=0.8)
f, ax = plt.subplots(figsize=(12,7))
ax = sns.barplot(df,x='Year',y='Total Goals')
ax.set_title('Average goals per year in World Cup')
df_goals = pd.read.csv('goals.csv')
sns.set_context('notebook',font_scale = 1.25)
f,ax2=plt.subplots(figsize=(12,7))
ax2= sns.boxplot(data = df_goals,x='Year',y='Goals',palette = 'Spectral')
ax2.set_title('Goals scored every year')
plt.show()






