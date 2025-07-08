
# Q-12: Logistics Delivery Time Regression Analysis

## 📚 Objective
Calculate the **regression slope** to understand how many **additional minutes** of delivery time are needed per **additional kilometer** of delivery distance.

---

## 🧰 Requirements

- Python 3.x
- SQLite
- pandas library

---

## 🧲 Installing SQLite (Windows)

### Step 1: Download SQLite
- Visit: https://www.sqlite.org/download.html
- Scroll to **Precompiled Binaries for Windows**
- Download: `sqlite-tools-win32-x86-*.zip`

### Step 2: Extract Files
- Extract ZIP to a folder like `D:\sqlite\`

### Step 3: Add to PATH (optional)
- Open Environment Variables → System Variables → Path → Add `D:\sqlite\`

### Step 4: Test It
Run:
```bash
sqlite3 --version
```

---

## 🔧 Steps to Solve

### 1. Load Data into SQLite

```bash
sqlite3 regression_analysis.db < q-sql-regression.sql
```

### 2. Open SQLite Shell

```bash
sqlite3 regression_analysis.db
```

### 3. View Table

```sql
.tables
PRAGMA table_info(delivery_data);
```

### 4. Get Required Values for Regression

```sql
.headers on
.mode column

SELECT
  COUNT(*) AS n,
  SUM(distance_km) AS sum_x,
  SUM(delivery_time_minutes) AS sum_y,
  SUM(distance_km * delivery_time_minutes) AS sum_xy,
  SUM(distance_km * distance_km) AS sum_x2
FROM delivery_data;
```

---

## 📐 Slope Formula

\[
b_1 = \frac{n \cdot \sum(xy) - \sum x \cdot \sum y}{n \cdot \sum(x^2) - (\sum x)^2}
\]

---

## 🐍 Python Code to Calculate Slope

```python
import sqlite3
import pandas as pd

# Connect to DB
conn = sqlite3.connect("regression_analysis.db")
df = pd.read_sql("SELECT * FROM delivery_data", conn)

# Regression calculations
n = len(df)
sum_x = df["distance_km"].sum()
sum_y = df["delivery_time_minutes"].sum()
sum_xy = (df["distance_km"] * df["delivery_time_minutes"]).sum()
sum_x2 = (df["distance_km"] ** 2).sum()

# Slope formula
numerator = n * sum_xy - sum_x * sum_y
denominator = n * sum_x2 - sum_x ** 2
slope = numerator / denominator

print("Slope (minutes/km):", round(slope, 2))
```

---

## ✅ Output

Submit the **slope rounded to 2 decimal places** (e.g., `2.54`) on the assignment platform.
