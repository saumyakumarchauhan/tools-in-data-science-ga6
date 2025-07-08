
# 📊 HR Analytics: Employee Satisfaction Factors

## 🎯 Objective

Analyze survey data to determine **which workplace factor has the weakest correlation** with employee satisfaction. Each student is given a **unique dataset**, but all datasets share the **same structure and column names**.

---

## 🧠 Business Context

TalentMetrics HR Consulting is working with a mid-size technology company to improve **employee retention and engagement**. To do so, they’ve collected detailed survey responses from 107 employees.

The dataset includes the following columns:

| Column Name        | Description                               |
|--------------------|-------------------------------------------|
| `Salary`           | Annual compensation in USD                |
| `Work_Hours`       | Average weekly working hours              |
| `Commute_Time`     | Average daily commute time (minutes)      |
| `Team_Size`        | Number of people in employee's team       |
| `Satisfaction_Score` | Job satisfaction rating (1–10 scale)    |

---

## 📦 Dataset

- Format: `.xlsx` Excel file
- Filename (example): `q-correlation-strength.xlsx`
- Total Records: 107 rows (excluding header)
- Note: Data values vary per student, but columns and layout are the same

---

## 📌 Task Summary

1. Calculate the **correlation** between each factor and `Satisfaction_Score`
2. Convert those correlations to **absolute values**
3. Find the factor with the **smallest absolute correlation value**
4. Submit the **exact variable name** (e.g., `Team_Size`) that has the weakest correlation

---

## 🧮 Step-by-Step Guide (Excel Instructions)

### 🔹 Step 1: Open the Excel File

Open your `.xlsx` file in Microsoft Excel.

You should see 5 columns like this:

| A           | B           | C             | D         | E                  |
|-------------|-------------|---------------|-----------|--------------------|
| Salary      | Work_Hours  | Commute_Time  | Team_Size | Satisfaction_Score |
| ...         | ...         | ...           | ...       | ...                |

---

### 🔹 Step 2: Calculate Correlation Coefficients

Choose a new column (e.g., column G) and use the `CORREL()` function to calculate correlation values:

| Cell | Formula                                            | What it Calculates       |
|------|----------------------------------------------------|--------------------------|
| G3   | `=CORREL(A2:A108, E2:E108)`                        | Salary vs Satisfaction   |
| G4   | `=CORREL(B2:B108, E2:E108)`                        | Work_Hours vs Satisfaction |
| G5   | `=CORREL(C2:C108, E2:E108)`                        | Commute_Time vs Satisfaction |
| G6   | `=CORREL(D2:D108, E2:E108)`                        | Team_Size vs Satisfaction |

📝 These will give you **4 correlation values**. Some may be negative.

---

### 🔹 Step 3: Convert to Absolute Values

In the next column (e.g., column H), calculate absolute values using:

| Cell | Formula       |
|------|---------------|
| H3   | `=ABS(G3)`    |
| H4   | `=ABS(G4)`    |
| H5   | `=ABS(G5)`    |
| H6   | `=ABS(G6)`    |

This ensures you're comparing correlation **strength**, not direction.

---

### 🔹 Step 4: Find the Weakest Correlation

Now find the smallest absolute value in column H:

| Cell | Formula       | Description                           |
|------|---------------|---------------------------------------|
| H7   | `=MIN(H3:H6)` | Finds the weakest (smallest) correlation |

Look at which row this minimum value came from — that's your answer!

| Row | Variable Name | Meaning            |
|-----|----------------|---------------------|
| H3  | `Salary`       | if H3 is the minimum |
| H4  | `Work_Hours`   | if H4 is the minimum |
| H5  | `Commute_Time` | if H5 is the minimum |
| H6  | `Team_Size`    | if H6 is the minimum |

✅ Submit the variable name **exactly as it appears** (including underscores).

---

## 🧠 Example Walkthrough

Let’s say you get the following:

| G (Correlation) | H (Absolute) | Variable       |
|------------------|----------------|-----------------|
| 0.2314           | 0.2314         | Salary          |
| -0.1058          | 0.1058         | Work_Hours      |
| -0.3109          | 0.3109         | Commute_Time    |
| **0.0606**       | **0.0606**     | **Team_Size** ✅ |

Then the correct answer to submit is:

```
Team_Size
```

---

## 🎯 Business Interpretation

Understanding correlation helps the HR team focus on the most impactful areas:

- Strong correlations → areas to improve for satisfaction
- Weak correlations → less impact, lower priority

For example:
- If **Commute_Time** has a strong negative correlation, remote work might help.
- If **Team_Size** has a weak correlation, team size changes may not affect satisfaction much.

---

## 💡 Tips

- Double-check your cell ranges (e.g., `A2:A108` if your data starts from row 2)
- Compare **absolute values**, not raw correlations
- Submit the name **exactly as shown in the dataset**

---

## ❓ Need Help?

- Revisit formulas: `=CORREL()`, `=ABS()`, `=MIN()`
- Ask your instructor or post in course forums
- Don’t guess — follow each step carefully for accuracy

---

**Good luck, and happy analyzing!** 💼📈
