# 📦 Supply Chain Forecasting: Product Demand (Month 19)

This guide will help you forecast future product demand using Microsoft Excel. The goal is to predict demand for a future month (e.g., **Month 19**) based on historical data using a **linear trend**.

---

## 📊 Dataset Format

You are provided an Excel file (e.g., `q-forecast-linear.xlsx`) with the following structure:

| Month | Product_Demand |
|-------|----------------|
|   1   |     xxxx       |
|   2   |     xxxx       |
|  ...  |     ....       |
|  18   |     xxxx       |

> ⚠️ Each student will receive **different demand values**, but the format (columns, row count) is the same.

---

## ✅ Your Task

Predict the **Product_Demand** for a given future month using Excel's forecasting functions.

> Your assigned month might be different — for example, Month 19. Be sure to update the formulas accordingly.

---

## 📘 Step-by-Step Instructions

### Step 1: Open the Excel File

- Open the given Excel file (e.g., `q-forecast-linear.xlsx`).

### Step 2: Use the `FORECAST` Function

In any empty cell, type:

```excel
=FORECAST(TARGET_MONTH, B2:B19, A2:A19)
```

Replace TARGET_MONTH with your specific month (e.g., 19).

- B2:B19 → Product_Demand values
- A2:A19 → Month values

🔁 Example (For Month 19)
```excel
=FORECAST(19, B2:B19, A2:A19)
```

🎯 Round your answer to the nearest whole number (e.g., 2183.74 → 2184).

🧪 Optional: Cross-Check Methods

1. Using TREND function:

```excel
=TREND(B2:B19, A2:A19, TARGET_MONTH)
```

2. Using SLOPE and INTERCEPT:

```excel
=SLOPE(B2:B19, A2:A19) * TARGET_MONTH + INTERCEPT(B2:B19, A2:A19)
```

3. Chart Method:

- Select both columns
- Insert a Line Chart
- Right-click the line → Add Trendline
- Enable: Forecast Forward: 1 Period

---

## 📌 Submission

Submit your forecasted product demand (rounded to the nearest whole number) for the assigned future month in your assignment portal.

---

## 🧠 Important Reminders

- Make sure to replace 19 with your own assigned month.
- All students have different values, but the same format.
- Check that your cell ranges (A2:A19, B2:B19) match your dataset.
- Use Microsoft Excel, unless otherwise specified.
