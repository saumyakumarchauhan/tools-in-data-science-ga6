import sqlite3
import pandas as pd

conn = sqlite3.connect("regression_analysis.db")
df = pd.read_sql("SELECT * FROM delivery_data", conn)

# Compute regression slope manually
n = len(df)
sum_x = df["distance_km"].sum()
sum_y = df["delivery_time_minutes"].sum()
sum_xy = (df["distance_km"] * df["delivery_time_minutes"]).sum()
sum_x2 = (df["distance_km"] ** 2).sum()

numerator = n * sum_xy - sum_x * sum_y
denominator = n * sum_x2 - sum_x ** 2
slope = numerator / denominator

print("Slope (minutes/km):", round(slope, 2))
