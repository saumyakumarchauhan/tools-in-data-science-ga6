
# 📈 E-commerce Analytics: Conversion Rate Factors

## 🎯 Objective

The goal of this assignment is to determine which product page attributes (predictor variables) significantly impact **Conversion Rate** using **regression analysis** and **statistical significance (p-values)**.

## 🗂️ Dataset Structure

Each student receives a different dataset, but with the same format:

| Page_Load_Time | Product_Images | Price | Reviews | Conversion_Rate |
|----------------|----------------|-------|---------|------------------|
| (seconds)      | (count)        | ($)   | (count) | (%)              |

## 🔍 Your Task

You need to:
1. Run a **multiple linear regression** in **Excel**.
2. Identify **which variables have a p-value < 0.05**.
3. Exclude `Intercept` and report only the **statistically significant predictors**.

---

## 🧮 Steps to Follow

### ✅ Step 1: Open the Dataset

Open the provided `.xlsx` file (e.g., `q-regression-strength.xlsx`), and locate the sheet with raw data (typically the first one).

### ✅ Step 2: Run Regression in Excel

1. Go to the **Data** tab.
2. Click **Data Analysis** → Choose **Regression**.
3. Fill the fields:

   - **Input Y Range**: Select the full `Conversion_Rate` column (including the header).  
     Example: `$E$1:$E$144`

   - **Input X Range**: Select all four independent variables: `Page_Load_Time`, `Product_Images`, `Price`, `Reviews` (including the header).  
     Example: `$A$1:$D$144`

   - ✅ Check the **Labels** checkbox (since row 1 has headers).
   - Output: Choose **New Worksheet Ply**.
   - Click **OK**.

### ✅ Step 3: Read the P-values

1. Scroll to the regression output table where each variable has a **P-value** listed.
2. The variables typically appear in this order:
   - Intercept
   - Page_Load_Time
   - Product_Images
   - Price
   - Reviews

3. Focus on the P-values (usually in column **F**, rows 17 to 21).
4. **Ignore the Intercept**.
5. Note down **only those variables** whose **P-value < 0.05**.

---

## 🧠 Interpretation Rules

- ✅ **p-value < 0.05** → Statistically significant
- ❌ **p-value ≥ 0.05** → Not statistically significant
- 🚫 **Do NOT include "Intercept"** in your final answer

---

## 📝 Final Answer Format

Write your answer like this (example):
```
Page_Load_Time, Product_Images, Reviews
```

✅ Include only the variable names with **p-value < 0.05**  
❌ Do **not** include any p-values or the Intercept

---

## 💡 Optional: Auto-generate the answer in Excel (for advanced users)

If your variable names are in **Column A** and p-values are in **Column F**, use this formula:

```excel
=TEXTJOIN(", ", TRUE, IF(F17:F21<0.05, A17:A21, ""))
```

> Requires Excel 365 or Excel 2021+

---

## 📬 Submit your result

Once you identify the correct predictors, enter the final answer into the submission box as instructed.

---

## 🧑‍🏫 Need Help?

If you're unsure whether your regression output is correct:
- Double-check your X and Y ranges.
- Ensure you included **labels** (headers) in your selection.
- Re-run regression if needed.

Good luck and happy analyzing! 🚀
