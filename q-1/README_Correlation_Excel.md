
# 📊 Correlation Analysis using Excel

This guide walks you through calculating and interpreting the **Pearson correlation coefficient** between two variables using **Microsoft Excel**. The example scenario involves analyzing the correlation between **COVID-19 Vaccination Rates** and **Mortality Rates**.

> ⚠️ **Note**: Since each user's Excel dataset may contain different data, the final correlation value (answer) will vary. However, if the following steps are followed carefully, the result will always be correct for their dataset.

---

## 🧠 What is Correlation?

Correlation is a statistical measure that expresses the extent to which two variables are linearly related. It ranges from:
- `+1`: Perfect positive correlation
- `0`: No correlation
- `-1`: Perfect negative correlation

---

## 📁 Requirements

- Microsoft Excel (any recent version)
- An `.xlsx` file with two columns you want to analyze (e.g., `Vaccination_Rate`, `Mortality_Rate`)

---

## ✅ Steps to Perform Correlation Analysis

### 1. **Open the Excel File**

Open the `.xlsx` file provided with the task. Identify the two numeric columns you want to correlate.

For example:
- Column A: `Vaccination_Rate`
- Column B: `Mortality_Rate`

> The actual column names or positions might differ depending on the dataset. Adjust accordingly.

---

### 2. **Using the CORREL Function**

1. Click on an empty cell.
2. Use the formula:

   ```excel
   =CORREL(Column1_Range, Column2_Range)
   ```

   Example:
   ```excel
   =CORREL(A2:A60, B2:B60)
   ```

3. Press **Enter**. This returns the **Pearson correlation coefficient**.

> 💡 Tip: Make sure the ranges contain **only numeric data** and are of **equal length**.

---

### 3. **(Optional) Visualize with a Scatter Plot**

1. Select both columns of data.
2. Go to **Insert → Charts → Scatter Plot**.
3. To add a trendline:
   - Right-click any data point.
   - Click **"Add Trendline"**.
   - Enable **“Display Equation on chart”** and **“R-squared value”** if needed.

---

### 4. **(Optional) Use Excel's Built-in Correlation Tool**

1. Enable the Analysis ToolPak:
   - File → Options → Add-ins → Excel Add-ins → Check "Analysis ToolPak"

2. Go to **Data → Data Analysis → Correlation**.

3. Select your data range and check **“Labels in first row”** (if applicable).

4. Choose output range and click **OK**.

---

## 📌 Interpreting the Result

Let’s say the result is:

```
-0.723
```

- **Direction**: Negative correlation (as one variable increases, the other tends to decrease).
- **Strength**:
  - 0.9–1.0: Very strong
  - 0.7–0.9: Strong
  - 0.5–0.7: Moderate
  - 0.3–0.5: Weak
  - Below 0.3: Very weak/negligible

This helps make informed decisions about public health, resource allocation, and communication strategies.

---

## 📥 Submission Instructions

- **Round** your correlation coefficient to **three decimal places** (e.g., `-0.723`).
- Submit only your value as per assignment requirements.

---

## 💡 Notes

- If your `.xlsx` file has a different number of rows or differently named columns, your formula should match your actual column ranges.
- Ensure no empty or non-numeric cells are included in your selected range.
- The answer will **vary** based on the dataset you received.

---

## 🔄 Example Formula Template

```excel
=CORREL(Sheet1!B2:B60, Sheet1!C2:C60)
```

Replace the range with your actual data location.

---

## 📞 Need Help?

If you face issues:
- Double-check that both columns have the same number of values.
- Ensure the data is numeric.
- Try using the Data Analysis Tool for a more visual matrix.

---

Happy analyzing! 📈
