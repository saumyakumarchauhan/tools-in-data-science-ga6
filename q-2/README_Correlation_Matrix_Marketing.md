
# 📊 Correlation Matrix Analysis in Excel (Marketing Analytics)

This guide is intended to help students perform correlation matrix analysis using Microsoft Excel. The task involves identifying the strongest statistical relationship (correlation) between selected pairs of marketing metrics.

> ⚠️ **Note**: While all students use the same steps, the actual data in your `.xlsx` file may vary. This means your final correlation values and strongest pair will likely differ. Follow the steps accurately, and your result will be correct for your dataset.

---

## 🧠 Objective

You are given a dataset containing 5 marketing metrics over multiple campaigns:

- `Ad_Spend`: Monthly advertising spend in dollars
- `Social_Engagement`: Social media likes, shares, comments
- `Website_Traffic`: Unique website visitors per month
- `Email_Opens`: Email newsletter open rates
- `Sales_Revenue`: Monthly sales revenue in dollars

Your task is to:
1. Create a correlation matrix.
2. Identify the **strongest correlation** (highest absolute value) **among these 4 specific variable pairs**:

   - Ad_Spend ↔ Social_Engagement
   - Ad_Spend ↔ Sales_Revenue
   - Social_Engagement ↔ Website_Traffic
   - Website_Traffic ↔ Sales_Revenue

3. Submit **only** the correlation coefficient of the strongest pair (rounded to 3 decimal places).

---

## ✅ Step-by-Step Instructions

### 1. **Open the Excel File**
- Open the file (e.g., `q-correlation-matrix.xlsx`) containing your marketing data.
- Confirm that the first row contains headers and data spans down to row 76 (or as per your file).

---

### 2. **Enable Analysis ToolPak (If Needed)**
1. Go to `File → Options → Add-ins`
2. At the bottom, choose **Excel Add-ins** → Click **Go**
3. Check **Analysis ToolPak** → Click **OK**

---

### 3. **Create the Correlation Matrix**
1. Go to `Data → Data Analysis → Correlation → OK`
2. Input Range: Select all 5 columns and all rows (including headers). Example: `A1:E76`
3. Grouped by: **Columns**
4. Check: ✅ **Labels in First Row**
5. Output Range: Select an empty area (e.g., `G1`)
6. Click **OK**

Excel will generate a 5×5 correlation matrix.

---

### 4. **Extract Correlation Values for 4 Specific Pairs**
Use the matrix or the CORREL function:

```excel
=CORREL(A2:A76, B2:B76)  // Ad_Spend and Social_Engagement
=CORREL(A2:A76, E2:E76)  // Ad_Spend and Sales_Revenue
=CORREL(B2:B76, C2:C76)  // Social_Engagement and Website_Traffic
=CORREL(C2:C76, E2:E76)  // Website_Traffic and Sales_Revenue
```

> Adjust ranges as needed for your file.

---

### 5. **Compare Correlations (Use ABS Function)**

To compare strengths, use the absolute values:

```excel
=ABS(CORREL(..., ...))
```

Identify the **highest absolute value** among the four.

---

### 6. **Submit Your Answer**

- Round the highest value to **3 decimal places**.
- **Submit only the correlation coefficient** (e.g., `0.846` or `-0.729` — whichever is strongest in absolute terms).

✅ Do NOT submit variable names, the full matrix, or all four values.

---

## 🧠 Tips

- Always verify that your data range is correct and contains no blank or non-numeric values.
- Ensure that column headers match the variables listed above.
- The diagonal of the correlation matrix is always 1 (each variable correlated with itself).

---

## 📞 Need Help?

If you're confused about which cell represents which pair in the matrix, or want to confirm your result, reach out to your instructor or peer support group.

---

Happy analyzing! 📈
