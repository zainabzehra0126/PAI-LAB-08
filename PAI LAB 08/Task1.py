import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", keep_default_na=False)
d = df[df["scenario"] == "01_StudyVsScore"].copy()
d["study_hours"] = pd.to_numeric(d["study_hours"])
d["exam_score"] = pd.to_numeric(d["exam_score"])

sns.scatterplot(data=d, x="study_hours", y="exam_score", hue="prep_course", style="prep_course", s=100)
plt.title("Study Hours vs. Exam Score by Prep Course Status")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True)
plt.show()