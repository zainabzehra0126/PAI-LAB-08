import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", keep_default_na=False)
d = df[df["scenario"] == "04_CustAgeDist"].copy()
d["age"] = pd.to_numeric(d["prep_course"])
d["gender"] = d["study_hours"]

sns.histplot(data=d, x="age", hue="gender", bins=5, kde=True)
plt.title("Customer Age Distribution by Gender")
plt.xlabel("Age")
plt.ylabel("Customer Count")
plt.show()