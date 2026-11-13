import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

df = data[data["scenario"] == "02_MonthlySales"]
techstore = df[df["school_type"] == "TechStore"]
apparelco = df[df["school_type"] == "ApparelCo"]
plt.figure(figsize=(9, 5))
plt.plot(techstore["study_hours"], techstore["exam_score"], marker="o", label="TechStore")
plt.plot( apparelco["study_hours"], apparelco["exam_score"], marker="o", label="ApparelCo")
plt.title("Monthly Revenue Trends (Jan - Jun 2023)")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.legend()
plt.tight_layout()
plt.show()