import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the data
df = pd.read_csv('q-python-datetime-analysis.csv')

# Step 2: Parse the timestamp column
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# Step 3: Extract the hour from timestamp
df['Hour'] = df['Timestamp'].dt.hour

# Step 4: Count number of requests per hour
hourly_counts = df['Hour'].value_counts().sort_index()

# Step 5: Find peak hour
peak_hour = hourly_counts.idxmax()
print("Peak Hour:", peak_hour)

# Step 6: Optional - plot
hourly_counts.plot(kind='bar', figsize=(10, 5), color='skyblue')
plt.title("Service Requests per Hour")
plt.xlabel("Hour (0-23)")
plt.ylabel("Number of Requests")
plt.grid(True)
plt.show()
