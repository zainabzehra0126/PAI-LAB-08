import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", keep_default_na=False)
d = df[df["scenario"] == "03_SalaryDiff"].copy()
d["exam_score"] = pd.to_numeric(d["exam_score"])

sns.boxplot(data=d, x="prep_course", y="exam_score", order=["Entry", "Mid", "Senior"],
            hue="prep_course", palette="Set2")
plt.title("Salary Spread Across Experience Levels")
plt.xlabel("Experience Level")
plt.ylabel("Salary ($)")
plt.show()