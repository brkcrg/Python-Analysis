import pandas as pd
import seaborn as sns
import matplotlib as plt
df = pd.read_csv('C:/Python/temel/corelation/sporverisi.csv')
korelasyon = df.corr()
# print(korelasyon)

# print(type(korelasyon))

# print(korelasyon["Sure"]["Nabiz"])

sns.heatmap(korelasyon, annot=True)

plt.show()
