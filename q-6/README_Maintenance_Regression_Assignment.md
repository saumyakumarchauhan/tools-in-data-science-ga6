
# 📊 Manufacturing Analytics: Equipment Maintenance Cost Prediction

## 🎯 Objective
To perform **simple linear regression analysis** using Excel to predict **Maintenance Cost** based on **Equipment Age**. This helps in understanding how well equipment age alone can explain the variation in maintenance costs.

---

## 📁 Dataset Description
Each student receives a dataset with different numeric values, but the structure is consistent across all files. The dataset contains 88 rows (excluding header) and includes the following columns:

- `Equipment_Age`: Age of the equipment in years
- `Usage_Hours`: Annual operating hours
- `Temperature`: Average operating temperature (°F)
- `Maintenance_Cost`: Annual maintenance cost in dollars

---

## 🧪 Task
You are required to:
1. Perform **simple linear regression** in Excel.
2. Use `Equipment_Age` as the **predictor (independent variable)**.
3. Use `Maintenance_Cost` as the **target (dependent variable)**.
4. Find the **R-squared** value from the regression output.
5. Interpret the model fit based on the R-squared value.

---

## 📝 Step-by-Step Instructions

### Step 1: Open the Dataset
- Open the provided Excel file (e.g., `q-regression-fit.xlsx`).

### Step 2: Enable Data Analysis ToolPak (if not enabled)
- Go to `File → Options → Add-ins`.
- At the bottom, select **Excel Add-ins** and click **Go**.
- Check **Analysis ToolPak** and click **OK**.

### Step 3: Run Regression
1. Go to `Data → Data Analysis → Regression`.
2. Set:
   - **Input Y Range**: `Maintenance_Cost` column (e.g., `D1:D89`)
   - **Input X Range**: `Equipment_Age` column (e.g., `A1:A89`)
3. Check ✅ **Labels** (if including headers).
4. Choose to output results in a **new worksheet**.
5. Click **OK**.

### Step 4: Locate R-squared
- In the **Regression Statistics** table, find the `R Square` value.
- It represents how much of the variation in maintenance cost is explained by equipment age.

---

## 📈 Interpretation of R-squared

| R-squared Range | Interpretation     |
|-----------------|--------------------|
| 0.0 – 0.3       | Weak model fit     |
| 0.3 – 0.7       | Moderate model fit |
| 0.7 – 1.0       | Strong model fit   |

### Example:
If R-squared = `0.5241`, the interpretation is:
> “Equipment age explains **52.41%** of the variation in maintenance costs. This represents a **moderate model fit**.”

---

## ✅ Submission Note
Each student will get a **different R-squared value** depending on their dataset, but the **steps, interpretation table, and format remain the same**.

Make sure to:
- Provide your **R-squared value**.
- Give a **brief interpretation** of the model fit.
