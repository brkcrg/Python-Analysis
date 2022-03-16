import pandas as pd
df = pd.read_csv('C:/Python/temel/corelation/BTC-USD.csv')
metin = df.to_string()
# print(metin)

liste = [0, 3, 4, 7, 8]
for i in liste:
    print(i, df["date"][i])

print(len(liste))
