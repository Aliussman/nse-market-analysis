import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/nifty50.csv")

sector_counts = df["Sector"].value_counts()

print(sector_counts)

sector_counts.plot(kind="bar")

plt.title("Sector Distribution of NIFTY 50 Companies")
plt.xlabel("Sector")
plt.ylabel("Number of Companies")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("visuals/sector_distribution.png")

plt.show()
