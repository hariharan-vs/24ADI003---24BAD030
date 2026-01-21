import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Housing.csv")

print(df.isnull().sum())

plt.scatter(df["area"], df["price"])
plt.show()

sns.heatmap(df.corr(), annot=True)
plt.show()
