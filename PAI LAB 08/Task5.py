import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", keep_default_na=False)
d = df[df["scenario"] == "05_AdVsRevenue"].copy()
d["study_hours"] = pd.to_numeric(d["study_hours"])
d["exam_score"] = pd.to_numeric(d["exam_score"])

sns.regplot(data=d, x="study_hours", y="exam_score", color="darkgreen", marker="+")
plt.title("Impact of Advertising Spend on Total Revenue")
plt.xlabel("Ad Spend ($)")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.show()