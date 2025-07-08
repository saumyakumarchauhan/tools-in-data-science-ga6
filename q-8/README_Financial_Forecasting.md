# Financial Forecasting: Model Accuracy Comparison

This guide helps you evaluate three different forecasting models used to predict loan default rates. While each student will have different dataset values, the format remains the same, so the steps apply universally.

## 📊 Dataset Format

Your Excel file should contain the following columns:

- `Month`: The month of observation (optional)
- `Actual`: Actual loan default rates
- `Linear Forecast`: Forecasted values using linear regression
- `Moving Average Forecast`: Forecasted values using moving average method
- `Exponential Forecast`: Forecasted values using exponential smoothing

## ✅ Objective

Calculate the **Mean Absolute Error (MAE)** for each forecast model and identify which model is most accurate (i.e., has the **lowest MAE**).

## 📌 Steps to Follow

1. **Open the Excel File** (e.g., `q-forecast-accuracy.xlsx`)
2. **Create New Columns** for Absolute Errors:
    - Linear Error: `=ABS(B2 - C2)`
    - Moving Average Error: `=ABS(B2 - D2)`
    - Exponential Error: `=ABS(B2 - E2)`
3. **Drag the formulas down** through all data rows.
4. **Calculate MAE** at the bottom of each error column:
    - Linear MAE: `=AVERAGE(F2:F25)`
    - Moving Avg MAE: `=AVERAGE(G2:G25)`
    - Exponential MAE: `=AVERAGE(H2:H25)`
5. **Compare the MAE values** and find the smallest one.
6. **Round the result** to 4 decimal places (e.g., `0.0234`)
7. **Submit the lowest MAE** value in your assignment.

## 📌 Formulas Reference

- **Absolute Error**: `=ABS(Actual - Forecast)`
- **MAE (Mean Absolute Error)**: `=AVERAGE(absolute_errors_range)`
- **RMSE**: `=SQRT(AVERAGE((Actual - Forecast)^2))`
- **MAPE**: `=AVERAGE(ABS((Actual - Forecast)/Actual))`

## 💡 Tip
- Ensure you're comparing all three methods fairly using the **same rows**.
- Double-check that you are referencing the correct columns.
- Don’t forget to round your answer to **4 decimal places**.

---

**Note:** Since each student's dataset will have different values but the same format, everyone must compute their own MAE values individually.

Good luck! 👍