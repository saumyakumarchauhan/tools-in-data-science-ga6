
# Q-11: E-learning Platform Correlation Analysis

## 📚 Objective
Calculate the **Pearson correlation coefficient** between:
- `study_hours_per_week`
- `completion_rate`

Using SQL + Python on the `student_learning_data` table.

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
- Extract the ZIP to a folder (e.g., `D:\sqlite\`)

### Step 3: Add to System PATH (optional)
- Search for **Environment Variables** in Windows
- Edit `Path` under **System Variables**
- Click **New** and add: `D:\sqlite\`
- Click **OK** to save

### Step 4: Verify Installation
Open a new terminal (Command Prompt or Git Bash), run:
```bash
sqlite3 --version
```

You should see the installed SQLite version.

---

## 🔧 Steps to Reproduce

### 1. Load Data into SQLite

```bash
sqlite3 correlation_analysis.db < q-sql-correlation.sql
```

Or from inside SQLite shell:

```sql
.read q-sql-correlation.sql
```

---

### 2. Check Table

```sql
.tables
PRAGMA table_info(student_learning_data);
```

---

### 3. Python Script to Calculate Correlation

Create `correlation_calc.py`:

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("correlation_analysis.db")
df = pd.read_sql("SELECT * FROM student_learning_data", conn)

correlation = df["study_hours_per_week"].corr(df["completion_rate"])
print("Correlation coefficient:", round(correlation, 3))
```

Run it:

```bash
python correlation_calc.py
```

---

## ✅ Output

Submit the Pearson correlation coefficient **rounded to 3 decimal places** (e.g., `0.756`).
