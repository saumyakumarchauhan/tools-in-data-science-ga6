
# Service Request DateTime Pattern Analysis (Python - 1 mark)

## Objective
Analyze service request timestamps to identify the **peak hour** (i.e., the hour of the day with the highest number of requests).

## Dataset Format
The dataset is a CSV file named `q-python-datetime-analysis.csv` containing a column with mixed-format timestamps.

Example format:

| Timestamp           |
|---------------------|
| 2024-01-15 08:45 AM |
| 15/01/2024 09:00    |
| Jan 15 2024 10:15   |
| ...                 |

## Steps to Solve

### 1. Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
```

### 2. Read the CSV File

```python
df = pd.read_csv('q-pytho-datetime-analysis.csv')
```

### 3. Parse the `Timestamp` Column

Convert mixed datetime strings to `datetime` objects:

```python
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
```

### 4. Extract the Hour

```python
df['Hour'] = df['Timestamp'].dt.hour
```

### 5. Count Requests by Hour

```python
hourly_counts = df['Hour'].value_counts().sort_index()
print(hourly_counts)
```

### 6. Identify the Peak Hour

```python
peak_hour = hourly_counts.idxmax()
print("Peak Hour:", peak_hour)
```

### 7. Optional: Plot the Hourly Distribution

```python
hourly_counts.plot(kind='bar', figsize=(10, 5), color='skyblue')
plt.title("Service Requests per Hour")
plt.xlabel("Hour (0-23)")
plt.ylabel("Number of Requests")
plt.grid(True)
plt.show()
```

## Notes
- Ensure `Timestamp` parsing is successful (check for `NaT` values if needed).
- The actual answer (peak hour) may vary for different students since datasets are different.

## Deliverable
Enter the hour (as a number from 0–23) that has the **highest number of requests** based on your analysis.

---

*This README is a general guide and can be used by all students who have the same dataset format but different values.*
