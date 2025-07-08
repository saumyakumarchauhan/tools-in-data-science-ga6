import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("correlation_analysis.db")

# Load the table into a DataFrame
df = pd.read_sql("SELECT * FROM student_learning_data", conn)

# Compute Pearson correlation
correlation = df["study_hours_per_week"].corr(df["completion_rate"])
print("Correlation coefficient:", round(correlation, 3))
