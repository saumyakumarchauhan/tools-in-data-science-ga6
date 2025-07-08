
# 📊 Real Estate Analytics: Property Price Prediction

## 🎯 Objective
To perform **simple linear regression** using Microsoft Excel to identify the relationship between a property's **square footage** and its **sale price**. This helps in estimating prices per square foot and identifying investment opportunities in the real estate market.

---

## 🧠 Business Context

**PropertyMax Analytics**, a real estate analytics firm, aims to help investors:

- Estimate property prices based on area
- Detect undervalued properties
- Analyze local real estate market trends
- Assess fair market values quickly

---

## 🗂️ Dataset Information

- Each student receives a **unique dataset**
- **File Name Example:** `q-regression-pair.xlsx`
- **No. of Rows:** 69 (including header)
- **Columns:**
  - `Square_Footage` (independent variable - X)
  - `Sale_Price` (dependent variable - Y)

---

## 🛠️ Tools & Features Used

- Microsoft Excel (2016 or later recommended)
- Excel’s **Data Analysis Toolpak**
- Excel Functions:
  - `=SLOPE()`
  - `=LINEST()`
- Scatter Plot with Trendline (Visualization method)

---

## 📈 Step-by-Step Instructions

### 🔹 Step 1: Open the Excel File
- Ensure you open the provided dataset file (e.g., `q-regression-pair.xlsx`)

### 🔹 Step 2: Enable Data Analysis ToolPak
1. Go to **File → Options → Add-ins**
2. Select **Analysis ToolPak** from **Excel Add-ins**
3. Click **Go → Check the box → OK**

### 🔹 Step 3: Run Regression
1. Go to the **Data tab → Data Analysis → Regression**
2. Fill in the dialog box:
   - **Input Y Range:** `Sale_Price` column (e.g., `B1:B70`)
   - **Input X Range:** `Square_Footage` column (e.g., `A1:A70`)
   - Check **Labels**
   - Select **New Worksheet Ply** for output
3. Click **OK**

### 🔹 Step 4: Alternative (Quick) Method
Use Excel formula:
```excel
=SLOPE(B2:B70, A2:A70)
```
> Adjust ranges based on your dataset if necessary.

### 🔹 Step 5: Optional Visualization
1. Select both columns → Insert → Scatter Plot
2. Add Trendline → Check “Display Equation on chart”

---

## 📊 Output to Report

- **Slope (Regression Coefficient):** 📌 `___` ← (Round to 2 decimal places)
  - This value represents how much the **Sale Price increases for each additional square foot**
  - Example: If slope = `142.78`, then price increases by ₹142.78 per square foot

---

## 🧾 Final Deliverables

- Your dataset Excel file (with regression output in new worksheet)
- Calculated slope value (rounded to 2 decimal places)
- This `README.md` filled with your result

---

## 📝 Example Interpretation

> Based on the analysis, we found that every 1 square foot increase in a property's area leads to an estimated increase of ₹XXX.XX in the sale price.  
> This information can be used for fast pricing estimates and investment analysis.

---

## ✅ Notes for All Students

- Although each student has a **different dataset**, the **procedure remains exactly the same**.
- Only the **slope value and interpretation** will differ based on the dataset.
- Follow the steps carefully and double-check your ranges before computing.
- Round your final slope to **2 decimal places** as instructed.

---
